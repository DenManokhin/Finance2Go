import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.12


Row {
    property alias model: solverParamsRepeater.model
    spacing: 20
    anchors.horizontalCenter: parent.horizontalCenter
    width: parent.width

    Repeater {
        id: solverParamsRepeater
        property int paramsCount: 1

        delegate: InputFieldDelegate {
            width: (parent.width - parent.spacing) / solverParamsRepeater.paramsCount
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
