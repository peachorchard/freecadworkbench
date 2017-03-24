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

import FreeCAD, FreeCADGui, Part
import pivy
from pivy import coin
import Angle

class ViewProviderAngle:
    def __init__(self, obj):
        '''Set this object to the proxy object of the actual view provider'''
        #obj.addProperty("App::PropertyColor","Color","octahedron.Octahedron","Color of the octahedron").Color=(1.0,0.0,0.0)
        obj.Proxy = self

    def attach(self, obj):
        '''Setup the scene sub-graph of the view provider, this method is mandatory'''
        self.shaded = coin.SoGroup()
        self.wireframe = coin.SoGroup()
        self.scale = coin.SoScale()
        self.color = coin.SoBaseColor()

        self.data=coin.SoCoordinate3()
        self.face=coin.SoIndexedLineSet()

        self.shaded.addChild(self.scale)
        self.shaded.addChild(self.color)
        self.shaded.addChild(self.data)
        self.shaded.addChild(self.face)
        obj.addDisplayMode(self.shaded,"Shaded");
        style=coin.SoDrawStyle()
        style.style = coin.SoDrawStyle.LINES
        self.wireframe.addChild(style)
        self.wireframe.addChild(self.scale)
        self.wireframe.addChild(self.color)
        self.wireframe.addChild(self.data)
        self.wireframe.addChild(self.face)
        obj.addDisplayMode(self.wireframe,"Wireframe");
        self.onChanged(obj,"Color")

    def updateData(self, fp, prop):
        '''If a property of the handled feature has changed we have the chance to handle this here'''
        # fp is the handled feature, prop is the name of the property that has changed

    def getDisplayModes(self,obj):
        "Return a list of display modes."
        modes=[]
        modes.append("Shaded")
        modes.append("Flat Lines")
        modes.append("Wireframe")
        return modes

    def getDefaultDisplayMode(self):
        "Return the name of the default display mode. It must be defined in getDisplayModes."
        return "Flat Lines"

    def setDisplayMode(self,mode):
        return mode

    def onChanged(self, vp, prop):
        "Here we can do something when a single property got changed"
        #FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
        #if prop == "Color":
        #    c = vp.getPropertyByName("Color")
        #    self.color.rgb.setValue(c[0],c[1],c[2])

    def getIcon(self):
        return """
            /* XPM */
            static char * angle_xpm[] = {
            "16 16 22 1",
            " 	c None",
            ".	c #454545",
            "+	c #6F6F6F",
            "@	c #5F5F5F",
            "#	c #8D8D8D",
            "$	c #8E8E8E",
            "%	c #565656",
            "&	c #8A8A8A",
            "*	c #464646",
            "=	c #7D7D7D",
            "-	c #888888",
            ";	c #626262",
            ">	c #525252",
            ",	c #868686",
            "'	c #5B5B5B",
            ")	c #8B8B8B",
            "!	c #4C4C4C",
            "~	c #848484",
            "{	c #636363",
            "]	c #434343",
            "^	c #717171",
            "/	c #828282",
            "                ",
            "      .+        ",
            "     @#$        ",
            "   %&$$$        ",
            "  *=$$$$        ",
            "  -;>,$$        ",
            "  -$$'%)        ",
            "  -$$$-!        ",
            "  -$$$$$        ",
            "  -$$$$$        ",
            "  -$$$$$        ",
            "  ~$$$$$        ",
            "   {#$$$        ",
            "    ]^$$        ",
            "      >/        ",
            "                "};
        """

    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None 
