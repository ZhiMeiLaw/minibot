"""
Batch regenerate all STLs using tessellation (fixes FreeCAD 1.1.1 MeshPart bug).
Run: freecadcmd CAD/run_all_stl.py
"""
import subprocess
import os

FREECAD_CMD = r"C:\tools\Dev\FreeCAD_1.1.1-Windows-x86_64-py311\bin\freecadcmd.exe"
CAD_DIR = os.path.dirname(os.path.abspath(__file__))
PARTS = [
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

for part in PARTS:
    full_path = os.path.join(CAD_DIR, part)
    print(f"Running: {part}")
    result = subprocess.run([FREECAD_CMD, full_path], capture_output=False)
    if result.returncode == 0:
        success += 1
    else:
        print(f"  [FAILED] {part}")
        fail += 1

print(f"\nDone: {success} succeeded, {fail} failed")
print(f"STL files: CAD/stl/")
