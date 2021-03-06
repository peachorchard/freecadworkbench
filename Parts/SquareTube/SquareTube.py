#    (c) Copyright 2017 Dale Royer.  All rights reserved.
#
#    This file is part of RoyerWorkbench.
#
#    RoyerWorkbench is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoyerWorkbench is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with RoyerWorkbench.  If not, see <http://www.gnu.org/licenses/>.

import FreeCAD as App
import Part
import pivy
from pivy import coin

import ViewProviderSquareTube

class SquareTube:
    def __init__(self, obj):
        "Add some custom properties to our feature"
        obj.addProperty("App::PropertyLength","Size","SquareTube","Outer size of the square tube").Size=1.0*25.4
        obj.addProperty("App::PropertyLength","Thickness","SquareTube","Thickness of the material of the square tube").Thickness=1.0/16.0*25.4
        obj.addProperty("App::PropertyLength","Length","SquareTube", "Length of the square tube").Length=12.0*25.4
        obj.addProperty("Part::PropertyPartShape","Shape","SquareTube", "Shape of the square tube")
        obj.Proxy = self

    def execute(self, fp):
        edge1 = Part.makeLine((0,0,0), (fp.Size, 0, 0))
        edge2 = Part.makeLine((fp.Size,0,0), (fp.Size, fp.Size, 0))
        edge3 = Part.makeLine((fp.Size,fp.Size,0), (0, fp.Size, 0))
        edge4 = Part.makeLine((0, fp.Size, 0), (0, 0, 0))
        wire1 = Part.Wire([edge1,edge2,edge3,edge4])
        face1 = Part.Face(wire1)

        edge5 = Part.makeLine((fp.Thickness,fp.Thickness, 0), (fp.Size-fp.Thickness, fp.Thickness, 0))
        edge6 = Part.makeLine((fp.Size-fp.Thickness,fp.Thickness,0), (fp.Size-fp.Thickness, fp.Size-fp.Thickness, 0))
        edge7 = Part.makeLine((fp.Size-fp.Thickness,fp.Size-fp.Thickness,0), (fp.Thickness, fp.Size-fp.Thickness, 0))
        edge8 = Part.makeLine((fp.Thickness, fp.Size-fp.Thickness, 0), (fp.Thickness, fp.Thickness, 0))
        wire2 = Part.Wire([edge5,edge6,edge7,edge8])
        face2 = Part.Face(wire2)

        diff = face1.cut(face2)
        ext = diff.extrude(App.Base.Vector(0, 0, fp.Length))
        fp.Shape = ext

def makeSquareTube():
    o = App.ActiveDocument.addObject("Part::FeaturePython", "SquareTube")
    SquareTube(o)
    ViewProviderSquareTube.ViewProviderSquareTube(o.ViewObject)
    App.ActiveDocument.recompute()
