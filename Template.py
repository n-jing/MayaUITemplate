# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya
import maya.OpenMayaUI as omui
import UI
from PySide2.QtCore import * 
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
import shiboken2 as shiboken

# neccessary api
def maya_useNewAPI(): pass

class TemplateUI(QMainWindow):
    ptr = omui.MQtUtil.mainWindow()
    parent = shiboken.wrapInstance(long(ptr), QWidget)
    titleName = 'Template Title'

    def __init__(self, parent = None):
        super(TemplateUI, self).__init__(self.parent)
        self.ui = UI.Ui_Dialog()
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
            print("***************process****************")
            build(nnz, LaplacianStep, Iterations, LaplacianIterNum, clusterRing)
        except Exception as e:
            raise e
        finally:
            cmds.undoInfo(closeChunk = True)
            
def showUI(arg):
    MainWindow = None
    # global MainWindow
    if MainWindow == None:
        MainWindow = TemplateUI()
    MainWindow.show()

def initializePlugin(plugin):
    fnPlugin = OpenMaya.MFnPlugin(plugin, 'TemplateUI', "1.0")
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
        cmds.menu('MainMenu', query = True, label = True)
    except:
        cmds.menu('MainMenu', label = 'TemplateMain')
    cmds.setParent('MainMenu', menu = True)
    cmds.menuItem('TemplateMenu', label = 'TemplateMenu', command = showUI)

def deleteUI():
    try:
        cmds.deleteUI('MainMenu', menuItem = True)
    except: pass
    try:
        itemArray = cmds.menu('MainMenu', query = True, itemArray = True)
        if itemArray == None:
            cmds.deleteUI('MainMenu')
    except: pass
