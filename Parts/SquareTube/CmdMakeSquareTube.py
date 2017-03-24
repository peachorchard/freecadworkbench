import ntpath

import FreeCADGui

import SquareTube

class CmdMakeSquareTube:
    def Activated(self):
        SquareTube.makeSquareTube()
        
    def GetResources(self):
        return {
            'Pixmap' :  ntpath.dirname(__file__)+'/squaretube.svg', 
            'MenuText': 'Square Tube', 
            'ToolTip': 'Insert a square tube into the active document'
            }

FreeCADGui.addCommand('MakeSquareTube', CmdMakeSquareTube())
