# P01-S03 - Deliver User and Access Management

- Type: Story
- Phase: 01 - Django Foundation
- Parent: None
- Depends on: P01-T03
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Administrators can govern who may use the application and what each identity may do across Jira connections and projects.

## Work

- Synchronize application identities and group claims from the configured OIDC provider.
- Manage group mappings, time-bounded direct assignments, roles, and connection or project scopes.
- Review effective access, revoke sessions, suspend application access, and certify assignments.

## Success Criteria

- [ ] Tasks P01-T08 through P01-T10 are Done.
- [ ] The application creates no Atlassian account, local production password, or independent identity lifecycle.
- [ ] Every authorization decision derives from current active assignments and scope with deny-by-default behavior.
- [ ] User, group, assignment, session, suspension, and access-review changes are attributable and auditable.

## Evidence

- [ ] OIDC, group mapping, scoped authorization, revocation, access review, audit, accessibility, and responsive evidence.