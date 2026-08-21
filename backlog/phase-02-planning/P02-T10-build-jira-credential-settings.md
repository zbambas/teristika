# P02-T10 - Build Jira Credential Settings

- Type: Task
- Phase: 02 - Read-Only Planning
- Parent: P02-S03
- Depends on: P02-T01
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

An administrator can maintain Jira authentication metadata and stage a new secret value securely.

## Work

- Add Settings pages and APIs for Jira site, authentication type, account identity, secret reference metadata, and candidate API token or OAuth secret input.
- Write candidate values directly to the configured external secret store and persist only reference, provider, version, fingerprint, creator, and timestamps.

## Success Criteria

- [ ] Existing secret values are never returned; settings show only provider, reference, fingerprint, version, rotation time, and test state.
- [ ] Blank secret input preserves the active secret and staged values expire if not activated.
- [ ] Secret submission requires administrator permission, TLS, CSRF protection, bounded input, and no browser persistence or autocomplete.
- [ ] Create, stage, disable, and reference changes create redacted audit events.

## Evidence

- [ ] Settings view, secret-store adapter, authorization, CSRF, input-boundary, expiry, audit, and seeded-secret scan tests.