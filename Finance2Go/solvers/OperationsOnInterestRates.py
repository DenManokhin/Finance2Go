import numpy as np


# 17 - формула нарощення складних відсотків
def get_accrued_amount(n: int, P: float, i: float) -> float:
    """ "
    Повертає нарощену суму на певну кількість років

    Parameters
    ----------
    P : float
        Початкова величина боргу(позики, кредиту)
    i : float
        Річна ставка складних відсотків
    n : int
        Кількість років нарощення
    Returns
    -------
    S : float
        Нарощена сума
    """
    return P * (1 + i) ** n


# 18 - формула нарощення складних відсотків
def get_accrued_amount_general(n: int, P: float, i: float) -> float:
    """ "
    Коли потрібно вирахувати проценти за весь період нарощення за складними відсотками

    Parameters
    ----------
    P : float
        Початкова величина боргу(позики, кредиту)
    i : float
        Річна ставка складних відсотків
    n : int
        Кількість років нарощення
    Returns
    -------
    S : float
        Нарощена сума
    """
    return P * ((1 + i) ** n - 1)


# 20 - змішаний метод, коли n - дробове число
def get_accrued_amount_mixed(P: float, i: float, c: int, d: float) -> float:
    """ "
    Коли потрібно вирахувати проценти за весь період нарощення за складними відсотками

    Parameters
    ----------
    P : float
        Початкова величина боргу(позики, кредиту)
    i : float
        Річна ставка складних відсотків
    c : int
        Ціла частина (від кількості років)
    d : float
        Дробова частина (від кількості років)
    Returns
    -------
    S : float
        Нарощена сума
    """
    return P * ((1 + i) ** c) * (1 + d * i)


# 21 - нарощення за номінальною ставкою
def get_accrued_amount_nominal(P: float, j: float, m: int, n: int) -> float:
    """ "
    Parameters
    ----------
    P : float
        Початкова величина боргу(позики, кредиту)
    j : float
        Річна ставка складних відсотків
    m : int
        кількість разів на рік коли нараховуються відсотки
    n : int
        Кількість років нарощення
    Returns
    -------
    S : float
        Нарощена сума
    """
    return P * (1 + j / m) ** (m * n)


# 22 - ефективна відсоткова ставка
def get_effective_rate(j: float, m: int) -> float:
    """ "
    Parameters
    ----------
    j : float
        Річна ставка складних відсотків
    m : int
        кількість разів на рік коли нараховуються відсотки
    Returns
    -------
    ic : float
        Ефективна ставка
    """
    return ((1 + j / m) ** m) - 1


# 23 - номінальна відсоткова ставка
def get_nominal_rate(ic: float, m: int) -> float:
    """ "
    Parameters
    ----------
    ic : float
        ефективна ставка
    m : int
        кількість разів на рік коли нараховуються відсотки
    Returns
    -------
    ic : float
        Ефективна ставка
    """
    return m * (((1 + ic) ** 1 / m) - 1)


# 25 - математичне дисконтування за складною відсотковою ставкою
def get_discont_price(S: float, i: float, n: int) -> float:
    """ "
    Parameters
    ----------
    S : float
        Сума
    i : float
        Річна ставка складних відсотків
    n: int
        Кількість років
    Returns
    -------
    P : float
        ціна
    """
    return S / ((1 + i) ** n)


# 26 - математичне дисконтування за складною відсотковою ставкою
def get_discont_price_several_time(S: float, j: float, n: int, m: int) -> float:
    """ "
    Parameters
    ----------
    S : float
        Сума
    j : float
        Номінальна відсоткова ставка складних відсотків
    n: int
        Кількість років
    m: int
        Кількість нарахувань у році
    Returns
    -------
    P : float
        ціна
    """
    return S / ((1 + j / m) ** (m * n))


# 27 - дисконтний множник
def get_discount_factor(j: float, n: int, m: int) -> float:
    """ "
    Parameters
    ----------
    j : float
        Номінальна відсоткова ставка складних відсотків
    n: int
        Кількість років
    m: int
        Кількість нарахувань у році
    Returns
    -------
    v : float
        дисконтний множник
    """
    return 1 / ((1 + j / m) ** (m * n))


# 28 - дисконт суми S
def get_discount_factor_sum(S: float, vn: float) -> float:
    """ "
    Parameters
    ----------
    S: float
        Сума
    vn: float
        дисконтний множник
    Returns
    -------
    D : float
        дисконт суми
    """
    return S * (1 - vn)


# 30 - Банківський облік за складною обліковою ставкою
def get_bank_accounting(S: float, d: float, n: int) -> float:
    """ "
    Parameters
    ----------
    S: float
        майбутня сума боргу
    d: float
        складна облікова ставка
    n: int
        тривалість угоди в роках
    Returns
    -------
    P : float
        сучасна (теперішня) сума боргу
    """
    return S * (1 - d) ** n


# 32 - Банківський облік за складною обліковою ставкою кілька разів на рік
def get_bank_accounting_several_times(S: float, f: float, m: int, n: int) -> float:
    """ "
    Parameters
    ----------
    S: float
        майбутня сума боргу
    f: float
        номінальна річна облікова ставка
    n: int
        тривалість угоди в роках
    m: int
        Кількість нарахувань у році
    Returns
    -------
    P : float
        сучасна (теперішня) сума боргу
    """
    return S * (1 - f / m) ** (m * n)


# 33 - Ефективна облікова ставка
def get_effective_discount_rate_nominal(f: float, m: int) -> float:
    """ "
    Parameters
    ----------
    f: float
        номінальна річна облікова ставка
    m: int
        Кількість нарахувань у році
    Returns
    -------
    de : float
        Ефективна облікова ставка
    """
    return 1 - (1 - f / m) ** m


# 34 - номінальна річна облікова ставка
def get_nominal_account_rate(de: float, m: int) -> float:
    """ "
    Parameters
    ----------
    de : float
        Ефективна облікова ставка
    m: int
        Кількість нарахувань у році
    Returns
    -------
    f: float
        номінальна річна облікова ставка
    """
    return m(1 - (1 - de) ^ (1 / m))


# 34 - номінальна річна облікова ставка
def get_effective_discount_rate(de: float, m: int) -> float:
    """ "
    Parameters
    ----------
    de : float
        Ефективна облікова ставка
    m: int
        Кількість нарахувань у році
    Returns
    -------
    f: float
        номінальна річна облікова ставка
    """
    return m(1 - (1 - de) ^ (1 / m))


# 35 - нарощення за складною обліковою ставкою
def get_increase_amount(P: float, d: float, n: int) -> float:
    """ "
    Parameters
    ----------
    P : float
        Сума яку отримає власник векселя
    n: int
        кількість років
    Returns
    -------
    S: float
        сума нарощення за складною обліковою ставкою
    """
    return P / ((1 - d) ** n)


# 36 - нарощення за номінальною обліковою ставкою
def get_increase_amount_nominal(P: float, f: float, m: int, n: int) -> float:
    """ "
    Parameters
    ----------
    P : float
        Сума яку отримає власник векселя
    f: float
        номінальна річна облікова ставка
    m: int
        Кількість нарахувань у році
    n: int
        кількість років
    Returns
    -------
    S: float
        сума нарощення за складною обліковою ставкою
    """
    return P / ((1 - f / m) ** (m * n))
