"""
Batch Generate All Assemblies - Mini-Atlas V6 Alpha
"""
import subprocess
import os
import sys

FREECAD_PATH = r"C:\tools\Dev\FreeCAD_1.1.1-Windows-x86_64-py311\bin\freecadcmd.exe"

if not os.path.exists(FREECAD_CMD := os.path.join(FREECAD_PATH)):
    print(f"[ERROR] FreeCAD not found at: {FREECAD_CMD}")
    print("Please update FREECAD_PATH in this file.")
    sys.exit(1)

assemblies = [
    "assemblies/hip_roll_asm.py",
    "assemblies/hip_pitch_asm.py",
    "assemblies/knee_asm.py",
    "assemblies/leg_asm.py",
    "assemblies/full_body_asm.py",
]

success = 0
fail = 0

for asm in assemblies:
    print(f"Running: {asm}")
    result = subprocess.run([FREECAD_CMD, asm], capture_output=False)
    if result.returncode == 0:
        success += 1
    else:
        print(f"  [FAILED] {asm}")
        fail += 1

print(f"\nDone: {success} succeeded, {fail} failed")
print(f"FCStd files: CAD/fcstd/")
