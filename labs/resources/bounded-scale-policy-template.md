# Bounded Optimisation and Scale Policy — Working Template

Save a copy as `C526-campaign-pack/08-bounded-scale-policy.md`.

## Authoritative Inputs

| Input | File | Version or date | Owner |
|---|---|---|---|
| Success brief | 01-success-brief.md | | |
| Prompt contract | 02-audience-and-prompt-contract.md | | |
| Performance diagnosis | 06-performance-diagnosis.md | | |
| Operations runbook | 07-operations-agent-runbook.md | | |

## Bounded Optimisation Policy

### Eligibility

- `Metric_Definition_Version` matches the approved version: ______
- `Window_Days` is 7 and the reporting window is complete: ______
- `Event_Status` is `healthy`: ______
- `Purchases` is at least 10: ______
- `Unresolved_Data_Quality_Issue` is `no`: ______

### Allowed Recommendations

### Maximum Change

### Cooldown

### Stop or Pause Conditions

### Approval and Log Requirements

## Scenario Results

| Scenario ID | Eligible? | Evidence | Guardrail status | Recommendation | Proposed change | Human approval | Cooldown end | Rollback trigger | Log note |
|---|---|---|---|---|---|---|---|---|---|

## Invariant Checks

| Scenario | Trigger present | Required policy effect | Agent effect | Corrected decision |
|---|---|---|---|---|
| SC06 | `As_Of_Datetime < Last_Change_Datetime + 72 hours` | HOLD; no budget proposal | | |

## Correction Log

| Scenario | Failure type | Evidence | Rule change | New recommendation |
|---|---|---|---|---|

## Human Decision Note

- Scenario:
- Current daily budget:
- Proposed percentage change:
- Proposed daily budget:
- Last change datetime:
- Cooldown end:
- Primary KPI evidence:
- Negative feedback rate:
- Capacity check:
- Margin context:
- Expected effect:
- Human approver:
- Rollback trigger:
- Status: PROPOSED — AWAITING HUMAN APPROVAL

## Campaign-Pack Manifest

| Artifact | Purpose | Authoritative inputs | Owner | Status | Last review | Next decision |
|---|---|---|---|---|---|---|

## 30-Day Draft-First Pilot

| Week | Focus | Evidence to review | Decision owner | Change allowed |
|---|---|---|---|---|
| 1 | Baseline and draft quality | | | |
| 2 | Exceptions and correction labels | | | |
| 3 | One controlled experiment | | | |
| 4 | Governance and authority review | | | |

## Test Evidence

| Input or case | Expected result | Observed result | Status | Reviewer | Date |
|---|---|---|---|---|---|
| SC02 | Tracking error blocks scaling | | | | |
| SC03 | Negative feedback rate above 0.03% blocks scaling | | | | |
| SC01 | Any proposed budget change is within 15%; cooldown uses last change + 72 hours | | | | |
| SC06 | As-of time is inside the 72-hour cooldown, so the result is HOLD with no budget proposal | | | | |
