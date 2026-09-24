import { signupConfig } from '../config/signup';

export interface SignupPayload {
  email: string;
  /** Which form on the page was used, e.g. "hero" or "final-cta". */
  source: string;
}

export class SignupError extends Error {
  constructor(readonly status?: number) {
    super(status ? `Signup failed with HTTP ${status}` : 'Signup failed');
    this.name = 'SignupError';
  }
}

export const isDemoMode = signupConfig.endpoint === '';

/** Sends a signup to the configured backend (or simulates it in demo mode). */
export async function submitSignup(payload: SignupPayload): Promise<void> {
  if (isDemoMode) {
    console.info(
      '[signup] Demo mode: PUBLIC_SIGNUP_ENDPOINT is not set, nothing was sent.',
      payload,
    );
    await new Promise((resolve) => setTimeout(resolve, 600));
    return;
  }

  let response: Response;
  try {
    response = await fetch(signupConfig.endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(payload),
      signal: AbortSignal.timeout(signupConfig.timeoutMs),
    });
  } catch {
    throw new SignupError();
  }

  if (!response.ok) throw new SignupError(response.status);
}
