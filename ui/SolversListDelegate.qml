import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.12


ItemDelegate {
    width: parent.width
    text: model.title
    font.pointSize: 10
    contentItem: Text {
        text: parent.text
        color: Material.foreground
        font: parent.font
        wrapMode: Text.Wrap
    }
    highlighted: ListView.isCurrentItem

    onClicked: {
        solversListView.currentIndex = index
        solverDescription.text = model.description
        solverParamsForm.model = model.params
        repeatableParamsForm.model = model.repeatableParams
        resultsForm.model = model.results
        resultsForm.controllerName = model.controller
        solverSection.visible = true
    }

    Rectangle {
        anchors.bottom: parent.bottom
        width: parent.width
        height: 1
        color: Material.foreground
    }
}
