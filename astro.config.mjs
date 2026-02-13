import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
// https://astro.build/config
export default defineConfig({
  site: 'https://www.olaizolaetxea.com',
  integrations: [
    react(),
    tailwind()
  ],
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp'
    }
  }
});