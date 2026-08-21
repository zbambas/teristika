# P01-T08 - Synchronize OIDC Identities

- Type: Task
- Phase: 01 - Django Foundation
- Parent: P01-S03
- Depends on: P01-T03
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Application users and group memberships reflect trusted OIDC identities without creating local production credentials.

## Work

- Upsert immutable provider subject, issuer, display metadata, group claims, last identity refresh, last sign-in, and provider status at authentication and approved directory synchronization.
- Add session lifetime, provider-disabled, group-removal, duplicate-email, changed-email, and identity-linking behavior based on issuer plus subject rather than email.

## Success Criteria

- [ ] Issuer and subject uniquely identify a user; email changes do not create a second identity.
- [ ] Untrusted issuers, missing required claims, disabled users, and ambiguous identity links are denied and audited.
- [ ] Group removal changes effective access at the next trusted refresh and revoked or suspended users cannot create a new session.
- [ ] Production authentication stores no local password and never creates or edits an Atlassian account.

## Evidence

- [ ] OIDC claim, issuer, subject, group refresh, disable, email change, session, linking, and audit tests.