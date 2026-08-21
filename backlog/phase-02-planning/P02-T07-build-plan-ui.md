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
- Show direct versus automatic selection, blockers, unsupported items, and operation filters.

## Success Criteria

- [ ] Required dependencies cannot be removed while their dependent remains selected.
- [ ] Plan approval requires an explicit confirmation and approver permission.
- [ ] Keyboard and mobile viewport checks complete the core workflow without overlapping content.

## Evidence

- [ ] Django view tests plus Senior QA desktop, mobile, and keyboard evidence.