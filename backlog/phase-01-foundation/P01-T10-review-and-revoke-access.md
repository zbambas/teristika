# P01-T10 - Review and Revoke User Access

- Type: Task
- Phase: 01 - Django Foundation
- Parent: P01-S03
- Depends on: P01-T09
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Administrators can inspect effective access, suspend application use, revoke sessions, and certify assignments.

## Work

- Add user detail, active sessions, last sign-in, identity refresh, group memberships, direct assignments, effective permissions, and recent security activity.
- Add immediate application suspension, session revocation, assignment expiry, periodic access review, reviewer decision, evidence export, and overdue escalation.

## Success Criteria

- [ ] Suspension and session revocation prevent further authenticated requests within the configured revocation bound.
- [ ] Access reviews enumerate every privileged or direct assignment and record certify, modify, or revoke decisions with reviewer and reason.
- [ ] Stale identities, provider-disabled users, expiring exceptions, dormant privileged users, and overdue reviews are visible and filterable.
- [ ] User detail and exports reveal no Jira secret, OIDC token, session token, or unauthorized project metadata.

## Evidence

- [ ] Suspension, session revocation, effective-access, review decision, expiry, stale-user, export-redaction, accessibility, and responsive tests.