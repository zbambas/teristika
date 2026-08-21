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
- Bind each active and staged credential record to exactly one Jira connection and show that connection's active provider, reference, identity, version, fingerprint, rotation time, and test state together.

## Success Criteria

- [ ] Existing secret values are never returned; settings show only provider, reference, fingerprint, version, rotation time, and test state.
- [ ] Blank secret input preserves the active secret and staged values expire if not activated.
- [ ] Selecting a different connection displays only that connection's active metadata; staging or discarding a candidate cannot alter another connection.
- [ ] Secret submission requires administrator permission, TLS, CSRF protection, bounded input, and no browser persistence or autocomplete.
- [ ] Create, stage, disable, and reference changes create redacted audit events.

## Evidence

- [ ] Settings view, connection isolation, secret-store adapter, authorization, CSRF, input-boundary, expiry, audit, and seeded-secret scan tests.