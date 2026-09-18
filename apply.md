---
title: "Business Financing Application"
description: "Submit a concise business financing request for working capital, term loans, equipment, factoring, SBA, bridge, or commercial mortgage options."
permalink: /apply/
layout: default
image: "/assets/social-apply.png"
breadcrumb_title: Application
---

<header class="page-intro application-intro">
  <p class="eyebrow">Business financing application</p>
  <h1>Tell me what your business needs.</h1>
  <p>About 3 minutes. Start with your contact details and funding request. Submitting does not authorize a credit pull.</p>
  <p class="intro-help">No sensitive documents needed. Prefer to talk? <a href="https://calendly.com/nlescalier/funding" target="_blank" rel="noopener noreferrer">Book a call</a>.</p>
</header>

<script>
  window.addEventListener("DOMContentLoaded", () => {
    const params = new URLSearchParams(window.location.search);
    const form = document.querySelector("form[name='financing_application']");
    const scenarioCarryover = document.getElementById("scenarioCarryover");
    const scenarioCarryoverText = document.getElementById("scenarioCarryoverText");

    const setFieldValue = (id, value) => {
      const field = document.getElementById(id);
      if (field && value) field.value = value;
    };

    const setSelectByText = (id, value) => {
      const field = document.getElementById(id);
      if (!field || !value) return;
      const option = Array.from(field.options).find((entry) => entry.value === value || entry.text === value);
      if (option) field.value = option.value;
    };

    const humanizeLeadSource = (value) => ({
      website: "the website",
      working_capital_calculator: "the working capital calculator",
      term_calculator: "the term loan calculator",
    }[value] || String(value || "the website").replace(/_/g, " "));

    const humanizeScenarioOrigin = (value) => ({
      payment: "payment-based",
      loanAmount: "loan-amount-based",
      interestRate: "rate-based",
      loanTerm: "term-based",
    }[value] || value);

    setFieldValue("lead_source", params.get("lead_source") || "website");
    setFieldValue("scenario_origin", params.get("scenario_origin") || "");

    const productInterest = params.get("product_interest");
    if (productInterest) {
      const select = document.getElementById("product_interest");
      const option = Array.from(select.options).find(
        (entry) => entry.value.toLowerCase() === productInterest.toLowerCase()
      );
      if (option) select.value = option.value;
      else setFieldValue("product_interest_other", productInterest);
    }

    setSelectByText("amount_requested", params.get("amount_requested"));
    setFieldValue("use_of_proceeds", params.get("use_of_proceeds"));
    setFieldValue("additional_context", params.get("additional_context"));

    const leadSource = params.get("lead_source") || "website";
    if (["term_calculator", "working_capital_calculator"].includes(leadSource)) {
      document.getElementById("currency").value = "USD";
    }
    const scenarioOrigin = params.get("scenario_origin");

    if (scenarioCarryover && scenarioCarryoverText && (leadSource !== "website" || scenarioOrigin)) {
      scenarioCarryover.hidden = false;
      scenarioCarryoverText.textContent = scenarioOrigin
        ? `Your ${humanizeScenarioOrigin(scenarioOrigin)} scenario from ${humanizeLeadSource(leadSource)} has been carried into this form.`
        : `Context from ${humanizeLeadSource(leadSource)} has been carried into this form.`;
    }

    if (params.toString() && typeof window.nicolasTrack === "function") {
      window.nicolasTrack("application_prefill_loaded", {
        lead_source: leadSource,
        product_interest: productInterest || "",
        scenario_origin: scenarioOrigin || "",
      });
    }

    form?.addEventListener("submit", () => {
      if (typeof window.nicolasTrack === "function") {
        window.nicolasTrack("application_submit_started", {
          lead_source: leadSource,
          product_interest: form.elements.product_interest.value || "",
        });
      }
    });
  });
</script>

<section class="section" id="application-form">
  <h2 class="visually-hidden">Business financing request</h2>
  <p class="form-required-note">Fields marked * are required. Other details are optional.</p>

  <div class="application-frame">
    <div class="notice-card" id="scenarioCarryover" hidden>
      <p class="eyebrow">Calculator scenario carried over</p>
      <p id="scenarioCarryoverText">Your calculator scenario has been carried into this form.</p>
    </div>

    <form class="contact-form" name="financing_application" action="https://formspree.io/f/mgonknak" method="POST" data-ajax-form="true" data-success-url="/application-received/">
      <input type="hidden" name="_subject" value="New financing application from nicolaslescalier.com">
      <input type="hidden" id="lead_source" name="lead_source" value="website">
      <input type="hidden" id="scenario_origin" name="scenario_origin" value="">
      <input type="hidden" name="utm_source">
      <input type="hidden" name="utm_medium">
      <input type="hidden" name="utm_campaign">
      <input type="hidden" name="utm_content">
      <input type="hidden" name="utm_term">
      <input type="hidden" name="gclid">
      <input type="hidden" name="landing_page">
      <input type="hidden" name="referrer_url">
      <input type="hidden" name="entry_path">
      <div class="form-honeypot" aria-hidden="true">
        <label for="application_company">Leave this field empty</label>
        <input type="text" id="application_company" name="_gotcha" tabindex="-1" autocomplete="off">
      </div>

      <div class="form-section">
        <div class="form-section__header">
          <span class="form-section__number">1</span>
          <div>
            <h3 class="form-section__title">Contact and business</h3>
            <p class="form-section__copy">Enough information to identify and respond to the request.</p>
          </div>
        </div>
        <div class="form-grid--application">
          <div><label for="first_name">First name <span aria-hidden="true">*</span></label><input type="text" id="first_name" name="first_name" required autocomplete="given-name"></div>
          <div><label for="last_name">Last name <span aria-hidden="true">*</span></label><input type="text" id="last_name" name="last_name" required autocomplete="family-name"></div>
          <div><label for="email">Business email <span aria-hidden="true">*</span></label><input type="email" id="email" name="email" required autocomplete="email" inputmode="email" spellcheck="false"></div>
          <div><label for="mobile_phone">Mobile phone <span aria-hidden="true">*</span></label><input type="tel" id="mobile_phone" name="mobile_phone" required autocomplete="tel" inputmode="tel"><p class="input-help">Used for service-related follow-up. Marketing texts require the separate optional consent below.</p></div>
          <div><label for="legal_company_name">Legal company name <span aria-hidden="true">*</span></label><input type="text" id="legal_company_name" name="legal_company_name" required autocomplete="organization"></div>
        </div>
      </div>

      <div class="form-section form-section--accent">
        <div class="form-section__header">
          <span class="form-section__number">2</span>
          <div>
            <h3 class="form-section__title">Funding request</h3>
            <p class="form-section__copy">These details usually determine the realistic product lane.</p>
          </div>
        </div>
        <div class="form-grid--application">
          <div><label for="business_country">Business location</label><select id="business_country" name="business_country"><option value="">Select country</option><option value="Canada">Canada</option><option value="United States">United States</option></select></div>
          <div><label for="currency">Currency for amounts and revenue</label><select id="currency" name="currency"><option value="">Select currency</option><option value="CAD">CAD — Canadian dollars</option><option value="USD">USD — U.S. dollars</option></select><p class="input-help">Use this currency for all amount and revenue ranges below. Calculator estimates use USD.</p></div>
          <div><label for="product_interest">Financing type</label><select id="product_interest" name="product_interest"><option value="">Not sure yet</option><option>Working capital loan</option><option>Line of credit</option><option>Term loan</option><option>Equipment financing</option><option>Factoring or invoice finance</option><option>PO financing</option><option value="SBA 7(a)">SBA 7(a) — U.S. business</option><option>Bridge or mortgage financing</option></select></div>
          <div><label for="amount_requested">Amount requested <span aria-hidden="true">*</span></label><select id="amount_requested" name="amount_requested" required><option value="">Select range</option><option>Under $25,000</option><option>$25,000-$50,000</option><option>$50,000-$100,000</option><option>$100,000-$250,000</option><option>$250,000-$500,000</option><option>$500,000-$1,000,000</option><option>$1,000,000+</option></select></div>
          <div><label for="timeline">Preferred timeline <span aria-hidden="true">*</span></label><select id="timeline" name="timeline" required><option value="">Select timing</option><option>Need it in 24-72 hours</option><option>Need it within 1 week</option><option>Need it within 2-4 weeks</option><option>Need it within 30-60 days</option><option>Planning ahead / exploring</option></select></div>
          <div><label for="monthly_revenue">Estimated monthly revenue <span aria-hidden="true">*</span></label><select id="monthly_revenue" name="monthly_revenue" required><option value="">Select range</option><option>Under $20,000</option><option>$20,000-$50,000</option><option>$50,000-$100,000</option><option>$100,000-$250,000</option><option>$250,000-$500,000</option><option>$500,000+</option></select></div>
          <div class="form-group--full"><label for="use_of_proceeds">Use of proceeds <span aria-hidden="true">*</span></label><textarea id="use_of_proceeds" name="use_of_proceeds" rows="3" required placeholder="What will the capital fund, why is it needed now, and what happens if timing slips?"></textarea></div>
        </div>
      </div>

      <details class="form-optional">
        <summary>Add optional underwriting context</summary>
        <div class="form-optional__content">
          <div class="form-grid--application">
          <div><label for="best_time">Best contact method or time</label><select id="best_time" name="best_time"><option value="">No preference</option><option>Email first</option><option>Text first</option><option>Morning</option><option>Midday</option><option>Afternoon</option><option>After 4pm</option></select></div>
          <div><label for="time_in_business">Time in business</label><select id="time_in_business" name="time_in_business"><option value="">Select range</option><option>Under 6 months</option><option>6-12 months</option><option>1-2 years</option><option>2-5 years</option><option>5+ years</option></select></div>
          <div class="form-group--full"><label for="current_constraints">Existing debt or constraints</label><textarea id="current_constraints" name="current_constraints" rows="3" placeholder="Existing advances, loans, liens, tax issues, seasonality, collateral, or other constraints"></textarea></div>
          <div><label for="product_interest_other">Other financing need</label><input type="text" id="product_interest_other" name="product_interest_other" placeholder="Describe another financing type" autocomplete="off"></div>

            <div><label for="industry">Industry</label><select id="industry" name="industry"><option value="">Select industry</option><option>Construction</option><option>E-commerce</option><option>Hospitality / restaurant</option><option>Manufacturing</option><option>Medical / healthcare</option><option>Professional services</option><option>Real estate / investor</option><option>Retail</option><option>Transportation / logistics</option><option>Wholesale / distribution</option><option>Other</option></select></div>
            <div><label for="state">Province, territory, or state</label><select id="state" name="state"><option value="">Select location</option><optgroup label="Canada"><option>Alberta</option><option>British Columbia</option><option>Manitoba</option><option>New Brunswick</option><option>Newfoundland and Labrador</option><option>Northwest Territories</option><option>Nova Scotia</option><option>Nunavut</option><option>Ontario</option><option>Prince Edward Island</option><option>Quebec</option><option>Saskatchewan</option><option>Yukon</option></optgroup><optgroup label="United States"><option>Alabama</option><option>Alaska</option><option>Arizona</option><option>Arkansas</option><option>California</option><option>Colorado</option><option>Connecticut</option><option>Delaware</option><option>District of Columbia</option><option>Florida</option><option>Georgia</option><option>Hawaii</option><option>Idaho</option><option>Illinois</option><option>Indiana</option><option>Iowa</option><option>Kansas</option><option>Kentucky</option><option>Louisiana</option><option>Maine</option><option>Maryland</option><option>Massachusetts</option><option>Michigan</option><option>Minnesota</option><option>Mississippi</option><option>Missouri</option><option>Montana</option><option>Nebraska</option><option>Nevada</option><option>New Hampshire</option><option>New Jersey</option><option>New Mexico</option><option>New York</option><option>North Carolina</option><option>North Dakota</option><option>Ohio</option><option>Oklahoma</option><option>Oregon</option><option>Pennsylvania</option><option>Rhode Island</option><option>South Carolina</option><option>South Dakota</option><option>Tennessee</option><option>Texas</option><option>Utah</option><option>Vermont</option><option>Virginia</option><option>Washington</option><option>West Virginia</option><option>Wisconsin</option><option>Wyoming</option></optgroup></select></div>
            <div><label for="entity_type">Entity type</label><select id="entity_type" name="entity_type"><option value="">Select entity type</option><option>Corporation</option><option>LLC</option><option>Nonprofit</option><option>Partnership</option><option>S-Corp</option><option>Sole Proprietorship</option></select></div>
            <div><label for="fico_range">Estimated FICO range</label><select id="fico_range" name="fico_range"><option value="">Select range</option><option>Below 550</option><option>550-599</option><option>600-649</option><option>650-699</option><option>700-749</option><option>750+</option><option>Not sure</option></select></div>
            <div class="form-group--full"><label for="additional_context">Anything else that matters?</label><textarea id="additional_context" name="additional_context" rows="3" placeholder="Optional context from a calculator or anything else that helps explain the request"></textarea></div>
          </div>
        </div>
      </details>

      <div class="notice-card">
        <p class="eyebrow">Optional marketing-text consent</p>
        <div class="checkbox-list">
          <div class="checkbox-list__item">
            <input type="checkbox" id="consent_sms_marketing" name="consent_sms_marketing" value="Yes">
            <div class="checkbox-list__copy">
              <label class="checkbox-list__label" for="consent_sms_marketing">I agree to receive recurring marketing text messages from Nicolas Lescalier and Premium Merchant Funding at the mobile number provided. Message frequency varies. Consent is not a condition of financing. Message and data rates may apply. Reply STOP to opt out or HELP for assistance.</label>
              <p class="checkbox-list__legal">Support: <a href="tel:+13056993636">305.699.3636</a>. SMS consent data will not be shared with third parties or affiliates for their own marketing purposes. See the <a href="/terms-and-conditions/">Terms</a> and <a href="/privacy-policy/">Privacy Policy</a>.</p>
            </div>
          </div>
        </div>
      </div>

      <p class="form-submit-note">By submitting, you authorize Nicolas Lescalier and Premium Merchant Funding to contact you by phone or email about this request and to share the submitted business information with appropriate financing providers for evaluation. Submission does not guarantee approval or authorize a credit pull. Review the <a href="/terms-and-conditions/">Terms and Conditions</a> and <a href="/privacy-policy/">Privacy Policy</a>.</p>
      <p class="form-submit-note"><strong>Do not upload or enter sensitive documents here.</strong> SSN/SIN, tax returns, bank statements, IDs, and account credentials should only be provided later through an approved secure process.</p>

      <div class="cta-row">
        <p class="form-status" data-form-status hidden aria-live="polite"></p>
        <button class="button" type="submit">Submit financing request</button>
        <a class="button button--secondary" href="/contact/">Send a shorter inquiry</a>
      </div>
    </form>
  </div>
</section>
