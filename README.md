# EnergizeOS EMS Knowledge Base (PUBLIC (P1 Redacted))

Org: https://github.com/enxpower
Private repo: energizeos-knowledge-base-private
Public repo: energizeos-knowledge-base-public

## Publishing
- SITE_BASE: https://docs.energizeos.com/ems/
- Publishing mode: P1 (Redacted subset)

## Important

---

# EnergizeOS™ EMS

## Master Index（Public Edition）

**Document Role**
This document defines the **public, authoritative index** of the EnergizeOS™ Energy Management System (EMS).
It establishes **system scope, functional boundaries, and architectural intent**, without exposing implementation details, control logic internals, wiring, or proprietary strategies.

---

## 0. System Positioning & Boundary Declaration

### 0.1 What EnergizeOS™ EMS *Is*

EnergizeOS™ EMS is a **supervisory-level energy management and control system** designed for:

* Commercial & Industrial (C&I) energy systems
* Grid-connected, islanded, and hybrid microgrids
* Multi-source energy coordination (Grid / BESS / PV / DG / Load)

Its core responsibilities are:

* **Decision-making**
* **Coordination**
* **Authorization**
* **Auditability**

---

### 0.2 What EnergizeOS™ EMS *Is NOT*

To avoid ambiguity, EnergizeOS™ EMS **explicitly does NOT**:

* Replace inverter / PCS internal controllers
* Replace certified protection relays (anti-islanding, UV/OV, UF/OF)
* Perform autonomous protection-grade tripping without hardware interlock
* Act as a real-time protection device
* Expose internal control logic, FAT scripts, IO tables, or relay matrices publicly

> EMS is **supervisory intelligence**, not protection hardware.

---

## 1. System Architecture – Public View

### 1.1 Layered Architecture Overview

```
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

This layered separation ensures:

* Deterministic behavior
* Auditable decisions
* Clear responsibility boundaries

---

### 1.2 EMS vs Protection vs Device Control

| Layer          | Responsibility                          | Owner               |
| -------------- | --------------------------------------- | ------------------- |
| Protection     | Trip on unsafe electrical conditions    | Certified Relay     |
| Device Control | Real-time control loops                 | PCS / DG Controller |
| EMS            | Authorization, sequencing, coordination | EnergizeOS™         |

---

## 2. Core Functional Domains (Public Scope)

### 2.1 Grid Interaction & Operating States

* Grid-connected operation
* Islanded operation
* Transition handling (Grid ↔ Island)
* State-aware authorization logic

> EMS **decides *when***, hardware **decides *how fast***.

---

### 2.2 Energy Resource Coordination

* Battery Energy Storage Systems (BESS)
* Photovoltaic (PV) generation
* Diesel / Gas Generators (DG)
* Site loads and critical loads

EMS provides:

* Priority coordination
* Constraint-aware dispatch
* Mode-dependent behavior

---

### 2.3 Strategy-Based Control Framework

EnergizeOS™ EMS executes **explicit, versioned strategy modules**, such as:

* Demand Charge Management (DCM)
* Time-of-Use Optimization (TOU)
* Grid / Island Transition Control
* Renewable Energy Utilization
* Generator Coordination (optional)

> Strategies are **policy-driven**, not hardcoded behaviors.

---

## 3. Control Authority & Safety Philosophy

### 3.1 Control Authority Rules

* **Trip authority**:

  * Primary: Protection relay
  * Secondary: EMS (redundant, supervised)

* **Close authority**:

  * EMS is the **sole authorized source**

Any non-EMS closing path is considered **out of scope**.

---

### 3.2 Safety-by-Design Principles

* Fail-safe over fail-operational
* Hardware-first protection
* Software-gated authorization
* Explicit interlock conditions
* Deterministic state transitions

---

## 4. Deployment & Integration Model (Public)

### 4.1 Typical Deployment Elements

* EMS Control Panel (ECP)
* Anti-Islanding Protection Panel (AIPP)
* Certified Protection Relays
* Meters (utility-grade)
* UPS-backed control power

---

### 4.2 EMS Integration Interfaces

* Discrete IO (DO / DI)
* Industrial communication protocols (e.g., Modbus TCP)
* Event & status feedback loops

> Interface definitions exist, but **are not public artifacts**.

---

## 5. Observability, Audit & Traceability

EnergizeOS™ EMS emphasizes **engineering auditability**:

* State transitions are logged
* Decisions are attributable to conditions
* Strategy execution is traceable
* Operator actions are recorded

This enables:

* FAT / SAT validation
* Post-event analysis
* Regulatory support

---

## 6. Public vs Private Knowledge Boundary

### 6.1 Publicly Available (This Repository)

* System architecture overview
* Functional scope definitions
* Role & responsibility boundaries
* Strategy categories (not implementations)
* Deployment concepts

---

### 6.2 Restricted / Private (Not Public)

* IO point tables
* Relay wiring diagrams
* FAT procedures
* Interlock matrices
* Strategy logic details
* Control scripts & thresholds

> These materials are delivered **only under contract**.

---

## 7. Intended Audience

This Master Index is intended for:

* EPCs & System Integrators
* Owners & Asset Operators
* Utility & Interconnection reviewers
* Technical decision-makers
* Investors & partners (technical due diligence)

---

## 8. Governance & Change Policy (Public)

* This index is **version-controlled**
* Structural changes require formal review
* Terminology changes are treated as breaking changes
* Implementation details will **never** be added here

---

## 9. Canonical Reference

* **System Name**: EnergizeOS™ EMS
* **Official Documentation Base**:
  `https://docs.energizeos.com/ems/`

---

### End of Document

---


继续往前，不回头。
