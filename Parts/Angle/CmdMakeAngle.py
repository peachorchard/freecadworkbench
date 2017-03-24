import ntpath

import FreeCADGui

import Angle

class CmdMakeAngle:
    def Activated(self):
        Angle.makeAngle()
        
    def GetResources(self):
        return {
            'Pixmap' :  ntpath.dirname(__file__)+'/angle.svg', 
            'MenuText': 'Angle', 
            'ToolTip': 'Insert an angle into the active document'
            }

FreeCADGui.addCommand('MakeAngle', CmdMakeAngle())
