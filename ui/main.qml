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

    StackView  {
        id: swipeView
        anchors.fill: parent

        initialItem: Item {
            id: solversListViewContainer
        }
        Item {
            id: solverContainer
        }
    }

    SplitView {
        id: splitView
        anchors.fill: parent

        states: [
            State {
                when: window.width < responsiveWidth
                ParentChange { target: solversListView; parent: solversListViewContainer; }
                PropertyChanges { target: splitView; visible: false }
            }
        ]

        Item {
            height: parent.height
            SplitView.minimumWidth: parent.width / 3

            ListView {
                id: solversListView

                focus: true
                currentIndex: -1
                anchors.fill: parent

                delegate: ItemDelegate {
                    width: solversListView.width
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
                        solverView.model = model.params
                        solverSection.visible = true
                        computeButton.handlerName = model.handler
                    }

                    Rectangle {
                        anchors.bottom: parent.bottom
                        width: parent.width
                        height: 1
                        color: Material.foreground
                    }
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

                Row {
                    id: solverGrid
                    spacing: 20
                    anchors.horizontalCenter: parent.horizontalCenter
                    width: 0.75 * parent.width

                    Repeater {
                        id: solverView
                        property int paramsCount: 1

                        delegate: ItemDelegate {

                            property string objectName: model.name
                            property double objectValue: model.defaultValue
                            width: (solverGrid.width - solverGrid.spacing) / solverView.paramsCount
                            hoverEnabled: false

                            Label {
                                text: model.name + " = "
                                font.pointSize: 14
                            }

                            TextField {
                                ToolTip.delay: 1000
                                ToolTip.timeout: 5000
                                ToolTip.visible: hovered
                                ToolTip.text: model.description

                                selectByMouse: true
                                horizontalAlignment: TextInput.AlignRight
                                text: "" + objectValue
                                font.pointSize: 12
                                leftPadding: parent.children[0].width
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
                                    console.log("" + value)
                                }
                            }
                        }

                        onModelChanged: {
                            paramsCount = model.count
                        }
                    }
                }

                Row {
                    padding: 10
                    spacing: 10
                    anchors.horizontalCenter: parent.horizontalCenter

                    TextField {
                        id: singleResult
                        readOnly: true
                    }

                    Button {
                        id: computeButton
                        text: "Обчислити"
                        property string handlerName

                        onClicked: {
                            let formData = {}
                            for (let i = 0; i < solverGrid.children.length; i++) {
                                let item = solverGrid.children[i]
                                if (item.objectName) {
                                    formData[item.objectName] = item.objectValue
                                }
                            }

                            singleResult.visible = true
                            singleResult.text = backend.dispatch(handlerName, formData)
                        }
                    }
                }
            }
        }
    }
}
