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
  content: {
    highlight: {
      langs: [
        'c',
        'cpp',
        'java',
        'py',
        'toml',
        'bash',
        'dockerfile',
        'yaml',
        'yml',
        'python',
      ]
    },
  },
  nitro: {
    prerender: {
      // Pre-render the homepage
      routes: ['/', '/setup/quickstart'],
      // Then crawl all the links on the page
      crawlLinks: true
    }
  },
  icon: {
    serverBundle: 'local',
  },
  extends: ['shadcn-docs-nuxt'],
  compatibilityDate: '2024-07-06',
});