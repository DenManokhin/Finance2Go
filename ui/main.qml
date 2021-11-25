import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id: window
    visible: true
    width: 640
    height: 480
    minimumWidth: 300
    minimumHeight: 300
    title: "Finance2Go"
    readonly property int responsiveWidth: 500

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
                    contentItem: Text {
                        text: parent.text
                        font: parent.font
                        wrapMode: Text.Wrap
                    }
                    highlighted: ListView.isCurrentItem

                    onClicked: {
                        solversListView.currentIndex = index
                    }

                    Rectangle {
                        anchors.bottom: parent.bottom
                        width: parent.width
                        height: 1
                        color: "black"
                    }
                }

                model: ListModel {
                    ListElement { title: "Проценти за вказану кількість років"; group: "Прості відсотки" }
                    ListElement { title: "Нарощення за простими відсотками"; group: "Прості відсотки" }
                }

                section.property: "group"
                section.criteria: ViewSection.FullString 
                section.delegate: ToolBar {
                    id: background
                    width: solversListView.width

                    Label {
                        id: label
                        text: section
                        anchors.fill: parent
                        horizontalAlignment: Qt.AlignHCenter
                        verticalAlignment: Qt.AlignVCenter
                    }
                }

                ScrollIndicator.vertical: ScrollIndicator { }
            }
        }
        Item {
            height: parent.height
            SplitView.minimumWidth: parent.width / 3

            Rectangle{
                id: solver
                anchors.fill: parent
                color: "lightgray"; border.width: 5; border.color: "white"
            }
        }
    }
}