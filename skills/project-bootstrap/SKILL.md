---
name: project-bootstrap
description: Inspect a new project request and select the minimum relevant capabilities from this skills repository. Use when starting a project, choosing reusable skills, or preparing project-specific agent instructions without loading the entire library.
---

# Project Bootstrap

1. Inspect the request, repository, deliverables, technologies, constraints, and existing instructions.
2. Read `references/skill-selection-rules.md`.
3. Discover candidate skills from their frontmatter `name` and `description`.
4. Select the smallest set covering the work.
5. Read each selected `SKILL.md`; load its references only when required.
6. Explain the selection and identify any missing capability instead of treating adjacent skills as substitutes.
