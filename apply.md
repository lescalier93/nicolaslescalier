---
title: "Business Financing Application"
description: "Submit a concise business financing request for working capital, term loans, equipment, factoring, SBA, bridge, or commercial mortgage options."
permalink: /apply/
layout: default
image: "/assets/social-apply.png"
breadcrumb_title: Application
---

<section class="section">
  <div class="section-band">
    <div class="section-band__panel">
      <p class="eyebrow">Business financing application</p>
      <h1>Start with the facts that determine product fit.</h1>
      <p>This concise intake covers the amount, timing, revenue, use of proceeds, and current constraints. It is enough for an initial broker review without collecting sensitive documents on a public form.</p>
      <div class="section-band__actions">
        <a class="button" href="#application-form">Start application</a>
        <a class="button button--secondary" href="https://calendly.com/nlescalier/funding" target="_blank" rel="noopener noreferrer">Book a call instead</a>
      </div>
    </div>
    <div class="mini-grid">
      <article class="mini-card">
        <h3>Usually about 3 minutes</h3>
        <p>Nine required fields plus focused selectors. Optional underwriting context stays collapsed unless you want to add it.</p>
      </article>
      <article class="mini-card">
        <h3>No sensitive documents</h3>
        <p>Do not submit SSN, tax returns, bank statements, login credentials, government ID, or bank-account information here.</p>
      </article>
    </div>
  </div>
</section>

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
      const radio = Array.from(document.querySelectorAll('input[name="product_interest"]')).find(
        (input) => input.value.toLowerCase() === productInterest.toLowerCase()
      );
      if (radio) radio.checked = true;
      else setFieldValue("product_interest_other", productInterest);
    }

    setSelectByText("amount_requested", params.get("amount_requested"));
    setFieldValue("use_of_proceeds", params.get("use_of_proceeds"));
    setFieldValue("additional_context", params.get("additional_context"));

    const leadSource = params.get("lead_source") || "website";
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
          product_interest: productInterest || "",
        });
      }
    });
  });
</script>

<section class="section" id="application-form">
  <p class="eyebrow">Financing request</p>
  <h2>Business financing request</h2>
  <p class="section-intro">Choose the closest answers. This does not lock you into a product or authorize a credit pull.</p>

  <div class="application-frame">
    <div class="application-intro-card">
      <div>
        <strong>Initial review only</strong>
        <span>Nicolas reviews fit as a commercial finance broker. Third-party providers make final underwriting and approval decisions.</span>
      </div>
      <div>
        <strong>Secure follow-up</strong>
        <span>If documents are needed, they should be requested later through an appropriate secure process.</span>
      </div>
    </div>

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

      <div class="form-section form-section--accent">
        <div class="form-section__header">
          <span class="form-section__number">1</span>
          <div>
            <h3 class="form-section__title">What are you trying to finance?</h3>
            <p class="form-section__copy">Choose the closest product or describe the need in your own words.</p>
          </div>
        </div>
        <div class="choice-grid">
          <div class="choice-card"><input type="radio" id="product_working_capital" name="product_interest" value="Working capital loan"><label for="product_working_capital"><strong>Working capital</strong><span>Fast, short-duration capital</span></label></div>
          <div class="choice-card"><input type="radio" id="product_loc" name="product_interest" value="Line of credit"><label for="product_loc"><strong>Line of credit</strong><span>Repeat-use revolving access</span></label></div>
          <div class="choice-card"><input type="radio" id="product_term" name="product_interest" value="Term loan"><label for="product_term"><strong>Term loan</strong><span>Fixed repayment for growth or refinance</span></label></div>
          <div class="choice-card"><input type="radio" id="product_equipment" name="product_interest" value="Equipment financing"><label for="product_equipment"><strong>Equipment</strong><span>Vehicles, machinery, or devices</span></label></div>
          <div class="choice-card"><input type="radio" id="product_factoring" name="product_interest" value="Factoring or invoice finance"><label for="product_factoring"><strong>Factoring</strong><span>Receivables-based liquidity</span></label></div>
          <div class="choice-card"><input type="radio" id="product_po" name="product_interest" value="PO financing"><label for="product_po"><strong>PO financing</strong><span>Purchase-order fulfillment</span></label></div>
          <div class="choice-card"><input type="radio" id="product_sba" name="product_interest" value="SBA 7(a)"><label for="product_sba"><strong>SBA 7(a)</strong><span>Longer-term government-backed path</span></label></div>
          <div class="choice-card"><input type="radio" id="product_cre" name="product_interest" value="Bridge or mortgage financing"><label for="product_cre"><strong>Bridge / CRE</strong><span>Acquisition, refinance, construction, or transition</span></label></div>
        </div>
        <div>
          <label for="product_interest_other">Not sure or something else?</label>
          <input type="text" id="product_interest_other" name="product_interest_other" placeholder="Describe the business problem or transaction" autocomplete="off">
        </div>
      </div>

      <div class="form-section">
        <div class="form-section__header">
          <span class="form-section__number">2</span>
          <div>
            <h3 class="form-section__title">Contact and business</h3>
            <p class="form-section__copy">Enough information to identify and respond to the request.</p>
          </div>
        </div>
        <div class="form-grid--application">
          <div><label for="first_name">First name</label><input type="text" id="first_name" name="first_name" required autocomplete="given-name"></div>
          <div><label for="last_name">Last name</label><input type="text" id="last_name" name="last_name" required autocomplete="family-name"></div>
          <div><label for="email">Business email</label><input type="email" id="email" name="email" required autocomplete="email" inputmode="email" spellcheck="false"></div>
          <div><label for="mobile_phone">Mobile phone</label><input type="tel" id="mobile_phone" name="mobile_phone" required autocomplete="tel" inputmode="tel"><p class="input-help">Used for service-related follow-up. Marketing texts require the separate optional consent below.</p></div>
          <div><label for="legal_company_name">Legal company name</label><input type="text" id="legal_company_name" name="legal_company_name" required autocomplete="organization"></div>
          <div><label for="best_time">Best contact method or time</label><select id="best_time" name="best_time"><option value="">No preference</option><option>Email first</option><option>Text first</option><option>Morning</option><option>Midday</option><option>Afternoon</option><option>After 4pm</option></select></div>
        </div>
      </div>

      <div class="form-section form-section--accent">
        <div class="form-section__header">
          <span class="form-section__number">3</span>
          <div>
            <h3 class="form-section__title">Funding request</h3>
            <p class="form-section__copy">These details usually determine the realistic product lane.</p>
          </div>
        </div>
        <div class="form-grid--application">
          <div><label for="amount_requested">Amount requested</label><select id="amount_requested" name="amount_requested" required><option value="">Select range</option><option>Under $25,000</option><option>$25,000-$50,000</option><option>$50,000-$100,000</option><option>$100,000-$250,000</option><option>$250,000-$500,000</option><option>$500,000-$1,000,000</option><option>$1,000,000+</option></select></div>
          <div><label for="timeline">Preferred timeline</label><select id="timeline" name="timeline" required><option value="">Select timing</option><option>Need it in 24-72 hours</option><option>Need it within 1 week</option><option>Need it within 2-4 weeks</option><option>Need it within 30-60 days</option><option>Planning ahead / exploring</option></select></div>
          <div><label for="monthly_revenue">Estimated monthly revenue</label><select id="monthly_revenue" name="monthly_revenue" required><option value="">Select range</option><option>Under $20,000</option><option>$20,000-$50,000</option><option>$50,000-$100,000</option><option>$100,000-$250,000</option><option>$250,000-$500,000</option><option>$500,000+</option></select></div>
          <div><label for="time_in_business">Time in business</label><select id="time_in_business" name="time_in_business"><option value="">Select range</option><option>Under 6 months</option><option>6-12 months</option><option>1-2 years</option><option>2-5 years</option><option>5+ years</option></select></div>
          <div class="form-group--full"><label for="use_of_proceeds">Use of proceeds</label><textarea id="use_of_proceeds" name="use_of_proceeds" rows="4" required placeholder="What will the capital fund, why is it needed now, and what happens if timing slips?"></textarea></div>
          <div class="form-group--full"><label for="current_constraints">Existing debt or constraints</label><textarea id="current_constraints" name="current_constraints" rows="3" placeholder="Existing advances, loans, liens, tax issues, seasonality, collateral, or other constraints"></textarea></div>
        </div>
      </div>

      <details class="form-optional">
        <summary>Add optional underwriting context</summary>
        <div class="form-optional__content">
          <div class="form-grid--application">
            <div><label for="industry">Industry</label><select id="industry" name="industry"><option value="">Select industry</option><option>Construction</option><option>E-commerce</option><option>Hospitality / restaurant</option><option>Manufacturing</option><option>Medical / healthcare</option><option>Professional services</option><option>Real estate / investor</option><option>Retail</option><option>Transportation / logistics</option><option>Wholesale / distribution</option><option>Other</option></select></div>
            <div><label for="state">Primary operating state</label><select id="state" name="state"><option value="">Select state</option><option>Alabama</option><option>Alaska</option><option>Arizona</option><option>Arkansas</option><option>California</option><option>Colorado</option><option>Connecticut</option><option>Delaware</option><option>District of Columbia</option><option>Florida</option><option>Georgia</option><option>Hawaii</option><option>Idaho</option><option>Illinois</option><option>Indiana</option><option>Iowa</option><option>Kansas</option><option>Kentucky</option><option>Louisiana</option><option>Maine</option><option>Maryland</option><option>Massachusetts</option><option>Michigan</option><option>Minnesota</option><option>Mississippi</option><option>Missouri</option><option>Montana</option><option>Nebraska</option><option>Nevada</option><option>New Hampshire</option><option>New Jersey</option><option>New Mexico</option><option>New York</option><option>North Carolina</option><option>North Dakota</option><option>Ohio</option><option>Oklahoma</option><option>Oregon</option><option>Pennsylvania</option><option>Rhode Island</option><option>South Carolina</option><option>South Dakota</option><option>Tennessee</option><option>Texas</option><option>Utah</option><option>Vermont</option><option>Virginia</option><option>Washington</option><option>West Virginia</option><option>Wisconsin</option><option>Wyoming</option></select></div>
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
      <p class="form-submit-note"><strong>Do not upload or enter sensitive documents here.</strong> SSN, tax returns, bank statements, IDs, and account credentials should only be provided later through an approved secure process.</p>

      <div class="cta-row">
        <p class="form-status" data-form-status hidden aria-live="polite"></p>
        <button class="button" type="submit">Submit financing request</button>
        <a class="button button--secondary" href="/contact/">Send a shorter inquiry</a>
      </div>
    </form>
  </div>
</section>
