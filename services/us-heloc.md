---
layout: default
title: "U.S. HELOCs | Up to 85% LTV"
description: "Explore U.S. HELOCs with Nicolas Lescalier: first, second, or third lien, up to 85% LTV, e-notary, and five-day funding for qualifying files."
permalink: /services/us-heloc/
breadcrumb_title: U.S. HELOCs
financing_key: heloc
faq:
  - question: "Where is this HELOC program available?"
    answer: "This offering is for U.S. properties only. Eligibility and final terms depend on the property, location, existing liens, and underwriting."
  - question: "Do I need an inspector to visit the property?"
    answer: "This program uses e-notary and does not require an inspector to visit the property. Eligibility and the closing process are confirmed during review."
  - question: "What rate will I receive?"
    answer: "HELOC rates vary by qualifications, including FICO and other underwriting factors. No fixed rate is quoted for this program on this page."
  - question: "Is funding within five days guaranteed?"
    answer: "Five-day funding is available for qualifying files. Approval and the funding date must be confirmed for your request."
---
{% assign heloc = site.data.financing_programs.heloc %}
<section class="hero hero--simple">
  <p class="eyebrow">Property financing · U.S. only</p>
  <h1>Access home equity with a HELOC.</h1>
  <p class="lede">First, second, or third lien options, with e-notary and no inspector visiting the property.</p>
  <div class="hero__actions"><a class="button" href="/contact/?need=HELOC">Discuss a HELOC</a></div>
  <p class="hero-note">A short property inquiry. No business application required.</p>
</section>

<section class="section program-feature">
  <h2>Program at a glance.</h2>
  <dl class="program-facts">
    <div><dt>Loan-to-value</dt><dd>Up to {{ heloc.max_ltv }}% LTV</dd></div>
    <div><dt>Lien position</dt><dd>1st, 2nd, or 3rd</dd></div>
    <div><dt>Funding available</dt><dd>Within {{ heloc.funding_days }} days</dd></div>
  </dl>
  <p class="quiet-note">For qualifying files. Rates depend on FICO and other underwriting factors. Existing liens, property eligibility, approval, and funding timing are reviewed for each request.</p>
</section>

<section class="section split">
  <div class="panel">
    <h2>Start with the property and existing debt.</h2>
    <p>Share the property’s state, estimated value, current mortgage and other lien balances, the amount requested, and your preferred timing. I’ll review the potential fit and explain the next steps.</p>
    <p>A HELOC is a line of credit secured by your home. Review the rate, fees, draw and repayment terms, and the effect of existing liens before accepting an offer. Read the <a href="https://www.consumerfinance.gov/ask-cfpb/what-is-a-home-equity-line-of-credit-heloc-en-107/">CFPB’s HELOC overview</a>.</p>
  </div>
  <aside class="simple-aside">
    <h3>Planning a property project?</h3>
    <p>For a construction request, compare the dedicated program with interest-only payments for the first twelve months.</p>
    <a class="text-link" href="/services/us-construction-loans/">U.S. construction loans</a>
  </aside>
</section>

<section class="section">
  <h2>HELOC questions.</h2>
  <div class="faq-list">{% for item in page.faq %}<details class="faq-item"><summary>{{ item.question | escape }}</summary><p>{{ item.answer | escape }}</p></details>{% endfor %}</div>
</section>
<section class="section"><div class="cta-panel"><h2>Review your property financing options.</h2><p>Contact Nicolas Lescalier, Funding Manager at Premium Merchant Funding. Start with a summary; sensitive documents can follow through the appropriate secure process.</p><a class="button" href="/contact/?need=HELOC">Start a HELOC inquiry</a></div></section>
