# dispatch-m2s — queries

- `delegation batch outcome lookup`: Given a Hermes batch ID, retrieve dispatched time, fan-out size, role, terminal result, and known transcript path.
- `owner-exit timeout correlation`: List batches with the `Delegation owner exited before recording a terminal result; outcome unknown.` error and whether smaller batch sizes were used afterward.
- `success pattern lookup`: List successful batches observed under smaller fan-outs after an owner-exit failure.
- `message ID reuse audit`: List all raw filings that share the same Hermes message ID and whether their content diverges across days.

