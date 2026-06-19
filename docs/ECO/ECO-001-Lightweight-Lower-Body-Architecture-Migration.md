# ECO-001-Lightweight-Lower-Body-Architecture-Migration.md

Version: 1.0

Status: APPROVED

Category:

Engineering Change Order (ECO)

Change Number:

ECO-001

Project:

Mini-Atlas V6 Alpha

Title:

Lightweight Lower Body Architecture Migration

Effective Date:

Alpha Architecture Freeze

---

# 1. Purpose

This ECO authorizes the migration from the original heavy-duty lower-body architecture to the lightweight Alpha architecture.

The purpose of this change is to:

* Reduce structural mass
* Improve manufacturability
* Reduce component cost
* Improve serviceability
* Enable production on Bambu A1 Mini
* Align all lower-body modules to a common Ø8 mechanical interface

---

# 2. Background

The original architecture was derived from larger humanoid concepts.

Several early documents adopted oversized mechanical components:

* 6803 bearings
* 6802 bearings
* Ø17 mm output shafts
* larger bearing carriers

During detailed design reviews, it was determined that these components exceeded the actual load requirements of Mini-Atlas V6 Alpha.

---

# 3. Change Summary

## Previous Architecture

Hip Roll:

6803 Bearing

Dimensions:

17 × 26 × 5 mm

Output Shaft:

Ø17 mm

---

Hip Pitch:

6802 Bearing

Dimensions:

15 × 24 × 5 mm

Output Shaft:

Ø15 mm+

---

Result:

* excessive mass
* excessive package volume
* difficult integration
* unnecessary strength margin

---

## New Architecture

Hip Roll:

688 Bearing

Dimensions:

8 × 16 × 5 mm

Output Shaft:

Ø8 mm

---

Hip Pitch:

698 Bearing

Dimensions:

8 × 19 × 6 mm

Output Shaft:

Ø8 mm

---

Result:

* reduced weight
* reduced envelope
* simplified manufacturing
* common shaft standard

---

# 4. Mechanical Interface Migration

## Shaft Standard

Previous:

Mixed shaft diameters

* Ø15
* Ø17

---

New Standard:

Ø8 mm

Status:

Frozen

---

## Carbon Tube Standard

Previous:

Multiple candidate sizes

---

New Standard:

OD10 × ID8 Carbon Tube

Status:

Frozen

---

# 5. Bearing Rationalization

## Approved Bearings

688

8 × 16 × 5 mm

Applications:

* Hip Roll
* Knee

---

698

8 × 19 × 6 mm

Applications:

* Hip Pitch

---

## Deprecated Bearings

6803

Status:

Deprecated

---

6802

Status:

Deprecated

---

MR128-only architecture

Status:

Deprecated

---

# 6. Structural Impact

## Benefits

Mass Reduction:

Estimated 25–40%

---

Package Volume Reduction:

Estimated 20–30%

---

Bearing Carrier Size:

Reduced

---

Assembly Complexity:

Reduced

---

Serviceability:

Improved

---

# 7. Manufacturing Impact

Target Printer:

Bambu A1 Mini

Build Volume:

180 × 180 × 180 mm

The new architecture enables all lower-body components to fit within printer constraints without segmentation.

---

# 8. BOM Impact

Affected Documents:

* BOM-00
* BOM-01
* BOM-02
* BOM-03

Required Action:

Replace:

* 6803
* 6802

With:

* 688
* 698

---

# 9. Documentation Impact

Affected Documents:

* MDS-03
* DR-004
* DR-005
* DR-006

---

Superseding Documents:

* CDS-03A

* CDS-03B

* CDS-03C

* CDS-03D

* CDS-04A

* CDS-04B

* CDS-04C

* CDS-04D

* CDS-05A

* CDS-05B

* CDS-05C

* CDS-05D

These CDS documents become the authoritative implementation reference.

---

# 10. Compatibility Statement

Parts designed under the old architecture:

* are not guaranteed compatible
* may require redesign
* shall not be used for new manufacturing releases

---

# 11. Approval

Status:

APPROVED

Change Authority:

Mini-Atlas Mechanical Architecture Board

---

# 12. Release Effect

This ECO becomes the mandatory migration reference for:

* CDS Documents
* BOM Documents
* Manufacturing Packages
* Future ECOs

---

END OF DOCUMENT
