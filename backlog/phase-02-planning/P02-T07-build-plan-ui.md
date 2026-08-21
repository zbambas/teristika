# P02-T07 - Build Selection and Plan Review UI

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S01
- Depends on: P02-T06
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An operator can select resources and review all plan decisions in Django pages.

## Work

- Build Django template and HTMX pages for parameters, resource selection, dependency expansion, and plan review.
- Show direct versus automatic selection with dependency reasons, current versus desired values, blockers, conflicts, unsupported items, shared impact, and operation filters.

## Success Criteria

- [ ] Required dependencies cannot be removed while their dependent remains selected.
- [ ] Plan approval requires an explicit confirmation and approver permission.
- [ ] The route, page heading, target fields, plan summary, and approval payload always identify the same connection and project.
- [ ] Changing target, blueprint, parameter, or resource selection marks the plan stale and disables approval and execution until a new plan is generated.
- [ ] Blockers or unresolved conflicts disable approval; unsupported exclusions and affected shared-resource projects remain visible.
- [ ] Approval confirmation identifies plan ID, target, blueprint version, checksum, operation totals, shared impact, and unsupported exclusions.
- [ ] Keyboard and mobile viewport checks complete the core workflow without overlapping content.

## Evidence

- [ ] Django view tests plus Senior QA desktop, mobile, and keyboard evidence.