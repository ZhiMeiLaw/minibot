import os

FREECAD_PATH = r"D:\dev-tools\FreeCAD_1.1.1-Windows-x86_64-py311"
FREECAD_CMD = os.path.join(FREECAD_PATH, "bin", "freecadcmd")

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
STL_DIR = os.path.join(OUTPUT_DIR, "stl")
FCSTD_DIR = os.path.join(OUTPUT_DIR, "fcstd")
DRAWINGS_DIR = os.path.join(OUTPUT_DIR, "drawings")
STEP_DIR = os.path.join(OUTPUT_DIR, "step")

for _dir in [STL_DIR, FCSTD_DIR, DRAWINGS_DIR, STEP_DIR]:
    os.makedirs(_dir, exist_ok=True)