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

                Grid {
                    id: grid
                    padding: 10
                    columns: 3
                    anchors.horizontalCenter: parent.horizontalCenter

                    Repeater {
                        id: solverView

                        delegate: Item {
                            Component.onCompleted: {
                                while (children.length) { children[0].parent = grid; }
                            }
                            Label {
                                text: model.name
                                font.pointSize: 22
                            }
                            Label {
                                text: "="
                                font.pointSize: 22
                            }
                            SpinBox {
                                ToolTip.delay: 1000
                                ToolTip.timeout: 5000
                                ToolTip.visible: hovered
                                ToolTip.text: model.description
                            }
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

                        onClicked: {
                            singleResult.visible = true
                        }
                    }
                }
            }
        }
    }
}
