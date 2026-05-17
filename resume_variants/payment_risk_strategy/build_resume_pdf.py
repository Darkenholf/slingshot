from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
    KeepTogether,
)


OUT = "/Users/richard/Documents/Slingshot/resume_variants/payment_risk_strategy/Yihan_Li_Payment_Risk_Strategy_DS.pdf"


def p(text, style):
    return Paragraph(text, style)


def role_header(company, location, title, dates, styles):
    top = Table(
        [[p(f"<b>{company}</b>", styles["role_company"]), p(location, styles["right"])]],
        colWidths=[5.1 * inch, 2.0 * inch],
        hAlign="LEFT",
    )
    top.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    bottom = Table(
        [[p(f"<i>{title}</i>", styles["role_title"]), p(dates, styles["right"])]],
        colWidths=[5.1 * inch, 2.0 * inch],
        hAlign="LEFT",
    )
    bottom.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return [top, bottom]


def section(title, styles):
    return [
        Spacer(1, 4),
        Paragraph(f"<b>{title}</b>", styles["section"]),
        HRFlowable(width="100%", thickness=0.55, color=colors.black, spaceBefore=0, spaceAfter=2),
    ]


def bullet(text, styles):
    return Paragraph(text, styles["bullet"], bulletText="•")


def main():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="name", fontName="Helvetica-Bold", fontSize=17.5, leading=19.0, alignment=TA_CENTER, spaceAfter=1))
    styles.add(ParagraphStyle(name="contact", fontName="Helvetica", fontSize=9.4, leading=10.3, alignment=TA_CENTER, spaceAfter=7))
    styles.add(ParagraphStyle(name="section", fontName="Helvetica-Bold", fontSize=10.4, leading=11.0, alignment=TA_LEFT, spaceBefore=0, spaceAfter=0))
    styles.add(ParagraphStyle(name="summary", fontName="Helvetica", fontSize=9.2, leading=10.35, alignment=TA_LEFT, spaceAfter=4))
    styles.add(ParagraphStyle(name="role_company", fontName="Helvetica-Bold", fontSize=10.4, leading=11.0, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name="role_title", fontName="Helvetica", fontSize=9.65, leading=10.35, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name="right", fontName="Helvetica", fontSize=9.65, leading=10.35, alignment=TA_RIGHT))
    styles.add(ParagraphStyle(name="bullet", fontName="Helvetica", fontSize=8.65, leading=9.75, leftIndent=18, firstLineIndent=-9, bulletIndent=4, spaceAfter=1.15))
    styles.add(ParagraphStyle(name="edu", fontName="Helvetica", fontSize=8.55, leading=9.4, spaceAfter=0.25))
    styles.add(ParagraphStyle(name="skills", fontName="Helvetica", fontSize=8.35, leading=9.15, spaceAfter=0.2))

    doc = SimpleDocTemplate(
        OUT,
        pagesize=letter,
        rightMargin=0.43 * inch,
        leftMargin=0.43 * inch,
        topMargin=0.34 * inch,
        bottomMargin=0.32 * inch,
    )

    story = []
    story.append(p("Yihan Li", styles["name"]))
    story.append(p("yihanli0829@gmail.com | 310-689-8174 | Los Angeles, CA 90024", styles["contact"]))

    story.append(p(
        "Data Scientist focused on <b>risk decisioning</b>, payment-adjacent analytics, marketplace experimentation, and production-grade metric design. Experienced in SQL/Python analysis over large-scale event and transaction-level data, causal inference, backtesting, anomaly detection, scoring logic, and translating ambiguous risk signals into product, operations, and governance decisions.",
        styles["summary"],
    ))

    story.extend(section("PROFESSIONAL EXPERIENCE", styles))
    story.extend(role_header("Goldman Sachs", "New York, NY", "Quantitative Strategist", "Nov 2025 - Present", styles))
    for text in [
        "Design and own production <b>risk metrics</b> across transaction- and entity-level pricing/liquidity signals for <b>100+ global entities</b>, defining new diagnostic indicators for evolving business scenarios and analyzing <b>billions of records</b> to detect anomalies, quantify risk shifts, and trigger drill-down investigations.",
        "Build root-cause decomposition frameworks for abnormal movements in ratio-based risk indicators, separating pricing, funding, balance-sheet, and regional drivers from noisy market moves across multi-billion-record datasets and cross-region cohorts.",
        "Apply <b>difference-in-differences</b> and historical backtesting to evaluate policy and market changes, balancing missed-risk vs <b>false-positive</b> escalation costs and improving confidence in risk-control decisions before stakeholder review.",
        "Develop thresholding and investigation-prioritization logic for risk indicators, translating continuous signal movements into actionable review paths and post-rollout monitoring routines for senior stakeholders while reducing low-signal investigation noise.",
        "Build <b>AI-assisted analytical validation workflows</b> with source traceability, edge-case checks, explainability review, and human-in-the-loop controls, ensuring model-driven insights are auditable, reliable, and governance-ready in high-stakes contexts.",
    ]:
        story.append(bullet(text, styles))

    story.extend(role_header("Blinkle AI (LLM-powered job marketplace)", "New York, NY", "Data Scientist (Part-time), Product", "Sep 2025 - Jan 2026", styles))
    for text in [
        "Designed the core <b>risk and quality metrics framework</b> for a two-sided job marketplace, defining north-star and diagnostic metrics across match quality, recommendation quality, suspicious behavior, and application conversion.",
        "Analyzed <b>millions of production user events</b> with SQL and Python to identify low-quality or suspicious behavior patterns that degraded matching quality, surfacing high-risk cohorts and downstream product friction points.",
        "Built <b>LLM-derived scoring features</b> from resume and job-description signals for screening/ranking pipelines, improving top-match accuracy by <b>37%</b> and creating structured decision signals for product and review workflows.",
        "Designed holdout and A/B experiments for screening and ranking interventions, quantifying false-match vs missed-match tradeoffs, precision-conversion-friction effects, and increasing application conversion by <b>41%</b>.",
    ]:
        story.append(bullet(text, styles))

    story.extend(role_header("ARB Interactive", "Miami, FL", "Data Scientist Intern, Payments", "Jun 2024 - Sep 2024", styles))
    for text in [
        "Analyzed hundreds of millions of payment-adjacent interaction events from a <b>2.1M-user</b> live-streaming platform to detect abnormal traffic, creator abuse, and high-risk behavioral cohorts, supporting fraud/abuse proxy monitoring and traffic-control interventions.",
        "Developed a creator-level <b>causal impact framework</b> using counterfactual baselines and retention modeling to estimate incremental ROI of incentive and intervention policies, improving policy ROI by <b>18%</b>.",
        "Built behavioral segmentation models with <b>K-Means clustering</b> to identify heterogeneous response and risk patterns, enabling targeted interventions that increased DAU by <b>12%</b> while reducing broad, unnecessary user friction.",
        "Designed, analyzed, and monitored A/B-tested policy interventions after rollout, measuring impact on creator retention, content quality, platform health, and the tradeoff between abuse prevention and user experience.",
    ]:
        story.append(bullet(text, styles))

    story.extend(section("EDUCATION", styles))
    story.append(p("<b>University of California, Los Angeles</b> | Master of Quantitative Economics | Jul 2025", styles["edu"]))
    story.append(p("<b>GPA:</b> 4.00/4.00 | <b>Coursework:</b> Database Management, Machine Learning, Time Series Forecasting, Optimization Methods", styles["edu"]))
    story.append(p("<b>Open For Good Project:</b> Used Qualtrics surveys and RNN models to quantify sentiment in sustainability disclosures.", styles["edu"]))
    story.append(p("<b>Nanjing University</b> | Bachelor of Economics, Minor in Mathematics | Jul 2023", styles["edu"]))
    story.append(p("<b>GPA:</b> 3.93/4.00 | <b>Coursework:</b> Mathematical Statistics, Stochastic Processes, Regression Analysis, Statistical Computing", styles["edu"]))
    story.append(p("<b>Honors:</b> National Scholarship, Top 1%; First Place, Citi Group Fintech Competition.", styles["edu"]))

    story.extend(section("TECHNICAL SKILLS", styles))
    story.append(p("<b>Risk & Analytics:</b> Risk Metrics Design, Fraud/Abuse Monitoring, Risk Decisioning, Risk Scoring, Anomaly Detection, Backtesting, Thresholding, Root-Cause Analysis, Cohort Analysis, Segmentation, Experimentation, Causal Inference, Difference-in-Differences", styles["skills"]))
    story.append(p("<b>Machine Learning:</b> Regression, Classification, Tree-Based Models, XGBoost, Feature Engineering, Model Validation, Explainability, LLM Structured Signal Extraction", styles["skills"]))
    story.append(p("<b>Tools:</b> Python, SQL, R, Spark, Airflow, AWS, Tableau, Stata, NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn", styles["skills"]))

    doc.build(story)


if __name__ == "__main__":
    main()
