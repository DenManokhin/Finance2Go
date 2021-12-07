import QtQuick 2.15

Item {
    RegularExpressionValidator {
        id: yearsValidator
        regularExpression: /^((\d{1,2})?(\.\d{1,2})?)$/
    }

    RegularExpressionValidator {
        id: moneyValidator
        regularExpression: /^\d{1,10}(\.\d{1,2})?$/
    }

    RegularExpressionValidator {
        id: percentValidator
        regularExpression: /^100|(\d{1,2}(\.\d{1,2})?)$/
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
