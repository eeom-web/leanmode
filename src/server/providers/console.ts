import type { SubscriberProvider } from '../subscribe';

/** Development provider: logs signups instead of sending them anywhere. */
export const consoleProvider: SubscriberProvider = {
  name: 'console',
  async subscribe(subscriber) {
    console.info('[subscribe] new signup', subscriber);
  },
};
