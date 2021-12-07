import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.12


ItemDelegate {

    property string objectName: model.name
    property double objectValue: model.defaultValue
    hoverEnabled: false

    Label {
        id: label
        text: model.label + " = "
        font.pointSize: 14
    }

    TextField {
        selectByMouse: true
        horizontalAlignment: TextInput.AlignRight
        text: "" + model.defaultValue
        font.pointSize: 12
        leftPadding: label.width
        width: parent.width

        validator: validators.getValidator(model.validator)

        onTextEdited: {
            objectValue = parseFloat(text)
//            let value = parseFloat(text.replace(",", "."))
//            console.log(value)
//            if (value < validator.bottom) {
//                return
//            }
//            if (value > validator.top) {
//                return
//            }
//            if (isNaN(value))
//                value = 0
//            parent.objectValue = value
        }
    }
}
