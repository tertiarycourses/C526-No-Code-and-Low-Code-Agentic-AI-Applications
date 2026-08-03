"""Topic 3 — Building and Optimising Ad Campaigns with AI."""

DOMAIN3 = [
    dict(
        num=5,
        topic=3,
        title="Design the Facebook Campaign Blueprint",
        objective="LO4: Design an aligned campaign, ad set, and ad structure with explicit audience, budget, placement, signal, and experiment rationale",
        duration="50 minutes",
        desc=(
            "You translate the campaign brief and creative matrix into a draft Meta Ads Manager blueprint without spending money. "
            "The blueprint makes every decision at campaign, ad set, and ad level visible, identifies account inputs that are still unknown, and keeps publication behind an authorised approval gate."
        ),
        build="C526-campaign-pack/05-campaign-blueprint.md containing a named campaign hierarchy, delivery rationale, experiment controls, preflight checklist, and optional unsubmitted Ads Manager draft screenshots.",
        services="Approved generative AI assistant, text editor, optional Meta Ads Manager draft view, Labs 1-4 outputs",
        prerequisites=[
            "Completed the success brief, audience map, content system, and ad-copy creative matrix.",
            "Use the synthetic scenario and hypothetical S$40 daily budget; do not activate advertising.",
            "Optional Meta Ads Manager access must be an account you are authorised to view; stop before Publish.",
        ],
        deck_steps=[
            "Map the business goal to objective, conversion location, event, and decision KPI.",
            "Specify one active-design prospecting ad set, one parked re-engagement design, and three controlled ads.",
            "Check naming, audience logic, budget, placements, schedule, and data readiness.",
            "Record unknowns and stop at the publication approval gate.",
        ],
        deck_test="Trace ad to KPI and explain one blocking unknown.",
        steps=[
            (
                "Create 05-campaign-blueprint.md and add the Alignment Chain below. Fill it from Lab 1 without changing the defined customer action or primary KPI.",
                "Business result → Facebook objective → Conversion location → Event → Primary KPI → Guardrail metrics",
            ),
            (
                "Use this scenario decision for the blueprint: Sales objective, website conversion location, Purchase event, hypothetical S$40 daily campaign budget, seven-day observation window. Mark event readiness UNKNOWN until a real implementation verifies it.",
                "Objective: Sales\nConversion location: Website\nEvent: Purchase (readiness UNKNOWN)\nBudget: S$40/day hypothetical\nObservation window: 7 days\nStatus: DESIGN ONLY — DO NOT ACTIVATE",
            ),
            (
                "Define a consistent naming convention, then name one campaign, two strategically distinct ad sets, and three hook-angle ads.",
                "Naming pattern: HH_SunriseBox_<LEVEL>_<AUDIENCE>_<ANGLE>_2026Q3\nCampaign: HH_SunriseBox_Campaign_Sales_2026Q3\nAd set P: HH_SunriseBox_AdSet_Prospecting_2026Q3\nAd set R: HH_SunriseBox_AdSet_Reengagement_2026Q3\nAds: ..._Convenience | ..._Freshness | ..._MorningRoutine",
            ),
            (
                "Describe the two ad-set designs. Prospecting uses the evidence-backed need as an audience suggestion with strict geographic control and appropriate exclusions. Re-engagement is PARKED and excluded from the experiment unless an authorised prior-interaction source is verified.",
                "Ad set columns: Role | Status | Audience evidence | Strict controls | Suggestions/source | Exclusions | Placements | Budget method | Schedule | Unknowns\nProspecting status: DESIGN ELIGIBLE\nRe-engagement status: PARKED — SOURCE UNKNOWN",
            ),
            (
                "Place the three Lab 4 ads only in HH_SunriseBox_AdSet_Prospecting_2026Q3 for the hook-angle experiment. Record the fixed controls and the one changed variable.",
                "Eligible ad set: HH_SunriseBox_AdSet_Prospecting_2026Q3\nFixed: audience, offer, proof set, destination, CTA intent, headline, description, 1:1 single-image format, 04-control-image-1080.png, schedule, optimisation\nChanged: primary-text hook angle\nPrimary comparison metric: cost per purchase\nSupporting diagnosis: link CTR and conversion rate",
            ),
            (
                "Ask the AI to review the blueprint for hierarchy mistakes and hidden contradictions. Paste the G-C-A-T-E contract and your current blueprint.",
                """Review this Facebook campaign blueprint as a preflight checker.

Return a table with columns: Level | Setting | Current value | Alignment check | Missing evidence | Risk | Required human decision.

Check:
- campaign objective matches the business result;
- conversion location, event, and destination agree;
- ad sets represent meaningful strategic differences rather than fragmentation;
- audience inputs are supported and do not imply sensitive traits;
- budget and schedule are clearly hypothetical;
- the A/B comparison changes one main variable;
- publication, spend, targeting, and data-source readiness remain approval-controlled.

Do not recommend activation. Use UNKNOWN where account or tracking evidence is absent.

BLUEPRINT:
<PASTE CURRENT BLUEPRINT>""",
            ),
            (
                "Resolve every contradiction that can be fixed from the existing course files. Use https://example.com/sunrise-box as the synthetic design destination. Keep live destination verification, account ID, Page identity, pixel or dataset ID, verified event status, payment method, and authorised re-engagement source as UNKNOWN unless supplied by an authorised owner.",
                "Design destination: https://example.com/sunrise-box\nLive destination verification: UNKNOWN\nUnknowns register: Field | Why required | Owner | Evidence needed | Gate blocked",
            ),
            (
                "Optional authorised practice: Open Meta Ads Manager, select + Create campaign, choose the blueprint objective, and inspect the campaign, ad set, and ad fields. Enter only synthetic names if the trainer provides a sandbox. Do not add a payment method and do not select Publish. Crop any screenshot to exclude Page, account, billing, pixel, dataset, and personal identifiers.",
                "Path: Meta Ads Manager → + Create campaign → Objective → Continue → Campaign → Ad set → Ad\nSTOP before Publish. Close or discard the draft. Screenshot rule: crop all real identifiers before saving.",
            ),
            (
                "Complete a preflight checklist covering identity, objective, audience, placements, budget, schedule, event readiness, destination, creative, tracking, rights, privacy, and approvals. Save the file.",
                "Preflight status values: READY FOR HUMAN REVIEW | REVISE | BLOCKED BY UNKNOWN\nFinal publication gate: BLOCKED until an authorised account owner resolves every required unknown.",
            ),
        ],
        test=(
            "Trace one ad from its hook through ad, ad set, campaign objective, event, and primary KPI. Then choose one UNKNOWN such as event readiness and explain exactly why the blueprint cannot safely move past its gate without that evidence."
        ),
        checkpoint="Lab 6 will use the fixed hook-angle experiment and campaign decision metrics to analyse a synthetic result table.",
        troubleshooting=[
            ("The blueprint has an ad-level objective", "Move the objective to campaign level; keep creative, copy, identity, destination, and tracking details at ad level."),
            ("The two ad sets differ only by minor interests", "Consolidate them unless they represent a meaningful prospecting versus authorised re-engagement strategy."),
            ("The AI recommends switching objectives to improve clicks", "Re-anchor it to the business result; clicks are a diagnostic signal, not a substitute for the defined customer action."),
        ],
        challenge="Create a second blueprint for a Leads objective and explain which event, destination, KPI, and copy elements must change rather than being copied from the Sales design.",
        reflection="Which campaign setting creates the largest downstream mismatch when it is chosen for convenience rather than business purpose?",
    ),
    dict(
        num=6,
        topic=3,
        title="Diagnose Performance and Design One Controlled Test",
        objective="LO5: Calculate Facebook metrics, locate a funnel break, distinguish evidence from inference, and recommend one bounded experiment",
        duration="55 minutes",
        desc=(
            "You calculate delivery, attention, conversion, and value metrics from a synthetic Facebook result table, then use an AI analyst under the prompt contract to diagnose the pattern. "
            "The lab finishes with one controlled next test rather than a bundle of untraceable changes."
        ),
        build="C526-campaign-pack/06-performance-diagnosis.md plus 06-facebook-metrics.xlsx with date window, CTR, CPC, conversion rate, CPA, ROAS, negative feedback rate, evidence-linked findings, and one experiment card.",
        services="Spreadsheet application, approved generative AI assistant, labs/resources/harbour-hearth-facebook-performance.csv, Lab 5 blueprint",
        prerequisites=[
            "Completed 05-campaign-blueprint.md with the hook-angle experiment defined.",
            "Open the synthetic performance CSV in a spreadsheet application.",
            "Use one consistent date window, currency, and click definition across all rows.",
        ],
        deck_steps=[
            "Validate the dataset and calculate the metric tree with explicit formulas.",
            "Compare variants and locate the break between delivery, attention, and conversion.",
            "Ask the agent for evidence-linked findings, assumptions, and uncertainty.",
            "Write one experiment card with stable controls and a decision rule.",
        ],
        deck_test="Recalculate one row; change one variable; name one stop rule.",
        steps=[
            (
                "Open harbour-hearth-facebook-performance.csv. Confirm the columns include Variant, Window_Start, Window_End, Impressions, Reach, Link_Clicks, Purchases, Spend_SGD, Revenue_SGD, and Negative_Feedback.",
                "Open: labs/resources/harbour-hearth-facebook-performance.csv",
            ),
            (
                "Check data quality before calculating: no blank variant names, no negative counts, Reach is not greater than Impressions, Spend is positive, and Window_Start and Window_End are identical across rows and span seven days.",
                "Data-quality log: Check | Result | Row affected | Action taken",
            ),
            (
                "Add six columns after Negative_Feedback: Negative_Feedback_Rate, Link_CTR, CPC_SGD, Conversion_Rate, CPA_SGD, and ROAS. Enter the formulas in row 2 and fill them down.",
                "K2 = IF(D2=0,\"\",J2/D2)\nL2 = IF(D2=0,\"\",F2/D2)\nM2 = IF(F2=0,\"\",H2/F2)\nN2 = IF(F2=0,\"\",G2/F2)\nO2 = IF(G2=0,\"\",H2/G2)\nP2 = IF(H2=0,\"\",I2/H2)",
            ),
            (
                "Format Negative_Feedback_Rate, Link_CTR, and Conversion_Rate as percentages; show Negative_Feedback_Rate to at least two decimal places so the 0.03% threshold remains observable. Format CPC_SGD and CPA_SGD as currency, and ROAS as a number with two decimal places. Do not replace unavailable values with zero.",
                "Display rule: unavailable denominator → blank or N/A, never 0.00. Negative_Feedback_Rate display precision: at least 0.00%.",
            ),
            (
                "Create 06-performance-diagnosis.md. Paste a rounded copy of the completed metric table and record the formulas in a Metric Definitions section.",
                "File: C526-campaign-pack/06-performance-diagnosis.md",
            ),
            (
                "Compare the three variants in funnel order: delivery, attention, conversion, value, then quality guard. Write one observed statement per stage without giving a cause yet.",
                "Observed statement format: Variant <ID> has <METRIC VALUE> versus <COMPARATOR> during the same seven-day window.",
            ),
            (
                "Paste the G-C-A-T-E contract, metric table, and fixed experiment controls into the AI assistant. Request evidence-linked diagnosis.",
                """Act as a cautious Facebook performance analyst. Use only the supplied synthetic table and experiment design.

Return:
1. Five observed findings, each citing variant and metric value.
2. A funnel-break table with Stage | Evidence | Possible explanation | What the data does not prove.
3. Data limitations and checks required before action.
4. Exactly three ranked hypotheses.
5. One recommended next experiment that changes one variable.

Rules:
- Do not call correlation a cause.
- Do not declare a winner using CTR alone.
- Use N/A when a denominator is zero.
- Keep spend changes as a human decision.
- Mention Negative_Feedback as a quality guard, not a performance objective.""",
            ),
            (
                "Verify every number in the AI response against your spreadsheet. Correct arithmetic, renamed metrics, unsupported causes, or claims that ignore the primary KPI.",
                "Verification table: AI claim | Spreadsheet evidence | Correct? | Correction",
            ),
            (
                "Write one Experiment Card. State the question, hypothesis, single changed variable, controls, primary metric, guardrail, observation window, minimum evidence condition, decision threshold, stop rule, and owner.",
                """## Experiment Card
Question:
Hypothesis:
Changed variable:
Fixed controls:
Primary metric:
Guardrail metric:
Observation window:
Minimum evidence condition:
Decision threshold:
Stop rule:
Human owner:""",
            ),
            (
                "Save the spreadsheet as C526-campaign-pack/06-facebook-metrics.xlsx and the diagnosis as 06-performance-diagnosis.md.",
                "Files: C526-campaign-pack/06-facebook-metrics.xlsx\nC526-campaign-pack/06-performance-diagnosis.md",
            ),
        ],
        test=(
            "Manually recalculate one row and match the spreadsheet within rounding. Independent benchmark: Freshness_Process CPA = S$11.88 and ROAS = 2.36. "
            "Then verify the Experiment Card changes exactly one variable and names at least one condition that would stop or delay the decision."
        ),
        checkpoint="Lab 7 will use your metric definitions and evidence-linked reporting style; Lab 8 will use the selected guardrail and stop rule in a scaling policy.",
        troubleshooting=[
            ("The spreadsheet shows a divide-by-zero error", "Use the IF denominator check exactly as shown and display N/A rather than inventing a metric."),
            ("The AI explains performance using facts not in the table", "Move the statement to Possible explanation and add the evidence needed to test it."),
            ("The next experiment changes copy, audience, and budget", "Choose the highest-priority hypothesis and change only the variable needed to test it."),
        ],
        challenge="Add frequency = impressions / reach, then describe one situation where a higher value might indicate useful repetition and another where it might indicate fatigue.",
        reflection="Why can the variant with the best click-through rate still be the wrong choice for the business objective?",
    ),
]
