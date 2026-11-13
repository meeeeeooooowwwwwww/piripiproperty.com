# Piripi & Sons Real Estate

A responsive coming-soon site for the Piripi & Sons Real Estate brand at [piripiproperty.com](https://piripiproperty.com).

## Site

- `public/index.html`: accessible split-layout homepage, preserving Corrie's complete original photograph on the left (no crop or vignette) and a property enquiry card on the right; stacks on smaller screens
- `public/assets/piripi-and-sons-real-estate.jpg`: Corrie’s supplied team photograph with PIRIPI & SONS REAL ESTATE branding
- The earlier crayon artwork is kept in the repository solely for rollback, and is no longer shown on the site
- `public/assets/site.css`: shared black/gold/silver design system, responsive split-layout homepage and contact-page styles
- `public/assets/enquiry-form.js` and `functions/api/enquiry.js`: same-origin POST sends each validated enquiry through Brevo transactional email. The visitor receives success only after Brevo acknowledges the message. The browser never receives Corrie's private Gmail address. A visible email-app fallback appears only when delivery fails.
- `public/assets/brand/*`: original vector monogram tracing plus stacked/horizontal brand lockups
- `public/favicon.svg`, `public/favicon.ico`, `public/favicon-32.png`, `public/apple-touch-icon.png`: matching logo-based favicon and touch-icon set
- `public/site.webmanifest`: web app identity/colour tokens
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
is preserved inside the social card with blurred side-fill rather than cropping. At build time,
`GITHUB_SHA` is applied to the OG/Twitter image URL as a cache-busting `?v=` query while the
stable `/social-preview.jpg` image remains available to previously published links.

The public pages and assets send `Cache-Control: no-cache, max-age=0, must-revalidate`
during active development. Third-party platforms such as Substack may cache the *page
URL itself*, which no website cache header can forcibly clear. To test a fresh Substack
embed, delete the old card and paste a fresh query URL, for example
`https://piripiproperty.com/?preview=20261113-2`, after a completed deployment.

To refresh a cached Facebook link preview, use https://developers.facebook.com/tools/debug/
and choose **Scrape Again** for https://piripiproperty.com/ .

## Initial public pages

- `/`: branded home with uncropped team photograph and right-side enquiry form on desktop; the form is below the photograph on mobile. The form POSTs to `/api/enquiry`; requires the Cloudflare Pages secret below for live direct delivery.
- `/contact/`: Corrie Piripi's phone and business email, including `tel:` and `mailto:` links.
- `/sitemap/`: readable navigation to Home and Contact.
- `/sitemap.xml`: machine-readable sitemap with all three public URLs.

These pages use the same Google tag and social-preview image as the homepage. Public SEO and structured data use the supplied brand **Piripi & Sons Real Estate** and name Corrie Piripi as a licensed real estate professional. `piripiproperty.com` remains the canonical domain. There is no assertion of a verified legal company name, independent agency/brokerage status, licence number or registered office. Add verified supervising agency and legal particulars once supplied by Corrie.

## Private enquiry delivery (Cloudflare Pages)

The form uses the **independent** Pages Function at `/api/enquiry`, not browser `mailto:`.
Configure **production** variables in Cloudflare > Workers & Pages > `piripiproperty` > Settings > Variables and Secrets, and redeploy after changing them:

- `BREVO_API_KEY` (**encrypted secret, required**): existing Brevo transactional API credential. Never place this in GitHub or browser scripts.
- `ENQUIRY_TO_EMAIL` (**encrypted secret, optional**): Corrie's private Gmail address after it is confirmed. Its value must not appear in the public GitHub repository or static assets. Without this setting, email defaults to `david@americafirst.co.nz` as the temporary inbox.
- `BREVO_FROM_EMAIL` (optional): default `david@grideater.com`, which must remain a verified Brevo sender. This is the sender, not the visitor's reply address.

Brevo does **not** require recipients to click a verification link, but **does** require an authorised sender and API key. The form is **not live direct-send** until `BREVO_API_KEY` is present and an end-to-end test succeeds. If unavailable, visitors receive an explicit error and can use the manual email-app alternative or phone Corrie. Do **not** claim an email was sent without a provider acknowledgement. When Corrie's Google Workspace is ready, change only the private recipient variable.

Abuse controls: same-origin-only JSON POSTs, field allowlist/length checks, minimum completion time and honeypot. Before promoting paid traffic, add Turnstile server-side validation and Cloudflare rate limiting for further abuse resistance.
