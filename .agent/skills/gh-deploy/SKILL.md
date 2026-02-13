---
name: gh-pages-deploy
description: Automates deployment to GitHub Pages for static sites.
---

# GitHub Pages Deployer

## Context
We are deploying a static site (Astro/HTML) to the `gh-pages` branch.

## Deployment Steps
When asked to "deploy" or "publish":

1. **Build the Site:**
   Run `npm run build` to generate the `dist/` folder.

2. **Publish Strategy:**
   Use the `gh-pages` npm package for reliability.
   - If not installed: `npm install -D gh-pages`
   - Add script to package.json: `"deploy": "gh-pages -d dist"`

3. **Execution:**
   Run `npm run deploy`.

4. **Domain Configuration:**
   Ensure a `CNAME` file exists in the `public/` folder with the content: `olaizolaextea.com` to link the custom domain.