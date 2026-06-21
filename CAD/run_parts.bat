@echo off
REM Batch Generate All Parts - Mini-Atlas V6 Alpha
set FREECAD=D:\dev-tools\FreeCAD_1.1.1-Windows-x86_64-py311\bin\freecadcmd.exe
cd /d %~dp0..

for %%f in (
    parts\hip_roll_base.py
    parts\hip_roll_output.py
    parts\hip_roll_torque_module.py
    parts\hip_pitch_base.py
    parts\hip_pitch_output.py
    parts\hip_pitch_torque_module.py
    parts\knee_base.py
    parts\knee_output.py
    parts\knee_torque_module.py
    parts\pelvis_main_frame.py
    parts\calf_tube.py
    parts\wheel_adapter.py
) do (
    echo Running: %%f
    "%FREECAD%" "CAD/%%f"
    if errorlevel 1 (
        echo ERROR running %%f
        exit /b 1
    )
)

echo.
echo All parts generated successfully.
echo STL files: CAD\stl\
pause