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
                validator: "years"
            },
            ListElement {
                name: "p"
                description: "Початкова сума грошей"
                defaultValue: 100000
                validator: "money"
            },
            ListElement {
                name: "i"
                description: "Відсоткова ставка"
                defaultValue: 0.25
                validator: "percent"
            }
        ]
        handler: "getInterest"
    }
}
