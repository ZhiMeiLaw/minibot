# Mini-Atlas V6 Alpha

# ECO-002 Documentation Consistency Fix

Version: 1.0

Status: APPROVED

Category:

Engineering Change Order (ECO)

Change Number:

ECO-002

Project:

Mini-Atlas V6 Alpha

Title:

Documentation Consistency Fix

Effective Date:

2026-06-27

---

# 1. Purpose

This ECO authorizes a comprehensive consistency fix across all Mini-Atlas V6 Alpha engineering documents.

The purpose of this change is to:

* Fix battery energy calculation error (66Wh -> 33.3Wh)
* Unify wheel motor driver IC (TB6612FNG -> DRV8871)
* Fix firmware OTA framework contradiction (ArduinoOTA -> ESP-IDF)
* Clean up all residual Ankle/STS3215 references after ECO-001
* Unify Fuse specifications across documents
* Sync DOC-INDEX with actual file structure
* Standardize file naming conventions

---

# 2. Background

ECO-001 (Lightweight Lower-Body Architecture Migration) removed the Ankle joint and migrated to the 6-servo architecture. However, several downstream documents were not updated to reflect this change. Additionally, a fundamental battery energy calculation error was discovered that affects all power/runtime analysis.

These inconsistencies pose risks for:
* Procurement (wrong driver IC, wrong fuse rating)
* Firmware development (ArduinoOTA not available in ESP-IDF)
* Runtime estimation (66Wh vs 33.3Wh doubles actual capability)
* Assembly (residual Ankle servo IDs)

---

# 3. Change Summary

## 3.1 Battery Energy Correction

| Parameter | Old Value | New Value |
|-----------|-----------|-----------|
| Pack Capacity | 6000mAh | 3000mAh |
| Pack Energy | 66Wh | 33.3Wh |
| Walking Runtime | 35-40 min | 19-20 min |
| Mixed Runtime | 50-60 min | 28-32 min |

Reason: 3S2P configuration - series connection does not multiply capacity. Samsung 30Q = 3000mAh per cell. 3S2P = 3000mAh @ 11.1V = 33.3Wh.

## 3.2 Wheel Driver IC Unification

All references to TB6612FNG are replaced with DRV8871.

Reason: DRV8871 (3A continuous) is required for GB37-520 wheel motors (1.5A acceleration per motor). TB6612FNG (1.2A continuous) is insufficient.

## 3.3 OTA Framework Consistency

EDS-05 OTA framework changed from ArduinoOTA to ESP-IDF Native OTA (Partition A/B).

Reason: FW-001 explicitly prohibits Arduino framework. ESP-IDF native OTA is the correct approach.

## 3.4 Ankle/STS3215 Cleanup

All residual references to Ankle joint and STS3215 servo are removed from:
* EDS-01: Servo count 8 -> 6, Ankle rows deleted
* EDS-02: Entire STS3215 sections deleted, current calculations updated
* EDS-05: Ankle servo IDs (4, 8) removed, new ID allocation 1-6
* MDS-01: Erroneous "4 DOF x 2 Legs = 8 Servo DOF" line deleted
* CDS-01: "V6-ASM-0004 Ankle Assembly" entry deleted

## 3.5 Fuse Specification Unification

All documents aligned to: ATO 25A Slow Blow x 1

Reason: EDS-03 analysis shows 20A has mis-trip risk at 18.5A peak. 25A Slow Blow is the latest approved specification.

## 3.6 DRV8871 Quantity

EDS-01 BOM Summary corrected from Qty 1 to Qty 2 (one per wheel motor).

## 3.7 DOC-INDEX Synchronization

DOC-INDEX updated to match actual file structure, numbering, and status values.

## 3.8 File Naming Standardization

Files with spaces/special characters renamed to hyphenated convention:
* MDS-03 Assembly Specification.md -> MDS-03-Assembly-Specification.md
* MDS-04 Pelvis & Electronics Assembly Specification.md -> MDS-04-Pelvis-Electronics-Assembly.md
* BOM-02_Engineering_BOM.md -> BOM-02-Engineering-BOM.md
* CDS-07-Full Leg Subsystem Integration.md -> CDS-07-Full-Leg-Subsystem-Integration.md

---

# 4. Affected Documents

| Doc | Change Type | Priority |
|-----|-------------|----------|
| EDS-01 | Battery, Servo count, Ankle cleanup, DRV8871 qty, Duplicate row | P0 |
| EDS-02 | Battery, Ankle sections, Current calculations, Runtime | P0 |
| EDS-03 | TB6612 -> DRV8871 (2 locations) | P0 |
| EDS-04 | Battery capacity/energy | P0 |
| EDS-05 | TB6612 -> DRV8871, ArduinoOTA -> ESP-IDF, Ankle IDs | P0 |
| MDS-01 | 4 DOF line deletion | P0 |
| CDS-01 | Ankle Assembly entry deletion | P0 |
| BOM-01 | Battery, Fuse qty, Pelvis/Wheel additions | P1 |
| PR-001 | Fuse specification | P1 |
| DOC-INDEX | Full synchronization | P2 |

---

# 4b. CAD Optimization (2026-06-27)

| File | Change Type | Priority |
|------|-------------|----------|
| CAD/parts/wheel_hub.py | **NEW** — Independent wheel hub (CDS-06 §7) | P0 |
| CAD/parts/wheel_adapter.py | Updated — 4xM3 bolt pattern (was 6) | P0 |
| CAD/parts/pelvis_main_frame.py | Updated — Added hatch mounting + battery retention | P0 |
| CAD/parts/pelvis_battery_bay.py | **NEW** — Slide-in battery tray (MDS-04 §3) | P0 |
| CAD/parts/pelvis_electronics_deck.py | **NEW** — ESP32/PDB mounting plate (MDS-04 §4-6) | P0 |
| CAD/parts/pelvis_service_hatch.py | **NEW** — Rear removable cover (MDS-04 §14) | P0 |
| CAD/assemblies/leg_asm.py | Updated — Includes wheel hub in assembly | P0 |
| CAD/assemblies/full_body_asm.py | Updated — Includes wheel hub in assembly | P0 |
| CAD/parts/calf_tube.py | Verified — Already correct (hollow tube) | P0 |
| CAD/parts/wheel_adapter.py | Verified — 4xM3 pattern confirmed | P0 |

> **ECO-002 变更**：Pelvis 拆分为 4 个独立零件（Main Frame + Battery Bay + Electronics Deck + Service Hatch），Wheel 拆分为 Adapter + Hub 两个零件。所有零件均可在 Bambu A1 Mini (180³mm) 上单次打印。

---

# 5. Compatibility Statement

Documents modified under this ECO should be treated as the authoritative version for all referenced parameters. Any hardware procurement or firmware development should reference ECO-002 for the corrected values.

---

# 6. Approval

Status:

APPROVED

Change Authority:

Mini-Atlas Documentation Review Board

---

END OF DOCUMENT
