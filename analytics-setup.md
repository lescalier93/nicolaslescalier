# Analytics & Tracking Setup

To monitor performance and user behaviour in the United States, configure Google Analytics 4 and Google Search Console.  Below is a quick setup guide:

## Google Analytics 4 (GA4)

1. **Create a GA4 property** for `nicolaslescalier.com` using your Google account.  In the Admin panel, click “Create Property” → select GA4 and choose the “Business and Finance” category.
2. **Data Stream** – choose “Web” and enter your domain (`nicolaslescalier.com`).  Copy the **Measurement ID** (looks like `G‑XXXXXXX`).
3. **Embed the GA4 snippet** into your site’s `<head>` via Jekyll.  Add this to your `_includes/header.html` above the closing `</head>` tag:

```html
<!-- Global site tag (GA4) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace `G-XXXXXXXXXX` with your actual Measurement ID.  This snippet loads GA4 asynchronously and tracks all page views.  GA4 automatically anonymises IPs to comply with privacy regulations.

## Google Search Console

1. Visit [search.google.com/search-console](https://search.google.com/search-console/about) and click “Start Now”.
2. Add a **Domain property**: enter `nicolaslescalier.com` and continue.
3. For verification, choose the **DNS TXT** method.  Copy the TXT record provided (e.g., `google-site-verification=xxxxxxxxxxxxxxxx`).
4. Log into your domain registrar (e.g. Google Domains, GoDaddy) and add the TXT record.  Save and return to Search Console to verify.
5. Once verified, submit your updated sitemap: go to “Indexing” → “Sitemaps” → enter `/sitemap.xml` and click “Submit”.  Monitor coverage and indexing issues weekly.

## Region Targeting

While your domain is `.com`, you can signal U.S. targeting by:

* Hosting on a U.S. server or using a CDN (Cloudflare) with a primary U.S. edge.
* Using U.S. English in your HTML (`lang="en-US"`).
* Including `targetCountry="US"` in your JSON‑LD Person schema.

## KPIs to Monitor

* **Keyword rankings** for “Nicolas Lescalier”, “merchant cash advance USA”, “U.S. small business loans” and similar terms.
* **Organic traffic growth** – track sessions and new users from the U.S. and Canada separately.
* **Click‑through rate (CTR)** on branded queries (Search Console → Performance → Queries).
* **Bounce rate and time on page** for new content (GA4 Engagement reports).  High dwell time indicates relevant content.
* **Backlink profile** – use Ahrefs or SerpRobot to monitor new backlinks and anchor text distribution.

Setting up analytics properly ensures you can measure progress and adjust strategies for maximum impact in the U.S. market.
