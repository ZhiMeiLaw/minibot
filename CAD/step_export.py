"""
Batch STEP Export
Mini-Atlas V6 Alpha
Opens each FCStd assembly and exports to STEP format.
Usage: freecadcmd CAD/step_export.py
"""
import FreeCAD as App
import Part
import os
import sys

CAD_DIR = os.path.dirname(os.path.abspath(__file__))
FCSTD_DIR = os.path.join(CAD_DIR, "fcstd")
STEP_DIR = os.path.join(CAD_DIR, "step")
os.makedirs(STEP_DIR, exist_ok=True)

fcstd_files = [f for f in os.listdir(FCSTD_DIR) if f.endswith(".fcstd")]

print(f"Found {len(fcstd_files)} FCStd files to export...")

for fname in sorted(fcstd_files):
    fcstd_path = os.path.join(FCSTD_DIR, fname)
    step_name = fname.replace(".fcstd", ".step")
    step_path = os.path.join(STEP_DIR, step_name)

    try:
        doc = App.openDocument(fcstd_path)
        # Find the top-level assembly object (last Part::Feature in doc)
        asm_obj = None
        for obj in doc.Objects:
            if obj.Label not in ("HipRollBase", "HipPitchBase", "KneeBase",
                                  "CalfTube", "WheelAdapter", "Pelvis"):
                if hasattr(obj, "Shape") and obj.Shape.Solids:
                    asm_obj = obj
                    break

        if asm_obj is None:
            # Fallback: export all solid shapes
            shapes = [obj.Shape for obj in doc.Objects
                      if hasattr(obj, "Shape") and obj.Shape.Solids]
            Part.export(shapes, step_path)
        else:
            Part.export([asm_obj.Shape], step_path)

        App.closeDocument(doc.Name)
        print(f"[OK] {step_name}")
    except Exception as e:
        print(f"[FAIL] {fname}: {e}")

print(f"\nSTEP files: {STEP_DIR}")