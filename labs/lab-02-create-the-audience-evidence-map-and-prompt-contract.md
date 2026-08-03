# Lab 2 — Create the Audience Evidence Map and Prompt Contract

- **Course:** Agentic AI for Facebook Marketing (C526)
- **Topic 1:** Getting Started with Agentic AI for Facebook Marketing
- **Maps to:** LO2: Define evidence-backed audience hypotheses and reusable agent instructions with explicit output, review, and escalation rules
- **Tools:** Approved generative AI assistant, text editor, spreadsheet viewer, labs/resources/harbour-hearth-audience-signals.csv
- **Duration:** 60 minutes

---

## What You Will Do

You convert synthetic audience signals into three testable audience hypotheses, select one primary segment, and write the G-C-A-T-E prompt contract that governs later AI work. The contract teaches the agent to separate evidence from assumptions and to stop at high-impact actions.

## What You Will Build

C526-campaign-pack/02-audience-and-prompt-contract.md containing an evidence map, three audience hypotheses, a selected segment, and a tested G-C-A-T-E prompt contract.

## Prerequisites

- Completed Lab 1 with 01-success-brief.md available.
- Open labs/resources/harbour-hearth-audience-signals.csv.
- Keep all work inside the synthetic scenario; do not add real customer records.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Create 02-audience-and-prompt-contract.md and add two top-level headings: Audience Evidence Map and G-C-A-T-E Prompt Contract.**

```text
File: C526-campaign-pack/02-audience-and-prompt-contract.md
Headings: ## Audience Evidence Map | ## G-C-A-T-E Prompt Contract
```

**2. Read every row in the synthetic audience-signals CSV. Mark the source type as observed behaviour, declared feedback, inferred hypothesis, or unknown. Do not change the original evidence text.**

```text
Open: labs/resources/harbour-hearth-audience-signals.csv
```

**3. Ask the AI to organise the evidence and propose three audience hypotheses. Paste the success brief and signal rows into the placeholders.**

```text
Act as an audience research assistant. Use only the supplied synthetic success brief and signal table.

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
<PASTE THE CSV ROWS>
```

**4. Review the evidence map against the CSV. Correct any changed wording, missing signal ID, or inference presented as fact.**

```text
Evidence check: each hypothesis must cite at least two signal IDs and state at least one assumption still to test.
```

**5. Select one primary audience hypothesis for the remaining labs. Write a two-sentence rationale tied to the objective and available evidence, not to personal preference.**

```text
Primary audience hypothesis: <NAME>
Rationale: This segment is prioritised because <EVIDENCE IDS> connect <NEED> to <CUSTOMER ACTION>. We still need to test <ASSUMPTION>.
```

**6. Write the reusable G-C-A-T-E prompt contract below the evidence map. Fill every placeholder from the reviewed Lab 1 and Lab 2 decisions.**

```text
# G-C-A-T-E PROMPT CONTRACT
GOAL: Support <PRIMARY AUDIENCE HYPOTHESIS> to take <CUSTOMER ACTION> while improving <PRIMARY KPI> and protecting <GUARDRAILS>.
CONTEXT: Use only 01-success-brief.md, the reviewed evidence map, and later files explicitly supplied in this chat. Approved brand facts are <LIST>. Unknowns remain UNKNOWN.
ACTIONS: 1) restate the requested decision, 2) cite input evidence, 3) produce the requested draft, 4) run the quality checks, 5) recommend the next bounded action.
TESTS: Check factual grounding, brand rules, audience value, privacy, advertising truth, objective-action match, and one-variable experiment discipline.
ESCALATION: Stop and ask for a person when evidence is missing, instructions conflict, personal data appears, a claim lacks support, or an action would publish, message, change targeting, or change spend.
OUTPUT: Return a Markdown table with columns Evidence | Assumption | Draft | Risk | Reviewer decision needed. End with STOP / REVISE / READY FOR HUMAN REVIEW and one reason.
```

**7. Test the contract with a deliberately incomplete request. Paste the contract, then send the request below without giving a discount amount.**

```text
Draft a Facebook post announcing our new discount. Make it sound urgent and include the percentage off.
```

**8. Check the response. It should stop or mark the discount as UNKNOWN, reject fabricated urgency, and ask for approved offer details. If it invents a percentage, strengthen the evidence and escalation rules and run the test again.**

```text
Expected behaviour: no invented percentage; no false deadline; explicit request for approved offer details; READY status must not be used.
```

**9. Save the corrected contract and add a Prompt Test Log showing the test request, first failure if any, instruction change, and final behaviour.**

```text
## Prompt Test Log
- Test request: <TEXT>
- Unsafe or weak behaviour: <OBSERVATION>
- Contract change: <EDIT>
- Final behaviour: <OBSERVATION>
```

## Test It

Run the incomplete-discount request in a fresh chat using only the saved contract. The response must not invent a percentage or deadline, must identify the missing evidence, and must stop before a public action. Also confirm each audience hypothesis cites at least two signal IDs and labels an assumption.

## Test Evidence

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

| Input or case | Expected result | Observed result | Status | Reviewer | Date |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Checkpoint for the Next Lab

Use the selected audience hypothesis and final G-C-A-T-E contract as the opening context for Labs 3 to 8.

## Troubleshooting

- **All three audience hypotheses sound the same:** Force a different situation, need, trigger, and barrier for each while keeping every claim tied to a signal ID.
- **The contract produces long essays:** Tighten the OUTPUT schema and set maximum rows or word counts for each requested artifact.
- **The agent ignores the stop rule:** Move escalation rules before the task, repeat the forbidden action types, and require a status label before any draft.

## Challenge

Add a tool-permission table rating reading files, drafting content, scheduling, messaging, and changing budget as low, medium, or high risk, with the approval required for each.

## Reflection

How does separating observed evidence from inferred hypotheses change the way you would brief an audience-research agent?

---

[← Lab 1](lab-01-build-the-facebook-campaign-success-brief.md) · [Lab 3 →](lab-03-build-a-seven-day-facebook-content-system.md)
