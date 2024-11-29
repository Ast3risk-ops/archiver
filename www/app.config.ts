export default defineAppConfig({
  shadcnDocs: {
    site: {
      name: 'Archiver',
      description: 'Never lose another Discord message again.',
      ogImage: '/hero.png',
      ogImageComponent: 'ShadcnDocs',
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
      logo: {
        light: '/logo.svg',
        dark: '/logo-dark.svg',
      },
      nav: [],
      links: [{
        icon: 'lucide:github',
        to: 'https://github.com/ast3risk-ops/archiver',
        target: '_blank',
      }],
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
      }],
    },
    toc: {
      enable: true,
      title: 'On This Page',
      links: [{
        title: 'Invite the bot',
        icon: 'simple-icons:discord',
        to: '#',
        target: '_blank',
      }, {
        title: 'Create Issues',
        icon: 'lucide:circle-dot',
        to: 'https://github.com/Ast3risk-ops/archiver/issues/new',
        target: '_blank',
      }],
    },
    search: {
      enable: true,
      inAside: false,
      placeholder: 'Search',
      placeholderDetailed: 'Type to start searching'
    }
  }
});
