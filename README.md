# EnergizeOS™ EMS — Master Index (Public Edition)

## Document role

This document is the **public, authoritative index** of the EnergizeOS™ Energy Management System (EMS).  
It defines system scope, functional boundaries, and architectural intent **without** exposing implementation details, internal control logic, wiring, or proprietary strategies.

---

## 0. System positioning and boundary declaration

### 0.1 What EnergizeOS™ EMS is

EnergizeOS™ EMS is a **supervisory-level** energy management and control system designed for:

- Commercial & Industrial (C&I) energy systems
- Grid-connected, islanded, and hybrid microgrids
- Multi-source energy coordination (Grid / BESS / PV / DG / Load)

Core responsibilities:

- Decision-making
- Coordination
- Authorization
- Auditability

### 0.2 What EnergizeOS™ EMS is **not**

To avoid ambiguity, EnergizeOS™ EMS explicitly does **not**:

- Replace inverter / PCS internal controllers
- Replace certified protection relays (anti-islanding, UV/OV, UF/OF)
- Perform autonomous **protection-grade** tripping without hardware interlock
- Act as a real-time protection device
- Expose internal control logic, FAT scripts, I/O tables, or relay matrices publicly

> EMS is supervisory intelligence, **not** protection hardware.

---

## 1. System architecture — public view

### 1.1 Layered architecture overview

```text
┌────────────────────────────────────┐
│ UI / API Layer                     │
│ (Operator, Admin, Integrations)    │
├────────────────────────────────────┤
│ Strategy & Control Logic Layer     │
│ (Policies, Scheduling, Arbitration)│
├────────────────────────────────────┤
│ Core Engine                        │
│ (State Machine, Safety Gating)     │
├────────────────────────────────────┤
│ Data & Interface Layer             │
│ (Meters, Relays, Controllers)      │
└────────────────────────────────────┘
```

This separation ensures:

- Deterministic behavior
- Auditable decisions
- Clear responsibility boundaries

### 1.2 EMS vs protection vs device control

| Layer | Responsibility | Owner |
|---|---|---|
| Protection | Trip on unsafe electrical conditions | Certified relay |
| Device control | Real-time control loops | PCS / DG controller |
| EMS | Authorization, sequencing, coordination | EnergizeOS™ |

---

## 2. Core functional domains (public scope)

### 2.1 Grid interaction and operating states

- Grid-connected operation
- Islanded operation
- Transition handling (Grid ↔ Island)
- State-aware authorization logic

> EMS decides **when**; hardware decides **how fast**.

### 2.2 Energy resource coordination

Managed resources typically include:

- Battery Energy Storage Systems (BESS)
- Photovoltaic (PV) generation
- Diesel / gas generators (DG)
- Site loads and critical loads

EMS provides:

- Priority coordination
- Constraint-aware dispatch
- Mode-dependent behavior

### 2.3 Strategy-based control framework

EnergizeOS™ EMS executes **explicit, versioned strategy modules**, such as:

- Demand Charge Management (DCM)
- Time-of-Use Optimization (TOU)
- Grid / Island Transition Control
- Renewable Energy Utilization
- Generator Coordination (optional)

> Strategies are policy-driven, not hardcoded behaviors.

---

## 3. Control authority and safety philosophy

### 3.1 Control authority rules

**Trip authority**

- Primary: protection relay
- Secondary: EMS (redundant, supervised)

**Close authority**

- EMS is the **sole authorized** source
- Any non-EMS closing path is considered **out of scope**

### 3.2 Safety-by-design principles

- Fail-safe over fail-operational
- Hardware-first protection
- Software-gated authorization
- Explicit interlock conditions
- Deterministic state transitions

---

## 4. Deployment and integration model (public)

### 4.1 Typical deployment elements

- EMS Control Panel (ECP)
- Anti-Islanding Protection Panel (AIPP)
- Certified protection relays
- Utility-grade meters
- UPS-backed control power

### 4.2 EMS integration interfaces

- Discrete I/O (DO / DI)
- Industrial protocols (e.g., Modbus TCP)
- Event & status feedback loops

> Interface definitions exist, but are not public artifacts.

---

## 5. Observability, audit, and traceability

EnergizeOS™ EMS emphasizes engineering auditability:

- State transitions are logged
- Decisions are attributable to conditions
- Strategy execution is traceable
- Operator actions are recorded

This enables:

- FAT / SAT validation
- Post-event analysis
- Regulatory support

---

## 6. Public vs private knowledge boundary

### 6.1 Publicly available (this repository)

- System architecture overview
- Functional scope definitions
- Role & responsibility boundaries
- Strategy categories (not implementations)
- Deployment concepts

### 6.2 Restricted / private (not public)

- I/O point tables
- Relay wiring diagrams
- FAT procedures
- Interlock matrices
- Strategy logic details
- Control scripts & thresholds

> These materials are delivered only under contract.

---

## 7. Intended audience

- EPCs & system integrators
- Owners & asset operators
- Utility & interconnection reviewers
- Technical decision-makers
- Investors & partners (technical due diligence)

---

## 8. Governance and change policy (public)

- This index is version-controlled
- Structural changes require formal review
- Terminology changes are treated as breaking changes
- Implementation details will never be added here

---

## 9. Canonical reference

- System name: **EnergizeOS™ EMS**
- Official documentation base: **https://docs.energizeos.com/ems/**
