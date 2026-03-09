// @ts-check
import { themes as prismThemes } from 'prism-react-renderer';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

/** @type {import('@docusaurus/types').Config} */
const config = {
    title: 'Finales Álgebra Lineal Computacional',
    tagline: 'Apuntes, Finales y Demostraciones',
    favicon: 'img/favicon.ico',

    url: 'https://nahuelrabey.github.io',
    baseUrl: '/apuntes_IA_final_ALC/',

    organizationName: 'nahuelrabey',
    projectName: 'apuntes_IA_final_ALC',

    onBrokenLinks: 'throw',
    onBrokenMarkdownLinks: 'warn',

    i18n: {
        defaultLocale: 'es',
        locales: ['es'],
    },

    presets: [
        [
            'classic',
            /** @type {import('@docusaurus/preset-classic').Options} */
            ({
                docs: {
                    routeBasePath: '/', // Serve the docs at the site's root
                    sidebarPath: './sidebars.js',
                    remarkPlugins: [remarkMath],
                    rehypePlugins: [rehypeKatex],
                },
                blog: false, // Disable the blog plugin
                theme: {
                    customCss: './src/css/custom.css',
                },
            }),
        ],
    ],

    stylesheets: [
        {
            href: 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css',
            type: 'text/css',
            crossorigin: 'anonymous',
        },
    ],

    themeConfig:
        /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
        ({
            colorMode: {
                defaultMode: 'dark',
                disableSwitch: false,
                respectPrefersColorScheme: true,
            },
            navbar: {
                title: 'ALC y Análisis',
                logo: {
                    alt: 'Logo',
                    src: 'img/logo.svg', // Ensure you have an image at static/img/logo.svg, or remove this property
                },
                items: [
                    {
                        type: 'docSidebar',
                        sidebarId: 'tutorialSidebar',
                        position: 'left',
                        label: 'Documentación',
                    },
                    {
                        href: 'https://github.com/nahuelrabey/apuntes_IA_final_ALC',
                        label: 'GitHub',
                        position: 'right',
                    },
                ],
            },
            footer: {
                style: 'dark',
                links: [],
                copyright: `Copyright © ${new Date().getFullYear()} Nahuel Rabey. Construido con Docusaurus.`,
            },
            prism: {
                theme: prismThemes.github,
                darkTheme: prismThemes.dracula,
                additionalLanguages: ['python', 'bash'],
            },
        }),
};

export default config;
