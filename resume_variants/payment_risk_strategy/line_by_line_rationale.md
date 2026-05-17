# Line-by-Line Rationale: Payment Risk Strategy Resume

Date: 2026-05-16  
Variant: `payment_risk_strategy_resume`

## Overall Strategy

This version targets risk strategy, fraud analytics, payment risk, marketplace integrity, and trust/safety data science roles. The logic is to make the candidate's story feel continuous:

1. Goldman Sachs: production risk monitoring, anomaly/root-cause analysis, backtesting, governance, and high-stakes decision support.
2. ARB Interactive: direct payments-adjacent platform analytics, abnormal behavior detection, interventions, and abuse-prevention/user-experience tradeoffs.
3. Blinkle AI: two-sided marketplace metrics, suspicious behavior detection, LLM-derived signals, and experimentation.

The resume intentionally avoids overstating direct card-fraud, chargeback, or payment-loss ownership where the original experience did not prove it. Instead, it uses adjacent but credible language: risk monitoring, abnormal behavior, high-risk cohorts, false investigation triggers, product friction, decision signals, interventions, and governance.

## Header

### `Yihan Li`

Kept unchanged. The name is clean and ATS-friendly.

### `yihanli0829@gmail.com | 310-689-8174 | Los Angeles, CA 90024`

Kept unchanged from the original resume. For California DS roles, the Los Angeles location is useful because it signals West Coast availability.

## Target Summary

### `Data Scientist / Quant Strategist focused on risk decisioning, payment-adjacent analytics, marketplace experimentation, and production monitoring.`

Added a short targeted summary because this resume is a pivot from quant/finance into fintech risk DS. The phrase "Data Scientist / Quant Strategist" preserves the current Goldman brand while immediately pointing the reader toward DS. "Risk decisioning" is the most important target-role phrase for Uber/PayPal/Block/Ramp-style roles. "Payment-adjacent analytics" is intentionally accurate: ARB is a Payments internship, but not necessarily card-network fraud or chargebacks.

### `Experienced in SQL/Python analysis over large-scale event and transaction-level data, causal inference, backtesting, anomaly detection, and translating ambiguous risk signals into product, operations, and governance decisions.`

This sentence is the resume's thesis. It links the tools and methods that appear across target JDs: SQL/Python, large-scale events, transaction-level data, causal inference, backtesting, anomaly detection, and cross-functional decisions. The final phrase broadens the audience from model teams to product, risk ops, and governance stakeholders.

## Goldman Sachs

### `Own production risk-monitoring analytics across transaction- and entity-level pricing/liquidity signals for 100+ global entities, analyzing billions of records to detect anomalies, quantify risk shifts, and trigger drill-down investigations.`

This keeps the strongest facts from the original bullet: production monitoring, transaction/entity-level signals, 100+ entities, billions of records. The wording changes "metrics monitoring" into "risk-monitoring analytics" to sound closer to payment risk DS. "Detect anomalies," "quantify risk shifts," and "drill-down investigations" map directly to fraud/risk analytics JDs without falsely claiming payment fraud.

### `Decompose abnormal movements in ratio-based risk indicators into pricing, funding, and balance-sheet drivers, separating structural changes from noisy market moves across multi-billion-record datasets and cross-region cohorts.`

This bullet keeps the original root-cause analysis content but makes the analytical skill clearer. Payment risk teams care about separating true risk pattern changes from noise; this bullet shows that ability in a Goldman context. "Cross-region cohorts" also connects to cohort-based platform analysis.

### `Apply difference-in-differences and historical backtesting to evaluate policy and market changes, reducing false investigation triggers and improving confidence in risk-control decisions before stakeholder review.`

This bullet is deliberately placed third because it is one of the strongest bridges to risk strategy roles. Uber and similar teams ask for experimentation, rollout monitoring, and fraud-rule evaluation. DID and backtesting show quasi-experimental rigor. "False investigation triggers" is safer than "false positives" unless the original system had a formal classifier.

### `Build auditable validation and control workflows for AI-assisted analytical outputs, ensuring model-driven insights are reliable, explainable, and usable in high-stakes governance and model-validation contexts.`

This bullet keeps the original AI workflow/governance idea but makes it relevant to fintech risk teams, where auditability, controls, and explainability matter. "Model-driven insights" is broad enough to cover AI-assisted analytics without overstating deployed ML model ownership.

## Blinkle AI

### `Designed the core risk and quality metrics framework for a two-sided job marketplace, defining north-star and diagnostic metrics across match quality, recommendation quality, suspicious behavior, and application conversion.`

This reframes the original marketplace metrics work as a risk-quality decision framework. The target reader should see marketplace/product DS plus risk thinking. "North-star and diagnostic metrics" is product DS language; "suspicious behavior" and "quality metrics" make it relevant to marketplace integrity.

### `Analyzed millions of production user events with SQL and Python to identify low-quality or suspicious behavior patterns that degraded matching quality, surfacing high-risk cohorts and downstream product friction points.`

This bullet emphasizes scale, production data, SQL/Python, suspicious behavior, high-risk cohorts, and friction. These are all reusable in payment risk interviews. It also avoids claiming fraud labels if the platform only had quality/suspicious-behavior proxies.

### `Built scoring features from LLM-derived resume and job-description signals for screening/ranking pipelines, improving top-match accuracy by 37% and creating more structured decision signals for product teams.`

This preserves the original 37% impact while making the work sound like a decisioning pipeline. "LLM-derived signals" is useful for modern DS roles, but the bullet avoids making the whole resume feel like an LLM resume. The phrase "structured decision signals" connects this work to risk scoring and ranking.

### `Designed holdout and A/B experiments for screening and ranking interventions, quantifying precision-conversion-friction tradeoffs and increasing application conversion by 41%.`

This keeps the original 41% impact and strengthens the risk-product logic. Payment risk strategy roles often involve interventions that reduce bad behavior but can hurt good users. "Precision-conversion-friction tradeoffs" mirrors that decision problem.

## ARB Interactive

### `Analyzed hundreds of millions of payment-adjacent interaction events from a 2.1M-user live-streaming platform to detect abnormal traffic, creator abuse, and high-risk behavioral cohorts for intervention and traffic-control strategies.`

This is the most direct payment/risk anchor. It keeps the original scale and 2.1M-user fact, adds "payment-adjacent" for relevance, and uses "abnormal traffic," "creator abuse," and "high-risk cohorts" to match fraud/risk strategy vocabulary. It avoids claiming card fraud or chargebacks.

### `Developed a creator-level causal impact framework using counterfactual baselines and retention modeling to estimate incremental ROI of incentive and intervention policies, improving policy ROI by 18%.`

This bullet keeps the original causal impact and 18% ROI result. "Creator-level" adds specificity. "Incentive and intervention policies" shows this was not only analysis but policy decision support.

### `Built behavioral segmentation models with K-Means clustering to identify heterogeneous response and risk patterns, enabling targeted interventions that increased DAU by 12% while reducing broad, unnecessary user friction.`

This preserves K-Means and the 12% DAU impact while tying the work to risk strategy. "Reducing broad, unnecessary user friction" is important because payment risk roles constantly balance fraud prevention with user experience. The wording suggests targeted rather than blunt interventions.

### `Designed and analyzed A/B tests for policy interventions, measuring impact on creator retention, content quality, platform health, and the tradeoff between abuse prevention and user experience.`

This bullet closes ARB with the exact interview story we want: intervention design, experiment analysis, and tradeoff thinking. "Platform health" and "abuse prevention vs user experience" are strong trust/safety and risk analytics phrases.

## Education

### `University of California, Los Angeles | Master of Quantitative Economics | Jul 2025`

Kept near the bottom because the experience section is stronger for this target. UCLA and the quantitative master's still matter, especially for DS roles requiring statistics/econometrics.

### `GPA: 4.00/4.00 | Coursework: Database Management, Machine Learning, Time Series Forecasting, Optimization Methods`

Compressed into one line to save space. The chosen coursework supports the target: databases for SQL/data work, ML for modeling, time series for monitoring, optimization for threshold/decision problems.

### `Open For Good Project: Used Qualtrics surveys and RNN models to quantify sentiment in sustainability disclosures.`

Kept but compressed. It shows NLP/modeling breadth, but it is not central to payment risk, so it should not take much space.

### `Nanjing University | Bachelor of Economics, Minor in Mathematics | Jul 2023`

Kept because economics + math reinforces quant rigor.

### `GPA: 3.93/4.00 | Coursework: Mathematical Statistics, Stochastic Processes, Regression Analysis, Statistical Computing`

Kept the coursework most relevant to DS/risk modeling. Removed extra academic detail to protect one-page fit.

### `Honors: National Scholarship, Top 1%; First Place, Citi Group Fintech Competition.`

Kept because the Citi fintech competition is unusually relevant for fintech roles and helps the broader story.

## Technical Skills

### `Risk & Analytics: Risk Metrics Design, Fraud/Abuse Monitoring, Risk Decisioning, Anomaly Detection, Backtesting, Root-Cause Analysis, Cohort Analysis, Segmentation, Experimentation, Causal Inference, Difference-in-Differences`

This is the most important skills row for this variant. It front-loads payment risk strategy language and mirrors JD terms from Uber/PayPal/Block/Ramp. "Fraud/Abuse Monitoring" is credible because the resume has abnormal behavior and abuse-prevention work, but it does not overclaim direct fraud-loss ownership.

### `Machine Learning: Regression, Classification, Tree-Based Models, XGBoost, Feature Engineering, Model Validation, LLM Structured Signal Extraction`

This row keeps ML credibility while avoiding a pure MLE framing. It also includes model validation from Goldman and LLM signal extraction from Blinkle.

### `Tools: Python, SQL, R, Spark, Airflow, AWS, Tableau, Stata, NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn`

This row is ATS-friendly and keeps tools compact. SQL and Python appear in both bullets and skills; Spark/Airflow/AWS/Tableau are preserved from the original skills section because they match many fintech risk DS JDs.

## What Changed From The Original Resume

- Added a targeted summary to make the pivot obvious within the first 10 seconds.
- Reduced repeated phrasing and made every experience support the payment risk story.
- Converted generic "risk metrics" language into "risk decisioning," "anomaly detection," "high-risk cohorts," "interventions," "backtesting," and "friction tradeoffs."
- Preserved all major quantified impacts from the original resume: 100+ entities, billions of records, 37% top-match accuracy, 41% conversion increase, 2.1M users, hundreds of millions of events, 18% ROI lift, and 12% DAU lift.
- Avoided unverified claims such as chargeback reduction, fraud-loss ownership, manual-review queue ownership, or real-time payment model deployment.

## Best Use Cases

Use this version for:

- Uber Risk Decision Science / Fraud Risk
- PayPal Fraud Risk / Risk Analytics / Product Analytics
- Block / Cash App Risk Strategy
- DoorDash Fraud / Integrity / Trust & Safety DS
- Affirm risk analytics or underwriting analytics roles
- Ramp / Brex risk strategy, credit risk, fraud strategy roles
- Chime authentication risk or financial-risk analytics roles

For Stripe, Plaid, Visa, Coinbase, Socure, Sardine, or other model-heavy fraud DS roles, build the second variant after adding a payment fraud decisioning project.
