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
        text: "" + objectValue
        font.pointSize: 12
        leftPadding: label.width
        width: parent.width

        validator: validators.getValidator(model.validator)

        onTextEdited: {
            let value = parseFloat(text.replace(",", "."))
            if (value < validator.bottom)
                value = validator.bottom
            if (value > validator.top)
                value = validator.top
            if (isNaN(value))
                value = 0
            text = "" + value
            parent.objectValue = value
        }
    }
}
