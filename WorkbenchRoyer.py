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

import FreeCADGui as Gui
import FreeCAD as App
from FreeCADGui import Workbench

class WorkbenchRoyer (Workbench):
    MenuText = "Royer"
    ToolTip = "A description of the Royer workbench"
    #Icon = """paste here the contents of a 16x16 xpm icon"""
    Icon = """
            /* XPM */
            static char * R_xpm[] = {
            "16 16 32 1",
            " 	c None",
            ".	c #FFFFFF",
            "+	c #000000",
            "@	c #0B0B0B",
            "#	c #373737",
            "$	c #A6A6A6",
            "%	c #A2A2A2",
            "&	c #E6E6E6",
            "*	c #5D5D5D",
            "=	c #2F2F2F",
            "-	c #EAEAEA",
            ";	c #070707",
            ">	c #131313",
            ",	c #E7E7E7",
            "'	c #5A5A5A",
            ")	c #393939",
            "!	c #E9E9E9",
            "~	c #0C0C0C",
            "{	c #B5B5B5",
            "]	c #F8F8F8",
            "^	c #060606",
            "/	c #CDCDCD",
            "(	c #8A8A8A",
            "_	c #FEFEFE",
            ":	c #FAFAFA",
            "<	c #292929",
            "[	c #989898",
            "}	c #BBBBBB",
            "|	c #0F0F0F",
            "1	c #E5E5E5",
            "2	c #535353",
            "3	c #515151",
            "................",
            "................",
            "...++++@#$......",
            "...+++++++%.....",
            "...++..&*+=.....",
            "...++...-+;.....",
            "...++...-+>.....",
            "...++..,*+'.....",
            "...++++++)!.....",
            "...+++++~{......",
            "...++.]$;^/.....",
            "...++...(+#_....",
            "...++...:<+[....",
            "...++....}+|1...",
            "...++.....2+3...",
            "................"};
        """
    def Initialize(self):
        "This function is executed when FreeCAD starts"
        #import MyModuleA, MyModuleB # import here all the needed files that create your FreeCAD commands
        #self.list = ["MyCommand1, MyCommand2"] # A list of command names created in the line above
        import Parts.SquareTube.CmdMakeSquareTube
        import Parts.Angle.CmdMakeAngle
        self.list = ["MakeSquareTube", "MakeAngle"]
        self.appendToolbar("Royer Commands",self.list) # creates a new toolbar with your commands
        self.appendMenu("Royer",self.list) # creates a new menu
        self.appendMenu(["Royer","My submenu"],self.list) # appends a submenu to an existing menu

    def Activated(self):
        "This function is executed when the workbench is activated"
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return

    def ContextMenu(self, recipient):
        "This is executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("Royer commands",self.list) # add commands to the context menu

    def GetClassName(self): 
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"
       
