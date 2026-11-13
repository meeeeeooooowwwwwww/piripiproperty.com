# Piripi Property

A simple, fixed, single-screen coming-soon website for [piripiproperty.com](https://piripiproperty.com).

## Site

- `public/index.html`: responsive, no-scroll full-screen page, with the illustration fully visible (no crop)
- `public/assets/piripi-and-sons-real-estate.jpg`: Corrie’s supplied team photograph with PIRIPI & SONS REAL ESTATE branding
- The earlier crayon artwork is kept in the repository solely for rollback, and is no longer shown on the site
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

## Social sharing previews

The page declares absolute Open Graph and X/Twitter Card metadata for \`https://piripiproperty.com/\`.
The CI workflow runs \`scripts/build_social_image.py\`, which renders a 1200x630 JPEG at
\`/social-preview.jpg\` from Corrie’s supplied team photograph. The entire photograph, including logo and people,
is preserved inside the social card with blurred side-fill rather than cropping.

To refresh a cached Facebook link preview, use https://developers.facebook.com/tools/debug/
and choose **Scrape Again** for https://piripiproperty.com/ .

## Initial public pages

- `/`: fixed coming-soon landing page, with unobtrusive links to Contact and Sitemap.
- `/contact/`: Corrie Piripi's phone and business email, including `tel:` and `mailto:` links.
- `/sitemap/`: readable navigation to Home and Contact.
- `/sitemap.xml`: machine-readable sitemap with all three public URLs.

These pages use the same Google tag and social-preview image as the homepage. The name `Piripi Property Limited` is deliberately excluded while registration is pending.
