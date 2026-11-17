# Piripi & Sons Real Estate — Internal SEO Development Scope
**Status:** Working engineering scope (not a client proposal or a change to signed/commercial terms)  
**Prepared:** 17 November 2026 (NZDT)  
**Site:** https://piripiproperty.com/  
**Repository:** https://github.com/meeeeeooooowwwwwww/piripiproperty.com

## 1. Product outcome and constraints

Build an SEO-first real-estate-agent website capable of generating qualified appraisal and seller enquiries **without** a property portfolio. Main thematic keyword family: **real estate agents**. Commercial priority: **Christchurch home sellers and appraisal requests**; Canterbury secondary; nationwide NZ subject-matter coverage without pretending to have offices or service coverage in unverified locations.

The full public identity is **Piripi & Sons Real Estate** (public brand, legal/agency status not yet independently verified); keep `piripiproperty.com` canonical and preserve supplied five-person artwork and black/gold/silver/ivory design.

**Non-goals in this release:** property listings/search, open homes, sold properties, fabricated testimonials, sales statistics or accolades, an automated online property valuation, nationwide fake location pages, CRM integration, real-estate portal integrations, new paid advertising, new paid third-party tools. Leave no empty Listings navigation item. These may become separate features after actual agency approvals and properties exist.

**Operating model:** independent Cloudflare Pages project `piripiproperty`, static content in `public/`, Pages Function at `functions/api/enquiry.js`, deploy via the existing Wrangler GitHub workflow. Avoid introducing a CMS, extra frontend framework or a database unless there is demonstrable value; start with reusable static HTML partial-generation script or templating at build-time while preserving static output.

## 2. Benchmark: 20 NZ real estate websites

This is a **qualitative pattern study**, not a measured ranking of the country's 20 best-performing sites. Reviewed publicly accessible website content/navigation on 17 November 2026; patterns only, no copying.

| # | Website | Page inspected / verified pattern | Take into Piripi |
|---|---|---|---|
| 1 | [Harcourts](https://harcourts.net/nz/) | [Find people](https://harcourts.net/nz/people), [seller guide](https://harcourts.net/nz/resources/selling/how-to-become-a-more-savvy-seller) | Search intent around selecting a salesperson, educational seller FAQs and evidence-based appraisals |
| 2 | [Ray White NZ](https://www.raywhite.co.nz/) | Find an agent, Insights and Property Appraisal visible in national navigation | Simple distinct trust and lead routes |
| 3 | [Bayleys](https://www.bayleys.co.nz/) | Free appraisal CTA, residential services and premium brand positioning | Prominent appraisal conversion and understated premium visuals |
| 4 | [Barfoot & Thompson](https://www.barfoot.co.nz/) | Buy/Sell structure, seller advice, local market reporting | Clear service taxonomy and regional information |
| 5 | [Property Brokers](https://www.propertybrokers.co.nz/) | Prominent "How can we help?" with appraisal vs general enquiry | Intent-based intake, adapted to no portfolio |
| 6 | [Tall Poppy](https://www.tallpoppy.co.nz/) | Book Appraisal and transparent marketing value proposition | One obvious seller action, plain-language offer |
| 7 | [Arizto](https://www.arizto.co.nz/) | What's Included / Our People / Book a Free Appraisal | Communicate what service entails before asking for a lead |
| 8 | [NZ Sotheby's International Realty](https://www.nzsothebysrealty.com/) | Segmented Sell / Agents / Regions / Insights | Elegant segmentation, not imitation of luxury claims |
| 9 | [LJ Hooker NZ](https://www.ljhooker.co.nz/) | Extensive selling/buying checklists, guides and appraisals | Resource clusters linking naturally into seller services |
| 10 | [Professionals](https://www.professionals.co.nz/) | Sell > Online Valuation / Market Appraisal / Selling Property | Explain appraisal vs valuation honestly; no fake instant valuations |
| 11 | [Tremains](https://www.tremains.co.nz/) | Sell > Request Appraisal / Our Agents / Advice & Guides | Seller-led navigation and guides |
| 12 | [EVES](https://www.eves.co.nz/) | Sell > Appraisal, preparing home, staging, auction, process | Practical consumer education rather than thin SEO pages |
| 13 | [Lodge](https://lodge.co.nz/) | Sell, appraisal, market reports, suburb info and FAQs | Local-market authority and recurring original insights |
| 14 | [Tommy's](https://tommys.co.nz/) | Sell/Marketing, FAQs, local community | Human, local service story and transparent process |
| 15 | [Lugtons](https://www.lugtons.co.nz/) | Repeated market-appraisal CTA and local market-stat commentary | Offer appraisal in multiple relevant sections, data with provenance |
| 16 | [Century 21 NZ](https://www.century21.co.nz/) | Sell > Appraisal / First Steps / Marketing Plan / Completing Sale | Selling-process hub with logical child topics |
| 17 | [First National NZ](https://firstnational.co.nz/) | Sell > Appraisal / Sellers Guide / Auction, resource glossary | Glossary and educational content architecture |
| 18 | [Ray White Metro Christchurch](https://rwmetro.co.nz/) | Local Sell > Strategies / Tips / Appraisal | Useful Christchurch-specific service context |
| 19 | [Kelleher Real Estate](https://kelleher.co.nz/) | Concise Selling, Buying, About & Contact | Independent-boutique clarity without enormous menus |
| 20 | [Vivacity Christchurch](https://www.vivacity.nz/) | Focused Christchurch Central market positioning and Sell/Buy paths | Strong genuine geographic specificity beats boilerplate suburb spam |

**Shared lessons:** seller pathways, trustworthy personal identity, an appraisal CTA, helpful guides, local context and functional contact are valuable **before** property inventory. Do not reproduce competitor copy/branding or their portfolio-dependent navigation.

## 3. Information architecture

Primary header:
- **Home**
- **Sell** (overview, Property Appraisal, Selling a House, Selling Costs, Methods of Sale, Preparing for Sale)
- **Buy** (overview, First-Home Buyer Guide, Buying Process)
- **Areas** (Christchurch, Canterbury, later only original and verified sub-areas)
- **About** (approach, Corrie profile)
- **Guides**
- **Contact**
- Persistent gold CTA: **Request an Appraisal**. On mobile provide visible menu and CTA, accessible keyboard operation.

The homepage should remain premium, with the supplied photograph shown entirely on desktop and mobile. Unlike the holding page, support natural scrolling for substantive sections: concise search-intent-led hero, sell/buy choices, appraisal value proposition, approach/Corrie credibility, regional coverage, 3–5 helpful FAQs, latest verified guides and contact CTA. Do not force a one-screen layout when content grows.

Page/keyword map (proposed; final wording and overlapping keyword intents to be validated before drafting):

| Route | Primary user intent | Priority |
|---|---|---|
| `/` | Brand plus real-estate-agent service entry; Christchurch launch context | P0 |
| `/sell/` | Sell my house / selling property in Christchurch and NZ | P0 |
| `/sell/property-appraisal/` | Request property appraisal Christchurch | P0 |
| `/about/` | Who is Piripi & Sons; approach and licence attribution | P0 |
| `/about/corrie-piripi/` | Who is Corrie; verified skills and role | P0 |
| `/areas/christchurch/` | What Corrie offers in Christchurch, accurate local details | P0 |
| `/contact/` | Send enquiry / call / email | P0 (existing route to improve) |
| `/buy/` | Home buyer guidance and enquiry (no property results) | P1 |
| `/real-estate-agents/` | Educational: choosing/working with NZ real estate professionals | P1 |
| `/sell/selling-your-house/` | NZ seller process and timeline | P1 |
| `/sell/costs-of-selling/` | Costs and commission explained, no invented fees | P1 |
| `/sell/methods-of-sale/` | Auction vs deadline vs negotiation/tender | P1 |
| `/sell/preparing-for-sale/` | Preparation checklist | P1 |
| `/areas/canterbury/` | Verified service areas and regional context | P1 |
| `/buy/first-home-buyers/` | First-home buyers NZ informational guide | P2 |
| `/buy/buying-process/` | Step-by-step offer, due diligence and settlement guide | P2 |
| `/guides/` | Articles index with real content, never empty placeholder | P2 |

Keep `/sitemap/` as quiet footer utility; regenerate `/sitemap.xml` with **only live indexable URLs**. Publish initial group first and add remaining pages only when their original copy is accurate and complete. A single SEO head term on every page is counterproductive: assign distinct search intent and avoid cannibalisation between homepage, national educational hub and local Christchurch page.

Suggested original guide backlog (editorial, not automatically publishable):
1. How do I choose a real estate agent in New Zealand?
2. What happens during a property appraisal?
3. What does it cost to sell a house in NZ?
4. Auction vs deadline sale vs negotiation.
5. Preparing your Christchurch home for sale.
6. Questions to ask before signing an agency agreement.
7. First-home buyer due diligence in NZ.
8. A dated Canterbury market update, only with attributed and licensed/permitted data.

Each guide must add original, genuinely useful analysis, current NZ guidance, references and an appropriate review date. Corrie should fact-check industry-specific advice and first-person claims. No scraping/rephrasing competitors into low-value filler.

## 4. Work packages and acceptance criteria

### PP-SEO-01 — Baseline audit and compliance gate (P0, blocking public expansion)
- Capture current Search Console index status (access-dependent), site crawl, PageSpeed/Core Web Vitals, lighthouse/accessibility baselines, redirect/canonical behaviour, GTM/GA4 event state and direct-enquiry status.
- Verify the exact REA licence type held by Corrie, supervising licensed agency, authorised trading presentation, name/legal details and required licence statements. **Do not present a salesperson as a "licensed real estate agent".** The current `/contact/` contains that phrase and the hidden homepage H1 also says "licensed real estate agent". Replace only when the accurate classification is verified.
- Verify owned brand artwork/image rights and the website-facing privacy notice.
**Done when:** documented audit plus compliance-approved public wording; no unsupported business-entity schema or office address.

### PP-SEO-02 — Static site build system and navigation (P0)
- Preserve `public/` output and existing deployment workflow; introduce simple shared header/footer/nav/SEO metadata generation to avoid page divergence.
- Add accessible responsive desktop/mobile navigation, current-page state, keyboard focus, sensible breadcrumbs and a repeated appraisal action.
- Use a content manifest with page URL, title, description, image, H1, category and indexability; generate navigation and both sitemaps from it.
**Done when:** menu reaches all public pages without broken links; only complete live routes in sitemap; header active state and mobile navigation tested at 320/375/768/1280px.

### PP-SEO-03 — High-intent pages (P0)
- Build complete, original `/sell/`, `/sell/property-appraisal/`, `/areas/christchurch/`, `/about/` and Corrie profile; update home and contact.
- Each page has a unique intent, helpful copy, one canonical H1, clear CTA and contextual internal links.
- Appraisal form asks for property location, contact details, enquiry details and consent wording; **does not** claim to estimate price automatically.
**Done when:** no empty page or unsupported claim; seller can reach and submit an appraisal enquiry from 3 navigation paths.

### PP-SEO-04 — Enquiry reliability and abuse protection (P0)
- Existing browser client and Cloudflare Pages Function already implement API-backed Brevo transactional delivery **if** required secrets are configured. JS switches to `mailto:` when GET readiness probe reports unavailable. Do not rebuild blindly.
- Verify production `BREVO_API_KEY` secret, `ENQUIRY_TO_EMAIL` recipient configuration, sender authorisation and actual successful end-to-end delivery; no public/private Gmail or secret leaks.
- Preserve existing required-field validation, honeypot and minimum form completion checks; implement server-side Turnstile verification and sensible rate limits before paid traffic; avoid overlogging personal data.
- Correctly distinguish accepted provider receipt from actual recipient delivery in operations checks.
**Done when:** real test inquiry lands in agreed inbox; success UI only after API acknowledgement; failure/fallback works; repeat/spam tests and abuse controls pass.

### PP-SEO-05 — Core technical SEO (P0)
- Unique readable titles, descriptions and canonical URLs; semantically correct H1/H2s; open-graph previews; appropriate image sizes, lazy loading except hero and stable URL design.
- Regenerate `robots.txt`, `sitemap.xml`, human sitemap; add safe JSON-LD WebSite/WebPage/Person and accurate BreadcrumbList as appropriate. RealEstateAgent/LocalBusiness only after verified agency/entity/physical/service-area details.
- Include noindex for truly non-public or duplicate material only; avoid unsubstantiated schema FAQ rich-result expectations.
**Done when:** automated sitemap/metadata/link/schema checks pass; no orphan P0 pages; Search Console inspection after launch confirms Google can fetch priority pages (indexing not guaranteed).

### PP-SEO-06 — Measurement and reporting (P0)
- Audit GTM ID `GTM-555PWRPR`, GA4 events and consent requirements; do not assume existing tag means conversions work.
- Instrument `appraisal_form_success`, `general_enquiry_success`, `phone_click`, `email_click` and primary CTA click; deduplicate and never leak message, phone, email or address as event parameters.
- Capture baseline impressions, clicks, indexed pages, organic landings and measured enquiries; report monthly changes, noting small-sample uncertainty.
**Done when:** verified test events appear in real-time/debug tooling; real success event only follows API acknowledgement.

### PP-SEO-07 — Content cluster build (P1/P2)
- Create remaining selling guides and education-led buyer pages; publish Canterbury only once area claims and original content are verified.
- Establish internal link rules: each guide points to its parent pillar, relevant sibling and natural seller/appraisal CTA; parent pages list useful children.
- No mass-generated suburbs, no scraped third-party photos or unlicensed market statistics, no obsolete market dates.
**Done when:** each route is editorially complete, reviewed, original, mobile-readable and has a clear next step.

### PP-SEO-08 — QA, security and staged production rollout (P0)
- Build preview deployment or equivalent pre-prod validation before applying live changes. Existing site is a separate Direct Upload Cloudflare Pages project; keep Wrangler workflow and project isolation.
- Test small devices and very short heights; accessible labels, focus traps/escape, contrast, text zoom, image cropping, no horizontal overflow, no clipped form controls.
- Run automated smoke and link checks, pre/post-deploy curl checks, and form submission tests. Do not publish a false list of achievements or placeholder testimonials.
**Done when:** production pages pass smoke and manual responsive checks, existing branding preserved and rollback path documented.

## 5. Delivery order and dependencies

**Release 0: unblock and measure.** PP-SEO-01, email/function readiness checks, compliance sign-off; collect baseline and screenshot samples. No claims about client licence, supervising agency or service coverage without verification.

**Release 1: high-value acquisition site.** PP-SEO-02/03/04/05/06; launch high-intent core navigation and seller/appraisal pages, profile, Christchurch and contact. Do not ship unreviewed placeholder content.

**Release 2: organic authority.** PP-SEO-07 plus P1 pages, then carefully selected P2 guides; verify content, citations and area accuracy; resubmit sitemap and inspect index coverage.

**Ongoing optimisation.** Use Search Console query data and genuine enquiry outcomes to prioritise improvements; test CTA placement, readability, mobile performance and relevant internal links, not vanity page counts.

### Release-level success measures
- All P0 pages are present, indexable and crawlable; no listings navigation without inventory.
- Clear seller journey: homepage → seller information → appraisal request → **verified** inbox receipt.
- No false licence/title or entity claim and no unverified office/address coverage.
- GA4 conversion actions are tested and Search Console is configured for relevant URLs.
- Zero dead internal links, no duplicate canonical routes, usable mobile navigation and accessible forms.
- Technical changes remain independent of GRID EATER's unrelated deployment systems.

## 6. Authoritative implementation references
- Current source: https://github.com/meeeeeooooowwwwwww/piripiproperty.com
- REA advertising/licence rules: https://www.rea.govt.nz/real-estate-professionals/obligations/marketing-as-an-individual-or-company/
- Google's SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google's helpful-content guidance: https://developers.google.com/search/docs/fundamentals/creating-helpful-content

**Scope-control rule:** this engineering plan is an internal development roadmap. Do not overwrite the 13 November client SOW, create an invoice, change commercial terms, contact Corrie or start paid advertising as part of adopting it.
