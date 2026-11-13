# Piripi Property

A simple, fixed, single-screen coming-soon website for [piripiproperty.com](https://piripiproperty.com).

## Site

- `public/index.html`: responsive, no-scroll full-screen page, with the illustration fully visible (no crop)
- `public/assets/piripi-property-coming-soon.webp`: approved crayon artwork
- `public/favicon.svg`: small house favicon
- `public/_headers`: Cloudflare Pages headers

## Independent Cloudflare deployment

This repository deploys **only** to the Cloudflare Pages project `piripiproperty`.
It does not deploy to, or depend on, GRID EATER or any other website's Worker.

- Production URL: https://piripiproperty.com
- Cloudflare Pages project: `piripiproperty`
- Fallback URL: https://piripiproperty.pages.dev
- Configuration: `wrangler.toml`
- Workflow: `.github/workflows/deploy-pages.yml`
- Trigger: each push to `main` and manual workflow dispatch
- Command: `wrangler pages deploy public --project-name=piripiproperty --branch=main`

The Pages project was initially created using **Direct Upload**, and subsequent updates use Wrangler from this repository's GitHub Actions workflow. Do not add a competing Pages Git integration or deploy a different project's files to this Pages project.

The repository secret `PIRIPIPROPERTY_CLOUDFLARE_API_TOKEN` is required. It must be a Cloudflare API token with **Account → Cloudflare Pages → Edit** access, stored in GitHub Actions secrets. No token values are checked into source control.

## Local deploy

Install Wrangler or run via npx, then authenticate with a Cloudflare API token and run:

```bash
npx wrangler pages deploy public --project-name=piripiproperty --branch=main
```

Keep the project name and output directory unchanged; those explicitly isolate this website.
