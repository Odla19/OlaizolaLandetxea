import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  // The full URL where your site will be hosted
  site: 'https://www.olaizolaetxea.com',

  // The repository name with leading/trailing slashes
  base: '/',

  integrations: [react(), tailwind()],

  // This ensures your build output matches the expected GitHub structure
  build: {
    assets: '_astro'
  }
});