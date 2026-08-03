"""Single source of truth for Agentic AI for Facebook Marketing (C526)."""

# ------------------------------------------------------------------ metadata
TITLE = "Agentic AI for Facebook Marketing (C526)"
SHORT_TITLE = "Agentic AI for Facebook Marketing (C526)"
COURSE_CODE = "C526"
VERSION = "v1.0"
VERSION_DATE = "3 August 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Course Trainer"
TRAINER_CERT = "Digital marketing and applied AI practitioner"
TRAINER_DELIVERS = "Facebook marketing, digital advertising, analytics, and applied AI workflows"
DAYS = 2
MODE = "Instructor-led, concept-first learning with connected hands-on labs"

# The advertised 15 instructional hours are delivered as 7.5 instructional
# hours per day. Each day also contains two 15-minute tea breaks, so the Lesson
# Plan totals 480 scheduled minutes excluding lunch.
DAY_MINUTES = 480
DAILY_TIMING = "9:00 am - 6:00 pm (1-hour lunch; two 15-minute tea breaks)"
DARK_THEME = False

ICE_BREAKER = [
    "Your name, role, and the Facebook Page or business context you support.",
    "One Facebook marketing task that currently takes too much time.",
    "One decision you would never allow an AI agent to make without approval.",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain how Facebook organic marketing, paid media, and an agentic AI workflow connect to a measurable business objective.",
    "LO2: Create a reusable campaign brief and prompt contract that defines audience evidence, brand voice, tools, guardrails, and approval gates.",
    "LO3: Produce an aligned Facebook content calendar, post set, ad-copy matrix, and creative briefs with consistent brand voice.",
    "LO4: Design a Facebook campaign blueprint across campaign, ad set, and ad levels, including audience, budget, placement, and experiment choices.",
    "LO5: Calculate and interpret Facebook performance metrics, diagnose a result, and recommend a controlled next action from evidence.",
    "LO6: Design a governed agentic workflow for scheduling, responses, reporting, optimisation, and scaling with privacy and advertising safeguards.",
]
LO_TITLES = [
    "Marketing System",
    "Prompt Contract",
    "Content System",
    "Campaign Design",
    "Performance Learning",
    "Governed Automation",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(
        num=1,
        code="01",
        title="Getting Started with Agentic AI for Facebook Marketing",
        subtitle="Facebook ecosystem | objectives and audiences | agent anatomy | prompting | approval gates",
        concepts=[
            ("Outcome before output", "Start with a business result and customer action, not a request to 'make posts'."),
            ("Organic and paid roles", "Organic content builds attention and proof; paid delivery buys controlled reach and learning."),
            ("Agentic loop", "An agent plans, uses tools, checks evidence, and iterates until a stop condition is reached."),
            ("Evidence boundary", "Facts, customer data, and performance numbers need provenance; unknowns remain labelled assumptions."),
            ("Prompt contract", "Role, goal, context, inputs, rules, output schema, and review criteria make work repeatable."),
            ("Audience hypothesis", "A segment is a testable need and behaviour pattern, not a stereotype or invented demographic."),
            ("Human authority", "Publishing, spend, targeting changes, and sensitive replies remain approval-controlled actions."),
            ("Audit trail", "Save the brief, inputs, versions, approvals, and final decision so the workflow can be reviewed."),
        ],
        teaching=[
            dict(
                title="Facebook Marketing as a Connected System",
                kind="flow",
                kicker="TOPIC 01 · SYSTEM VIEW",
                visual=["Business objective", "Audience need", "Useful content", "Organic or paid delivery", "Measured customer action"],
                paragraphs=[
                    "Facebook marketing is a system, not a sequence of unrelated posts. A useful plan begins with a business objective, identifies the customer action that would demonstrate progress, then chooses content and delivery methods that make that action more likely. Organic posts, community conversations, Page information, and paid ads should therefore share one message hierarchy and one measurement plan.",
                    "The same content can perform different jobs at different stages. A how-to video may build awareness, a customer proof post may reduce uncertainty, and a limited offer may invite a conversion. An AI agent can help coordinate these jobs, but it cannot decide what success means for the business. The marketer supplies the objective, evidence, constraints, and final judgement.",
                ],
            ),
            dict(
                title="From Generative AI to an Agentic Workflow",
                kind="compare",
                kicker="TOPIC 01 · WHAT MAKES IT AGENTIC",
                left_title="Single AI task",
                right_title="Agentic workflow",
                left=[
                    "One prompt produces one draft",
                    "The user manually supplies every input",
                    "No persistent state or explicit stop rule",
                    "Quality depends on one response",
                ],
                right=[
                    "A goal is decomposed into multiple steps",
                    "Tools retrieve data or create controlled outputs",
                    "State, checks, retries, and stop conditions are explicit",
                    "A person approves high-impact actions",
                ],
                paragraphs=[
                    "Generative AI creates text, images, or analysis from a prompt. An agentic workflow goes further: it manages a multi-step goal, selects or calls tools, observes results, and decides what to do next within defined limits. A content assistant that drafts one caption is useful, but it becomes agentic only when it can work through a plan such as research, draft, check, revise, route for approval, and record the outcome.",
                    "Not every task needs autonomy. Deterministic work such as applying a known naming convention is usually safer as a checklist or rule. Agentic reasoning is more valuable when inputs are unstructured, trade-offs are contextual, or the path changes after new evidence. Begin with the smallest useful loop and add tools only when each tool has a clear purpose and risk level.",
                ],
            ),
            dict(
                title="The Six-Part Marketing Agent",
                kind="tiles",
                kicker="TOPIC 01 · AGENT ANATOMY",
                visual=[
                    ("Goal", "The result, customer action, time horizon, and success threshold."),
                    ("Context", "Brand, offer, audience evidence, channel role, and constraints."),
                    ("Instructions", "Decision rules, required steps, output format, and escalation logic."),
                    ("Tools", "Approved data sources, content tools, calendars, and reporting surfaces."),
                    ("Memory", "Briefs, past variants, decisions, and lessons that should persist."),
                    ("Checks", "Brand, factual, privacy, policy, and performance validation before action."),
                ],
                paragraphs=[
                    "A reliable marketing agent needs more than a clever prompt. Its goal defines the finish line. Context explains the brand and audience. Instructions describe the route and exceptions. Tools determine what the agent may read or change. Memory preserves only the state needed for the next decision. Checks test whether the result is safe and useful before the workflow proceeds.",
                    "A weakness in any one part propagates. If the goal says 'increase engagement' but does not name the customer action or time window, the agent may optimise reactions that have no business value. If the tools include a publishing action without an approval gate, a drafting error becomes a public error. Design the system before choosing the model.",
                ],
            ),
            dict(
                title="Objective, Customer Action, and KPI Chain",
                kind="flow",
                kicker="TOPIC 01 · MEASUREMENT LOGIC",
                visual=["Business result", "Marketing objective", "Customer action", "Primary KPI", "Guardrail metric"],
                paragraphs=[
                    "A measurement chain prevents vanity metrics from becoming the strategy. The business result might be breakfast-box revenue. The marketing objective could be qualified pre-orders. The customer action is a completed order. The primary KPI may be cost per purchase or return on ad spend, while a guardrail could be refund rate, negative feedback, or response quality.",
                    "Choose the Meta campaign objective that most closely matches the larger business goal and the event that can be measured reliably. An awareness objective is not a cheaper substitute for a sales objective when sales are the real decision criterion. Equally, a sales objective is weak when the business has no trustworthy conversion signal. The objective, data signal, and KPI must agree.",
                ],
            ),
            dict(
                title="Audience Evidence Before Targeting",
                kind="tiles",
                kicker="TOPIC 01 · AUDIENCE DESIGN",
                visual=[
                    ("Observed", "Existing customer questions, purchases, site behaviour, and Page interactions."),
                    ("Declared", "Needs and preferences people voluntarily shared through interviews or forms."),
                    ("Inferred", "A labelled hypothesis derived from patterns, never presented as fact."),
                    ("Excluded", "Sensitive traits, unjustified personal data, and segments the offer should not reach."),
                    ("Testable", "A need, trigger, barrier, message angle, and measurable response."),
                    ("Revisable", "A segment changes when evidence contradicts the original hypothesis."),
                ],
                paragraphs=[
                    "Audience research should separate what is known from what is inferred. Observed data may show that weekday pre-orders peak before 9 am. Customer interviews may reveal that convenience matters more than variety. An AI model can propose segment hypotheses, but it must label them as hypotheses and cite the supplied evidence instead of manufacturing demographic detail.",
                    "Meta's delivery systems can work with broad audiences, audience suggestions, and strict controls such as location, minimum age, language, and exclusions. The marketer's job is to provide a commercially meaningful signal without narrowing the audience through stereotypes. Any customer list requires the organisation to have the necessary rights, permissions, and lawful basis for its use.",
                ],
            ),
            dict(
                title="The Prompt Contract",
                kind="flow",
                kicker="TOPIC 01 · REUSABLE INSTRUCTIONS",
                visual=["Role and goal", "Grounded inputs", "Decision rules", "Output schema", "Review and escalation"],
                paragraphs=[
                    "A prompt contract turns an informal request into an operating instruction. It tells the agent who it is helping, what outcome matters, which inputs are authoritative, which choices are allowed, and exactly what form the result must take. A structured output such as a table with evidence, assumptions, risks, and next action is easier to review than a persuasive paragraph.",
                    "Include failure behaviour. The agent should say 'insufficient evidence' when a required input is missing, request clarification when two constraints conflict, and stop when the next action would publish, spend money, change targeting, or expose personal data. These rules reduce silent guessing and make human review faster.",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Content Creation and Ad Copy with AI",
        subtitle="content pillars | message hierarchy | post and ad copy | creative briefs | brand consistency",
        concepts=[
            ("One message hierarchy", "Audience tension, promise, proof, offer, and action align every content format."),
            ("Content pillars", "Repeatable themes create variety without losing strategic focus."),
            ("Hook with relevance", "Earn attention by naming a useful tension, not by exaggerating or withholding truth."),
            ("Proof before pressure", "Specific evidence reduces uncertainty more effectively than louder claims."),
            ("Format follows job", "Image, carousel, and video choices should match the message and stage of awareness."),
            ("Brand voice rules", "Observable language patterns are easier for AI to follow than vague adjectives."),
            ("Variant discipline", "Change one meaningful variable at a time so later performance can teach you something."),
            ("Human creative review", "Check accuracy, rights, representation, readability, and platform fit before use."),
        ],
        teaching=[
            dict(
                title="The Facebook Message Hierarchy",
                kind="flow",
                kicker="TOPIC 02 · MESSAGE DESIGN",
                visual=["Audience tension", "Relevant promise", "Reason to believe", "Offer or next step", "Clear action"],
                paragraphs=[
                    "A message hierarchy is the stable logic underneath many creative executions. It begins with a real audience tension, states a relevant promise, supplies a reason to believe, presents the offer or next step, and asks for one clear action. When this logic is strong, a post, carousel, short video, and ad can feel different while still telling the same story.",
                    "An AI agent should not invent proof. Give it approved product facts, testimonials with permission, delivery details, prices, and limitations. Ask it to mark any unsupported claim with a placeholder. The marketer then decides whether evidence exists or the claim should be removed.",
                ],
            ),
            dict(
                title="Content Pillars and the Customer Journey",
                kind="tiles",
                kicker="TOPIC 02 · EDITORIAL SYSTEM",
                visual=[
                    ("Teach", "Answer a useful question and build problem awareness."),
                    ("Show", "Demonstrate the product, process, or customer experience."),
                    ("Prove", "Use evidence, reviews, comparisons, or behind-the-scenes detail."),
                    ("Invite", "Present an offer and make the next action unmistakable."),
                    ("Engage", "Ask a meaningful question or respond to community signals."),
                    ("Learn", "Use performance and comments to refine the next content cycle."),
                ],
                paragraphs=[
                    "Content pillars are repeatable strategic themes, not arbitrary labels. A local bakery might teach breakfast-planning tips, show how the box is packed, prove freshness with process details, and invite pre-orders. Each pillar has a job in the customer journey and a set of evidence it may use.",
                    "A calendar balances these jobs across time. It also records format, audience, message angle, call to action, owner, status, and learning question. The learning question is what makes the calendar agent-ready: every item declares what the team hopes to discover, not only what it plans to publish.",
                ],
            ),
            dict(
                title="Brand Voice as Observable Rules",
                kind="compare",
                kicker="TOPIC 02 · CONSISTENCY",
                left_title="Weak instruction",
                right_title="Operational rule",
                left=[
                    "Sound friendly and premium",
                    "Make it engaging",
                    "Use our usual tone",
                    "Avoid sounding robotic",
                ],
                right=[
                    "Use warm, direct sentences of 8-18 words",
                    "Open with a specific customer situation",
                    "Use Singapore English naturally; avoid forced slang",
                    "One helpful detail before one invitation",
                ],
                paragraphs=[
                    "Brand adjectives such as friendly, bold, or premium are too abstract on their own. Translate them into observable rules: sentence length, point of view, vocabulary, rhythm, humour boundaries, words to use, words to avoid, and examples that demonstrate the tone. These rules can be evaluated consistently by a person or a checking agent.",
                    "Examples are powerful but should not become a copying target. Give two or three representative examples and explain why they work. Add negative examples that show exaggeration, pressure, unexplained jargon, or tone that does not fit the brand. This creates a usable boundary around creative variation.",
                ],
            ),
            dict(
                title="Facebook Copy Anatomy",
                kind="flow",
                kicker="TOPIC 02 · COPY SYSTEM",
                visual=["Specific hook", "Useful value", "Credible proof", "Offer detail", "Single call to action"],
                paragraphs=[
                    "Facebook copy competes in a fast feed, so the opening must quickly show relevance. Relevance is not the same as sensationalism. A useful hook names a situation, question, or benefit that the intended audience recognises. The body earns attention by delivering value and proof, while the call to action tells the reader exactly what to do next.",
                    "Ad copy and organic copy share the same hierarchy but operate under different delivery conditions. An ad needs a clear match between creative, primary text, headline, destination, and optimisation goal. Organic content can invest more space in conversation and community. The agent should generate variants around one controlled variable, such as hook angle, rather than changing hook, offer, format, and audience all at once.",
                ],
            ),
            dict(
                title="Creative System: Image, Carousel, and Video",
                kind="tiles",
                kicker="TOPIC 02 · CREATIVE CHOICE",
                visual=[
                    ("Single image", "One idea, one focal point, fast recognition, strong offer or proof."),
                    ("Carousel", "A sequence, comparison, product range, or step-by-step story."),
                    ("Short video", "Motion, demonstration, personality, transformation, or process."),
                    ("First frame", "Make the subject and value understandable before sound or context."),
                    ("Mobile clarity", "Large type, high contrast, simple composition, and safe cropping."),
                    ("Rights and truth", "Use authorised assets; review generated details and implied claims."),
                ],
                paragraphs=[
                    "Format should follow the communication job. A single image works when one focal message is enough. A carousel supports sequence, comparison, or multiple proof points. Short video is useful when motion, demonstration, or personality carries meaning. The first frame should communicate subject and relevance even without sound.",
                    "AI image generation accelerates exploration, but it introduces review duties. Check hands, text, packaging, locations, product attributes, cultural details, and any implied endorsement. Keep asset provenance and licence information. Generated creative is a draft until the marketer verifies that it truthfully represents the offer.",
                ],
            ),
            dict(
                title="Content Quality Gate",
                kind="flow",
                kicker="TOPIC 02 · BEFORE APPROVAL",
                visual=["Grounded facts", "Brand fit", "Audience value", "Creative and rights check", "Objective and action match"],
                paragraphs=[
                    "A content quality gate gives reviewers a shared standard. First verify every fact against an approved source. Then check brand voice, audience usefulness, readability, visual truth, asset rights, and the connection between message, offer, destination, and objective. A piece can be attractive and still fail if it asks for the wrong action.",
                    "Record the reason for rejection or revision. These labels become learning data for the next prompt version: unsupported claim, unclear action, off-brand tone, weak proof, visual mismatch, or policy risk. The agent improves when feedback is structured and specific, not when the reviewer simply says 'make it better'.",
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Building and Optimising Ad Campaigns with AI",
        subtitle="campaign hierarchy | audiences | budgets and placements | metrics | experiments | optimisation",
        concepts=[
            ("Campaign level", "The objective and overall campaign decision live here."),
            ("Ad set level", "Audience, placements, budget, schedule, conversion location, and performance goal live here."),
            ("Ad level", "Identity, format, media, text, headline, destination, and tracking live here."),
            ("Signal quality", "Optimisation is only as useful as the event definition and data feeding it."),
            ("Metric tree", "Delivery, attention, action, conversion, and value metrics answer different questions."),
            ("One-variable test", "A controlled comparison changes one main factor and keeps the rest stable."),
            ("Diagnosis before action", "A weak result may come from delivery, creative, audience, offer, destination, or tracking."),
            ("Learning stability", "Frequent major edits destroy comparability and interrupt the platform's learning."),
        ],
        teaching=[
            dict(
                title="Campaign, Ad Set, and Ad Hierarchy",
                kind="flow",
                kicker="TOPIC 03 · ACCOUNT STRUCTURE",
                visual=["Campaign: objective", "Ad set: delivery choices", "Ad: message and creative", "Event: measured action", "Report: decision evidence"],
                paragraphs=[
                    "Meta Ads Manager uses three distinct levels. The campaign holds the objective. An ad set defines the conversion location or performance goal where available, audience, placements, budget, and schedule. The ad contains the business identity, format, media, copy, destination, and related tracking. Naming and reviewing each level separately prevents silent configuration mistakes.",
                    "A campaign blueprint should make the dependency chain visible. If the objective is sales but the ad links to an information page with no purchase event, the creative cannot repair the measurement mismatch. The agent can prepare a draft structure and flag missing inputs, but the authorised advertiser remains responsible for account settings and publication.",
                ],
            ),
            dict(
                title="Objective, Event, and Optimisation Alignment",
                kind="tiles",
                kicker="TOPIC 03 · SIGNAL DESIGN",
                visual=[
                    ("Objective", "The type of result the campaign is designed to pursue."),
                    ("Conversion location", "Where the desired action occurs: website, app, messaging, or another supported surface."),
                    ("Performance goal", "The result the delivery system should seek within the objective."),
                    ("Event", "The observed action that represents progress or value."),
                    ("Data quality", "Accuracy, completeness, timeliness, match quality, and lawful collection."),
                    ("Decision KPI", "The metric and threshold used to continue, change, stop, or scale."),
                ],
                paragraphs=[
                    "The platform needs a measurable signal that matches the business action. A campaign designed for purchases should have a reliable purchase event and a destination where purchases can occur. When the signal is sparse or unreliable, optimise to an earlier meaningful event temporarily and state the limitation rather than pretending the result represents revenue.",
                    "The Meta pixel and Conversions API can send website events into Meta's measurement and optimisation surfaces. They are not a way to bypass privacy controls. Organisations need a valid purpose, appropriate notice or consent where required, secure handling, and a documented data map. Use only data the organisation is authorised to process.",
                ],
            ),
            dict(
                title="Audience Strategy: Prospecting and Re-engagement",
                kind="compare",
                kicker="TOPIC 03 · TARGETING LOGIC",
                left_title="Prospecting",
                right_title="Re-engagement",
                left=[
                    "Reach people who have not yet shown a direct signal",
                    "Use broad delivery or evidence-based suggestions",
                    "Teach the problem and establish relevance",
                    "Exclude recent purchasers when the offer makes that appropriate",
                ],
                right=[
                    "Reach people with an authorised prior interaction",
                    "Use Page, site, video, lead, or customer-list signals where permitted",
                    "Resolve objections and make the next step easy",
                    "Control recency, frequency, exclusions, and data rights",
                ],
                paragraphs=[
                    "Prospecting and re-engagement solve different problems. Prospecting discovers potential demand among people without a direct prior signal. Re-engagement follows up with people who have interacted with the business, subject to the organisation's rights and the platform's available audience options. The message should change with the relationship, not merely repeat the same offer.",
                    "Over-segmentation fragments data and can slow learning. Start with the fewest ad sets needed to express a meaningful strategic difference. Use strict controls for genuine constraints and treat other audience inputs as hypotheses. Consolidate similar ad sets when they pursue the same goal with the same message and evidence.",
                ],
            ),
            dict(
                title="The Facebook Performance Metric Tree",
                kind="tiles",
                kicker="TOPIC 03 · METRICS",
                visual=[
                    ("Delivery", "Impressions, reach, frequency, spend, CPM = spend / impressions × 1,000."),
                    ("Attention", "Link CTR = link clicks / impressions; use one click definition consistently."),
                    ("Traffic cost", "CPC = spend / link clicks; low cost is useful only when visits are relevant."),
                    ("Conversion", "Conversion rate = purchases / link clicks; CPA = spend / purchases."),
                    ("Value", "ROAS = attributed revenue / ad spend; interpret with margin and attribution limits."),
                    ("Quality guards", "Negative feedback rate = negative feedback / impressions × 100, plus operational exceptions."),
                ],
                paragraphs=[
                    "Metrics form a diagnostic tree. Delivery metrics reveal whether the system reached people. Attention metrics show whether the message earned a click. Conversion metrics show whether the destination and offer produced the intended action. Value metrics connect results to economics. A single metric rarely explains a problem by itself.",
                    "Use stable definitions and denominators. Link click-through rate is link clicks divided by impressions, while a broader click metric may include other interactions. Negative feedback rate is negative feedback divided by impressions, multiplied by 100. Cost per purchase becomes unavailable when purchases are zero; label it N/A instead of dividing by zero. Return on ad spend uses attributed revenue, so it should be read alongside margin, attribution settings, and data-quality limits.",
                ],
            ),
            dict(
                title="A/B Testing as Causal Learning",
                kind="flow",
                kicker="TOPIC 03 · EXPERIMENT DESIGN",
                visual=["Question", "One changed variable", "Stable controls", "Decision window and threshold", "Documented learning"],
                paragraphs=[
                    "A useful A/B test answers one decision question. Change one main variable, such as hook angle, while keeping audience, offer, destination, optimisation, and measurement stable. Define the primary metric, minimum decision window, practical threshold, and stop conditions before reviewing the result. Otherwise the team is likely to stop when a favourite variant happens to be ahead.",
                    "Statistical confidence is important, but operational decisions also need practical significance and business context. A small click-through improvement may not matter if conversion rate falls. An agent can calculate and summarise, but it should not declare a winner when volume is too low, the variants changed multiple factors, or tracking is inconsistent.",
                ],
            ),
            dict(
                title="Optimisation Diagnosis Before Change",
                kind="flow",
                kicker="TOPIC 03 · CONTROLLED RESPONSE",
                visual=["Validate data", "Locate funnel break", "Form one hypothesis", "Choose one bounded change", "Observe before the next change"],
                paragraphs=[
                    "Optimisation begins by validating the data: date range, attribution setting, currency, event definition, missing rows, and account changes. Then locate the funnel break. Weak delivery suggests budget, bid, audience, or eligibility issues. Adequate delivery with weak attention points toward message or creative. Strong clicks with weak conversion points toward offer, destination, trust, or tracking.",
                    "Make one bounded change that tests the diagnosis, then allow an appropriate observation window. Large simultaneous edits create a new campaign state and erase the ability to learn what caused the movement. Record the hypothesis, action, approver, timestamp, expected effect, stop rule, and observed result.",
                ],
            ),
        ],
    ),
    dict(
        num=4,
        code="04",
        title="Automating and Scaling Facebook Marketing with AI Agents",
        subtitle="workflow design | scheduling and responses | reporting | bounded optimisation | scaling | privacy and advertising safeguards",
        concepts=[
            ("Automate repetition", "Use rules for stable steps; reserve agent reasoning for contextual choices."),
            ("Draft before action", "Early workflows prepare and recommend while a person approves publication or spend."),
            ("Risk-tier tools", "Reading data is lower risk than publishing, editing budgets, or messaging a customer."),
            ("Stop conditions", "Every loop needs limits for retries, spend, time, confidence, and policy uncertainty."),
            ("Response triage", "Routine questions may use approved answers; complaints, safety, and personal data escalate."),
            ("Evidence-linked reports", "Each insight names the metric, comparison, date window, and supporting row."),
            ("Scale by proof", "Increase exposure only when results, operations, and customer experience remain healthy."),
            ("Reversible actions", "Prefer drafts, small changes, cooldowns, logs, and rollback paths."),
        ],
        teaching=[
            dict(
                title="Should This Task Be Automated?",
                kind="flow",
                kicker="TOPIC 04 · AUTOMATION FIT",
                visual=["Repeatable trigger", "Reliable input", "Clear rule or judgement boundary", "Verifiable output", "Safe failure path"],
                paragraphs=[
                    "A task is a good automation candidate when it has a repeatable trigger, accessible and reliable inputs, a clear decision boundary, an output that can be checked, and a safe way to stop or recover. Scheduling an approved post at a specified time fits well. Inventing a response to a sensitive complaint with no policy or escalation path does not.",
                    "Separate deterministic and agentic work. A rule can calculate a threshold, apply a naming convention, or route a message containing a known keyword. An agent can summarise comments, classify intent, or draft a context-sensitive reply. Combining them produces a safer workflow: rules constrain the space in which reasoning occurs.",
                ],
            ),
            dict(
                title="The Governed Agentic Operating Loop",
                kind="flow",
                kicker="TOPIC 04 · OPERATING MODEL",
                visual=["Observe authorised inputs", "Plan within policy", "Create draft or recommendation", "Validate and approve", "Act, log, and monitor"],
                paragraphs=[
                    "A governed loop starts with authorised inputs, plans within a written policy, creates a draft or recommendation, validates the result, requests approval at the required gate, performs the approved action, logs what happened, and monitors the outcome. The loop ends when the goal is met, evidence is insufficient, a limit is reached, or risk requires escalation.",
                    "Early deployments should keep publication, messaging, targeting, and spend changes behind human approval. As reliability evidence grows, some low-risk reversible actions may be delegated. Autonomy is therefore a property of each action, not a label applied to the whole system.",
                ],
            ),
            dict(
                title="Facebook Operations You Can Coordinate",
                kind="tiles",
                kicker="TOPIC 04 · BUSINESS SUITE",
                visual=[
                    ("Planning", "Turn approved strategy into a dated calendar with owners and dependencies."),
                    ("Scheduling", "Prepare or schedule approved Page posts in Meta Business Suite."),
                    ("Inbox", "Classify messages and comments, then draft from an approved response bank."),
                    ("Automations", "Use greetings, away messages, instant replies, or keywords for bounded routine cases."),
                    ("Insights", "Collect reach, engagement, and post-level evidence for a consistent date window."),
                    ("Reporting", "Summarise movements, causes, limitations, and the next controlled experiment."),
                ],
                paragraphs=[
                    "Meta Business Suite provides operational surfaces for Page posts, Planner, Inbox, automations, and Insights. An agentic workflow can prepare content and recommendations around these surfaces, but account roles and feature availability differ. The workflow should detect missing permissions and fall back to a draft or hand-off rather than attempting to bypass access controls.",
                    "Automated responses are suitable for routine, low-risk information such as an approved collection window or ordering link. They are not a substitute for judgement in complaints, refunds, safety concerns, legal questions, or messages containing personal data. Each response rule needs an owner, active hours, approved wording, review date, and escalation route.",
                ],
            ),
            dict(
                title="Bounded Optimisation Policy",
                kind="tiles",
                kicker="TOPIC 04 · CONTROL LIMITS",
                visual=[
                    ("Eligibility", "Minimum data volume and clean tracking before any recommendation."),
                    ("Allowed action", "Exactly what may change: pause, draft a variant, or propose a budget adjustment."),
                    ("Magnitude", "Maximum percentage or absolute change in one decision cycle."),
                    ("Cooldown", "Minimum observation time before another material change."),
                    ("Stop rule", "Spend, CPA, tracking, negative-feedback, capacity, or policy condition that halts the loop."),
                    ("Approval and log", "Named approver plus before/after values, reason, and rollback instruction."),
                ],
                paragraphs=[
                    "A bounded optimisation policy turns vague autonomy into explicit authority. It states when the system has enough data to act, which actions are allowed, the maximum change size, the cooldown period, the stop conditions, the approval owner, and the evidence that must be logged. Anything outside the policy becomes a recommendation for a person.",
                    "Thresholds should reflect economics and operational capacity, not generic internet advice. A bakery that can fulfil 40 boxes a day should not scale merely because return on ad spend is high. Inventory, service capacity, refund rate, customer sentiment, and cash constraints are part of the optimisation boundary.",
                ],
            ),
            dict(
                title="Scale Through a Learning Ladder",
                kind="flow",
                kicker="TOPIC 04 · SCALING",
                visual=["Validate signal", "Repeat the result", "Stabilise operations", "Increase exposure gradually", "Expand one dimension at a time"],
                paragraphs=[
                    "Scaling begins with trustworthy measurement and a repeatable result. Confirm that performance survives more than one short window and that fulfilment, response quality, inventory, and customer experience remain stable. Increase exposure gradually, observe, and keep a rollback path. A winning creative can fatigue, and a broadening audience can change lead quality.",
                    "Expand one dimension at a time: budget, audience, placement, geography, offer, or creative volume. This preserves learning. Meta's automated budget and audience products can distribute delivery dynamically, but the marketer still defines objective, constraints, exclusions, data rights, and the business limit beyond which more volume is not desirable.",
                ],
            ),
            dict(
                title="Privacy, Advertising, and Incident Safeguards",
                kind="tiles",
                kicker="TOPIC 04 · RESPONSIBLE OPERATION",
                visual=[
                    ("Purpose and consent", "Use personal data only for an appropriate notified purpose with a valid basis."),
                    ("Data minimisation", "Give the agent only the fields needed; use synthetic or aggregated data for practice."),
                    ("Truthful advertising", "Substantiate claims and ensure creative and destination tell the same story."),
                    ("Fair treatment", "Avoid discriminatory assumptions, sensitive inference, manipulation, or exclusion without justification."),
                    ("Access and security", "Use least privilege, approved tools, protected secrets, and retention limits."),
                    ("Incident response", "Pause, preserve logs, contain harm, notify the owner, correct the output, and learn."),
                ],
                paragraphs=[
                    "Singapore's PDPA sets obligations for the collection, use, disclosure, protection, accuracy, retention, and transfer of personal data. Marketing teams should map what data enters an AI or advertising tool, why it is needed, who can access it, how long it is retained, and how a person can exercise applicable rights. Never paste customer identifiers or confidential lists into an unapproved AI tool.",
                    "Advertising safeguards cover claims, creative rights, audience fairness, offer clarity, destination consistency, and platform rules. If an agent produces a risky public output or makes an incorrect action, pause the workflow, preserve the evidence, contain the impact, notify the responsible owner, correct or reverse the action where possible, and update the guardrail that failed.",
                ],
            ),
        ],
    ),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Strategy, prompting, and Facebook content creation",
    2: "Campaign design, performance learning, automation, and scaling",
}

# ------------------------------------------------------------------ schedule
def SCHEDULE(lab_titles):
    return {
        1: (DAY_THEMES[1], [
            ("9:00", "9:20", 20, "admin", "Welcome, outcomes, learning approach, and campaign scenario"),
            ("9:20", "10:10", 50, "topic", "Topic 1 — Facebook marketing system, objectives, and agent anatomy"),
            ("10:10", "10:25", 15, "break", "Tea break"),
            ("10:25", "11:10", 45, "topic", "Topic 1 — audience evidence, prompting, and approval gates"),
            ("11:10", "12:00", 50, "lab", "Hands-on: " + lab_titles([1])),
            ("12:00", "13:00", 60, "lab", "Hands-on: " + lab_titles([2])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "14:50", 50, "topic", "Topic 2 — message hierarchy, content pillars, and brand voice"),
            ("14:50", "15:35", 45, "lab", "Hands-on: " + lab_titles([3])),
            ("15:35", "15:50", 15, "break", "Tea break"),
            ("15:50", "16:25", 35, "topic", "Topic 2 — copy anatomy, creative formats, and quality gates"),
            ("16:25", "17:40", 75, "lab", "Hands-on: " + lab_titles([4])),
            ("17:40", "18:00", 20, "recap", "Day 1 recap, artifact checkpoint, and questions"),
        ]),
        2: (DAY_THEMES[2], [
            ("9:00", "9:15", 15, "recap", "Day 1 retrieval practice and campaign-pack checkpoint"),
            ("9:15", "10:15", 60, "topic", "Topic 3 — campaign hierarchy, objectives, signals, and audiences"),
            ("10:15", "10:30", 15, "break", "Tea break"),
            ("10:30", "11:15", 45, "topic", "Topic 3 — metrics, experiments, and optimisation diagnosis"),
            ("11:15", "12:05", 50, "lab", "Hands-on: " + lab_titles([5])),
            ("12:05", "13:00", 55, "lab", "Hands-on: " + lab_titles([6])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "14:50", 50, "topic", "Topic 4 — governed workflows, scheduling, responses, and reporting"),
            ("14:50", "15:50", 60, "lab", "Hands-on: " + lab_titles([7])),
            ("15:50", "16:05", 15, "break", "Tea break"),
            ("16:05", "16:35", 30, "topic", "Topic 4 — bounded optimisation, scaling, privacy, and advertising safeguards"),
            ("16:35", "17:40", 65, "lab", "Hands-on: " + lab_titles([8])),
            ("17:40", "18:00", 20, "recap", "Course recap, implementation plan, and next steps"),
        ]),
    }

# ------------------------------------------------------------------ optional deck framing
COURSE_OVERVIEW = dict(
    section_title="Agentic Facebook Marketing Fundamentals",
    concepts_title="The Five Decisions Every Workflow Must Preserve",
    concepts=[
        ("Why", "Which business result and customer action matter?"),
        ("Who", "Which evidence-backed audience need are we serving?"),
        ("What", "Which promise, proof, offer, and creative communicate value?"),
        ("Where", "Should the message use organic, paid, or community delivery?"),
        ("Next", "Which metric and rule determine the next controlled action?"),
    ],
    framework_title="The G-C-A-T-E Agent Framework",
    framework=[
        ("Goal", "Business result, customer action, KPI, time horizon, and finish condition."),
        ("Context", "Brand, offer, audience evidence, channel role, and authorised inputs."),
        ("Actions", "Ordered steps and tools the workflow may use."),
        ("Tests", "Factual, brand, privacy, advertising, and performance checks."),
        ("Escalation", "Approval gates, stop conditions, owner, and recovery path."),
    ],
    statement=dict(
        headline="Let AI accelerate the loop; keep people accountable for the outcome.",
        body="Drafting and analysis can move quickly only when goals, evidence, permissions, and approval gates are explicit.",
        kicker="OPERATING PRINCIPLE",
    ),
    pillars_title="The Campaign Operations Pack You Will Build",
    pillars=[
        ("Strategy Pack", ["Success brief", "Audience evidence map", "Prompt contract"]),
        ("Creative Pack", ["Content calendar", "Post set", "Copy and creative matrix"]),
        ("Growth Pack", ["Campaign blueprint", "Performance diagnosis", "Automation and scale policy"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Start from the shared Harbour & Hearth brand brief and the previous lab checkpoint.",
        "Use AI to propose structured work from authorised inputs, not to invent business facts.",
        "Apply a human quality gate and record corrections in the campaign operations pack.",
        "Verify observable evidence before carrying the artifact into the next lab.",
    ],
)

LAB_SHOTS = {}

# ------------------------------------------------------------------ Learner Guide content
LG_INTRO = (
    "This Learner Guide is the self-contained study text for Agentic AI for Facebook Marketing (C526). "
    "It explains the concepts behind Facebook planning, content, advertising, performance learning, and governed automation before guiding you through eight connected labs."
)
LG_INTRO2 = (
    "The course uses the synthetic Harbour & Hearth bakery scenario so every learner can work with the same evidence without exposing customer data or spending live advertising budget. "
    "Save each lab output in one campaign operations folder; the final lab combines the complete set into a launch-ready, human-governed operating pack."
)
LG_SETUP = dict(
    needs=[
        "A Windows or Mac laptop with a modern web browser and spreadsheet application.",
        "Access to an approved generative AI assistant such as ChatGPT, Microsoft Copilot, Claude, or Google Gemini.",
        "The course repository downloaded locally, including labs/resources/.",
        "Optional Facebook Page or Meta Business Suite task access for viewing draft and scheduling surfaces; no live ad spend is required.",
        "A new local folder named C526-campaign-pack for the eight lab artifacts.",
    ],
    verify_text="Open the brand brief and performance dataset, create the campaign-pack folder, and confirm your AI assistant can return a Markdown table without using confidential information.",
    verify_code="Open labs/resources/harbour-hearth-brand-brief.md\nOpen labs/resources/harbour-hearth-facebook-performance.csv\nCreate folder: C526-campaign-pack",
    conventions=[
        "Replace placeholders such as <PASTE BRIEF> with the specified synthetic course material.",
        "Never paste real customer identifiers, account secrets, unpublished results, or confidential creative into an unapproved AI tool.",
        "AI output is a proposal. Check facts, calculations, brand voice, rights, audience fairness, and the intended customer action.",
        "Work in draft mode. Do not publish a post, enable an automation, or activate an ad unless your organisation separately authorises it.",
        "Keep filenames exactly as shown so every later lab can find the earlier checkpoint.",
    ],
)
LAB_NOTE = "Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them."
LAB_TEST_EVIDENCE = "Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory."

LG_WRAPUP = dict(
    title="Wrap-Up — From Course Pack to Operating Practice",
    intro="Your final campaign operations pack connects strategy, content, campaign structure, measurement, and governed automation. Its value comes from the traceable decisions between the files, not from any one AI-generated draft.",
    sections=[
        dict(
            title="Before using the workflow at work",
            bullets=[
                "Replace the synthetic brief with an approved business brief and document every authorised data source.",
                "Validate current Meta interface options, account permissions, objectives, and advertising rules for the intended market.",
                "Set named owners for brand review, privacy review, publishing, customer escalation, and budget approval.",
                "Start with draft-and-recommend mode, measure errors and corrections, then expand authority only where evidence supports it.",
            ],
        ),
        dict(
            title="Evidence to retain",
            bullets=[
                "Input version, prompt version, generated variants, reviewer corrections, and approval decision.",
                "Metric definitions, reporting window, source extract, calculations, and known data limitations.",
                "Before-and-after campaign settings, reason for change, owner, cooldown, result, and rollback action.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Re-run the campaign pack with one real, authorised offer while keeping all actions in draft.",
    "Create a small library of approved brand examples, evidence sources, response templates, and rejection labels.",
    "Review Meta's current official guidance before changing campaign settings or enabling a new automation.",
    "Pilot one low-risk workflow for two weeks, track corrections and exceptions, and revise the prompt contract.",
    "Hold a monthly review of data access, content quality, customer impact, performance thresholds, and rollback readiness.",
]

LG_GLOSSARY = [
    ("Ad", "The creative, text, identity, destination, and related tracking shown to an audience."),
    ("Ad set", "The campaign level where audience, placements, budget, schedule, and performance choices are configured."),
    ("Agent", "A system that uses a model, instructions, and tools to pursue a multi-step goal within guardrails."),
    ("Approval gate", "A required human decision before a high-impact action can proceed."),
    ("Attribution", "The rule used to associate an observed customer action with marketing activity."),
    ("Campaign", "The top advertising level that contains the objective and one or more ad sets."),
    ("Conversion rate", "The share of relevant visits or clicks that complete the defined conversion action."),
    ("CPA", "Cost per acquisition or result: spend divided by the number of defined results."),
    ("CPC", "Cost per click: spend divided by the selected click count."),
    ("CPM", "Cost per one thousand impressions: spend divided by impressions, multiplied by 1,000."),
    ("CTR", "Click-through rate: selected clicks divided by impressions, expressed as a percentage."),
    ("Guardrail", "A rule, check, permission, or technical control that constrains unsafe or unwanted behaviour."),
    ("Impression", "One delivery of content or an ad to a screen; the same person can generate multiple impressions."),
    ("Prompt contract", "Reusable instructions defining goal, inputs, rules, output schema, and escalation behaviour."),
    ("Reach", "The estimated number of distinct people who saw the content or ad."),
    ("ROAS", "Return on ad spend: attributed revenue divided by advertising spend."),
    ("Stop condition", "A defined state that ends or pauses an agentic loop."),
]

NEXT_STEPS = dict(
    title="Put the Workflow into Practice",
    items=[
        "Choose one authorised Facebook offer and rebuild the campaign pack in draft mode.",
        "Measure reviewer corrections and turn repeated failures into clearer rules or examples.",
        "Pilot one low-risk automation with an owner, stop rule, log, and rollback path.",
        "Review performance and customer-impact guardrails before increasing autonomy or spend.",
    ],
)

THANK_YOU = dict(
    body="You can now coordinate Facebook strategy, content, campaigns, performance learning, and automation as one evidence-led, human-governed system.",
    kicker="C526 · KEEP BUILDING, CHECKING, AND LEARNING",
)

VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial aligned release: 4 topics, 8 connected labs, and 2 days / 15 instructional hours.", "Tertiary Infotech Academy Courseware Team"),
]
