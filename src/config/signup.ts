/**
 * Email signup configuration.
 *
 * The form posts `{ email, source }` as JSON to `endpoint`. Any backend that
 * accepts this contract works — see `src/server/subscribe.ts` for a ready
 * handler that will forward signups to the email provider (Brevo) once connected.
 *
 * While `PUBLIC_SIGNUP_ENDPOINT` is empty the form runs in demo mode:
 * it validates and shows the success state, but sends nothing.
 */
export const signupConfig = {
  endpoint: (import.meta.env.PUBLIC_SIGNUP_ENDPOINT ?? '').trim(),
  successUrl: (import.meta.env.PUBLIC_SIGNUP_SUCCESS_URL ?? '').trim(),
  timeoutMs: 15_000,
} as const;

export const signupCopy = {
  label: 'E-posta adresin',
  placeholder: 'E-posta adresini gir',
  button: 'Ücretsiz Planı Al',
  buttonLoading: 'Gönderiliyor…',
  note: '30 günlük rehberi e-posta adresine gönderelim.',
  errors: {
    empty: 'Lütfen e-posta adresini gir.',
    invalid: 'Lütfen geçerli bir e-posta adresi gir.',
    failed: 'Şu anda kaydını alamadık. Lütfen birazdan tekrar dene.',
  },
  success: {
    title: 'Teşekkürler, kaydın alındı.',
    text: '30 günlük planı e-posta adresine gönderiyoruz. Gelen kutunu kontrol et; e-postayı göremezsen spam klasörüne de göz at.',
  },
} as const;
