import QtQuick 2.15


ListModel {
    ListElement {
        title: "Формула простих відсотків"
        description: "Банк надав клієнту позику **p** грн. на **n** років за ставкою **i**% простих річних. Визначити проценти **I** та нарощену на кінець терміну суму **S**."
        group: "Прості відсотки"
        params: [
            ListElement {
                name: "n"
                label: "n"
                defaultValue: 5
                validator: "years"
            },
            ListElement {
                name: "p"
                label: "p"
                defaultValue: 100000
                validator: "money"
            },
            ListElement {
                name: "i"
                label: "i"
                defaultValue: 0.25
                validator: "percent"
            }
        ]
        results: [
            ListElement {
                label: "I"
                handler: "getInterest"
            },
            ListElement {
                label: "S"
                handler: "getAccumulatedSum"
            }
        ]
    }
}
