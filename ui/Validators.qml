import QtQuick 2.15

Item {
    DoubleValidator {
        id: yearsValidator
        bottom: 0
        top: 100
        decimals: 2
        locale: "uk_UA"
        notation: DoubleValidator.StandardNotation
    }

    DoubleValidator {
        id: moneyValidator
        bottom: 0
        top: 100000000000000000000
        decimals: 2
        locale: "uk_UA"
        notation: DoubleValidator.StandardNotation
    }

    DoubleValidator {
        id: percentValidator
        bottom: 0
        top: 1
        decimals: 4
        locale: "uk_UA"
        notation: DoubleValidator.StandardNotation
    }

    function getValidator(name) {
        switch (name) {
            case "years":
                return yearsValidator
            case "money":
                return moneyValidator
            case "percent":
                return percentValidator
        }
    }
}
