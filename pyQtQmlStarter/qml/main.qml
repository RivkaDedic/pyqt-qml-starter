import QtQuick 2.7
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.2
import QtQuick.Window 2.2

ApplicationWindow {
    id: appWindow
    visible: true
    width: 1280 //Screen.width
    height: 768 //Screen.height
    title: qsTr("pyqt-qml-starter")
    
    RowLayout {
        Button {
            text: "Ok"
            onClicked: guiHandler.setStringVariable("Ok")
        }
        Button {
            text: "Cancel"
            onClicked: guiHandler.setStringVariable("Cancel")
        }
    }
}