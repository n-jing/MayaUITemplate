# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya
import maya.OpenMayaUI as omui
import ssds_ui
from PySide2.QtCore import * 
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
import shiboken2 as shiboken

def maya_useNewAPI(): pass

class ssdsUI(QMainWindow):
    ptr = omui.MQtUtil.mainWindow()
    parent = shiboken.wrapInstance(long(ptr), QWidget)
    titleName = 'SkinDecomp v.'

    def __init__(self, parent = None):
        super(ssdsUI, self).__init__(self.parent)
        self.ui = ssds_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(self.titleName)
        
    def invokeBuild(self):
        nnz = self.ui.nnz.value()
        LaplacianStep = self.ui.laplacianStep.value()
        Iterations = self.ui.iterations.value()
        LaplacianIterNum = self.ui.laplacianIterationNum.value()
        clusterRing = self.ui.clusterRing.value()

        cmds.undoInfo(openChunk = True)
        try:
            cands = build(nnz, LaplacianStep, Iterations, LaplacianIterNum, clusterRing)
        except Exception as e:
            raise e
        finally:
            cmds.undoInfo(closeChunk = True)
            
def showUI(arg):
    ssdsUiWindow = None
    # global ssdsUiWindow
    if ssdsUiWindow == None:
        ssdsUiWindow = ssdsUI()
    ssdsUiWindow.show()

def initializePlugin(plugin):
    fnPlugin = OpenMaya.MFnPlugin(plugin, 'Template', "1.0")
    try:
        createUI()
    except: raise
 
def uninitializePlugin(plugin):
    fnPlugin = OpenMaya.MFnPlugin(plugin)
    try:
        deleteUI()
    except: raise

def createUI():
    cmds.setParent('MayaWindow')
    try:
        cmds.menu('SkinDecomp', query = True, label = True)
    except:
        cmds.menu('SkinDecomp', label = 'SkinDecomp')
    cmds.setParent('SkinDecomp', menu = True)
    cmds.menuItem('SkinDecomp', label = 'SkinDecomp', command = showUI)

def deleteUI():
    try:
        cmds.deleteUI('SkinDecomp', menuItem = True)
    except: pass
    try:
        itemArray = cmds.menu('SkinDecomp', query = True, itemArray = True)
        if itemArray == None:
            cmds.deleteUI('SkinDecomp')
    except: pass
