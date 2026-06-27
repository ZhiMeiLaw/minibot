"""
Batch Generate All Parts - Mini-Atlas V6 Alpha
"""
import subprocess
import os
import sys

FREECAD_PATH = r"C:\tools\Dev\FreeCAD_1.1.1-Windows-x86_64-py311\bin\freecadcmd.exe"

if not os.path.exists(FREECAD_CMD := os.path.join(FREECAD_PATH)):
    print(f"[ERROR] FreeCAD not found at: {FREECAD_CMD}")
    print("Please update FREECAD_PATH in this file.")
    sys.exit(1)

parts = [
    "parts/pelvis_main_frame.py",
    "parts/pelvis_battery_bay.py",
    "parts/pelvis_electronics_deck.py",
    "parts/pelvis_service_hatch.py",
    "parts/hip_roll_base.py",
    "parts/hip_roll_output.py",
    "parts/hip_roll_torque_module.py",
    "parts/hip_pitch_base.py",
    "parts/hip_pitch_output.py",
    "parts/hip_pitch_torque_module.py",
    "parts/knee_base.py",
    "parts/knee_output.py",
    "parts/knee_torque_module.py",
    "parts/wheel_adapter.py",
    "parts/wheel_hub.py",
    "parts/calf_tube.py",
]

success = 0
fail = 0

for part in parts:
    print(f"Running: {part}")
    result = subprocess.run([FREECAD_CMD, part], capture_output=False)
    if result.returncode == 0:
        success += 1
    else:
        print(f"  [FAILED] {part}")
        fail += 1

print(f"\nDone: {success} succeeded, {fail} failed")
print(f"STL files: CAD/stl/")
