# Agentic AI for Facebook Marketing (C526) — Learner Guide

**Course Code:** C526  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 3 August 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with Agentic AI for Facebook Marketing](#topic-01--getting-started-with-agentic-ai-for-facebook-marketing)
  - [Facebook Marketing as a Connected System](#facebook-marketing-as-a-connected-system)
  - [From Generative AI to an Agentic Workflow](#from-generative-ai-to-an-agentic-workflow)
  - [The Six-Part Marketing Agent](#the-six-part-marketing-agent)
  - [Objective, Customer Action, and KPI Chain](#objective-customer-action-and-kpi-chain)
  - [Audience Evidence Before Targeting](#audience-evidence-before-targeting)
  - [The Prompt Contract](#the-prompt-contract)
  - [Lab 1 — Build the Facebook Campaign Success Brief](#lab-1--build-the-facebook-campaign-success-brief)
  - [Lab 2 — Create the Audience Evidence Map and Prompt Contract](#lab-2--create-the-audience-evidence-map-and-prompt-contract)
- [Topic 02 — Content Creation and Ad Copy with AI](#topic-02--content-creation-and-ad-copy-with-ai)
  - [The Facebook Message Hierarchy](#the-facebook-message-hierarchy)
  - [Content Pillars and the Customer Journey](#content-pillars-and-the-customer-journey)
  - [Brand Voice as Observable Rules](#brand-voice-as-observable-rules)
  - [Facebook Copy Anatomy](#facebook-copy-anatomy)
  - [Creative System: Image, Carousel, and Video](#creative-system-image-carousel-and-video)
  - [Content Quality Gate](#content-quality-gate)
  - [Lab 3 — Build a Seven-Day Facebook Content System](#lab-3--build-a-seven-day-facebook-content-system)
  - [Lab 4 — Create the Ad Copy and Creative Matrix](#lab-4--create-the-ad-copy-and-creative-matrix)
- [Topic 03 — Building and Optimising Ad Campaigns with AI](#topic-03--building-and-optimising-ad-campaigns-with-ai)
  - [Campaign, Ad Set, and Ad Hierarchy](#campaign-ad-set-and-ad-hierarchy)
  - [Objective, Event, and Optimisation Alignment](#objective-event-and-optimisation-alignment)
  - [Audience Strategy: Prospecting and Re-engagement](#audience-strategy-prospecting-and-re-engagement)
  - [The Facebook Performance Metric Tree](#the-facebook-performance-metric-tree)
  - [A/B Testing as Causal Learning](#ab-testing-as-causal-learning)
  - [Optimisation Diagnosis Before Change](#optimisation-diagnosis-before-change)
  - [Lab 5 — Design the Facebook Campaign Blueprint](#lab-5--design-the-facebook-campaign-blueprint)
  - [Lab 6 — Diagnose Performance and Design One Controlled Test](#lab-6--diagnose-performance-and-design-one-controlled-test)
- [Topic 04 — Automating and Scaling Facebook Marketing with AI Agents](#topic-04--automating-and-scaling-facebook-marketing-with-ai-agents)
  - [Should This Task Be Automated?](#should-this-task-be-automated)
  - [The Governed Agentic Operating Loop](#the-governed-agentic-operating-loop)
  - [Facebook Operations You Can Coordinate](#facebook-operations-you-can-coordinate)
  - [Bounded Optimisation Policy](#bounded-optimisation-policy)
  - [Scale Through a Learning Ladder](#scale-through-a-learning-ladder)
  - [Privacy, Advertising, and Incident Safeguards](#privacy-advertising-and-incident-safeguards)
  - [Lab 7 — Design the Facebook Operations Agent Runbook](#lab-7--design-the-facebook-operations-agent-runbook)
  - [Lab 8 — Simulate a Bounded Optimisation and Scale Loop](#lab-8--simulate-a-bounded-optimisation-and-scale-loop)
- [Wrap-Up — From Course Pack to Operating Practice](#wrap-up--from-course-pack-to-operating-practice)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide is the self-contained study text for Agentic AI for Facebook Marketing (C526). It explains the concepts behind Facebook planning, content, advertising, performance learning, and governed automation before guiding you through eight connected labs.

The course uses the synthetic Harbour & Hearth bakery scenario so every learner can work with the same evidence without exposing customer data or spending live advertising budget. Save each lab output in one campaign operations folder; the final lab combines the complete set into a launch-ready, human-governed operating pack.


## Course Learning Outcomes

- LO1: Explain how Facebook organic marketing, paid media, and an agentic AI workflow connect to a measurable business objective.
- LO2: Create a reusable campaign brief and prompt contract that defines audience evidence, brand voice, tools, guardrails, and approval gates.
- LO3: Produce an aligned Facebook content calendar, post set, ad-copy matrix, and creative briefs with consistent brand voice.
- LO4: Design a Facebook campaign blueprint across campaign, ad set, and ad levels, including audience, budget, placement, and experiment choices.
- LO5: Calculate and interpret Facebook performance metrics, diagnose a result, and recommend a controlled next action from evidence.
- LO6: Design a governed agentic workflow for scheduling, responses, reporting, optimisation, and scaling with privacy and advertising safeguards.


## Before You Start — Preparation

**What you need**

- A Windows or Mac laptop with a modern web browser and spreadsheet application.
- Access to an approved generative AI assistant such as ChatGPT, Microsoft Copilot, Claude, or Google Gemini.
- The course repository downloaded locally, including labs/resources/.
- Optional Facebook Page or Meta Business Suite task access for viewing draft and scheduling surfaces; no live ad spend is required.
- A new local folder named C526-campaign-pack for the eight lab artifacts.

**Verify your setup**

Open the brand brief and performance dataset, create the campaign-pack folder, and confirm your AI assistant can return a Markdown table without using confidential information.

```bash
Open labs/resources/harbour-hearth-brand-brief.md
Open labs/resources/harbour-hearth-facebook-performance.csv
Create folder: C526-campaign-pack
```

**Conventions used in every lab**

- Replace placeholders such as <PASTE BRIEF> with the specified synthetic course material.
- Never paste real customer identifiers, account secrets, unpublished results, or confidential creative into an unapproved AI tool.
- AI output is a proposal. Check facts, calculations, brand voice, rights, audience fairness, and the intended customer action.
- Work in draft mode. Do not publish a post, enable an automation, or activate an ad unless your organisation separately authorises it.
- Keep filenames exactly as shown so every later lab can find the earlier checkpoint.


## Topic 01 — Getting Started with Agentic AI for Facebook Marketing

Facebook ecosystem | objectives and audiences | agent anatomy | prompting | approval gates

**Key concepts**

- Outcome before output — Start with a business result and customer action, not a request to 'make posts'.
- Organic and paid roles — Organic content builds attention and proof; paid delivery buys controlled reach and learning.
- Agentic loop — An agent plans, uses tools, checks evidence, and iterates until a stop condition is reached.
- Evidence boundary — Facts, customer data, and performance numbers need provenance; unknowns remain labelled assumptions.
- Prompt contract — Role, goal, context, inputs, rules, output schema, and review criteria make work repeatable.
- Audience hypothesis — A segment is a testable need and behaviour pattern, not a stereotype or invented demographic.
- Human authority — Publishing, spend, targeting changes, and sensitive replies remain approval-controlled actions.
- Audit trail — Save the brief, inputs, versions, approvals, and final decision so the workflow can be reviewed.


### Facebook Marketing as a Connected System

Facebook marketing is a system, not a sequence of unrelated posts. A useful plan begins with a business objective, identifies the customer action that would demonstrate progress, then chooses content and delivery methods that make that action more likely. Organic posts, community conversations, Page information, and paid ads should therefore share one message hierarchy and one measurement plan.

The same content can perform different jobs at different stages. A how-to video may build awareness, a customer proof post may reduce uncertainty, and a limited offer may invite a conversion. An AI agent can help coordinate these jobs, but it cannot decide what success means for the business. The marketer supplies the objective, evidence, constraints, and final judgement.

**Visual framework**

- Business objective
- Audience need
- Useful content
- Organic or paid delivery
- Measured customer action


### From Generative AI to an Agentic Workflow

Generative AI creates text, images, or analysis from a prompt. An agentic workflow goes further: it manages a multi-step goal, selects or calls tools, observes results, and decides what to do next within defined limits. A content assistant that drafts one caption is useful, but it becomes agentic only when it can work through a plan such as research, draft, check, revise, route for approval, and record the outcome.

Not every task needs autonomy. Deterministic work such as applying a known naming convention is usually safer as a checklist or rule. Agentic reasoning is more valuable when inputs are unstructured, trade-offs are contextual, or the path changes after new evidence. Begin with the smallest useful loop and add tools only when each tool has a clear purpose and risk level.

**Visual framework**

Single AI task: One prompt produces one draft | The user manually supplies every input | No persistent state or explicit stop rule | Quality depends on one response

Agentic workflow: A goal is decomposed into multiple steps | Tools retrieve data or create controlled outputs | State, checks, retries, and stop conditions are explicit | A person approves high-impact actions


### The Six-Part Marketing Agent

A reliable marketing agent needs more than a clever prompt. Its goal defines the finish line. Context explains the brand and audience. Instructions describe the route and exceptions. Tools determine what the agent may read or change. Memory preserves only the state needed for the next decision. Checks test whether the result is safe and useful before the workflow proceeds.

A weakness in any one part propagates. If the goal says 'increase engagement' but does not name the customer action or time window, the agent may optimise reactions that have no business value. If the tools include a publishing action without an approval gate, a drafting error becomes a public error. Design the system before choosing the model.

**Visual framework**

- Goal — The result, customer action, time horizon, and success threshold.
- Context — Brand, offer, audience evidence, channel role, and constraints.
- Instructions — Decision rules, required steps, output format, and escalation logic.
- Tools — Approved data sources, content tools, calendars, and reporting surfaces.
- Memory — Briefs, past variants, decisions, and lessons that should persist.
- Checks — Brand, factual, privacy, policy, and performance validation before action.


### Objective, Customer Action, and KPI Chain

A measurement chain prevents vanity metrics from becoming the strategy. The business result might be breakfast-box revenue. The marketing objective could be qualified pre-orders. The customer action is a completed order. The primary KPI may be cost per purchase or return on ad spend, while a guardrail could be refund rate, negative feedback, or response quality.

Choose the Meta campaign objective that most closely matches the larger business goal and the event that can be measured reliably. An awareness objective is not a cheaper substitute for a sales objective when sales are the real decision criterion. Equally, a sales objective is weak when the business has no trustworthy conversion signal. The objective, data signal, and KPI must agree.

**Visual framework**

- Business result
- Marketing objective
- Customer action
- Primary KPI
- Guardrail metric


### Audience Evidence Before Targeting

Audience research should separate what is known from what is inferred. Observed data may show that weekday pre-orders peak before 9 am. Customer interviews may reveal that convenience matters more than variety. An AI model can propose segment hypotheses, but it must label them as hypotheses and cite the supplied evidence instead of manufacturing demographic detail.

Meta's delivery systems can work with broad audiences, audience suggestions, and strict controls such as location, minimum age, language, and exclusions. The marketer's job is to provide a commercially meaningful signal without narrowing the audience through stereotypes. Any customer list requires the organisation to have the necessary rights, permissions, and lawful basis for its use.

**Visual framework**

- Observed — Existing customer questions, purchases, site behaviour, and Page interactions.
- Declared — Needs and preferences people voluntarily shared through interviews or forms.
- Inferred — A labelled hypothesis derived from patterns, never presented as fact.
- Excluded — Sensitive traits, unjustified personal data, and segments the offer should not reach.
- Testable — A need, trigger, barrier, message angle, and measurable response.
- Revisable — A segment changes when evidence contradicts the original hypothesis.


### The Prompt Contract

A prompt contract turns an informal request into an operating instruction. It tells the agent who it is helping, what outcome matters, which inputs are authoritative, which choices are allowed, and exactly what form the result must take. A structured output such as a table with evidence, assumptions, risks, and next action is easier to review than a persuasive paragraph.

Include failure behaviour. The agent should say 'insufficient evidence' when a required input is missing, request clarification when two constraints conflict, and stop when the next action would publish, spend money, change targeting, or expose personal data. These rules reduce silent guessing and make human review faster.

**Visual framework**

- Role and goal
- Grounded inputs
- Decision rules
- Output schema
- Review and escalation


### Lab 1 — Build the Facebook Campaign Success Brief

Learning outcome: LO1: Connect a Facebook marketing workflow to a measurable business objective, customer action, KPI, and guardrails.

Goal: You begin the connected Harbour & Hearth scenario by turning an approved brand brief into a concise success brief of no more than 600 words. The lab establishes the objective, customer action, evidence, limits, and decision metrics that every later content, campaign, and automation artifact must follow.

Duration: 50 minutes.

**What you'll build**

C526-campaign-pack/01-success-brief.md of no more than 600 words containing the campaign decision chain, approved facts, KPI definitions, guardrails, stop conditions, and retained Test Evidence.   (Tools: Web browser, approved generative AI assistant, text editor, labs/resources/harbour-hearth-brand-brief.md.)

**Prerequisites**

- Create a local folder named C526-campaign-pack.
- Open labs/resources/harbour-hearth-brand-brief.md in a text editor.
- Use a new AI chat that contains no real customer or account data.

**Step-by-step**

1. Create the campaign-pack folder. Inside it, create a blank text file named 01-success-brief.md.

   ```bash
   Folder: C526-campaign-pack
File: C526-campaign-pack/01-success-brief.md
   ```

2. Read the Harbour & Hearth brand brief once without using AI. Highlight the offer, approved facts, target action, constraints, and facts that are explicitly unknown.

   ```bash
   Open: labs/resources/harbour-hearth-brand-brief.md
   ```

3. Start a new AI chat. Paste the prompt below, then paste the complete synthetic brand brief where indicated.

   ```bash
   You are a Facebook marketing strategist preparing a decision brief. Use only facts in the supplied synthetic brand brief. Do not invent audience statistics, product claims, customer quotes, or performance. Label missing information as UNKNOWN.

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
<PASTE THE COMPLETE HARBOUR & HEARTH BRAND BRIEF>
   ```

4. Compare the AI output line by line with the brand brief. Delete or relabel every statement that cannot be traced to a source heading.

   ```bash
   Reviewer rule: sourced fact / labelled assumption / UNKNOWN — there is no fourth category.
   ```

5. Write the decision chain as one sentence and place it at the top of the file.

   ```bash
   Because <BUSINESS RESULT>, Facebook will pursue <OBJECTIVE> by encouraging <CUSTOMER ACTION>; we will judge it mainly by <PRIMARY KPI> while protecting <GUARDRAIL 1> and <GUARDRAIL 2>.
   ```

6. Add the primary KPI formula and two named guardrails. Use cost per purchase as the primary efficiency KPI, return on ad spend as value context, negative feedback rate as the customer-impact guard, and fulfilment headroom as the operating guard.

   ```bash
   Cost per purchase = advertising spend / attributed purchases
Return on ad spend = attributed revenue / advertising spend
Negative feedback rate (%) = negative feedback / impressions × 100
Fulfilment headroom = daily box capacity - forecast daily boxes
Pause threshold for practice: negative feedback rate > 0.03% or fulfilment headroom < 0
   ```

7. Add at least three stop conditions: missing or broken conversion data, an unsupported claim, and any action that would publish or spend without approval.

   ```bash
   STOP when: tracking is missing or inconsistent; a claim has no approved source; the next action publishes, messages, changes targeting, or changes spend without the named approver.
   ```

8. Paste the reviewed output into 01-success-brief.md. Add a final Review Log with your initials, today's date, and the corrections you made.

   ```bash
   ## Review Log
- Reviewer: <INITIALS>
- Date: <YYYY-MM-DD>
- Corrections: <LIST THE FACTS, ASSUMPTIONS, OR WORDING YOU CHANGED>
   ```

9. Check the document word count. If it exceeds 600 words, remove repetition while preserving every required heading, definition, guardrail, unknown, and source reference.

   ```bash
   Length limit: 600 words maximum
   ```


**Test it**

Open 01-success-brief.md and confirm it contains one measurable customer action, a primary KPI with formula, two guardrail metrics, at least three stop conditions, and an UNKNOWN section. Choose any three offer facts at random; each must trace to a heading in the synthetic brand brief.

**Test evidence**

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

**Checkpoint for the next lab**

Keep 01-success-brief.md open. Lab 2 will use its objective, approved facts, guardrails, and unknowns as authoritative inputs.

**Troubleshooting**

- The AI invents customer demographics or market size: Delete the claim, add it to UNKNOWN, and repeat the instruction to use only supplied evidence.
- The objective and KPI do not match: Rewrite the chain from the customer action backwards; a purchase action needs a purchase-related decision metric.
- The brief exceeds 600 words: Move supporting explanation into notes and keep only decisions, definitions, constraints, and unknowns in the main brief.

**Challenge**

Add one leading indicator and one lagging indicator, then explain what decision each can support without replacing the primary KPI.

**Reflection**

Which part of the decision chain most needs human business judgement, and why would an AI model be unable to supply it safely from the brief alone?

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Lab 2 — Create the Audience Evidence Map and Prompt Contract

Learning outcome: LO2: Define evidence-backed audience hypotheses and reusable agent instructions with explicit output, review, and escalation rules.

Goal: You convert synthetic audience signals into three testable audience hypotheses, select one primary segment, and write the G-C-A-T-E prompt contract that governs later AI work. The contract teaches the agent to separate evidence from assumptions and to stop at high-impact actions.

Duration: 60 minutes.

**What you'll build**

C526-campaign-pack/02-audience-and-prompt-contract.md containing an evidence map, three audience hypotheses, a selected segment, and a tested G-C-A-T-E prompt contract.   (Tools: Approved generative AI assistant, text editor, spreadsheet viewer, labs/resources/harbour-hearth-audience-signals.csv.)

**Prerequisites**

- Completed Lab 1 with 01-success-brief.md available.
- Open labs/resources/harbour-hearth-audience-signals.csv.
- Keep all work inside the synthetic scenario; do not add real customer records.

**Step-by-step**

1. Create 02-audience-and-prompt-contract.md and add two top-level headings: Audience Evidence Map and G-C-A-T-E Prompt Contract.

   ```bash
   File: C526-campaign-pack/02-audience-and-prompt-contract.md
Headings: ## Audience Evidence Map | ## G-C-A-T-E Prompt Contract
   ```

2. Read every row in the synthetic audience-signals CSV. Mark the source type as observed behaviour, declared feedback, inferred hypothesis, or unknown. Do not change the original evidence text.

   ```bash
   Open: labs/resources/harbour-hearth-audience-signals.csv
   ```

3. Ask the AI to organise the evidence and propose three audience hypotheses. Paste the success brief and signal rows into the placeholders.

   ```bash
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

4. Review the evidence map against the CSV. Correct any changed wording, missing signal ID, or inference presented as fact.

   ```bash
   Evidence check: each hypothesis must cite at least two signal IDs and state at least one assumption still to test.
   ```

5. Select one primary audience hypothesis for the remaining labs. Write a two-sentence rationale tied to the objective and available evidence, not to personal preference.

   ```bash
   Primary audience hypothesis: <NAME>
Rationale: This segment is prioritised because <EVIDENCE IDS> connect <NEED> to <CUSTOMER ACTION>. We still need to test <ASSUMPTION>.
   ```

6. Write the reusable G-C-A-T-E prompt contract below the evidence map. Fill every placeholder from the reviewed Lab 1 and Lab 2 decisions.

   ```bash
   # G-C-A-T-E PROMPT CONTRACT
GOAL: Support <PRIMARY AUDIENCE HYPOTHESIS> to take <CUSTOMER ACTION> while improving <PRIMARY KPI> and protecting <GUARDRAILS>.
CONTEXT: Use only 01-success-brief.md, the reviewed evidence map, and later files explicitly supplied in this chat. Approved brand facts are <LIST>. Unknowns remain UNKNOWN.
ACTIONS: 1) restate the requested decision, 2) cite input evidence, 3) produce the requested draft, 4) run the quality checks, 5) recommend the next bounded action.
TESTS: Check factual grounding, brand rules, audience value, privacy, advertising truth, objective-action match, and one-variable experiment discipline.
ESCALATION: Stop and ask for a person when evidence is missing, instructions conflict, personal data appears, a claim lacks support, or an action would publish, message, change targeting, or change spend.
OUTPUT: Return a Markdown table with columns Evidence | Assumption | Draft | Risk | Reviewer decision needed. End with STOP / REVISE / READY FOR HUMAN REVIEW and one reason.
   ```

7. Test the contract with a deliberately incomplete request. Paste the contract, then send the request below without giving a discount amount.

   ```bash
   Draft a Facebook post announcing our new discount. Make it sound urgent and include the percentage off.
   ```

8. Check the response. It should stop or mark the discount as UNKNOWN, reject fabricated urgency, and ask for approved offer details. If it invents a percentage, strengthen the evidence and escalation rules and run the test again.

   ```bash
   Expected behaviour: no invented percentage; no false deadline; explicit request for approved offer details; READY status must not be used.
   ```

9. Save the corrected contract and add a Prompt Test Log showing the test request, first failure if any, instruction change, and final behaviour.

   ```bash
   ## Prompt Test Log
- Test request: <TEXT>
- Unsafe or weak behaviour: <OBSERVATION>
- Contract change: <EDIT>
- Final behaviour: <OBSERVATION>
   ```


**Test it**

Run the incomplete-discount request in a fresh chat using only the saved contract. The response must not invent a percentage or deadline, must identify the missing evidence, and must stop before a public action. Also confirm each audience hypothesis cites at least two signal IDs and labels an assumption.

**Test evidence**

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

**Checkpoint for the next lab**

Use the selected audience hypothesis and final G-C-A-T-E contract as the opening context for Labs 3 to 8.

**Troubleshooting**

- All three audience hypotheses sound the same: Force a different situation, need, trigger, and barrier for each while keeping every claim tied to a signal ID.
- The contract produces long essays: Tighten the OUTPUT schema and set maximum rows or word counts for each requested artifact.
- The agent ignores the stop rule: Move escalation rules before the task, repeat the forbidden action types, and require a status label before any draft.

**Challenge**

Add a tool-permission table rating reading files, drafting content, scheduling, messaging, and changing budget as low, medium, or high risk, with the approval required for each.

**Reflection**

How does separating observed evidence from inferred hypotheses change the way you would brief an audience-research agent?

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


## Topic 02 — Content Creation and Ad Copy with AI

content pillars | message hierarchy | post and ad copy | creative briefs | brand consistency

**Key concepts**

- One message hierarchy — Audience tension, promise, proof, offer, and action align every content format.
- Content pillars — Repeatable themes create variety without losing strategic focus.
- Hook with relevance — Earn attention by naming a useful tension, not by exaggerating or withholding truth.
- Proof before pressure — Specific evidence reduces uncertainty more effectively than louder claims.
- Format follows job — Image, carousel, and video choices should match the message and stage of awareness.
- Brand voice rules — Observable language patterns are easier for AI to follow than vague adjectives.
- Variant discipline — Change one meaningful variable at a time so later performance can teach you something.
- Human creative review — Check accuracy, rights, representation, readability, and platform fit before use.


### The Facebook Message Hierarchy

A message hierarchy is the stable logic underneath many creative executions. It begins with a real audience tension, states a relevant promise, supplies a reason to believe, presents the offer or next step, and asks for one clear action. When this logic is strong, a post, carousel, short video, and ad can feel different while still telling the same story.

An AI agent should not invent proof. Give it approved product facts, testimonials with permission, delivery details, prices, and limitations. Ask it to mark any unsupported claim with a placeholder. The marketer then decides whether evidence exists or the claim should be removed.

**Visual framework**

- Audience tension
- Relevant promise
- Reason to believe
- Offer or next step
- Clear action


### Content Pillars and the Customer Journey

Content pillars are repeatable strategic themes, not arbitrary labels. A local bakery might teach breakfast-planning tips, show how the box is packed, prove freshness with process details, and invite pre-orders. Each pillar has a job in the customer journey and a set of evidence it may use.

A calendar balances these jobs across time. It also records format, audience, message angle, call to action, owner, status, and learning question. The learning question is what makes the calendar agent-ready: every item declares what the team hopes to discover, not only what it plans to publish.

**Visual framework**

- Teach — Answer a useful question and build problem awareness.
- Show — Demonstrate the product, process, or customer experience.
- Prove — Use evidence, reviews, comparisons, or behind-the-scenes detail.
- Invite — Present an offer and make the next action unmistakable.
- Engage — Ask a meaningful question or respond to community signals.
- Learn — Use performance and comments to refine the next content cycle.


### Brand Voice as Observable Rules

Brand adjectives such as friendly, bold, or premium are too abstract on their own. Translate them into observable rules: sentence length, point of view, vocabulary, rhythm, humour boundaries, words to use, words to avoid, and examples that demonstrate the tone. These rules can be evaluated consistently by a person or a checking agent.

Examples are powerful but should not become a copying target. Give two or three representative examples and explain why they work. Add negative examples that show exaggeration, pressure, unexplained jargon, or tone that does not fit the brand. This creates a usable boundary around creative variation.

**Visual framework**

Weak instruction: Sound friendly and premium | Make it engaging | Use our usual tone | Avoid sounding robotic

Operational rule: Use warm, direct sentences of 8-18 words | Open with a specific customer situation | Use Singapore English naturally; avoid forced slang | One helpful detail before one invitation


### Facebook Copy Anatomy

Facebook copy competes in a fast feed, so the opening must quickly show relevance. Relevance is not the same as sensationalism. A useful hook names a situation, question, or benefit that the intended audience recognises. The body earns attention by delivering value and proof, while the call to action tells the reader exactly what to do next.

Ad copy and organic copy share the same hierarchy but operate under different delivery conditions. An ad needs a clear match between creative, primary text, headline, destination, and optimisation goal. Organic content can invest more space in conversation and community. The agent should generate variants around one controlled variable, such as hook angle, rather than changing hook, offer, format, and audience all at once.

**Visual framework**

- Specific hook
- Useful value
- Credible proof
- Offer detail
- Single call to action


### Creative System: Image, Carousel, and Video

Format should follow the communication job. A single image works when one focal message is enough. A carousel supports sequence, comparison, or multiple proof points. Short video is useful when motion, demonstration, or personality carries meaning. The first frame should communicate subject and relevance even without sound.

AI image generation accelerates exploration, but it introduces review duties. Check hands, text, packaging, locations, product attributes, cultural details, and any implied endorsement. Keep asset provenance and licence information. Generated creative is a draft until the marketer verifies that it truthfully represents the offer.

**Visual framework**

- Single image — One idea, one focal point, fast recognition, strong offer or proof.
- Carousel — A sequence, comparison, product range, or step-by-step story.
- Short video — Motion, demonstration, personality, transformation, or process.
- First frame — Make the subject and value understandable before sound or context.
- Mobile clarity — Large type, high contrast, simple composition, and safe cropping.
- Rights and truth — Use authorised assets; review generated details and implied claims.


### Content Quality Gate

A content quality gate gives reviewers a shared standard. First verify every fact against an approved source. Then check brand voice, audience usefulness, readability, visual truth, asset rights, and the connection between message, offer, destination, and objective. A piece can be attractive and still fail if it asks for the wrong action.

Record the reason for rejection or revision. These labels become learning data for the next prompt version: unsupported claim, unclear action, off-brand tone, weak proof, visual mismatch, or policy risk. The agent improves when feedback is structured and specific, not when the reviewer simply says 'make it better'.

**Visual framework**

- Grounded facts
- Brand fit
- Audience value
- Creative and rights check
- Objective and action match


### Lab 3 — Build a Seven-Day Facebook Content System

Learning outcome: LO3: Produce a journey-aligned Facebook content calendar and post set from approved facts, audience evidence, and brand rules.

Goal: You use the success brief, selected audience, and prompt contract to design a seven-day Facebook calendar that balances teaching, proof, invitation, and learning. You then turn the selected Invite entry into one publication-ready control post while keeping every fact traceable.

Duration: 45 minutes.

**What you'll build**

C526-campaign-pack/03-content-system.md containing four content pillars, a seven-day calendar, one complete control post, a quality gate, a reviewer correction log, and retained Test Evidence.   (Tools: Approved generative AI assistant, text editor or spreadsheet, Lab 1 and Lab 2 files.)

**Prerequisites**

- Completed 01-success-brief.md and 02-audience-and-prompt-contract.md.
- Selected one primary audience hypothesis in Lab 2.
- No confidential brand assets or real customer comments are used.

**Step-by-step**

1. Create 03-content-system.md. At the top, paste the final decision chain and the selected audience hypothesis from Labs 1 and 2.

   ```bash
   File: C526-campaign-pack/03-content-system.md
Inputs: 01-success-brief.md + selected audience hypothesis from 02-audience-and-prompt-contract.md
   ```

2. Define four content pillars named Teach, Show, Prove, and Invite. For each, write its customer-journey job, allowed evidence, suitable formats, and the action it may request.

   ```bash
   Table columns: Pillar | Journey job | Allowed evidence | Suitable formats | Allowed customer action
   ```

3. Start a fresh AI chat. Paste the G-C-A-T-E contract, the success brief, selected audience hypothesis, and the four-pillar table. Then request the calendar.

   ```bash
   Create a seven-day Facebook organic content calendar for the synthetic Harbour & Hearth Sunrise Breakfast Box.

Return exactly seven rows with columns:
Day | Journey job | Pillar | Format | Hook | Approved evidence used | Main value | Call to action | Learning question | Human review focus

Constraints:
- Use Teach, Show, Prove, and Invite; include each at least once.
- Use at least three formats across single image, carousel, and short video.
- Keep one main message and one customer action per row.
- Cite the exact source heading or signal ID for every evidence claim.
- Do not invent a price, promotion, testimonial, customer count, health claim, or scarcity.
- The learning question must name the metric or feedback signal that could improve the next content cycle.
   ```

4. Review the seven rows as one system. Confirm all four pillars appear, no two consecutive rows do the same journey job, and the Invite posts do not outnumber the combined Teach and Prove posts.

   ```bash
   Calendar balance check: all 4 pillars present; at least 3 formats; one CTA per row; every row has an evidence reference and learning question.
   ```

5. Choose one Invite row as the paid-message control for Lab 4. Ask the AI to draft that one complete post using the output schema below.

   ```bash
   For the selected Invite calendar row, return:
POST ID
PURPOSE: one sentence
PRIMARY TEXT: 60-110 words, warm and direct
ON-CREATIVE TEXT: maximum 8 words
CALL TO ACTION: one action
CREATIVE BRIEF: subject, setting, composition, proof detail, mobile-readability note
EVIDENCE USED: exact source heading or signal ID
REVIEW FLAGS: factual, brand, rights, privacy, or advertising concerns

Use Singapore English naturally without forced slang. One helpful detail must appear before the invitation.
   ```

6. Apply the Content Quality Gate to the control draft. Mark Grounded facts, Brand fit, Audience value, Creative and rights check, and Objective-action match as OK or REVISE, with one sentence of evidence.

   ```bash
   Quality Gate columns: Post ID | Grounded facts | Brand fit | Audience value | Creative and rights | Objective-action match | Reviewer decision
   ```

7. Revise every REVISE item yourself or with a focused follow-up prompt. Do not ask for a total rewrite when one sentence is the problem.

   ```bash
   Focused revision prompt: Revise only <NAMED ELEMENT>. Preserve every approved fact, the selected audience need, the format, and the single call to action. Explain the change in one sentence.
   ```

8. Save the final calendar, control post, quality gate, and a Correction Log listing what the AI got wrong and what instruction would prevent the same issue.

   ```bash
   ## Correction Log
| Post ID | Problem label | Exact correction | Prompt rule to add next time |
   ```


**Test it**

Pick one calendar row and trace its audience need to the Lab 2 hypothesis, its claim to an approved source, its action to the Lab 1 customer action, and its learning question to a named signal. The chain must be complete without relying on an invented fact.

**Test evidence**

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

**Checkpoint for the next lab**

Lab 4 will use the final Invite post and its learning question as the control message for paid creative variants.

**Troubleshooting**

- The calendar is seven versions of the same offer: Reassert the journey job and require different Teach, Show, Prove, and Invite value before changing formats.
- The captions sound generic: Paste the operational brand rules and ask for one specific approved detail before the call to action.
- Evidence citations disappear during revision: Require the source column to remain unchanged and reject any new claim without a source heading or signal ID.

**Challenge**

Draft one Teach post and one Prove post from the calendar, then add a community-engagement question that invites a useful response without collecting personal data.

**Reflection**

Which calendar field makes the system learn over time instead of becoming a faster content factory?

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Lab 4 — Create the Ad Copy and Creative Matrix

Learning outcome: LO3: Generate controlled ad-copy variants and AI-assisted creative prototypes while preserving message, brand, truth, and review evidence.

Goal: You turn the strongest Invite message from Lab 3 into a controlled creative matrix. The lab produces three same-format hook-angle copy variants that reuse one control image, plus clearly separated carousel and short-video extension briefs, then applies a human quality gate before anything reaches an advertising account.

Duration: 75 minutes.

**What you'll build**

C526-campaign-pack/04-ad-copy-creative-matrix.md, one 1080 × 1080 control image, one 360-pixel phone-preview screenshot, and non-experiment carousel and short-video extension briefs.   (Tools: Approved generative AI assistant, approved image tool or Canva, text editor, Labs 2-3 files, labs/resources/harbour-hearth-brand-brief.md.)

**Prerequisites**

- Completed 03-content-system.md with one final Invite post selected as the control message.
- Open 02-audience-and-prompt-contract.md and labs/resources/harbour-hearth-brand-brief.md.
- Use only the synthetic brand brief and generic or generated visual elements.
- If your organisation has no approved image tool, create text-only creative briefs and wireframes instead of uploading assets elsewhere.

**Step-by-step**

1. Create 04-ad-copy-creative-matrix.md. Copy the selected Invite post into a Control Message section and label the fixed elements: audience, offer, proof, destination, CTA, single-image format, and shared control image.

   ```bash
   Fixed controls: Audience | Offer | Proof | Destination | CTA | Headline = Sunrise Breakfast Box | Description = Pre-order by 6 pm | Format = 1:1 single image | Shared image
Changed variable: Primary-text hook angle
   ```

2. Choose three distinct hook angles that can be supported by the brief: convenience, freshness/process, and local morning routine. Do not change the offer or proof between angles.

   ```bash
   Angles: A — Convenience | B — Freshness/process | C — Local morning routine
   ```

3. Paste the prompt contract and fixed controls into the AI assistant, then request a copy matrix.

   ```bash
   Create three Facebook ad-copy variants that differ only in hook angle: convenience, freshness/process, and local morning routine.

Return a table with:
Variant | Hook angle | Primary text (50-90 words) | Fixed headline | Fixed description | CTA label | Approved proof used | Risk flag

Rules:
- Keep audience, offer, destination, proof set, and CTA intent constant.
- Keep the 1:1 single-image format and exact same control image constant.
- Repeat the exact headline "Sunrise Breakfast Box" and description "Pre-order by 6 pm" in every row.
- Do not invent urgency, discounts, testimonials, health benefits, availability, or delivery areas.
- Use one clear claim per sentence.
- If a character limit cannot be met without losing truth, mark REVISE instead of omitting a necessary qualifier.
   ```

4. Create one shared control-image prompt for all three variants. Specify subject, setting, composition, lighting, brand colours, square crop, mobile-safe focal point, and exclusions. Product details must match the brand brief.

   ```bash
   Shared image prompt: <SUBJECT>, <SETTING>, <COMPOSITION>, <LIGHT/STYLE>, palette <COLOURS>, 1:1 square crop, mobile-first focal point, no text, no logos, no people unless required, do not alter <APPROVED PRODUCT DETAILS>.
   ```

5. Open your approved image-generation tool. Generate the shared control image on a 1080 × 1080 canvas, inspect it at full size, and save the best draft locally. If generation is unavailable, create a labelled square wireframe and export it as PNG.

   ```bash
   Output: C526-campaign-pack/04-control-image-1080.png
Canvas: 1080 × 1080 pixels
Status: DRAFT — NOT FOR PUBLICATION
   ```

6. Inspect the shared image against the approved brief. Record any altered product, packaging, text, cultural detail, impossible object, or misleading impression. Preview it at 360 pixels wide and save a screenshot as retained evidence.

   ```bash
   Visual review: product truth | packaging truth | legibility | focal point | cropping | representation | misleading detail | asset provenance
Evidence: C526-campaign-pack/04-phone-preview-360.png
   ```

7. Create a five-card carousel extension brief. Mark it NON-EXPERIMENT so it cannot be confused with the same-format hook test. Give each card one job and no more than eight words of on-card text.

   ```bash
   Card 1: recognise the morning tension
Card 2: show preparation
Card 3: show approved product proof
Card 4: explain the ordering step
Card 5: one call to action
   ```

8. Create a 15-second vertical-video extension brief with five timed beats. Mark it NON-EXPERIMENT and specify visual, on-screen text, voiceover, and proof source for each beat.

   ```bash
   Storyboard columns: Time | Visual | On-screen text | Voiceover | Approved proof source
Timing: 0-2s | 2-5s | 5-8s | 8-12s | 12-15s
   ```

9. Apply the final creative gate to all three copy variants, the shared image, and the two extension briefs: fact source, brand rule, audience value, rights/provenance, mobile clarity, destination match, and single CTA. Mark each READY FOR HUMAN REVIEW or REVISE.

   ```bash
   Final gate columns: Asset | Facts | Brand | Value | Rights | Mobile | Destination | CTA | Decision | Reviewer note
   ```

10. Save the copy matrix, shared image prompt, visual review, extension briefs, and final gate in 04-ad-copy-creative-matrix.md. Keep both evidence PNGs beside it.

   ```bash
   Files: C526-campaign-pack/04-ad-copy-creative-matrix.md
C526-campaign-pack/04-control-image-1080.png
C526-campaign-pack/04-phone-preview-360.png
   ```


**Test it**

Compare variants A, B, and C row by row. Audience, offer, proof set, destination, CTA intent, 1:1 format, and shared image filename must be identical; only the primary-text hook angle may change. Open 04-phone-preview-360.png and confirm the focal idea remains understandable without fabricated text or product details.

**Test evidence**

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

**Checkpoint for the next lab**

Lab 5 will place the three controlled copy variants into one campaign blueprint and preserve the hook angle as the experiment variable.

**Troubleshooting**

- The AI changes the offer between variants: Paste the fixed-controls table above the task and require it to repeat the controls verbatim in every row.
- Generated packaging or food looks inaccurate: Remove brand marks, simplify the composition, restate the approved product details, or use a wireframe pending an authorised real photograph.
- The carousel or video changes the experiment: Label both as NON-EXPERIMENT extensions; only the three same-image copy variants enter Lab 5.

**Challenge**

Create a fourth single-image copy variant that changes proof presentation rather than hook angle, and explain why it belongs in a separate experiment.

**Reflection**

What can a human reviewer see in an AI-generated image that a text-only brand prompt may fail to control?

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


## Topic 03 — Building and Optimising Ad Campaigns with AI

campaign hierarchy | audiences | budgets and placements | metrics | experiments | optimisation

**Key concepts**

- Campaign level — The objective and overall campaign decision live here.
- Ad set level — Audience, placements, budget, schedule, conversion location, and performance goal live here.
- Ad level — Identity, format, media, text, headline, destination, and tracking live here.
- Signal quality — Optimisation is only as useful as the event definition and data feeding it.
- Metric tree — Delivery, attention, action, conversion, and value metrics answer different questions.
- One-variable test — A controlled comparison changes one main factor and keeps the rest stable.
- Diagnosis before action — A weak result may come from delivery, creative, audience, offer, destination, or tracking.
- Learning stability — Frequent major edits destroy comparability and interrupt the platform's learning.


### Campaign, Ad Set, and Ad Hierarchy

Meta Ads Manager uses three distinct levels. The campaign holds the objective. An ad set defines the conversion location or performance goal where available, audience, placements, budget, and schedule. The ad contains the business identity, format, media, copy, destination, and related tracking. Naming and reviewing each level separately prevents silent configuration mistakes.

A campaign blueprint should make the dependency chain visible. If the objective is sales but the ad links to an information page with no purchase event, the creative cannot repair the measurement mismatch. The agent can prepare a draft structure and flag missing inputs, but the authorised advertiser remains responsible for account settings and publication.

**Visual framework**

- Campaign: objective
- Ad set: delivery choices
- Ad: message and creative
- Event: measured action
- Report: decision evidence


### Objective, Event, and Optimisation Alignment

The platform needs a measurable signal that matches the business action. A campaign designed for purchases should have a reliable purchase event and a destination where purchases can occur. When the signal is sparse or unreliable, optimise to an earlier meaningful event temporarily and state the limitation rather than pretending the result represents revenue.

The Meta pixel and Conversions API can send website events into Meta's measurement and optimisation surfaces. They are not a way to bypass privacy controls. Organisations need a valid purpose, appropriate notice or consent where required, secure handling, and a documented data map. Use only data the organisation is authorised to process.

**Visual framework**

- Objective — The type of result the campaign is designed to pursue.
- Conversion location — Where the desired action occurs: website, app, messaging, or another supported surface.
- Performance goal — The result the delivery system should seek within the objective.
- Event — The observed action that represents progress or value.
- Data quality — Accuracy, completeness, timeliness, match quality, and lawful collection.
- Decision KPI — The metric and threshold used to continue, change, stop, or scale.


### Audience Strategy: Prospecting and Re-engagement

Prospecting and re-engagement solve different problems. Prospecting discovers potential demand among people without a direct prior signal. Re-engagement follows up with people who have interacted with the business, subject to the organisation's rights and the platform's available audience options. The message should change with the relationship, not merely repeat the same offer.

Over-segmentation fragments data and can slow learning. Start with the fewest ad sets needed to express a meaningful strategic difference. Use strict controls for genuine constraints and treat other audience inputs as hypotheses. Consolidate similar ad sets when they pursue the same goal with the same message and evidence.

**Visual framework**

Prospecting: Reach people who have not yet shown a direct signal | Use broad delivery or evidence-based suggestions | Teach the problem and establish relevance | Exclude recent purchasers when the offer makes that appropriate

Re-engagement: Reach people with an authorised prior interaction | Use Page, site, video, lead, or customer-list signals where permitted | Resolve objections and make the next step easy | Control recency, frequency, exclusions, and data rights


### The Facebook Performance Metric Tree

Metrics form a diagnostic tree. Delivery metrics reveal whether the system reached people. Attention metrics show whether the message earned a click. Conversion metrics show whether the destination and offer produced the intended action. Value metrics connect results to economics. A single metric rarely explains a problem by itself.

Use stable definitions and denominators. Link click-through rate is link clicks divided by impressions, while a broader click metric may include other interactions. Negative feedback rate is negative feedback divided by impressions, multiplied by 100. Cost per purchase becomes unavailable when purchases are zero; label it N/A instead of dividing by zero. Return on ad spend uses attributed revenue, so it should be read alongside margin, attribution settings, and data-quality limits.

**Visual framework**

- Delivery — Impressions, reach, frequency, spend, CPM = spend / impressions × 1,000.
- Attention — Link CTR = link clicks / impressions; use one click definition consistently.
- Traffic cost — CPC = spend / link clicks; low cost is useful only when visits are relevant.
- Conversion — Conversion rate = purchases / link clicks; CPA = spend / purchases.
- Value — ROAS = attributed revenue / ad spend; interpret with margin and attribution limits.
- Quality guards — Negative feedback rate = negative feedback / impressions × 100, plus operational exceptions.


### A/B Testing as Causal Learning

A useful A/B test answers one decision question. Change one main variable, such as hook angle, while keeping audience, offer, destination, optimisation, and measurement stable. Define the primary metric, minimum decision window, practical threshold, and stop conditions before reviewing the result. Otherwise the team is likely to stop when a favourite variant happens to be ahead.

Statistical confidence is important, but operational decisions also need practical significance and business context. A small click-through improvement may not matter if conversion rate falls. An agent can calculate and summarise, but it should not declare a winner when volume is too low, the variants changed multiple factors, or tracking is inconsistent.

**Visual framework**

- Question
- One changed variable
- Stable controls
- Decision window and threshold
- Documented learning


### Optimisation Diagnosis Before Change

Optimisation begins by validating the data: date range, attribution setting, currency, event definition, missing rows, and account changes. Then locate the funnel break. Weak delivery suggests budget, bid, audience, or eligibility issues. Adequate delivery with weak attention points toward message or creative. Strong clicks with weak conversion points toward offer, destination, trust, or tracking.

Make one bounded change that tests the diagnosis, then allow an appropriate observation window. Large simultaneous edits create a new campaign state and erase the ability to learn what caused the movement. Record the hypothesis, action, approver, timestamp, expected effect, stop rule, and observed result.

**Visual framework**

- Validate data
- Locate funnel break
- Form one hypothesis
- Choose one bounded change
- Observe before the next change


### Lab 5 — Design the Facebook Campaign Blueprint

Learning outcome: LO4: Design an aligned campaign, ad set, and ad structure with explicit audience, budget, placement, signal, and experiment rationale.

Goal: You translate the campaign brief and creative matrix into a draft Meta Ads Manager blueprint without spending money. The blueprint makes every decision at campaign, ad set, and ad level visible, identifies account inputs that are still unknown, and keeps publication behind an authorised approval gate.

Duration: 50 minutes.

**What you'll build**

C526-campaign-pack/05-campaign-blueprint.md containing a named campaign hierarchy, delivery rationale, experiment controls, preflight checklist, and optional unsubmitted Ads Manager draft screenshots.   (Tools: Approved generative AI assistant, text editor, optional Meta Ads Manager draft view, Labs 1-4 outputs.)

**Prerequisites**

- Completed the success brief, audience map, content system, and ad-copy creative matrix.
- Use the synthetic scenario and hypothetical S$40 daily budget; do not activate advertising.
- Optional Meta Ads Manager access must be an account you are authorised to view; stop before Publish.

**Step-by-step**

1. Create 05-campaign-blueprint.md and add the Alignment Chain below. Fill it from Lab 1 without changing the defined customer action or primary KPI.

   ```bash
   Business result → Facebook objective → Conversion location → Event → Primary KPI → Guardrail metrics
   ```

2. Use this scenario decision for the blueprint: Sales objective, website conversion location, Purchase event, hypothetical S$40 daily campaign budget, seven-day observation window. Mark event readiness UNKNOWN until a real implementation verifies it.

   ```bash
   Objective: Sales
Conversion location: Website
Event: Purchase (readiness UNKNOWN)
Budget: S$40/day hypothetical
Observation window: 7 days
Status: DESIGN ONLY — DO NOT ACTIVATE
   ```

3. Define a consistent naming convention, then name one campaign, two strategically distinct ad sets, and three hook-angle ads.

   ```bash
   Naming pattern: HH_SunriseBox_<LEVEL>_<AUDIENCE>_<ANGLE>_2026Q3
Campaign: HH_SunriseBox_Campaign_Sales_2026Q3
Ad set P: HH_SunriseBox_AdSet_Prospecting_2026Q3
Ad set R: HH_SunriseBox_AdSet_Reengagement_2026Q3
Ads: ..._Convenience | ..._Freshness | ..._MorningRoutine
   ```

4. Describe the two ad-set designs. Prospecting uses the evidence-backed need as an audience suggestion with strict geographic control and appropriate exclusions. Re-engagement is PARKED and excluded from the experiment unless an authorised prior-interaction source is verified.

   ```bash
   Ad set columns: Role | Status | Audience evidence | Strict controls | Suggestions/source | Exclusions | Placements | Budget method | Schedule | Unknowns
Prospecting status: DESIGN ELIGIBLE
Re-engagement status: PARKED — SOURCE UNKNOWN
   ```

5. Place the three Lab 4 ads only in HH_SunriseBox_AdSet_Prospecting_2026Q3 for the hook-angle experiment. Record the fixed controls and the one changed variable.

   ```bash
   Eligible ad set: HH_SunriseBox_AdSet_Prospecting_2026Q3
Fixed: audience, offer, proof set, destination, CTA intent, headline, description, 1:1 single-image format, 04-control-image-1080.png, schedule, optimisation
Changed: primary-text hook angle
Primary comparison metric: cost per purchase
Supporting diagnosis: link CTR and conversion rate
   ```

6. Ask the AI to review the blueprint for hierarchy mistakes and hidden contradictions. Paste the G-C-A-T-E contract and your current blueprint.

   ```bash
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

7. Resolve every contradiction that can be fixed from the existing course files. Use https://example.com/sunrise-box as the synthetic design destination. Keep live destination verification, account ID, Page identity, pixel or dataset ID, verified event status, payment method, and authorised re-engagement source as UNKNOWN unless supplied by an authorised owner.

   ```bash
   Design destination: https://example.com/sunrise-box
Live destination verification: UNKNOWN
Unknowns register: Field | Why required | Owner | Evidence needed | Gate blocked
   ```

8. Optional authorised practice: Open Meta Ads Manager, select + Create campaign, choose the blueprint objective, and inspect the campaign, ad set, and ad fields. Enter only synthetic names if the trainer provides a sandbox. Do not add a payment method and do not select Publish. Crop any screenshot to exclude Page, account, billing, pixel, dataset, and personal identifiers.

   ```bash
   Path: Meta Ads Manager → + Create campaign → Objective → Continue → Campaign → Ad set → Ad
STOP before Publish. Close or discard the draft. Screenshot rule: crop all real identifiers before saving.
   ```

9. Complete a preflight checklist covering identity, objective, audience, placements, budget, schedule, event readiness, destination, creative, tracking, rights, privacy, and approvals. Save the file.

   ```bash
   Preflight status values: READY FOR HUMAN REVIEW | REVISE | BLOCKED BY UNKNOWN
Final publication gate: BLOCKED until an authorised account owner resolves every required unknown.
   ```


**Test it**

Trace one ad from its hook through ad, ad set, campaign objective, event, and primary KPI. Then choose one UNKNOWN such as event readiness and explain exactly why the blueprint cannot safely move past its gate without that evidence.

**Test evidence**

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

**Checkpoint for the next lab**

Lab 6 will use the fixed hook-angle experiment and campaign decision metrics to analyse a synthetic result table.

**Troubleshooting**

- The blueprint has an ad-level objective: Move the objective to campaign level; keep creative, copy, identity, destination, and tracking details at ad level.
- The two ad sets differ only by minor interests: Consolidate them unless they represent a meaningful prospecting versus authorised re-engagement strategy.
- The AI recommends switching objectives to improve clicks: Re-anchor it to the business result; clicks are a diagnostic signal, not a substitute for the defined customer action.

**Challenge**

Create a second blueprint for a Leads objective and explain which event, destination, KPI, and copy elements must change rather than being copied from the Sales design.

**Reflection**

Which campaign setting creates the largest downstream mismatch when it is chosen for convenience rather than business purpose?

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Lab 6 — Diagnose Performance and Design One Controlled Test

Learning outcome: LO5: Calculate Facebook metrics, locate a funnel break, distinguish evidence from inference, and recommend one bounded experiment.

Goal: You calculate delivery, attention, conversion, and value metrics from a synthetic Facebook result table, then use an AI analyst under the prompt contract to diagnose the pattern. The lab finishes with one controlled next test rather than a bundle of untraceable changes.

Duration: 55 minutes.

**What you'll build**

C526-campaign-pack/06-performance-diagnosis.md plus 06-facebook-metrics.xlsx with date window, CTR, CPC, conversion rate, CPA, ROAS, negative feedback rate, evidence-linked findings, and one experiment card.   (Tools: Spreadsheet application, approved generative AI assistant, labs/resources/harbour-hearth-facebook-performance.csv, Lab 5 blueprint.)

**Prerequisites**

- Completed 05-campaign-blueprint.md with the hook-angle experiment defined.
- Open the synthetic performance CSV in a spreadsheet application.
- Use one consistent date window, currency, and click definition across all rows.

**Step-by-step**

1. Open harbour-hearth-facebook-performance.csv. Confirm the columns include Variant, Window_Start, Window_End, Impressions, Reach, Link_Clicks, Purchases, Spend_SGD, Revenue_SGD, and Negative_Feedback.

   ```bash
   Open: labs/resources/harbour-hearth-facebook-performance.csv
   ```

2. Check data quality before calculating: no blank variant names, no negative counts, Reach is not greater than Impressions, Spend is positive, and Window_Start and Window_End are identical across rows and span seven days.

   ```bash
   Data-quality log: Check | Result | Row affected | Action taken
   ```

3. Add six columns after Negative_Feedback: Negative_Feedback_Rate, Link_CTR, CPC_SGD, Conversion_Rate, CPA_SGD, and ROAS. Enter the formulas in row 2 and fill them down.

   ```bash
   K2 = IF(D2=0,"",J2/D2)
L2 = IF(D2=0,"",F2/D2)
M2 = IF(F2=0,"",H2/F2)
N2 = IF(F2=0,"",G2/F2)
O2 = IF(G2=0,"",H2/G2)
P2 = IF(H2=0,"",I2/H2)
   ```

4. Format Negative_Feedback_Rate, Link_CTR, and Conversion_Rate as percentages; show Negative_Feedback_Rate to at least two decimal places so the 0.03% threshold remains observable. Format CPC_SGD and CPA_SGD as currency, and ROAS as a number with two decimal places. Do not replace unavailable values with zero.

   ```bash
   Display rule: unavailable denominator → blank or N/A, never 0.00. Negative_Feedback_Rate display precision: at least 0.00%.
   ```

5. Create 06-performance-diagnosis.md. Paste a rounded copy of the completed metric table and record the formulas in a Metric Definitions section.

   ```bash
   File: C526-campaign-pack/06-performance-diagnosis.md
   ```

6. Compare the three variants in funnel order: delivery, attention, conversion, value, then quality guard. Write one observed statement per stage without giving a cause yet.

   ```bash
   Observed statement format: Variant <ID> has <METRIC VALUE> versus <COMPARATOR> during the same seven-day window.
   ```

7. Paste the G-C-A-T-E contract, metric table, and fixed experiment controls into the AI assistant. Request evidence-linked diagnosis.

   ```bash
   Act as a cautious Facebook performance analyst. Use only the supplied synthetic table and experiment design.

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
- Mention Negative_Feedback as a quality guard, not a performance objective.
   ```

8. Verify every number in the AI response against your spreadsheet. Correct arithmetic, renamed metrics, unsupported causes, or claims that ignore the primary KPI.

   ```bash
   Verification table: AI claim | Spreadsheet evidence | Correct? | Correction
   ```

9. Write one Experiment Card. State the question, hypothesis, single changed variable, controls, primary metric, guardrail, observation window, minimum evidence condition, decision threshold, stop rule, and owner.

   ```bash
   ## Experiment Card
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
Human owner:
   ```

10. Save the spreadsheet as C526-campaign-pack/06-facebook-metrics.xlsx and the diagnosis as 06-performance-diagnosis.md.

   ```bash
   Files: C526-campaign-pack/06-facebook-metrics.xlsx
C526-campaign-pack/06-performance-diagnosis.md
   ```


**Test it**

Manually recalculate one row and match the spreadsheet within rounding. Independent benchmark: Freshness_Process CPA = S$11.88 and ROAS = 2.36. Then verify the Experiment Card changes exactly one variable and names at least one condition that would stop or delay the decision.

**Test evidence**

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

**Checkpoint for the next lab**

Lab 7 will use your metric definitions and evidence-linked reporting style; Lab 8 will use the selected guardrail and stop rule in a scaling policy.

**Troubleshooting**

- The spreadsheet shows a divide-by-zero error: Use the IF denominator check exactly as shown and display N/A rather than inventing a metric.
- The AI explains performance using facts not in the table: Move the statement to Possible explanation and add the evidence needed to test it.
- The next experiment changes copy, audience, and budget: Choose the highest-priority hypothesis and change only the variable needed to test it.

**Challenge**

Add frequency = impressions / reach, then describe one situation where a higher value might indicate useful repetition and another where it might indicate fatigue.

**Reflection**

Why can the variant with the best click-through rate still be the wrong choice for the business objective?

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


## Topic 04 — Automating and Scaling Facebook Marketing with AI Agents

workflow design | scheduling and responses | reporting | bounded optimisation | scaling | privacy and advertising safeguards

**Key concepts**

- Automate repetition — Use rules for stable steps; reserve agent reasoning for contextual choices.
- Draft before action — Early workflows prepare and recommend while a person approves publication or spend.
- Risk-tier tools — Reading data is lower risk than publishing, editing budgets, or messaging a customer.
- Stop conditions — Every loop needs limits for retries, spend, time, confidence, and policy uncertainty.
- Response triage — Routine questions may use approved answers; complaints, safety, and personal data escalate.
- Evidence-linked reports — Each insight names the metric, comparison, date window, and supporting row.
- Scale by proof — Increase exposure only when results, operations, and customer experience remain healthy.
- Reversible actions — Prefer drafts, small changes, cooldowns, logs, and rollback paths.


### Should This Task Be Automated?

A task is a good automation candidate when it has a repeatable trigger, accessible and reliable inputs, a clear decision boundary, an output that can be checked, and a safe way to stop or recover. Scheduling an approved post at a specified time fits well. Inventing a response to a sensitive complaint with no policy or escalation path does not.

Separate deterministic and agentic work. A rule can calculate a threshold, apply a naming convention, or route a message containing a known keyword. An agent can summarise comments, classify intent, or draft a context-sensitive reply. Combining them produces a safer workflow: rules constrain the space in which reasoning occurs.

**Visual framework**

- Repeatable trigger
- Reliable input
- Clear rule or judgement boundary
- Verifiable output
- Safe failure path


### The Governed Agentic Operating Loop

A governed loop starts with authorised inputs, plans within a written policy, creates a draft or recommendation, validates the result, requests approval at the required gate, performs the approved action, logs what happened, and monitors the outcome. The loop ends when the goal is met, evidence is insufficient, a limit is reached, or risk requires escalation.

Early deployments should keep publication, messaging, targeting, and spend changes behind human approval. As reliability evidence grows, some low-risk reversible actions may be delegated. Autonomy is therefore a property of each action, not a label applied to the whole system.

**Visual framework**

- Observe authorised inputs
- Plan within policy
- Create draft or recommendation
- Validate and approve
- Act, log, and monitor


### Facebook Operations You Can Coordinate

Meta Business Suite provides operational surfaces for Page posts, Planner, Inbox, automations, and Insights. An agentic workflow can prepare content and recommendations around these surfaces, but account roles and feature availability differ. The workflow should detect missing permissions and fall back to a draft or hand-off rather than attempting to bypass access controls.

Automated responses are suitable for routine, low-risk information such as an approved collection window or ordering link. They are not a substitute for judgement in complaints, refunds, safety concerns, legal questions, or messages containing personal data. Each response rule needs an owner, active hours, approved wording, review date, and escalation route.

**Visual framework**

- Planning — Turn approved strategy into a dated calendar with owners and dependencies.
- Scheduling — Prepare or schedule approved Page posts in Meta Business Suite.
- Inbox — Classify messages and comments, then draft from an approved response bank.
- Automations — Use greetings, away messages, instant replies, or keywords for bounded routine cases.
- Insights — Collect reach, engagement, and post-level evidence for a consistent date window.
- Reporting — Summarise movements, causes, limitations, and the next controlled experiment.


### Bounded Optimisation Policy

A bounded optimisation policy turns vague autonomy into explicit authority. It states when the system has enough data to act, which actions are allowed, the maximum change size, the cooldown period, the stop conditions, the approval owner, and the evidence that must be logged. Anything outside the policy becomes a recommendation for a person.

Thresholds should reflect economics and operational capacity, not generic internet advice. A bakery that can fulfil 40 boxes a day should not scale merely because return on ad spend is high. Inventory, service capacity, refund rate, customer sentiment, and cash constraints are part of the optimisation boundary.

**Visual framework**

- Eligibility — Minimum data volume and clean tracking before any recommendation.
- Allowed action — Exactly what may change: pause, draft a variant, or propose a budget adjustment.
- Magnitude — Maximum percentage or absolute change in one decision cycle.
- Cooldown — Minimum observation time before another material change.
- Stop rule — Spend, CPA, tracking, negative-feedback, capacity, or policy condition that halts the loop.
- Approval and log — Named approver plus before/after values, reason, and rollback instruction.


### Scale Through a Learning Ladder

Scaling begins with trustworthy measurement and a repeatable result. Confirm that performance survives more than one short window and that fulfilment, response quality, inventory, and customer experience remain stable. Increase exposure gradually, observe, and keep a rollback path. A winning creative can fatigue, and a broadening audience can change lead quality.

Expand one dimension at a time: budget, audience, placement, geography, offer, or creative volume. This preserves learning. Meta's automated budget and audience products can distribute delivery dynamically, but the marketer still defines objective, constraints, exclusions, data rights, and the business limit beyond which more volume is not desirable.

**Visual framework**

- Validate signal
- Repeat the result
- Stabilise operations
- Increase exposure gradually
- Expand one dimension at a time


### Privacy, Advertising, and Incident Safeguards

Singapore's PDPA sets obligations for the collection, use, disclosure, protection, accuracy, retention, and transfer of personal data. Marketing teams should map what data enters an AI or advertising tool, why it is needed, who can access it, how long it is retained, and how a person can exercise applicable rights. Never paste customer identifiers or confidential lists into an unapproved AI tool.

Advertising safeguards cover claims, creative rights, audience fairness, offer clarity, destination consistency, and platform rules. If an agent produces a risky public output or makes an incorrect action, pause the workflow, preserve the evidence, contain the impact, notify the responsible owner, correct or reverse the action where possible, and update the guardrail that failed.

**Visual framework**

- Purpose and consent — Use personal data only for an appropriate notified purpose with a valid basis.
- Data minimisation — Give the agent only the fields needed; use synthetic or aggregated data for practice.
- Truthful advertising — Substantiate claims and ensure creative and destination tell the same story.
- Fair treatment — Avoid discriminatory assumptions, sensitive inference, manipulation, or exclusion without justification.
- Access and security — Use least privilege, approved tools, protected secrets, and retention limits.
- Incident response — Pause, preserve logs, contain harm, notify the owner, correct the output, and learn.


### Lab 7 — Design the Facebook Operations Agent Runbook

Learning outcome: LO6: Design a governed workflow for content scheduling, routine responses, escalation, and evidence-linked reporting.

Goal: You design a draft-first operations workflow that coordinates approved Facebook content, Meta Business Suite surfaces, routine Inbox responses, and a weekly report. You then simulate message triage on synthetic scenarios so routine questions and human-escalation cases follow different paths.

Duration: 60 minutes.

**What you'll build**

C526-campaign-pack/07-operations-agent-runbook.md containing the workflow map, permission table, response bank, triage results, scheduling checklist, weekly report schema, and retained Test Evidence.   (Tools: Approved generative AI assistant, text editor or spreadsheet, brand brief, message scenarios, runbook template, optional Meta Business Suite view.)

**Prerequisites**

- Completed Labs 1-6 and have the content calendar, prompt contract, and metric definitions available.
- Open labs/resources/harbour-hearth-brand-brief.md, harbour-hearth-message-scenarios.csv, and operations-runbook-template.md.
- Do not use real messages, names, phone numbers, email addresses, or order details.
- Any Meta Business Suite activity remains in draft or view-only mode unless an authorised Page owner separately approves it.

**Step-by-step**

1. Open operations-runbook-template.md and save a copy as 07-operations-agent-runbook.md. Keep its four workflow lanes: Content Planning, Scheduling, Inbox Triage, and Weekly Reporting.

   ```bash
   Template: labs/resources/operations-runbook-template.md
Save as: C526-campaign-pack/07-operations-agent-runbook.md
   ```

2. For each lane, complete the operating-loop fields: trigger, authorised inputs, agent task, tool or surface, validation, human approval, action, log evidence, and stop or escalation path.

   ```bash
   Runbook columns: Lane | Trigger | Inputs | Agent task | Tool/surface | Validation | Approval | Action | Log | Stop/escalation
   ```

3. Create a permission table for reading course files, drafting content, preparing a schedule, publishing a post, drafting a reply, sending a reply, reading aggregate insights, changing targeting, and changing budget.

   ```bash
   Permission columns: Action | Risk level | Reversible? | Allowed in this workflow | Human role required | Evidence to log
   ```

4. Set this lab's authority: the agent may read synthetic files, draft content, classify synthetic messages, and prepare recommendations. Publishing, sending messages, changing targeting, and changing spend are blocked behind a person.

   ```bash
   Allowed: read synthetic inputs; draft; classify; calculate; recommend
Blocked: publish; send; change targeting; change budget; upload customer lists
   ```

5. Build an approved routine-response bank for the collection window, product information, ordering link, delivery-area unknown, and order-specific help. General opening hours remain UNKNOWN. Use only the brand brief; route order-specific and personal-data cases to a person.

   ```bash
   Response bank columns: Intent | Approved reply | Source | Prohibited additions | Escalation condition | Owner
Do not broaden the approved 7:30-11:00 collection window into general opening hours.
   ```

6. Open the synthetic message-scenarios CSV. Paste it, the response bank, and the G-C-A-T-E contract into the AI assistant. Ask for triage only, not message sending.

   ```bash
   Classify each synthetic Facebook message scenario.

Return columns:
scenario_id | intent | routine_or_human | approved_response_id | draft_reply_or_handoff_note | risk_reason | log_fields

Rules:
- Use only the approved response bank and brand brief.
- Routine replies may give approved public information.
- Escalate complaints, refunds, safety concerns, legal threats, account issues, order-specific cases, and any personal data.
- Never request or repeat personal data in the draft.
- Do not send anything; output is for human review.
   ```

7. Review the triage table. Any scenario containing an order number, contact detail, complaint, safety concern, refund request, or legal language must route to a person even if part of the question looks routine.

   ```bash
   Triage invariant: higher-risk content overrides a routine keyword match.
   ```

8. Write the scheduling checklist from the Lab 3 calendar. Include Page identity, content ID, approved asset, final copy, link, time zone, date and time, reviewer, status, and rollback owner.

   ```bash
   Scheduling status values: DRAFT | READY FOR HUMAN REVIEW | APPROVED TO SCHEDULE | SCHEDULED | PAUSED
   ```

9. Optional view-only practice: In Meta Business Suite, open Planner and locate the Create post and scheduling controls described by the trainer. Do not schedule or publish. Record any interface difference in the runbook so the owner can verify the current path.

   ```bash
   Reference path: Facebook Page → Meta Business Suite → Create post / Planner → Scheduling options
Action in this lab: view only; close without saving or scheduling.
   ```

10. Create the weekly report schema. Every finding must name the date window, source, metric definition, comparison, evidence row, limitation, and recommended next action with owner.

   ```bash
   Report sections: Objective status | Content delivered | Metric movement | Audience feedback themes | Risks and exceptions | One next experiment | Decisions needed
   ```

11. Save the completed runbook with a Change Log for response-bank updates, workflow exceptions, and owner decisions.

   ```bash
   ## Change Log
| Date | Workflow or response ID | Evidence | Change | Owner | Review date |
   ```


**Test it**

Use M01 as the routine case and M06 as the escalation case. M01 must cite the approved collection window; M06 must contain a handoff note without repeating the phone number. Also confirm every high-impact action in the permission table names a human role.

**Test evidence**

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

**Checkpoint for the next lab**

Lab 8 will reuse the permission table, report evidence rules, human roles, stop paths, and change log as the foundation of a bounded scale policy.

**Troubleshooting**

- The agent treats every message as routine: Move the override risks above keyword rules and require risk classification before response selection.
- The runbook says 'review as needed': Name the exact check, human role, evidence, and status transition required at that point.
- Scheduling instructions do not match the current interface: Record the interface difference, use the current official Help path, and keep the action in view or draft mode.

**Challenge**

Add a response-quality sampling plan that reviews a percentage of routine drafts each week and turns recurring corrections into response-bank changes.

**Reflection**

Which operations step benefits most from deterministic rules, and which benefits most from contextual agent reasoning?

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Lab 8 — Simulate a Bounded Optimisation and Scale Loop

Learning outcome: LO6 and LO5: Apply performance, operational, privacy, and customer-impact limits to a human-governed scaling decision.

Goal: You complete the course by converting all prior guardrails into a bounded optimisation policy, then run synthetic scenarios through an agent that may recommend but cannot execute. The final campaign operations pack shows when to hold, pause, investigate, or propose a small scale step and records the evidence behind each decision.

Duration: 65 minutes.

**What you'll build**

C526-campaign-pack/08-bounded-scale-policy.md plus a final manifest linking all eight campaign-pack checkpoints, owners, approvals, stop conditions, and rollback evidence.   (Tools: Approved generative AI assistant, spreadsheet or text editor, scale scenarios, bounded-policy template, Labs 1-7 outputs.)

**Prerequisites**

- Completed all Labs 1-7; this lab reuses the success brief, prompt contract, performance diagnosis, and operations runbook.
- Open labs/resources/harbour-hearth-scale-scenarios.csv and bounded-scale-policy-template.md.
- Use only synthetic scenarios and hypothetical budget values.
- The workflow may recommend actions but may not change a real campaign or send a message.

**Step-by-step**

1. Open bounded-scale-policy-template.md and save a copy as 08-bounded-scale-policy.md. Fill its primary KPI, guardrail metrics, stop rule, permission table, and human roles from Labs 1, 6, and 7.

   ```bash
   Template: labs/resources/bounded-scale-policy-template.md
Save as: C526-campaign-pack/08-bounded-scale-policy.md
Inputs: 01-success-brief.md | 02-audience-and-prompt-contract.md | 06-performance-diagnosis.md | 07-operations-agent-runbook.md
   ```

2. Write the policy with six blocks: eligibility, allowed recommendations, maximum change, cooldown, stop or pause conditions, and approval plus log requirements.

   ```bash
   ## Bounded Optimisation Policy
Eligibility: same metric definitions; complete 7-day window; event status healthy; minimum 10 purchases; no unresolved data-quality issue.
Allowed recommendations: HOLD, PAUSE, INVESTIGATE, PROPOSE CREATIVE TEST, PROPOSE BUDGET CHANGE.
Maximum budget recommendation: +15% or -15% per decision cycle.
Cooldown: 72 hours after a material change before another scale recommendation.
Stop or pause: tracking error; unsupported claim; privacy concern; negative feedback rate above 0.03%; fulfilment capacity below forecast demand; negative margin context; missing approver.
Approval and log: named marketing owner approves; record before/after value, evidence, reason, timestamp, expected result, rollback action.
   ```

3. Open harbour-hearth-scale-scenarios.csv and read the column definitions. Confirm that Metric_Definition_Version matches the approved version, Event_Status is healthy, and Unresolved_Data_Quality_Issue is no before treating a row as eligible. Keep every row unchanged so classmates work from the same evidence.

   ```bash
   Open: labs/resources/harbour-hearth-scale-scenarios.csv
Eligibility evidence: Metric_Definition_Version = v1 | Event_Status = healthy | Unresolved_Data_Quality_Issue = no
   ```

4. Paste the G-C-A-T-E contract, bounded policy, and scenario table into the AI assistant. Make its authority recommendation-only.

   ```bash
   You are a recommendation-only Facebook campaign operations agent. Apply the bounded policy to each synthetic scenario independently.

Return columns:
scenario_id | eligible_yes_no | evidence | guardrail_status | recommendation | proposed_change | human_approval_needed | cooldown_end | rollback_trigger | log_note

Decision order:
1. Validate data and eligibility.
2. Apply privacy, advertising, customer-impact, capacity, and tracking stop rules.
3. Review the primary KPI and value context.
4. Apply the cooldown: when As_Of_Datetime is earlier than Last_Change_Datetime + 72 hours, choose HOLD and make no budget proposal.
5. Choose only one allowed recommendation and cap any budget proposal at 15%.

Never execute a change. When evidence conflicts or is missing, choose INVESTIGATE or HOLD and name the missing evidence.
   ```

5. Check the scenario decisions against policy invariants. A tracking error, privacy concern, unsupported claim, negative feedback rate above 0.03%, negative margin context, or capacity shortfall must prevent scaling even when ROAS is strong. A cooldown violation is also decisive: when As_Of_Datetime is earlier than Last_Change_Datetime + 72 hours, the recommendation must be HOLD with no budget proposal. Use SC06 to verify this rule.

   ```bash
   Invariant check columns: Scenario | Trigger present | Required policy effect | Agent effect | Corrected decision
SC06 expected effect: HOLD | Proposed change: none
   ```

6. For any incorrect agent decision, identify whether the failure came from missing input, ambiguous policy, wrong calculation, or instruction order. Revise the policy or prompt and rerun only that scenario.

   ```bash
   Correction log: Scenario | Failure type | Evidence | Rule change | New recommendation
   ```

7. Choose one eligible healthy scenario and write a human Decision Note. Calculate the proposed daily budget from Current_Daily_Budget_SGD, calculate Cooldown_End from Last_Change_Datetime + 72 hours, and include expected effect, capacity check, guardrails, approver, and rollback trigger.

   ```bash
   Status must remain PROPOSED — AWAITING HUMAN APPROVAL.
   ```

8. Create the final campaign-pack manifest. List each numbered artifact, its purpose, authoritative inputs, owner, current status, last review date, and next decision it supports.

   ```bash
   Manifest columns: Artifact | Purpose | Authoritative inputs | Owner | Status | Last review | Next decision
   ```

9. Add a 30-day draft-first pilot plan with weekly checkpoints for content quality, metric integrity, response exceptions, customer impact, and policy changes. Keep all public or financial actions under the named owners.

   ```bash
   Week 1: baseline and draft quality
Week 2: exception and correction labels
Week 3: one controlled experiment
Week 4: governance review and authority decision
   ```

10. Save 08-bounded-scale-policy.md and confirm the C526-campaign-pack folder contains artifacts 01 through 08, the two Lab 4 image-evidence files, and the metric workbook.

   ```bash
   Final folder: C526-campaign-pack/
Required numbered files: 01, 02, 03, 04, 05, 06, 07, 08
Evidence: 04-control-image-1080.png | 04-phone-preview-360.png | 06-facebook-metrics.xlsx
   ```


**Test it**

Run four invariants: Tracking_Error = yes must block scaling; Negative_Feedback_Rate_Pct > 0.03 must block scaling; a proposed budget change must be no greater than 15%; and As_Of_Datetime earlier than Last_Change_Datetime + 72 hours must produce HOLD with no budget proposal. Record SC06 as the cooldown Test Evidence row. Finally, trace the selected scale recommendation back to its metric row, policy rule, human owner, and rollback trigger.

**Test evidence**

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

**Checkpoint for the next lab**

The completed C526-campaign-pack is your reusable implementation model. Replace synthetic inputs only after your organisation authorises the data, owners, platform access, and operating limits.

**Troubleshooting**

- The agent scales whenever ROAS is high: Move stop conditions before performance evaluation and require guardrail status to be clear before any scale recommendation.
- The proposed change exceeds 15%: Add a deterministic cap calculation and reject any recommendation whose absolute percentage is greater than 15.
- The policy contains vague terms such as 'enough data': Replace them with a named window, minimum event count, data-quality condition, owner, and exception path.

**Challenge**

Design a second authority level that may automatically pause on a verified tracking outage but still cannot resume or change budget without a person; explain why pause and resume have different risk.

**Reflection**

What evidence would you require before increasing this workflow's autonomy beyond recommendation-only mode?

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


## Wrap-Up — From Course Pack to Operating Practice

Your final campaign operations pack connects strategy, content, campaign structure, measurement, and governed automation. Its value comes from the traceable decisions between the files, not from any one AI-generated draft.

**Before using the workflow at work**

- Replace the synthetic brief with an approved business brief and document every authorised data source.
- Validate current Meta interface options, account permissions, objectives, and advertising rules for the intended market.
- Set named owners for brand review, privacy review, publishing, customer escalation, and budget approval.
- Start with draft-and-recommend mode, measure errors and corrections, then expand authority only where evidence supports it.

**Evidence to retain**

- Input version, prompt version, generated variants, reviewer corrections, and approval decision.
- Metric definitions, reporting window, source extract, calculations, and known data limitations.
- Before-and-after campaign settings, reason for change, owner, cooldown, result, and rollback action.

---


## Next Steps

- Re-run the campaign pack with one real, authorised offer while keeping all actions in draft.
- Create a small library of approved brand examples, evidence sources, response templates, and rejection labels.
- Review Meta's current official guidance before changing campaign settings or enabling a new automation.
- Pilot one low-risk workflow for two weeks, track corrections and exceptions, and revise the prompt contract.
- Hold a monthly review of data access, content quality, customer impact, performance thresholds, and rollback readiness.


## Glossary

- **Ad** — The creative, text, identity, destination, and related tracking shown to an audience.
- **Ad set** — The campaign level where audience, placements, budget, schedule, and performance choices are configured.
- **Agent** — A system that uses a model, instructions, and tools to pursue a multi-step goal within guardrails.
- **Approval gate** — A required human decision before a high-impact action can proceed.
- **Attribution** — The rule used to associate an observed customer action with marketing activity.
- **Campaign** — The top advertising level that contains the objective and one or more ad sets.
- **Conversion rate** — The share of relevant visits or clicks that complete the defined conversion action.
- **CPA** — Cost per acquisition or result: spend divided by the number of defined results.
- **CPC** — Cost per click: spend divided by the selected click count.
- **CPM** — Cost per one thousand impressions: spend divided by impressions, multiplied by 1,000.
- **CTR** — Click-through rate: selected clicks divided by impressions, expressed as a percentage.
- **Guardrail** — A rule, check, permission, or technical control that constrains unsafe or unwanted behaviour.
- **Impression** — One delivery of content or an ad to a screen; the same person can generate multiple impressions.
- **Prompt contract** — Reusable instructions defining goal, inputs, rules, output schema, and escalation behaviour.
- **Reach** — The estimated number of distinct people who saw the content or ad.
- **ROAS** — Return on ad spend: attributed revenue divided by advertising spend.
- **Stop condition** — A defined state that ends or pauses an agentic loop.
