/**
 * Framework-agnostic signup endpoint (Web standard Request/Response).
 *
 * The static site does not run this by itself. Mount it wherever the backend
 * will live, e.g. an Astro endpoint with a server adapter, a Netlify/Vercel
 * function or a Cloudflare Worker:
 *
 *   import { handleSubscribe } from './subscribe';
 *   import { createSystemeIoProvider } from './providers/systeme-io';
 *
 *   const provider = createSystemeIoProvider({
 *     apiKey: process.env.SYSTEME_IO_API_KEY,
 *     tagId: process.env.SYSTEME_IO_TAG_ID,
 *   });
 *   export const POST = ({ request }) => handleSubscribe(request, { provider });
 *
 * Contract: POST { email, source } (JSON or form-encoded)
 *   → 200 { ok: true } | 400 { ok: false, error: "invalid_email" } | 502 { ok: false, error: "provider_error" }
 */
import { isValidEmail, normalizeEmail } from '../lib/email';

export interface Subscriber {
  email: string;
  /** Which form was used, e.g. "hero" or "final-cta". */
  source: string;
  locale: 'tr';
}

export interface SubscriberProvider {
  readonly name: string;
  subscribe(subscriber: Subscriber): Promise<void>;
}

export interface SubscribeOptions {
  provider: SubscriberProvider;
  /** Origins allowed to call the endpoint from the browser, e.g. ["https://leanmodepro.com"]. */
  allowedOrigins?: string[];
}

/** Hidden field that only bots fill in. */
const HONEYPOT_FIELD = 'website';

export async function handleSubscribe(
  request: Request,
  { provider, allowedOrigins = [] }: SubscribeOptions,
): Promise<Response> {
  const cors = corsHeaders(request.headers.get('Origin'), allowedOrigins);

  if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });
  if (request.method !== 'POST') {
    return json({ ok: false, error: 'method_not_allowed' }, 405, { ...cors, Allow: 'POST, OPTIONS' });
  }

  const body = await readBody(request);
  if (!body) return json({ ok: false, error: 'invalid_body' }, 400, cors);

  // Pretend success so bots get no signal.
  if (body[HONEYPOT_FIELD]) return json({ ok: true }, 200, cors);

  const email = normalizeEmail(body.email ?? '');
  if (!isValidEmail(email)) return json({ ok: false, error: 'invalid_email' }, 400, cors);

  const source = (body.source ?? '').replace(/[^a-z0-9-]/gi, '').slice(0, 40) || 'unknown';

  try {
    await provider.subscribe({ email, source, locale: 'tr' });
  } catch (error) {
    console.error(`[subscribe] ${provider.name} failed`, error);
    return json({ ok: false, error: 'provider_error' }, 502, cors);
  }

  return json({ ok: true }, 200, cors);
}

async function readBody(request: Request): Promise<Record<string, string> | null> {
  const type = request.headers.get('Content-Type') ?? '';
  try {
    if (type.includes('application/json')) {
      const data: unknown = await request.json();
      if (!data || typeof data !== 'object') return null;
      return Object.fromEntries(
        Object.entries(data).filter((entry): entry is [string, string] => typeof entry[1] === 'string'),
      );
    }
    if (type.includes('application/x-www-form-urlencoded') || type.includes('multipart/form-data')) {
      const form = await request.formData();
      return Object.fromEntries(
        [...form.entries()].filter((entry): entry is [string, string] => typeof entry[1] === 'string'),
      );
    }
  } catch {
    return null;
  }
  return null;
}

function corsHeaders(origin: string | null, allowedOrigins: string[]): Record<string, string> {
  if (!origin || !allowedOrigins.includes(origin)) return {};
  return {
    'Access-Control-Allow-Origin': origin,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Accept',
    Vary: 'Origin',
  };
}

function json(data: unknown, status: number, headers: Record<string, string> = {}): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', ...headers },
  });
}
