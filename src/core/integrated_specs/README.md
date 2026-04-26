# Integrated Canonical Specifications

This directory contains canonical specifications synchronized from Project-AI.
These files are intended to be used natively by this repository's logic.

## Included modules

- `interface_abstractions.py`
  - Canonical base interfaces and payload models (`BaseSubsystem`, `ICommandable`, `IMonitorable`, `IObservable`, `SubsystemCommand`, `SubsystemResponse`).
- `domain_base.py`
  - Shared implementation layer that imports `interface_abstractions.py` and provides reusable domain subsystem behavior.
- `governance.py`
  - Triumvirate governance and law evaluation engine.
- `identity.py`
  - AGI identity model, genesis event, personality matrix, and bonding primitives.
- `meta_identity.py`
  - Self-actualization and meta-identity milestone tracking.
- `canonical_bundle.py`
  - Non-design canonical bundle artifacts for auditability and reproducibility.

**Removability**: This directory and its contents can be safely removed if this repository needs to operate independently of the Project-AI monolith.
