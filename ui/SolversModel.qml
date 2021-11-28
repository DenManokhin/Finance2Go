import QtQuick 2.15


ListModel {
    ListElement {
        title: "Проценти за вказану кількість років"
        description: "Банк надав клієнту позику **p** грн. на **n** років за ставкою **i**% простих річних. Визначити проценти та нарощену на кінець терміну суму."
        group: "Прості відсотки"
        params: [
            ListElement {
                name: "n"
                description: "Термін угоди"
                defaultValue: 5
                min: 0
                max: 100
                decimals: 2
            },
            ListElement {
                name: "p"
                description: "Початкова сума грошей"
                defaultValue: 100000
                min: 0
                max: 10000000
                decimals: 2
            },
            ListElement {
                name: "i"
                description: "Відсоткова ставка"
                defaultValue: 0.25
                min: 0
                max: 1
                decimals: 4
            }
        ]
        handler: "getInterest"
    }
}
