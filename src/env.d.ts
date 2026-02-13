/// <reference path="../.astro/types.d.ts" />
/// <reference types="astro/client" />
/// <reference types="react" />

interface ImportMetaEnv {
  readonly PUBLIC_SITE_URL: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}