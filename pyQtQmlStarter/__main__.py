import sys
import logging

from PyQt5.QtCore import (QObject, Qt, pyqtProperty, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType, QQmlComponent
from PyQt5.QtWidgets import QApplication

class GuiHandler(QObject):
    """ Container class which will be made available in qml and can be used to
    interact with python 
    """
    def __init__(self):
        QObject.__init__(self)
 
    @pyqtSlot(str)
    def setStringVariable(self, stringVariable):
        """ Slot, callable from qml"""
        logging.debug(stringVariable)

class Application():
    """ Main application class which handles setup
    and start of the qml engine
    """
    def __init__(self, mainqml):
        """mainqml - path to the intitial qml file to be loaded """
        self.app = QGuiApplication(sys.argv)
        self.app.setAttribute(Qt.AA_EnableHighDpiScaling)
        self.engine = QQmlApplicationEngine()
        self._mainqml = mainqml
        self.engine.quit.connect(self.app.quit)
        self.engine.load(self._mainqml)
        
    def setContextProperty(self, name, contextObject):
        """ Adds a new context property object to the qml engine """
        self.engine.rootContext().setContextProperty(name, contextObject)

    def execute(self):
        """ Executes the application"""
        self.app.exec_()

if __name__ == "__main__":
    # run tests and continue only, if all tests pass
    import pytest; 
    if pytest.main() != 0: sys.exit()
    
    # setup logging configuration
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s',)
    
    # initialize gui handler and application
    guiHandler = GuiHandler()
    app = Application("pyQtQmlStarter/qml/main.qml")
    
    # make a python class available to qml
    app.setContextProperty('guiHandler', guiHandler)  
    
    #execute application    
    app.execute()
   
    # cleanup and exit
    sys.exit()
    
