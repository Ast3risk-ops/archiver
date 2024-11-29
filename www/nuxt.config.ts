// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  site: {
    url: 'https://archiver.asterisk.lol'
  },
  app: {
    head: {
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.svg' }
      ]
    },
  },
  extends: ['shadcn-docs-nuxt'],
  compatibilityDate: '2024-07-06',
});