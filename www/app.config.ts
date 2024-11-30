export default defineAppConfig({
  shadcnDocs: {
    site: {
      name: 'Archiver',
      description: 'Never lose another Discord message again.',
      ogImage: '/hero.png',
      ogImageComponent: 'ShadcnDocs',
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
      credits: 'Copyright © Asterisk 2024',
      links: [{
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
        title: 'Invite the bot',
        icon: 'simple-icons:discord',
        to: '#',
        target: '_blank',
      }, {
        title: 'Report a bug',
        icon: 'lucide:bug',
        to: 'https://github.com/Ast3risk-ops/archiver/issues/new?assignees=Ast3risk-ops&labels=bug&projects=&template=bug.yml&title=%F0%9F%90%9B+',
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
