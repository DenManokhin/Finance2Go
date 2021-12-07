import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.12


Column {
    property ListModel model
    visible: model && model.count > 0
    width: parent.width

    Row {
        width: parent.width

        Button {
            id: addParamsForm
            text: "Додати період"
            width: parent.width / 2
            onClicked: repeatableParamsList.append()
        }
        Button {
            id: removeParamsForm
            text: "Видалити період"
            width: parent.width / 2
            onClicked: repeatableParamsList.pop()
        }
    }

    Column {
        id: repeatableParamsList
        width: parent.width
        property int count: children.length

        function append() {
            Qt.createQmlObject("SolverParamsForm {model: repeatableParamsForm.model}", repeatableParamsList)
        }

        function pop() {
            if (count !== 0)
                repeatableParamsList.children[count-1].destroy()
        }

        Component.onCompleted: append()
    }

    function getFormData() {
        let forms = []
        for (let i=0; i<repeatableParamsList.count; i++) {
            let form = repeatableParamsList.children[i].getFormData()
            forms.push(form)
        }
        return forms
    }
}
