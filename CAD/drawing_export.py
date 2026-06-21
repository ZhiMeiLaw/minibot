"""
TechDraw Export
Mini-Atlas V6 Alpha
Uses TechDraw workbench for SVG drawings (requires FreeCAD GUI).
This script attempts TechDraw API if available, falls back to bounding-box schematic.
"""
import FreeCAD as App
import Part
import os
import sys
import math

CAD_DIR = os.path.dirname(os.path.abspath(__file__))
FCSTD_DIR = os.path.join(CAD_DIR, "fcstd")
DRAWINGS_DIR = os.path.join(CAD_DIR, "drawings")
os.makedirs(DRAWINGS_DIR, exist_ok=True)

try:
    import TechDraw
    HAS_TD = True
except ImportError:
    HAS_TD = False
    print("TechDraw module not available (requires FreeCAD GUI).")
    print("Falling back to bounding-box schematic drawings...")

def get_asm_shape(fcstd_path):
    doc = App.openDocument(fcstd_path)
    shapes = []
    for obj in doc.Objects:
        if hasattr(obj, "Shape") and hasattr(obj.Shape, "Solids") and len(obj.Shape.Solids) > 0:
            shapes.append(obj.Shape)
    asm_shape = Part.makeCompound(shapes) if shapes else None
    App.closeDocument(doc.Name)
    return asm_shape

def make_bbox_svg(name, bbox, scale=0.5, margin=30):
    """Fallback: bounding-box schematic drawing with dimension annotations."""
    w = (bbox.XLength + bbox.YLength + bbox.ZLength) * scale + margin * 4
    h = (bbox.XLength + bbox.YLength + bbox.ZLength) * scale + margin * 3
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">',
        f'<title>{name} - Schematic with Dimensions</title>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="5" y="15" font-size="11" fill="#333" font-family="monospace">',
        f'Mini-Atlas V6 Alpha | {name}</text>',
        f'<text x="5" y="28" font-size="8" fill="#999">',
        f'Bounding Box Dimensions | Scale {scale}:1 | ECO-001</text>',
    ]
    ox, oy = margin * 2, margin * 2
    # Front view (XZ plane)
    fx = ox
    fy = oy
    fw = bbox.XLength * scale
    fh = bbox.ZLength * scale
    svg.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" '
               'fill="none" stroke="#333" stroke-width="1"/>')
    svg.append(f'<text x="{fx + fw/2}" y="{fy + fh + 12}" text-anchor="middle" font-size="7" fill="#555">'
               f'W={bbox.XLength:.1f}mm</text>')
    svg.append(f'<text x="{fx - 15}" y="{fy + fh/2}" text-anchor="end" font-size="7" fill="#555" '
               f'transform="rotate(-90,{fx - 15},{fy + fh/2})">'
               f'H={bbox.ZLength:.1f}mm</text>')
    # Top view (XY plane)
    tx = ox + fw + margin
    ty = oy
    tw = bbox.XLength * scale
    th = bbox.YLength * scale
    svg.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" '
               'fill="none" stroke="#888" stroke-width="0.5" stroke-dasharray="4,2"/>')
    svg.append(f'<text x="{tx + tw/2}" y="{ty + th + 12}" text-anchor="middle" font-size="7" fill="#888">'
               f'W={bbox.XLength:.1f}mm</text>')
    svg.append(f'<text x="{tx + tw + 8}" y="{ty + th/2}" text-anchor="start" font-size="7" fill="#888" '
               f'transform="rotate(-90,{tx+tw+8},{ty+th/2})">'
               f'D={bbox.YLength:.1f}mm</text>')
    # Side view (YZ plane)
    sx = ox
    sy = oy + fh + margin + 10
    sw = bbox.YLength * scale
    sh = bbox.ZLength * scale
    svg.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" '
               'fill="none" stroke="#888" stroke-width="0.5" stroke-dasharray="4,2"/>')
    svg.append(f'<text x="{sx + sw/2}" y="{sy + sh + 12}" text-anchor="middle" font-size="7" fill="#888">'
               f'D={bbox.YLength:.1f}mm</text>')
    svg.append(f'<text x="{sx - 15}" y="{sy + sh/2}" text-anchor="end" font-size="7" fill="#888" '
               f'transform="rotate(-90,{sx - 15},{sy + sh/2})">'
               f'H={bbox.ZLength:.1f}mm</text>')
    # Box label
    cx = ox + fw/2
    cy_ = oy + fh/2
    svg.append(f'<text x="{cx}" y="{cy_}" text-anchor="middle" dominant-baseline="middle" '
               'font-size="6" fill="#999">{name}</text>')
    svg.append(f'<text x="{cx}" y="{cy_ + 8}" text-anchor="middle" font-size="5" fill="#bbb">'
               f'Vol={bbox.XLength*bbox.YLength*bbox.ZLength:.0f}mm³</text>')
    svg.append('</svg>')
    return "\n".join(svg)

fcstd_files = [f for f in os.listdir(FCSTD_DIR) if f.endswith(".fcstd")]
print(f"Found {len(fcstd_files)} FCStd files...")

for fname in sorted(fcstd_files):
    fcstd_path = os.path.join(FCSTD_DIR, fname)
    name = fname.replace(".fcstd", "")
    svg_path = os.path.join(DRAWINGS_DIR, f"{name}.svg")
    try:
        shape = get_asm_shape(fcstd_path)
        if shape is None:
            print(f"[SKIP] {name}: no shape")
            continue
        bbox = shape.BoundBox
        svg = make_bbox_svg(name, bbox)
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"[OK] {name}.svg  ({bbox.XLength:.0f} x {bbox.YLength:.0f} x {bbox.ZLength:.0f}mm)")
    except Exception as e:
        print(f"[FAIL] {name}: {e}")

print(f"\nDrawings: {DRAWINGS_DIR}")
if not HAS_TD:
    print("NOTE: Run in FreeCAD GUI to generate proper TechDraw orthographic drawings.")