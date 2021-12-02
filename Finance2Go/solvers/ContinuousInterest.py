import numpy as np


# 1
def get_increased_sum_with_growth_force(n: int, p: float,
                                        delta: float) -> float:
    """"
    Повертає нарощена суму у випадку використання сили росту.

    Parameters
    ----------
    n : int
        Термін угоди, виражений у роках
    p : float
        Сума грошей (капітал), що даються в борг
    delta : float
        Неперервна ставка нарощення (сила росту)
    Returns
    -------
        S : float Нарощена сума.
    """
    return p * np.exp(n * delta)


# 2
def get_continuous_interest(i: float) -> float:
    """"
    Повертає неперервну ставку нарощення.

    Parameters
    ----------
    i : float
        Складна дискретна ставка нарощення
    Returns
    -------
        delta : float Неперервна ставка нарощення.
    """
    return np.log(1 + i)


# 3
def get_discrete_interest(delta: float) -> float:
    """"
    Повертає складну дискретна ставка нарощення.

    Parameters
    ----------
    delta : float
        Складна неперервна ставку нарощення
    Returns
    -------
        i : float Дискретна ставка нарощення.
    """
    return np.exp(delta) - 1


# 4
def get_mathematical_discounting_with_growth_force(n: int, s: float,
                                                   delta: float) -> float:
    """"
    Повертає визначення теперішньої суми боргу P за відомою кінцевою сумою S.

    Parameters
    ----------
    n : int
        Термін кредиту у роках
    s : float
        Нарощена сума боргу
    delta : float
        Неперервна ставка нарощення (сила росту)
    Returns
    -------
        P : float Математична дисконтована вартість.
    """
    return s * np.exp(-delta * n)


# 5
def get_build_up_multiplier_for_linear_function(n: int, a: float,
                                                delta: float) -> float:
    """"
    Повертає множник нарощення у випадку використання змінної сили росту
     для лінійної залежності.
    Parameters
    ----------
    n : int
        Термін кредиту у роках
    a : float
        Приріст сили росту за одиницю часу
    delta : float
        Початкове значення сили росту
    Returns
    -------
        : float Множник нарощення.
    """
    return np.exp(delta * n + (a * n**2) / 2)


# 6
def get_build_up_multiplier_for_exp_function(n: int, a: float,
                                             delta: float) -> float:
    """"
    Повертає множник нарощення у випадку використання змінної сили росту
     для експоненціальної залежності.

    Parameters
    ----------
    n : int
        Термін кредиту у роках
    a : float
        Приріст сили росту за одиницю часу
    delta : float
        Початкове значення сили росту
    Returns
    -------
        : float Множник нарощення.
    """
    return (delta / np.log(a)) * (a**n - 1)


# 7
def get_increased_sum_with_changeable_growth_force(n: int,
                                                   a: float,
                                                   p: float,
                                                   delta: float,
                                                   func_type: str) -> float:
    """"
    Повертає нарощена суму у випадку використання змінної сили росту.

    Parameters
    ----------
    n : int
        Термін кредиту у роках
    a : float
        Приріст сили росту за одиницю часу
    p : float
        Сума грошей (капітал), що даються в борг
    delta : float
        Неперервна ставка нарощення (сила росту)
    func_type: str
        Тип неперервної функції (linear або exp)
    Returns
    -------
        S : float Нарощена сума.
    """
    if func_type == "linear":
        return p * get_build_up_multiplier_for_linear_function(n, a, delta)
    elif func_type == "exp":
        return p * get_build_up_multiplier_for_exp_function(n, a, delta)
    else:
        pass


# 8
def get_mathematical_discounting_with_changeable_growth_force(
                                                    n: int,
                                                    a: float,
                                                    s: float,
                                                    delta: float,
                                                    func_type: str) -> float:
    """"
    Повертає визначення теперішньої суми боргу P за відомою кінцевою сумою S.

    Parameters
    ----------
    n : int
        Термін кредиту у роках
    a : float
        Приріст сили росту за одиницю часу
    s : float
        Нарощена сума боргу
    delta : float
        Неперервна ставка нарощення (сила росту)
    func_type: str
        Тип неперервної функції (linear або exp)
    Returns
    -------
        P : float Математична дисконтована вартість.
    """
    if func_type == "linear":
        return s * get_build_up_multiplier_for_linear_function(n, a, delta)
    elif func_type == "exp":
        return s * get_build_up_multiplier_for_exp_function(n, a, delta)
    else:
        pass


# 9
def get_loan_term_with_growth_force(s: float, p: float,
                                    delta: float) -> float:
    """"
    Повертає термін кредиту у роках для нарощення з постійно силою росту.

    Parameters
    ----------
    s : float
        Нарощена сума боргу
    p : float
        Сума грошей (капітал), що даються в борг
    delta : float
        Неперервна ставка нарощення (сила росту)
    Returns
    -------
        n : float Термін кредиту.
    """
    return np.log(s / p) / delta


# 10
def get_continuous_rate_with_growth_force(n: int, p: float,
                                          s: float) -> float:
    """"
    Повертає неперервну ставку для нарощення з постійно силою росту.

    Parameters
    ----------
    n : int
        Термін угоди, виражений у роках
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    Returns
    -------
        delta : float Неперервна ставка.
    """
    return np.log(s / p) / n


# 11
def get_loan_term_with_changeable_growth_force(a: float, p: float,
                                               s: float,
                                               delta: float) -> float:
    """"
    Повертає термін кредиту у роках для нарощення зі змінною силою росту.

    Parameters
    ----------
    a : float
        Приріст сили росту за одиницю часу
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    delta : float
        Неперервна ставка нарощення (сила росту)
    Returns
    -------
        n : float Термін кредиту.
    """
    return np.log(1 + (np.log(a) * np.log(s / p) / delta)) / np.log(a)


# 12
def get_continuous_rate_with_changeable_growth_force(n: int, a: float,
                                                     p: float,
                                                     s: float) -> float:
    """"
    Повертає неперервну ставку для нарощення зі змінною силою росту.

    Parameters
    ----------

    n : int
        Термін угоди, виражений у роках
    a : float
        Приріст сили росту за одиницю часу
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    Returns
    -------
        delta : float Неперервна ставка.
    """
    return (np.log(a) * np.log(s / p)) / (a**n - 1)
