# C526 — Agentic AI for Facebook Marketing

Single-source courseware for the Tertiary Infotech Academy two-day commercial short course.

## Package

- Trainer slide deck and learner-slide PDF
- Learner Guide in Markdown, DOCX, and PDF
- Lesson Plan in DOCX and PDF
- Eight connected hands-on labs with synthetic resources

All learner-facing artifacts are generated from the same `course_data.py` and `data_domainN.py` modules in `.agents/skills/non-wsq-courseware-build/build/` so the course identity, topic order, outcomes, schedule, and lab sequence stay aligned.

## Build

From Git Bash on Windows:

```bash
COURSE_REPO="$(pwd)" bash ".agents/skills/non-wsq-courseware-build/build/build_courseware.sh"
```

The build writes current artifacts to `courseware/`, the Markdown Learner Guide to the repository root, and lab files to `labs/`.

## Course outline

1. Getting Started with Agentic AI for Facebook Marketing
2. Content Creation and Ad Copy with AI
3. Building and Optimising Ad Campaigns with AI
4. Automating and Scaling Facebook Marketing with AI Agents

Course code: C526 · Version v1.0
