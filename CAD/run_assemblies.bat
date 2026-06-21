@echo off
REM Batch Generate All Assemblies - Mini-Atlas V6 Alpha
set FREECAD=D:\dev-tools\FreeCAD_1.1.1-Windows-x86_64-py311\bin\freecadcmd.exe
cd /d %~dp0..

for %%f in (
    assemblies\hip_roll_asm.py
    assemblies\hip_pitch_asm.py
    assemblies\knee_asm.py
    assemblies\leg_asm.py
    assemblies\full_body_asm.py
) do (
    echo Running: %%f
    "%FREECAD%" "CAD/%%f"
    if errorlevel 1 (
        echo ERROR running %%f
        exit /b 1
    )
)

echo.
echo All assemblies generated successfully.
echo FCStd files: CAD\fcstd\
pause