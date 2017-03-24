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
