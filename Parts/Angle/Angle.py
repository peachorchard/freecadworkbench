import FreeCAD as App
from FreeCAD import Part
import pivy
from pivy import coin

import ViewProviderAngle

class Angle:
    def __init__(self, obj):
        "Add some custom properties to our feature"
        obj.addProperty("App::PropertyLength","Size","Angle","Outer size of the angle").Size=1.0*25.4
        obj.addProperty("App::PropertyLength","Thickness","Angle","Thickness of the material of the angle").Thickness=1.0/8.0*25.4
        obj.addProperty("App::PropertyLength","Length","Angle", "Length of the angle").Length=12.0*25.4
        obj.addProperty("Part::PropertyPartShape","Shape","Angle", "Shape of the angle")
        obj.Proxy = self

    def execute(self, fp):
        edge1 = Part.makeLine((0,0,0), (fp.Size, 0, 0))
        edge2 = Part.makeLine((fp.Size,0,0), (fp.Size, fp.Thickness, 0))
        edge3 = Part.makeLine((fp.Size,fp.Thickness,0), (fp.Thickness, fp.Thickness, 0))
        edge4 = Part.makeLine((fp.Thickness, fp.Thickness, 0), (fp.Thickness, fp.Size, 0))
        edge5 = Part.makeLine((fp.Thickness, fp.Size, 0), (0, fp.Size, 0))
        edge6 = Part.makeLine((0, fp.Size, 0), (0, 0, 0))
        wire1 = Part.Wire([edge1,edge2,edge3,edge4,edge5,edge6])
        face1 = Part.Face(wire1)

        ext = face1.extrude(App.Base.Vector(0, 0, fp.Length))
        fp.Shape = ext

def makeAngle():
    o = App.ActiveDocument.addObject("Part::FeaturePython", "Angle")
    Angle(o)
    ViewProviderAngle.ViewProviderAngle(o.ViewObject)
    App.ActiveDocument.recompute()
