import QtQuick 2.15


ListModel {
    ListElement {
        title: "Проценти за вказану кількість років"
        description: "Банк надав клієнту позику **p** грн. на **n** років за ставкою **i**% простих річних. Визначити проценти та нарощену на кінець терміну суму."
        group: "Прості відсотки"
        params: [
            ListElement {
                name: "n"
                description: "Термін угоди, виражений у періодах"
            },
            ListElement {
                name: "p"
                description: "Сума грошей (капітал), що даються в борг"
            },
            ListElement {
                name: "i"
                description: "Відсоткова ставка віднесена до певного періоду"
            }
        ]
    }
}
