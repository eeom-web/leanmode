import type { SubscriberProvider } from '../subscribe';

export interface SystemeIoConfig {
  /** Systeme.io public API key — server-side secret, never a PUBLIC_* variable. */
  apiKey?: string;
  /** Tag assigned to new contacts; an automation on this tag sends the e-book. */
  tagId?: string;
}

/**
 * Systeme.io provider — prepared, NOT implemented yet (no account/API key available).
 *
 * To connect it:
 *  1. In Systeme.io, create a tag for this lead magnet and an automation that
 *     sends the 30-day plan email when the tag is added.
 *  2. Create an API key in Systeme.io and set SYSTEME_IO_API_KEY and
 *     SYSTEME_IO_TAG_ID on the server.
 *  3. Implement `subscribe()` below following the official Systeme.io API
 *     documentation: create (or find) the contact by email, then assign the tag.
 *
 * Until then it fails loudly, so a misconfigured deployment never drops signups silently.
 */
export function createSystemeIoProvider(config: SystemeIoConfig): SubscriberProvider {
  return {
    name: 'systeme-io',
    async subscribe() {
      if (!config.apiKey || !config.tagId) {
        throw new Error('Systeme.io is not configured: set SYSTEME_IO_API_KEY and SYSTEME_IO_TAG_ID.');
      }
      throw new Error('Systeme.io provider is not implemented yet.');
    },
  };
}
