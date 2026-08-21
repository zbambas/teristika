# P01-T05 - Build Application Shell

- Type: Task
- Phase: 01 - Django Foundation
- Parent: P01-S02
- Depends on: P01-S01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Authenticated pages share responsive navigation, target context, and user controls.

## Work

- Build the Django base template with primary navigation, page header, target connection context, user menu, and mobile navigation.
- Derive active navigation and visibility from named URLs and application permissions.
- Group top-level destinations as Portfolio, Operate, and Govern; expose Jira connections, users and access, credentials, and offline repository policy as named Settings sections rather than separate top-level administration destinations.

## Success Criteria

- [ ] Every MVP area has one named navigation destination and one visible active state.
- [ ] Unauthorized destinations are absent and direct access remains server-authorized.
- [ ] Keyboard, narrow mobile, and wide desktop navigation work without clipping or overlap.
- [ ] The closed mobile drawer is not keyboard-focusable; the open drawer contains focus until Escape, selection, or dismissal closes it and restores focus to the menu control.
- [ ] Browser refresh, back, and forward preserve the named destination and selected project or Settings section; baseline links and forms remain usable without HTMX enhancement.

## Evidence

- [ ] Template, navigation, permission, keyboard, and responsive tests plus QA screenshots.