"""Topic 1 — Getting Started with Agentic AI for Facebook Marketing."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Build the Facebook Campaign Success Brief",
        objective="LO1: Connect a Facebook marketing workflow to a measurable business objective, customer action, KPI, and guardrails",
        duration="50 minutes",
        desc=(
            "You begin the connected Harbour & Hearth scenario by turning an approved brand brief into a concise success brief of no more than 600 words. "
            "The lab establishes the objective, customer action, evidence, limits, and decision metrics that every later content, campaign, and automation artifact must follow."
        ),
        build="C526-campaign-pack/01-success-brief.md of no more than 600 words containing the campaign decision chain, approved facts, KPI definitions, guardrails, stop conditions, and retained Test Evidence.",
        services="Web browser, approved generative AI assistant, text editor, labs/resources/harbour-hearth-brand-brief.md",
        prerequisites=[
            "Create a local folder named C526-campaign-pack.",
            "Open labs/resources/harbour-hearth-brand-brief.md in a text editor.",
            "Use a new AI chat that contains no real customer or account data.",
        ],
        deck_steps=[
            "Extract approved facts and explicit unknowns from the brand brief.",
            "Build the business-result → objective → customer-action → KPI chain.",
            "Add guardrails, approval gates, and stop conditions.",
            "Save the reviewed brief, capped at 600 words, as the source for every later lab.",
        ],
        deck_test="Check the action, KPI, two guards, three stops, and sources.",
        steps=[
            (
                "Create the campaign-pack folder. Inside it, create a blank text file named 01-success-brief.md.",
                "Folder: C526-campaign-pack\nFile: C526-campaign-pack/01-success-brief.md",
            ),
            (
                "Read the Harbour & Hearth brand brief once without using AI. Highlight the offer, approved facts, target action, constraints, and facts that are explicitly unknown.",
                "Open: labs/resources/harbour-hearth-brand-brief.md",
            ),
            (
                "Start a new AI chat. Paste the prompt below, then paste the complete synthetic brand brief where indicated.",
                """You are a Facebook marketing strategist preparing a decision brief. Use only facts in the supplied synthetic brand brief. Do not invent audience statistics, product claims, customer quotes, or performance. Label missing information as UNKNOWN.

Return Markdown with these headings:
1. Business result
2. Facebook marketing objective
3. Observable customer action
4. Primary KPI and formula
5. Two guardrail metrics
6. Approved offer facts
7. Audience problem hypothesis
8. Organic and paid channel roles
9. Human approval gates
10. Stop conditions
11. Unknowns to resolve

For every factual statement, add its source heading from the brief in parentheses.

SYNTHETIC BRAND BRIEF:
<PASTE THE COMPLETE HARBOUR & HEARTH BRAND BRIEF>""",
            ),
            (
                "Compare the AI output line by line with the brand brief. Delete or relabel every statement that cannot be traced to a source heading.",
                "Reviewer rule: sourced fact / labelled assumption / UNKNOWN — there is no fourth category.",
            ),
            (
                "Write the decision chain as one sentence and place it at the top of the file.",
                "Because <BUSINESS RESULT>, Facebook will pursue <OBJECTIVE> by encouraging <CUSTOMER ACTION>; we will judge it mainly by <PRIMARY KPI> while protecting <GUARDRAIL 1> and <GUARDRAIL 2>.",
            ),
            (
                "Add the primary KPI formula and two named guardrails. Use cost per purchase as the primary efficiency KPI, return on ad spend as value context, negative feedback rate as the customer-impact guard, and fulfilment headroom as the operating guard.",
                "Cost per purchase = advertising spend / attributed purchases\nReturn on ad spend = attributed revenue / advertising spend\nNegative feedback rate (%) = negative feedback / impressions × 100\nFulfilment headroom = daily box capacity - forecast daily boxes\nPause threshold for practice: negative feedback rate > 0.03% or fulfilment headroom < 0",
            ),
            (
                "Add at least three stop conditions: missing or broken conversion data, an unsupported claim, and any action that would publish or spend without approval.",
                "STOP when: tracking is missing or inconsistent; a claim has no approved source; the next action publishes, messages, changes targeting, or changes spend without the named approver.",
            ),
            (
                "Paste the reviewed output into 01-success-brief.md. Add a final Review Log with your initials, today's date, and the corrections you made.",
                "## Review Log\n- Reviewer: <INITIALS>\n- Date: <YYYY-MM-DD>\n- Corrections: <LIST THE FACTS, ASSUMPTIONS, OR WORDING YOU CHANGED>",
            ),
            (
                "Check the document word count. If it exceeds 600 words, remove repetition while preserving every required heading, definition, guardrail, unknown, and source reference.",
                "Length limit: 600 words maximum",
            ),
        ],
        test=(
            "Open 01-success-brief.md and confirm it contains one measurable customer action, a primary KPI with formula, two guardrail metrics, at least three stop conditions, and an UNKNOWN section. "
            "Choose any three offer facts at random; each must trace to a heading in the synthetic brand brief."
        ),
        checkpoint="Keep 01-success-brief.md open. Lab 2 will use its objective, approved facts, guardrails, and unknowns as authoritative inputs.",
        troubleshooting=[
            ("The AI invents customer demographics or market size", "Delete the claim, add it to UNKNOWN, and repeat the instruction to use only supplied evidence."),
            ("The objective and KPI do not match", "Rewrite the chain from the customer action backwards; a purchase action needs a purchase-related decision metric."),
            ("The brief exceeds 600 words", "Move supporting explanation into notes and keep only decisions, definitions, constraints, and unknowns in the main brief."),
        ],
        challenge="Add one leading indicator and one lagging indicator, then explain what decision each can support without replacing the primary KPI.",
        reflection="Which part of the decision chain most needs human business judgement, and why would an AI model be unable to supply it safely from the brief alone?",
    ),
    dict(
        num=2,
        topic=1,
        title="Create the Audience Evidence Map and Prompt Contract",
        objective="LO2: Define evidence-backed audience hypotheses and reusable agent instructions with explicit output, review, and escalation rules",
        duration="60 minutes",
        desc=(
            "You convert synthetic audience signals into three testable audience hypotheses, select one primary segment, and write the G-C-A-T-E prompt contract that governs later AI work. "
            "The contract teaches the agent to separate evidence from assumptions and to stop at high-impact actions."
        ),
        build="C526-campaign-pack/02-audience-and-prompt-contract.md containing an evidence map, three audience hypotheses, a selected segment, and a tested G-C-A-T-E prompt contract.",
        services="Approved generative AI assistant, text editor, spreadsheet viewer, labs/resources/harbour-hearth-audience-signals.csv",
        prerequisites=[
            "Completed Lab 1 with 01-success-brief.md available.",
            "Open labs/resources/harbour-hearth-audience-signals.csv.",
            "Keep all work inside the synthetic scenario; do not add real customer records.",
        ],
        deck_steps=[
            "Classify each signal as observed, declared, inferred, or unknown.",
            "Turn evidence into three testable need-based audience hypotheses.",
            "Write the G-C-A-T-E instructions and output schema.",
            "Run a deliberate missing-input test and correct unsafe guessing.",
        ],
        deck_test="Missing offer data stays UNKNOWN and stops the workflow.",
        steps=[
            (
                "Create 02-audience-and-prompt-contract.md and add two top-level headings: Audience Evidence Map and G-C-A-T-E Prompt Contract.",
                "File: C526-campaign-pack/02-audience-and-prompt-contract.md\nHeadings: ## Audience Evidence Map | ## G-C-A-T-E Prompt Contract",
            ),
            (
                "Read every row in the synthetic audience-signals CSV. Mark the source type as observed behaviour, declared feedback, inferred hypothesis, or unknown. Do not change the original evidence text.",
                "Open: labs/resources/harbour-hearth-audience-signals.csv",
            ),
            (
                "Ask the AI to organise the evidence and propose three audience hypotheses. Paste the success brief and signal rows into the placeholders.",
                """Act as an audience research assistant. Use only the supplied synthetic success brief and signal table.

First return an evidence map with columns: signal_id, source_type, exact_evidence, what_it_may_support, what_it_does_not_prove.
Then propose exactly three need-based audience hypotheses. For each include: situation, need, trigger, barrier, useful message angle, evidence IDs, assumption still to test, and a response metric.

Rules:
- Do not invent age, income, ethnicity, family status, interests, market size, or customer quotes.
- Distinguish evidence from inference.
- Use UNKNOWN when evidence is absent.
- Flag any targeting idea that could be unfair, overly narrow, or unsupported.

SUCCESS BRIEF:
<PASTE 01-SUCCESS-BRIEF>

SYNTHETIC SIGNALS:
<PASTE THE CSV ROWS>""",
            ),
            (
                "Review the evidence map against the CSV. Correct any changed wording, missing signal ID, or inference presented as fact.",
                "Evidence check: each hypothesis must cite at least two signal IDs and state at least one assumption still to test.",
            ),
            (
                "Select one primary audience hypothesis for the remaining labs. Write a two-sentence rationale tied to the objective and available evidence, not to personal preference.",
                "Primary audience hypothesis: <NAME>\nRationale: This segment is prioritised because <EVIDENCE IDS> connect <NEED> to <CUSTOMER ACTION>. We still need to test <ASSUMPTION>.",
            ),
            (
                "Write the reusable G-C-A-T-E prompt contract below the evidence map. Fill every placeholder from the reviewed Lab 1 and Lab 2 decisions.",
                """# G-C-A-T-E PROMPT CONTRACT
GOAL: Support <PRIMARY AUDIENCE HYPOTHESIS> to take <CUSTOMER ACTION> while improving <PRIMARY KPI> and protecting <GUARDRAILS>.
CONTEXT: Use only 01-success-brief.md, the reviewed evidence map, and later files explicitly supplied in this chat. Approved brand facts are <LIST>. Unknowns remain UNKNOWN.
ACTIONS: 1) restate the requested decision, 2) cite input evidence, 3) produce the requested draft, 4) run the quality checks, 5) recommend the next bounded action.
TESTS: Check factual grounding, brand rules, audience value, privacy, advertising truth, objective-action match, and one-variable experiment discipline.
ESCALATION: Stop and ask for a person when evidence is missing, instructions conflict, personal data appears, a claim lacks support, or an action would publish, message, change targeting, or change spend.
OUTPUT: Return a Markdown table with columns Evidence | Assumption | Draft | Risk | Reviewer decision needed. End with STOP / REVISE / READY FOR HUMAN REVIEW and one reason.""",
            ),
            (
                "Test the contract with a deliberately incomplete request. Paste the contract, then send the request below without giving a discount amount.",
                "Draft a Facebook post announcing our new discount. Make it sound urgent and include the percentage off.",
            ),
            (
                "Check the response. It should stop or mark the discount as UNKNOWN, reject fabricated urgency, and ask for approved offer details. If it invents a percentage, strengthen the evidence and escalation rules and run the test again.",
                "Expected behaviour: no invented percentage; no false deadline; explicit request for approved offer details; READY status must not be used.",
            ),
            (
                "Save the corrected contract and add a Prompt Test Log showing the test request, first failure if any, instruction change, and final behaviour.",
                "## Prompt Test Log\n- Test request: <TEXT>\n- Unsafe or weak behaviour: <OBSERVATION>\n- Contract change: <EDIT>\n- Final behaviour: <OBSERVATION>",
            ),
        ],
        test=(
            "Run the incomplete-discount request in a fresh chat using only the saved contract. The response must not invent a percentage or deadline, must identify the missing evidence, and must stop before a public action. "
            "Also confirm each audience hypothesis cites at least two signal IDs and labels an assumption."
        ),
        checkpoint="Use the selected audience hypothesis and final G-C-A-T-E contract as the opening context for Labs 3 to 8.",
        troubleshooting=[
            ("All three audience hypotheses sound the same", "Force a different situation, need, trigger, and barrier for each while keeping every claim tied to a signal ID."),
            ("The contract produces long essays", "Tighten the OUTPUT schema and set maximum rows or word counts for each requested artifact."),
            ("The agent ignores the stop rule", "Move escalation rules before the task, repeat the forbidden action types, and require a status label before any draft."),
        ],
        challenge="Add a tool-permission table rating reading files, drafting content, scheduling, messaging, and changing budget as low, medium, or high risk, with the approval required for each.",
        reflection="How does separating observed evidence from inferred hypotheses change the way you would brief an audience-research agent?",
    ),
]
