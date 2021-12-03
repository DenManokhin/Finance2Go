import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.12


ApplicationWindow {
    id: window
    visible: true
    width: 640
    height: 480
    minimumWidth: 300
    minimumHeight: 300
    title: "Finance2Go"
    readonly property int responsiveWidth: 500
    property QtObject backend

    Material.theme: Material.Light

    Validators {
        id: validators
    }

    SplitView {
        id: splitView
        anchors.fill: parent

        Item {
            height: parent.height
            SplitView.minimumWidth: parent.width / 3

            ListView {
                id: solversListView

                focus: true
                currentIndex: -1
                anchors.fill: parent

                delegate: SolversListDelegate {
                }

                model: SolversModel {
                    id: solversModel
                }

                section.property: "group"
                section.criteria: ViewSection.FullString 
                section.delegate: ToolBar {
                    id: background
                    width: solversListView.width

                    Label {
                        id: label
                        text: section
                        font.pointSize: 10
                        anchors.fill: parent
                        horizontalAlignment: Qt.AlignHCenter
                        verticalAlignment: Qt.AlignVCenter
                        wrapMode: Text.Wrap
                    }
                }

                ScrollIndicator.vertical: ScrollIndicator { }
            }
        }

        Item {
            height: parent.height
            SplitView.minimumWidth: parent.width / 3

            Column {
                id: solverSection
                width: parent.width
                visible: false

                Text {
                    id: solverDescription
                    font.pointSize: 12
                    width: parent.width
                    horizontalAlignment: Text.AlignJustify
                    wrapMode: Text.Wrap
                    padding: 10
                    textFormat: Text.MarkdownText
                }

                SolverParamsForm {
                    id: solverParamsForm
                }

                Column {
                    id: repeatableParamsForm
                    property ListModel model
                    visible: model && model.count > 0
                    width: 0.75 * parent.width
                    anchors.horizontalCenter: parent.horizontalCenter

                    onModelChanged: repeatableParamsList.append()

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
                    }
                }

                Row {
                    id: resultsForm
                    padding: 10
                    spacing: 20
                    anchors.horizontalCenter: parent.horizontalCenter
                    width: 0.75 * parent.width
                    property alias model: resultsFormRepeater.model
                    property string controllerName

                    Repeater {
                        id: resultsFormRepeater
                        property int paramsCount: 1

                        delegate: OutputFieldDelegate {
                            width: (parent.width - parent.spacing) / resultsFormRepeater.paramsCount - computeButton.width
                        }

                        onModelChanged: {
                            paramsCount = model.count
                        }
                    }

                    Button {
                        id: computeButton
                        text: "Обчислити"
                        property string handlerName

                        onClicked: {
                            let formData = solverParamsForm.getFormData()
                            for (let i = 0; i < resultsForm.children.length; i++) {
                                let item = resultsForm.children[i]
                                if (item instanceof OutputFieldDelegate) {
                                    item.result = backend.dispatch(resultsForm.controllerName, item.handlerName, formData)
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
