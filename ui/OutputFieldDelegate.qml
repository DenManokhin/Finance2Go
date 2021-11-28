import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.12


ItemDelegate {

    property string handlerName: model.handler
    property alias result: textField.text
    hoverEnabled: false

    Label {
        id: label
        text: model.name + " = "
        font.pointSize: 14
    }

    TextField {
        id: textField
        readOnly: true
        selectByMouse: true
        horizontalAlignment: TextInput.AlignRight
        font.pointSize: 12
        leftPadding: label.width
        width: parent.width
    }
}
