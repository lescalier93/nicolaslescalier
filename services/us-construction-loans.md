---
layout: default
title: "U.S. Construction Loans | 12 Months Interest Only"
description: "Discuss U.S. construction financing with Nicolas Lescalier. Interest-only payments for the first 12 months; rates and terms depend on qualifications."
permalink: /services/us-construction-loans/
breadcrumb_title: U.S. construction loans
financing_key: construction
faq:
  - question: "Are construction loans available in Canada?"
    answer: "This construction-loan offering is available in the United States only."
  - question: "How do payments work in the first year?"
    answer: "The program offers interest-only payments for the first twelve months. Interest-only payments do not reduce principal. The written offer must confirm the payment calculation and repayment requirements after that period."
  - question: "What rate will I receive?"
    answer: "Rates vary by qualifications, including FICO and other underwriting factors. The project and financing structure also require review; this page does not quote a fixed rate."
---
{% assign construction = site.data.financing_programs.construction %}
<section class="hero hero--simple">
  <p class="eyebrow">Property financing · U.S. only</p>
  <h1>Construction financing for your next project.</h1>
  <p class="lede">Interest-only payments for the first {{ construction.interest_only_months }} months, with rates and terms based on your qualifications and project.</p>
  <div class="hero__actions"><a class="button" href="/contact/?need=Construction%20loan">Discuss a construction loan</a></div>
  <p class="hero-note">An online review with Nicolas Lescalier. Subject to underwriting and approval.</p>
</section>

<section class="section split">
  <div class="panel">
    <h2>Plan for the build and the repayment.</h2>
    <p>Interest-only payments cover interest during the initial period; they do not pay down principal. Review what happens after month twelve, including the remaining term and repayment requirements.</p>
    <p>The written offer should explain how funds are released, how payments are calculated, and what is required as the project progresses.</p>
  </div>
  <aside class="simple-aside">
    <h3>What to share first</h3>
    <ul class="plain-list"><li>Property location and project type</li><li>Estimated budget and requested financing</li><li>Current project stage and target timeline</li><li>Existing property debt and the plan after completion</li></ul>
  </aside>
</section>

<section class="section">
  <h2>Construction financing questions.</h2>
  <div class="faq-list">{% for item in page.faq %}<details class="faq-item"><summary>{{ item.question | escape }}</summary><p>{{ item.answer | escape }}</p></details>{% endfor %}</div>
  <p class="resource-note">Comparing property options? Explore <a href="/services/us-heloc/">U.S. HELOCs</a>, <a href="/services/us-mortgage-financing/">commercial mortgages</a>, or <a href="/services/us-bridge-financing/">bridge financing</a>.</p>
</section>
<section class="section"><div class="cta-panel"><h2>Tell me about the project.</h2><p>Start with a short inquiry. I’ll help you identify the information needed for a construction financing review.</p><a class="button" href="/contact/?need=Construction%20loan">Start a construction inquiry</a></div></section>
