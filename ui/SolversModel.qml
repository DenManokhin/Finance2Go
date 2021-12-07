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
                defaultValue: 25
                validator: "percent"
            }
        ]
        repeatableParams: []
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
        controller: "simpleInterest"
    }

    ListElement {
        title: "Різні відсоткові ставки для різних періодів"
        description: "Фінансовою угодою передбачено такі умови нарахування простих відсотків на депозит: перші **n** років – **i**% річних, наступні... . Визначити множник нарощення та нарощену суму, якщо початковий вклад становив **p** грн."
        group: "Прості відсотки"
        params: [
            ListElement {
                name: "p"
                label: "p"
                defaultValue: 10000
                validator: "money"
            }
        ]
        repeatableParams: [
            ListElement {
                name: "n"
                label: "n"
                defaultValue: 0.25
                validator: "years"
            },
            ListElement {
                name: "i"
                label: "i"
                defaultValue: 15
                validator: "percent"
            }
        ]
        results: [
            ListElement {
                label: "S"
                handler: "getAccumulatedValueForDifferentPeriods"
            }
        ]
        controller: "simpleInterest"
    }
}
