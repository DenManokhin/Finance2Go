import numpy as np


# 1
def get_years_period_duration_with_i(p: float, s: float, i:float) -> float:
    """"
    Повертає тривалість періоду у роках.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    i : float
        Відсоткова ставка віднесена до певного періоду
    Returns
    -------
        n : float Тривалість періоду у роках.
    """
    return (s/p - 1) / i


# 2
def get_years_period_duration_with_d(p: float, s: float, d:float) -> float:
    """"
    Повертає тривалість періоду у роках.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    d : float
        Облікова ставка
    Returns
    -------
        n : float Тривалість періоду у роках.
    """
    return (1 - p/s) / d


# 3
def get_days_period_duration_with_i(p: float, s: float,
                                    i: float, k: int) -> float:
    """"
    Повертає тривалість періоду у днях.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    i : float
        Відсоткова ставка віднесена до певного періоду
    Returns
    -------
        t : float Тривалість періоду у днях.
    """
    return ((s/p - 1) / i) * k


# 4
def get_days_period_duration_with_d(p: float, s: float,
                                    d: float, k: int) -> float:
    """"
    Повертає тривалість періоду у днях.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    d : float
        Облікова ставка
    k: int
        Часова база нарахування відсотків
    Returns
    -------
        t : float Тривалість періоду у днях.
    """
    return ((1 - p/s) / d) * k


# 5
def get_interest_rate_with_years_period_duration(p: float, s: float,
                                                 n: float) -> float:
    """"
    Повертає відсоткову ставку для періоду у роках.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    n : float
        Тривалість періоду у роках
    Returns
    -------
        i : float Відсоткова ставка віднесена до певного періоду.
    """
    return (s/p - 1) / n


# 6
def get_discount_rate_with_years_period_duration(p: float, s: float,
                                                 n: float) -> float:
    """"
    Повертає облікову ставку для періоду у роках.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    n : float
        Тривалість періоду у роках
    Returns
    -------
        d : float Облікова ставка віднесена до певного періоду.
    """
    return (1 - p/s) / n


# 7
def get_interest_rate_with_days_period_duration(p: float, s: float,
                                                t: float, k: int) -> float:
    """"
    Повертає відсоткову ставку для періоду у днях.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    t : float
        Тривалість періоду у днях
    k: int
        Часова база нарахування відсотків
    Returns
    -------
        i : float Відсоткова ставка віднесена до певного періоду.
    """
    return ((s/p - 1) / t) * k


# 8
def get_discount_rate_with_days_period_duration(p: float, s: float,
                                                t: float, k: int) -> float:
    """"
    Повертає облікову ставку для періоду у днях.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    t : float
        Тривалість періоду у днях
    k: int
        Часова база нарахування відсотків
    Returns
    -------
        d : float Облікова ставка віднесена до певного періоду.
    """
    return ((1 - p/s) / t) * k


# 10
def get_complex_interest_years_period_duration_with_i(p: float, s: float,
                                                      i: float) -> float:
    """"
    Повертає тривалість періоду у роках.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    i : float
        Відсоткова ставка віднесена до певного періоду
    Returns
    -------
        n : float Тривалість періоду у роках.
    """
    return np.log(s/p) / np.log(1 + i)


# 11
def get_complex_interest_years_period_duration_with_d(p: float, s: float,
                                                      d: float) -> float:
    """"
    Повертає тривалість періоду у роках.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    d : float
        Облікова ставка
    Returns
    -------
        n : float Тривалість періоду у роках.
    """
    return np.log(p/s) / np.log(1 - d)


# 12
def get_years_period_duration_with_j(p: float, s: float,
                                     j: float, m: int) -> float:
    """"
    Повертає тривалість періоду у роках.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    j : float
        Річний множник нарощення за номінальною ставкою
    m:  int
        Кількість нарахувань у році.
    Returns
    -------
        n : float Тривалість періоду у роках.
    """
    return np.log(s/p) / (m * np.log(1 + j/m))


# 13
def get_years_period_duration_with_f(p: float, s: float,
                                     f: float, m: int) -> float:
    """"
    Повертає тривалість періоду у роках.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    f : float
        Номінальна річна облікова ставка
    m:  int
        Кількість нарахувань у році.
    Returns
    -------
        n : float Тривалість періоду у роках.
    """
    return np.log(p/s) / (m * np.log(1 + f/m))


# 14
def get_complex_interest_interest_rate_with_years_period_duration(
                                                            p: float,
                                                            s: float,
                                                            n: float) -> float:
    """"
    Повертає відсоткову ставку для періоду у роках.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    n : float
        Тривалість періоду у роках
    Returns
    -------
        i : float Відсоткова ставка віднесена до певного періоду.
    """
    return (s/p)**(1/n) - 1


# 15
def get_complex_interest_discount_rate_with_years_period_duration(
                                                            p: float,
                                                            s: float,
                                                            n: float) -> float:
    """"
    Повертає облікову ставку для періоду у роках.

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    n : float
        Тривалість періоду у роках
    Returns
    -------
        d : float Облікова ставка віднесена до певного періоду.
    """
    return 1 - (p/s)**(1/n)


# 16
def get_annual_accumulation_factor_with_years_period_duration(p: float,
                                                              s: float,
                                                              n: float,
                                                              m: int) -> float:
    """"
    Повертає річний множник нарощення за номінальною ставкою

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    n : float
        Тривалість періоду у роках
    m : int
        Кількість нарахувань в році
    Returns
    -------
        j : float Річний множник нарощення за номінальною ставкою.
    """
    return ((s/p)**(1/n*m) - 1) * m


# 17
def get_annual_discount_rate_with_years_period_duration(p: float,
                                                        s: float,
                                                        n: float,
                                                        m: int) -> float:
    """"
    Повертає номінальну річну облікову ставку

    Parameters
    ----------
    p : float
        Сума грошей (капітал), що даються в борг
    s : float
        Нарощена сума боргу
    n : float
        Тривалість періоду у роках
    m : int
        Кількість нарахувань в році
    Returns
    -------
        f : float Номінальна річна облікова ставка.
    """
    return (1 - (p/s)**(1/n*m)) * m
