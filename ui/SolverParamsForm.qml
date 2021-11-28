import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.12


Row {
    property alias model: solverView.model
    spacing: 20
    anchors.horizontalCenter: parent.horizontalCenter
    width: 0.75 * parent.width

    Repeater {
        id: solverView
        property int paramsCount: 1

        delegate: InputFieldDelegate {
        }

        onModelChanged: {
            paramsCount = model.count
        }
    }

    function getFormData() {
        let formData = {}
        for (let i = 0; i < children.length; i++) {
            let item = children[i]
            if (item.objectName) {
                formData[item.objectName] = item.objectValue
            }
        }
        return formData
    }
}
