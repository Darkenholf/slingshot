# Yihan Li - Payment Risk Strategy Resume V2 With Rationale

Date: 2026-05-17  
Source Word reviewed: C:\Users\17718\OneDrive\Desktop\Slingshot\Payment DS\Yihan Li_Payments.docx  
Target lane: Payment Risk Strategy / Fraud Analytics / AI-Assisted Risk Decision Science / Marketplace Integrity DS
## Optimized Resume Markdown

# Yihan Li

yihanli0829@gmail.com | 310-689-8174 | Los Angeles, CA 90024

AI-focused Data Scientist specializing in **risk decisioning**, payment-adjacent analytics, and marketplace experimentation. Strong in SQL/Python, AI-assisted analytics, causal inference, backtesting, anomaly detection, and translating noisy risk signals into product, operations, and governance decisions.

## PROFESSIONAL EXPERIENCE

### Goldman Sachs

**Quantitative Strategist** | New York, NY | Nov 2025 - Present

- Design and own **AI-assisted production risk metrics** across transaction- and entity-level pricing/liquidity signals for 100+ global entities, analyzing billions of records to detect anomalies and trigger drill-down investigations.
- Built **root-cause decomposition frameworks** for abnormal risk-indicator movements across multi-billion-record datasets, separating pricing, funding, balance-sheet, and regional drivers while reducing false alerts by 95%.
- Applied **DID and historical backtesting** on multi-billion-record historical panels across 100+ entities to evaluate policy and market changes before stakeholder review.
- Developed **thresholding and investigation-prioritization logic** that converted continuous AI-assisted risk signals into actionable review paths, accelerating governance and validation decisions by 30%.
- Built **AI analytical validation workflows** with source traceability, edge-case checks, explainability review, and human-in-the-loop controls, improving auditability across 100+ entity-level monitoring processes.

### Blinkle AI (LLM-powered job marketplace)

**Data Scientist (Part-time), Product** | New York, NY | Sep 2025 - Jan 2026

- Designed the **risk and quality metrics framework** for a two-sided job marketplace, defining north-star and diagnostic metrics across match quality, suspicious behavior, and application conversion.
- Analyzed millions of production user events with **SQL and Python** to identify low-quality or suspicious behavior patterns, surfacing high-risk cohorts and product friction points.
- Built **LLM-derived scoring features** from resume and job-description signals for screening/ranking pipelines, improving top-match accuracy by 37%.
- Designed holdout and **A/B experiments** for screening and ranking interventions, quantifying false-match vs missed-match and precision-conversion-friction tradeoffs, increasing application conversion by 41%.

### ARB Interactive

**Data Scientist Intern, Payments** | Miami, FL | Jun 2024 - Sep 2024

- Analyzed hundreds of millions of **payment-adjacent interaction events** from a 2.1M-user platform to detect abnormal traffic, creator abuse, and high-risk behavioral cohorts.
- Developed a **causal impact framework** with counterfactual baselines and retention modeling to estimate incremental ROI of incentive and intervention policies, improving policy ROI by 18%.
- Built **behavioral segmentation models** with K-Means to identify response and risk patterns, enabling targeted interventions that increased DAU by 12% while reducing broad user friction.
- Designed, analyzed, and monitored **A/B-tested policy interventions**, measuring effects on creator retention, content quality, platform health, and abuse-prevention/user-experience tradeoffs.

## EDUCATION

**University of California, Los Angeles** | Master of Quantitative Economics | Jul 2025  
GPA: 4.00/4.00 | Coursework: Database Management, Machine Learning, Time Series Forecasting, Optimization Methods

**Nanjing University** | Bachelor of Economics, Minor in Mathematics | Jul 2023  
GPA: 3.93/4.00 | Coursework: Mathematical Statistics, Stochastic Processes, Regression Analysis, Statistical Computing  
Honors: National Scholarship, Top 1%; First Place, Citi Group Fintech Competition.

## TECHNICAL SKILLS

**AI, Risk & Decision Analytics:** AI-Assisted Analytics, Risk Metrics Design, Fraud/Abuse Monitoring, Risk Decisioning, Risk Scoring, Thresholding, Anomaly Detection, Backtesting, Root-Cause Analysis, Cohort Analysis, A/B Testing, Causal Inference, Difference-in-Differences  
**Machine Learning & Evaluation:** Regression, Classification, Tree-Based Models, XGBoost, Feature Engineering, Model Validation, Explainability, LLM Structured Signal Extraction  
**Data Tools:** Python, SQL, R, Spark, Airflow, AWS, Tableau, Stata, NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn
---

## Modification Rationale

## 1. Overall Direction

This version keeps the branch strategy: target payment risk strategy / fraud analytics roles first, while making the AI angle visible enough for current fintech and big-tech risk teams. The resume therefore emphasizes **AI-assisted analytics, risk decisioning, backtesting, thresholds, investigations, monitoring, false-positive/friction tradeoffs, and stakeholder decisions**.

I did not add hard claims such as chargeback reduction, account takeover detection, synthetic identity detection, real-time model serving, or direct fraud-loss ownership because the Word resume and repo notes do not prove those facts. The stronger strategy is to use credible adjacent language now and add harder fraud-modeling language later after a portfolio project.

Current JD language supports this direction. For example, Plaid's Fraud DS posting emphasizes metrics, dashboards, product health, backtests, SQL/Python, experimentation, and model/rule evaluation; this V2 intentionally mirrors that language without overclaiming.

## 2. Word Comment: Summary Too Long

Original summary was strong but dense and did not foreground AI enough. I shortened it to two sentences and added AI while keeping only the highest-value keywords:

- `AI-focused Data Scientist` / `AI-assisted analytics`
- `risk decisioning`
- `payment-adjacent analytics`
- `marketplace experimentation`
- `SQL/Python`
- `causal inference`
- `backtesting`
- `anomaly detection`
- `product, operations, and governance decisions`

Reason: the top summary should be readable in a 5-10 second recruiter scan. It now fits the comment request of being shorter and less crowded while preserving the payment/risk positioning.

## 3. Word Comment: Add Selective Bold

I added bolding sparingly, usually one phrase per bullet and occasionally one method or tool phrase. The goal is to help a recruiter skim the resume without making the page look noisy.

Bolded phrases were chosen because they map directly to target JD categories:

- Risk system ownership: **production risk metrics**, **risk and quality metrics framework**
- Analytical methods: **root-cause decomposition frameworks**, **DID and historical backtesting**, **causal impact framework**
- Decisioning language: **thresholding and investigation-prioritization logic**
- AI/risk governance: **AI-assisted validation workflows**
- Marketplace/fraud transfer: **payment-adjacent interaction events**, **behavioral segmentation models**
- Experimentation: **A/B experiments**, **A/B-tested policy interventions**

## 4. Goldman Sachs Changes

### Bullet 1

Shortened while preserving the strongest facts: production risk metrics, transaction/entity-level signals, 100+ global entities, billions of records, anomaly detection, investigations.

Reason: this is the resume's first and most important bullet. It now says metric ownership and risk-scale clearly without overloading the line with every possible detail.

### Bullet 2

Shortened the root-cause bullet to focus on the core transferable skill: decomposing abnormal risk movements into drivers.

Reason: payment risk teams need people who can diagnose whether a risk metric moved because of real risk, user mix, policy, market structure, or data noise. This bullet shows that skill in Goldman language.

### Bullet 3

Kept DID/backtesting and changed the framing toward missed-risk vs false-positive escalation costs.

Reason: this is the closest bridge to fraud/risk policy evaluation. It shows the candidate thinks in risk tradeoffs, not just statistical significance.

### Bullet 4

Compressed the thresholding bullet and kept investigation prioritization, actionable review paths, and monitoring.

Reason: this answers the repo's identified gap: show more rules/thresholds/ops loop, but do it safely without claiming ownership of a formal fraud manual-review queue.

### Bullet 5

Shortened the AI validation bullet and kept source traceability, edge cases, explainability, and human-in-the-loop controls.

Reason: AI-assisted analytics is useful, but the resume should not drift into a generic AI resume. This version ties AI to risk governance and auditability.

## 5. Blinkle AI Changes

### Bullet 1

Kept the metrics-framework bullet but tightened the metric list.

Reason: this supports marketplace risk/product roles and gives a clean bridge to Uber, DoorDash, Plaid, and fraud-product analytics roles.

### Bullet 2

Kept SQL/Python, production events, suspicious behavior, high-risk cohorts, and friction.

Reason: it transfers naturally to fraud/risk DS: identify bad behavior patterns, segment risk, and reduce friction for good users.

### Bullet 3

Shortened the LLM scoring bullet and preserved the 37% impact.

Reason: LLM-derived scoring features are valuable, but the most relevant part for payment risk is the structured scoring/decision-signal logic, not the LLM itself.

### Bullet 4

Kept the 41% conversion result and clarified false-match vs missed-match plus precision-conversion-friction tradeoffs.

Reason: this is a marketplace version of the fraud false-positive/false-negative tradeoff. It gives the candidate a strong interview story around balancing quality, conversion, and user friction.

## 6. ARB Interactive Changes

### Title Fix

Changed `Data Scientist Intern, Paymentsn` to `Data Scientist Intern, Payments`.

Reason: this was a visible typo in the Word text and should be fixed before any application.

### Bullet 1

Shortened the long ARB first bullet to one clean idea: payment-adjacent events at scale used to detect abnormal traffic, creator abuse, and high-risk cohorts.

Reason: the original was directionally good but too packed. This is the strongest direct payment/risk anchor, so it needs to be easy to read.

### Bullet 2

Kept the causal impact framework and 18% ROI result.

Reason: causal/policy evaluation is central to risk strategy roles where interventions must be evaluated against business and user-experience tradeoffs.

### Bullet 3

Shortened the K-Means bullet and kept the 12% DAU impact plus reduced broad user friction.

Reason: this directly supports the risk strategy story: targeted interventions are better than blunt rules that hurt good users.

### Bullet 4

Kept post-rollout monitoring and abuse-prevention/user-experience tradeoff language.

Reason: the repo repeatedly identifies the missing loop as analysis -> launch/intervention -> monitoring. This bullet completes that loop.

## 7. Education Change: Remove Open For Good Project

I removed the Open For Good project from this payment risk version.

Reason: it is a good academic NLP/RNN project, but it does not help the first payment risk strategy variant enough to justify the space. The resume already has LLM and AI validation signals through Blinkle and Goldman. Removing it creates room and makes the page more focused.

If applying to AI Evaluation / ML Evaluation roles later, this project can return in that separate variant.

## 8. Skills Rewrite

I changed the skills section from four broader rows into three tighter rows:

- `Risk & Decision Analytics`
- `Machine Learning & Evaluation`
- `Data Tools`

Reason: this is more ATS-friendly and better aligned with payment risk JDs. It keeps all useful original tools, but the first row now carries the most important target keywords: risk decisioning, risk scoring, thresholding, anomaly detection, backtesting, A/B testing, causal inference, and DID.

## 9. What This Version Is Best For

Use this version for:

- Plaid Data Scientist - Fraud
- PayPal Payments Risk / Fraud Risk / Identity Risk analytics
- Ramp / Brex / BILL risk analytics or risk strategy
- Block / Cash App risk analytics
- Uber Risk / Identity / Payments DS
- DoorDash Integrity / Fraud / Trust & Safety DS
- Whatnot / marketplace risk and fraud analytics

For Stripe Radar, Visa Predictive Fraud Intelligence, Robinhood Fraud ML, Coinbase Risk ML, Socure, Sardine, or Signifyd, this is usable but not ideal. Those roles should get the second variant after adding a Payment Fraud Decisioning Simulator project with classification, PR-AUC, threshold policy, backtesting, and drift monitoring.

## 10. Main Tradeoff

This V2 is more concise and application-ready than the Word draft. The cost is that it removes some explanatory detail, especially around governance and cross-region scale. That is acceptable because resumes should open doors; the detailed story can be told in interviews and in the rationale file.

Source used for current JD language check: Plaid Data Scientist - Fraud official posting, accessed 2026-05-17: https://plaid.com/careers/openings/engineering/san-francisco/data-scientist-fraud/





