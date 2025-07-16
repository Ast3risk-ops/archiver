// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  site: {
    url: 'https://archiver.asterisk.lol',
    name: 'Archiver'
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
      routes: ['/'],
      // Then crawl all the links on the page
      crawlLinks: true
    },
    preset: "cloudflare_pages",
    cloudflare: {
      deployConfig: true,
      nodeCompat: true,
      wrangler: { "name": "archiver-www" }
    }
  },
  modules: ['@nuxtjs/robots', '@nuxtjs/sitemap'],
  icon: {
    serverBundle: 'local',
  },
  extends: ['shadcn-docs-nuxt'],
  i18n: { 
    defaultLocale: 'en', 
    locales: [ 
      { 
        code: 'en', 
        name: 'English', 
        language: 'en-CA',
      }, 
    ], 
  },
  compatibilityDate: '2025-07-15',
});
