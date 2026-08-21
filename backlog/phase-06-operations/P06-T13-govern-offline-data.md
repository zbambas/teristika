# P06-T13 - Govern Offline Data Lifecycle

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S03
- Depends on: P06-T12
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Offline Jira data follows explicit encryption, access, retention, purge, backup, and recovery policies.

## Work

- Encrypt structured and attachment data at rest, reuse live connection and project authorization, and record repository access and administrative actions.
- Add per-connection retention, attachment policy, scheduled sync, storage quota, purge, reindex, backup, restore, and legal-hold controls.

## Success Criteria

- [ ] Revoked connection or project access removes browse and search access immediately without waiting for the next sync.
- [ ] Purge removes structured records, indexes, attachment objects, and encryption-key references and is auditable and non-recoverable outside approved backup policy.
- [ ] Backup and restore preserve manifest integrity, permissions, encryption, search consistency, and snapshot completeness.
- [ ] Storage quota and retention failures stop safely without deleting the last complete permitted snapshot.

## Evidence

- [ ] Encryption, authorization revocation, retention, legal hold, purge, quota, reindex, backup, restore, audit, and recovery tests.