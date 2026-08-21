# P06-T06 - Add Observability and Recovery Controls

- Type: Task
- Phase: 06 - Operations and Release
- Parent: P06-S01
- Depends on: P06-T05
- Pair: Senior Developer + Senior QA
- Status: Backlog

## Outcome

Operators can detect service failures and recover durable state without unsafe replay.

## Work

- Add liveness, readiness, structured logging, metrics, worker heartbeat, and alert thresholds.
- Document and test PostgreSQL restore and pending-job reconciliation.
- Surface overall readiness and worker-heartbeat freshness in the shared application shell, with a route to detailed diagnostics for degraded states.

## Success Criteria

- [ ] Readiness distinguishes PostgreSQL or Redis failure from one unavailable Jira connection.
- [ ] The shell never reports all systems ready when a required web, database, broker, or worker heartbeat check is degraded, and its status is conveyed by text as well as color.
- [ ] Metrics expose queue age, jobs, Jira latency, retries, throttling, and validation totals.
- [ ] A restored database reconciles pending jobs without replaying completed steps.

## Evidence

- [ ] Health, shell-status, heartbeat-freshness, metric, alert, backup, restore, and reconciliation test report.