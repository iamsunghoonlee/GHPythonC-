"""Inputs:
        surface : a surface to subdivide
        uDiv: The u(y) direction number of subdivision
        vDiv: The v(x) direction number of subdivision
    Output:
        surfaces: the divided surfaces"""

import Rhino.Geometry as rg

curves = []

domain = rg.Interval(0, 1)
surface.SetDomain(0, domain)
surface.SetDomain(1, domain)

for u in range(uDiv):
    if u == 0 or u/uDiv == 1:
        continue
    else:
        uCurve = surface.IsoCurve(1, u/uDiv)
        curves.append(uCurve)
        
for v in range(vDiv):
    if v == 0 or v/vDiv == 1:
        continue
    else:
        vCurve = surface.IsoCurve(0, v/vDiv)
        curves.append(vCurve)

#Get BrepFace
surfBrep = surface.ToBrep()
brepFace = surfBrep.Faces[0]
splits = brepFace.Split(curves, 0.001)
faces = splits.Faces

surfaces = []

for i in range(faces.Count):
    surfaces.append(faces.ExtractFace(i))
