# Lab 5 — Design the Facebook Campaign Blueprint

- **Course:** Agentic AI for Facebook Marketing (C526)
- **Topic 3:** Building and Optimising Ad Campaigns with AI
- **Maps to:** LO4: Design an aligned campaign, ad set, and ad structure with explicit audience, budget, placement, signal, and experiment rationale
- **Tools:** Approved generative AI assistant, text editor, optional Meta Ads Manager draft view, Labs 1-4 outputs
- **Duration:** 50 minutes

---

## What You Will Do

You translate the campaign brief and creative matrix into a draft Meta Ads Manager blueprint without spending money. The blueprint makes every decision at campaign, ad set, and ad level visible, identifies account inputs that are still unknown, and keeps publication behind an authorised approval gate.

## What You Will Build

C526-campaign-pack/05-campaign-blueprint.md containing a named campaign hierarchy, delivery rationale, experiment controls, preflight checklist, and optional unsubmitted Ads Manager draft screenshots.

## Prerequisites

- Completed the success brief, audience map, content system, and ad-copy creative matrix.
- Use the synthetic scenario and hypothetical S$40 daily budget; do not activate advertising.
- Optional Meta Ads Manager access must be an account you are authorised to view; stop before Publish.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Create 05-campaign-blueprint.md and add the Alignment Chain below. Fill it from Lab 1 without changing the defined customer action or primary KPI.**

```text
Business result → Facebook objective → Conversion location → Event → Primary KPI → Guardrail metrics
```

**2. Use this scenario decision for the blueprint: Sales objective, website conversion location, Purchase event, hypothetical S$40 daily campaign budget, seven-day observation window. Mark event readiness UNKNOWN until a real implementation verifies it.**

```text
Objective: Sales
Conversion location: Website
Event: Purchase (readiness UNKNOWN)
Budget: S$40/day hypothetical
Observation window: 7 days
Status: DESIGN ONLY — DO NOT ACTIVATE
```

**3. Define a consistent naming convention, then name one campaign, two strategically distinct ad sets, and three hook-angle ads.**

```text
Naming pattern: HH_SunriseBox_<LEVEL>_<AUDIENCE>_<ANGLE>_2026Q3
Campaign: HH_SunriseBox_Campaign_Sales_2026Q3
Ad set P: HH_SunriseBox_AdSet_Prospecting_2026Q3
Ad set R: HH_SunriseBox_AdSet_Reengagement_2026Q3
Ads: ..._Convenience | ..._Freshness | ..._MorningRoutine
```

**4. Describe the two ad-set designs. Prospecting uses the evidence-backed need as an audience suggestion with strict geographic control and appropriate exclusions. Re-engagement is PARKED and excluded from the experiment unless an authorised prior-interaction source is verified.**

```text
Ad set columns: Role | Status | Audience evidence | Strict controls | Suggestions/source | Exclusions | Placements | Budget method | Schedule | Unknowns
Prospecting status: DESIGN ELIGIBLE
Re-engagement status: PARKED — SOURCE UNKNOWN
```

**5. Place the three Lab 4 ads only in HH_SunriseBox_AdSet_Prospecting_2026Q3 for the hook-angle experiment. Record the fixed controls and the one changed variable.**

```text
Eligible ad set: HH_SunriseBox_AdSet_Prospecting_2026Q3
Fixed: audience, offer, proof set, destination, CTA intent, headline, description, 1:1 single-image format, 04-control-image-1080.png, schedule, optimisation
Changed: primary-text hook angle
Primary comparison metric: cost per purchase
Supporting diagnosis: link CTR and conversion rate
```

**6. Ask the AI to review the blueprint for hierarchy mistakes and hidden contradictions. Paste the G-C-A-T-E contract and your current blueprint.**

```text
Review this Facebook campaign blueprint as a preflight checker.

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
<PASTE CURRENT BLUEPRINT>
```

**7. Resolve every contradiction that can be fixed from the existing course files. Use https://example.com/sunrise-box as the synthetic design destination. Keep live destination verification, account ID, Page identity, pixel or dataset ID, verified event status, payment method, and authorised re-engagement source as UNKNOWN unless supplied by an authorised owner.**

```text
Design destination: https://example.com/sunrise-box
Live destination verification: UNKNOWN
Unknowns register: Field | Why required | Owner | Evidence needed | Gate blocked
```

**8. Optional authorised practice: Open Meta Ads Manager, select + Create campaign, choose the blueprint objective, and inspect the campaign, ad set, and ad fields. Enter only synthetic names if the trainer provides a sandbox. Do not add a payment method and do not select Publish. Crop any screenshot to exclude Page, account, billing, pixel, dataset, and personal identifiers.**

```text
Path: Meta Ads Manager → + Create campaign → Objective → Continue → Campaign → Ad set → Ad
STOP before Publish. Close or discard the draft. Screenshot rule: crop all real identifiers before saving.
```

**9. Complete a preflight checklist covering identity, objective, audience, placements, budget, schedule, event readiness, destination, creative, tracking, rights, privacy, and approvals. Save the file.**

```text
Preflight status values: READY FOR HUMAN REVIEW | REVISE | BLOCKED BY UNKNOWN
Final publication gate: BLOCKED until an authorised account owner resolves every required unknown.
```

## Test It

Trace one ad from its hook through ad, ad set, campaign objective, event, and primary KPI. Then choose one UNKNOWN such as event readiness and explain exactly why the blueprint cannot safely move past its gate without that evidence.

## Test Evidence

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

| Input or case | Expected result | Observed result | Status | Reviewer | Date |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Checkpoint for the Next Lab

Lab 6 will use the fixed hook-angle experiment and campaign decision metrics to analyse a synthetic result table.

## Troubleshooting

- **The blueprint has an ad-level objective:** Move the objective to campaign level; keep creative, copy, identity, destination, and tracking details at ad level.
- **The two ad sets differ only by minor interests:** Consolidate them unless they represent a meaningful prospecting versus authorised re-engagement strategy.
- **The AI recommends switching objectives to improve clicks:** Re-anchor it to the business result; clicks are a diagnostic signal, not a substitute for the defined customer action.

## Challenge

Create a second blueprint for a Leads objective and explain which event, destination, KPI, and copy elements must change rather than being copied from the Sales design.

## Reflection

Which campaign setting creates the largest downstream mismatch when it is chosen for convenience rather than business purpose?

---

[← Lab 4](lab-04-create-the-ad-copy-and-creative-matrix.md) · [Lab 6 →](lab-06-diagnose-performance-and-design-one-controlled-test.md)
