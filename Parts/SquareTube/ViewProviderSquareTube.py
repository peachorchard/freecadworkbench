import FreeCAD, FreeCADGui, Part
import pivy
from pivy import coin
import SquareTube

class ViewProviderSquareTube:
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
            static char * squaretube_xpm[] = {
            "16 16 39 1",
            " 	c None",
            ".	c #454545",
            "+	c #6F6F6F",
            "@	c #5A5A5A",
            "#	c #626262",
            "$	c #5F5F5F",
            "%	c #8D8D8D",
            "&	c #8E8E8E",
            "*	c #5D5D5D",
            "=	c #7F7F7F",
            "-	c #525252",
            ";	c #565656",
            ">	c #8A8A8A",
            ",	c #5E5E5E",
            "'	c #6D6D6D",
            ")	c #464646",
            "!	c #7D7D7D",
            "~	c #7B7B7B",
            "{	c #4A4A4A",
            "]	c #888888",
            "^	c #868686",
            "/	c #606060",
            "(	c #8C8C8C",
            "_	c #5B5B5B",
            ":	c #8B8B8B",
            "<	c #616161",
            "[	c #515151",
            "}	c #4C4C4C",
            "|	c #414141",
            "1	c #828282",
            "2	c #636363",
            "3	c #848484",
            "4	c #797979",
            "5	c #434343",
            "6	c #717171",
            "7	c #858585",
            "8	c #575757",
            "9	c #676767",
            "0	c #2A2A2A",
            "                ",
            "      .+@#      ",
            "     $%&*&=-    ",
            "   ;>&&&,&&&'   ",
            "  )!&&&&$&&&~{  ",
            "  ]#-^&&/&(;#&  ",
            "  ]&&_;:<;[>&&  ",
            "  ]&&&]}|1&&&&  ",
            "  ]&&&&&2&&&&&  ",
            "  ]&&&&&2&&&&&  ",
            "  ]&&&&&2&&&&&  ",
            "  3&&&&&2&&&&&  ",
            "   2%&&&2&&&4}  ",
            "    56&&2&78    ",
            "      -1#9      ",
            "        0       "};
        """

    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None 
