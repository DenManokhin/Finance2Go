import numpy as np


# 1
def get_interest(n: float, p: float, i: float) ->\
        float:
    """"
    Повертає проценти за вказану кількість років.

    Parameters
    ----------
    n : float
        Термін угоди, виражений у періодах
    p : int
        Сума грошей (капітал), що даються в борг
    i : float
        Відсоткова ставка віднесена до певного періоду
    Returns
    -------
        I : float Відсоткові гроші (проценти)
    """
    return n * p * i


# 2
def get_accumulated_sum(n: float, p: float, i: float) ->\
        float:
    """"
    Повертає формулу нарощення за простими відсотками.

    Parameters
    ----------
    n : float
        Термін угоди, виражений у періодах
    p : float
        Сума грошей (капітал), що даються в борг
    i : float
        Відсоткова ставка віднесена до певного періоду
    Returns
    -------
        S : float Сума боргу на момент закінчення угоди за вказану
        кількість років.
    """
    return p * (1 + n * i)


# 3
def get_increased_sum_with_fractional_n(t: int, k: int, p: float, i: float) ->\
        float:
    """"
    Повертає нарощену суму, взяши у формулі нарощення за простими
    відсотками термін угоди як дробове число.

    Parameters
    ----------
    t : int
        Кількість днів позики
    k : int
        Часова база нарахування відсотків (кількість днів у році)
    p : float
        Сума грошей (капітал), що даються в борг
    i : float
        Відсоткова ставка віднесена до певного періоду
    Returns
    -------
        S : float Сума боргу на момент закінчення угоди за вказану
        кількість років.
    """
    return get_accumulated_sum(t/k, p, i)


# 4
def get_increased_sum_for_different_periods(n: np.array, p: float,
                                            i: np.array) -> float:
    """"
    Повертає нарощену суму, де відсоткові ставки встановлюються
    окремо для різних періодів.

    Parameters
    ----------
    n : np.array
        Тривалість періоду нарахування за постійною ставкою i_t
    p : float
        Сума грошей (капітал), що даються в борг
    i : np.array
        Відсоткова ставка простих відсотків в періоді t
    Returns
    -------
        S : float Сума боргу на момент закінчення угоди.
    """
    return p * (1 + n.dot(i))


# 5
def get_increased_sum_with_reinvestment(n: np.array, p: float, i: np.array) \
        -> float:
    """"
    Повертає нарощену суму з капіталізацією.

    Parameters
    ----------
    n : np.array
        Тривалість періодів нарощення
    p : float
        Сума грошей (капітал), що даються в борг
    i : np.array
        Відсоткові ставки у відповідні періоди
    Returns
    -------
        S : float Сума багаторазового нарощення відсоткового доходу.
    """
    return p * np.prod(1 + n * i)


# 6
def get_interest_with_changeable_investment(n: np.array, r: np.array,
                                            i: float) -> float:
    """"
    Повертає проценти із врахуванням змінного капіталу.

    Parameters
    ----------
    n : np.array
        Термін зберігання коштів до нової зміни залишків на рахунку
    r : np.array
        Залишок коштів на рахунку в момент часу j після чергового
        надходження чи списання коштів
    i : float
        Відсоткова ставка віднесена до певного періоду
    Returns
    -------
        I : float Відсоткові гроші (проценти)
    """
    return np.sum(n * r * i)


# 7
def get_interest_with_changeable_investment_and_fractional_n(t: np.array,
                                                             k: int,
                                                             r: np.array,
                                                             i: int) -> float:
    """"
    Повертає проценти із врахуванням змінного капіталу та інтервалами між
    моментами змін залишків на рахунку в днях, а відсоткову ставку у вигляді
    відсотків.

    Parameters
    ----------
    t : np.array
        Кількість днів між послідовними змінами залишків на рахунку
    k: int
        Часова база нарахування відсотків
    r : np.array
        Залишок коштів на рахунку в момент часу j після чергового
        надходження чи списання коштів,
    i : int
        Відсоткова ставка віднесена до певного періоду (у відсотках)
    Returns
    -------
        I : float Відсоткові гроші (проценти)
    """
    return ((r.dot(t)) / 100) / (k / i)


# 8
def get_one_time_payment_sum(n: float, s: float, m: int) -> float:
    """"
    Повертає величину разової виплати за користування кредитом.

    Parameters
    ----------
    n : float
        Термін кредиту у роках
    s : float
        Нарощена сума боргу
    m : int
        Кількість виплат у році
    Returns
    -------
        R : float Величина разової виплати.
    """
    return s / (n * m)


# 9
def get_discount(s: float, p: float) -> float:
    """"
    Повертає дисконт величини S.

    Parameters
    ----------
    s : float
        Нарощена сума боргу
    p : float
        Дисконтована вартість (зведена, теперішня величина) суми S
    Returns
    -------
        D : float Дисконт (== I).
    """
    return s - p


# 10
def get_mathematical_discounting(n: float, s: float, i: float) -> float:
    """"
    Повертає визначення теперішньої суми боргу P за відомою кінцевою сумою S.

    Parameters
    ----------
    n : float
        Термін кредиту у роках
    s : float
        Нарощена сума боргу
    i : float
        Відсоткова ставка віднесена до певного періоду
    Returns
    -------
        P : float Математична дисконтована вартість.
    """
    return s / (1 + n * i)


# 11
def get_bank_accounting(n: float, s: float, d: float) -> float:
    """"
    Повертає визначення теперішньої суми боргу P за відомою величиною S у
    майбутньому.

    Parameters
    ----------
    n : float
        Термін кредиту у роках
    s : float
        Нарощена сума боргу
    d : float
        Облікова ставка віднесена до певного періоду
    Returns
    -------
        P : float Банківський облік (або ж облік векселів).
    """
    return s * (1 - n * d)


# 12
def get_discount_rate(n: float, s: float, p: float) -> float:
    """"
    Повертає значення облікової ставки.

    Parameters
    ----------
    n : float
        Термін кредиту у роках
    s : float
        Нарощена сума боргу
    p : float
        Банківський облік
    Returns
    -------
        d : float Облікова ставка.
    """
    return (s - p) / (n * s)


# 13
def get_increased_sum_with_discount_rate(n: float, p: float,
                                            d: float) -> float:
    """"
    Повертає нарощену суму.

    Parameters
    ----------
    n : float
        Термін кредиту у роках
    p : float
        Сума грошей (капітал), що даються в борг
    d : float
        Облікова ставка віднесена до певного періоду
    Returns
    -------
        S : float Сума боргу на момент закінчення угоди.
    """
    return p / (1 - n * d)
