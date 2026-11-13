# Piripi Property | Coming Soon

Single-screen, fixed, scroll-free temporary homepage for https://piripiproperty.com.

## Files
- `public/index.html`: fixed viewport, image not cropped (`background-size: contain`).
- `public/assets/piripi-property-coming-soon.webp`: crayon artwork with male agent, Piripi Property branding and “Website coming soon.”
- `public/favicon.svg`: placeholder favicon.
- `public/_headers`: Cloudflare Pages security/caching headers.

## Publish to Cloudflare Pages (recommended: Git connection)
1. Make sure all files, including `public/assets/piripi-property-coming-soon.webp`, are committed to the `main` branch.
2. Cloudflare dashboard > Workers & Pages > Create application > Pages > Connect to Git. Select `meeeeeooooowwwwwww/piripiproperty.com` and branch `main`.
3. Framework preset: **None**. Build command: `exit 0` (or leave empty). Build output directory: `public`.
4. When the deployment succeeds, open Pages > Custom domains and add `piripiproperty.com`. Add `www.piripiproperty.com` separately if wanted.

Cloudflare Pages Git integration automatically publishes later pushes to `main`. Do **not** choose a Direct Upload project if you want automatic Git-based deployments later.

## Optional one-off publication
The ZIP created alongside this repository contains the deployable files at its top level. In Cloudflare Pages choose Direct Upload and upload the ZIP; note this creates a deployment that cannot later be switched to Git integration within the same Pages project.
