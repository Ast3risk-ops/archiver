export default defineAppConfig({
  shadcnDocs: {
    site: {
      name: 'Archiver',
      description: 'Never lose a Discord message again.',
      ogImage: '/hero.png',
      ogImageComponent: 'ShadcnDocs',
      ogImageColor: 'dark',
      umami: {
        enable: true,
        src: 'https://t.asterisk.lol/script.js',
        dataWebsiteId: '11eb1bd6-9ded-4e71-b22d-5608beaff662',
      },    
    },
    theme: {
      customizable: false,
      color: 'zinc',
      radius: 0.5,
    },
    header: {
      title: 'Archiver',
      showTitle: true,
      border: true,
      darkModeToggle: true,
      showTitleInMobile: false,
      logo: {
        light: '/logo.svg',
        dark: '/logo-dark.svg',
      },
      nav: [],
      links: [{
        icon: 'lucide:github',
        to: 'https://github.com/ast3risk-ops/archiver',
        target: '_blank',
        rel: 'noopener noreferrer',
      },
      {
        icon: 'radix-icons:discord-logo',
        to: 'https://discord.gg/d3a9dW9KHN',
        target: '_blank',
      },
      ],
    },
    banner: {
      enable: true,
      showClose: true,
      content: '**:smart-icon{name="⭐"} Star us on GitHub!** :icon{name="lucide:arrow-up-right" size=16}',
      to: 'https://github.com/Ast3risk-ops/archiver',
      target: '_blank',
      rel: 'noopener noreferrer',
      border: true,
    },
    aside: {
      useLevel: true,
      collapse: false,
    },
    main: {
      breadCrumb: true,
      showTitle: true,
      padded: true,
      editLink: {
        enable: true,
        pattern: 'https://github.com/Ast3risk-ops/archiver/edit/main/www/content/:path',
        text: 'Edit this page',
        icon: 'lucide:file-pen-line',
        placement: ['docsFooter', 'toc'],
      },
    },
    footer: {
      credits: 'Made with ❤️ by the Archiver team',
      links: [
      {
        icon: 'lucide:asterisk',
        to: '/terms',
        title: 'Terms of Service',
        },
        {
        icon: 'lucide:file-lock',
        to: '/terms/privacy-policy',
        title: 'Privacy Policy',
        },
        {
          icon: 'lucide:mail',
          to: 'mailto:me@asterisk.lol?subject=Archiver'
      },
      {
        icon: 'lucide:github',
        to: 'https://github.com/ast3risk-ops/archiver',
        target: '_blank',
      },
      {
        icon: 'radix-icons:discord-logo',
        to: 'https://discord.gg/d3a9dW9KHN',
        target: '_blank',
        },
      ],
    },
    toc: {
      enable: true,
      enableInMobile: false,
      title: 'On This Page',
      links: [{
        title: 'Install the app',
        icon: 'radix-icons:discord-logo',
        to: 'https://discord.com/oauth2/authorize?client_id=1311438512045949029',
        target: '_blank',
      },
        {
          title: 'Support server',
          icon: 'lucide:message-circle-question',
          to: 'https://discord.gg/d3a9dW9KHN',
          target: '_blank',
      },
      {
        title: 'Report a bug',
        icon: 'lucide:bug',
        to: 'https://github.com/Ast3risk-ops/archiver/issues/new?template=bug.yml',
        target: '_blank',
        rel: 'noopener noreferrer',
      }],
    },
    search: {
      enable: true,
      inAside: false,
      style: 'input',
      placeholder: 'Search',
      placeholderDetailed: 'Type to start searching'
    }
  }
});
