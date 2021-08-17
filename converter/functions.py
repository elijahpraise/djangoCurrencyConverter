import requests


def rate_display(url):
    """
    :param url: Takes url as string.
    :return: Rates in dictionary format.
    """
    try:
        api_handle = requests.get(url)
    except ValueError:
        print('does not exist.')
    # change to json format and then to native python dictionary format.
    body = dict(api_handle.json())
    rates = dict(body.get('rates'))
    return rates


def symbols_display(rates=dict):
    """
    :param rates: Takes rate of different currencies from rate_display.
    :return: All abbreviations of available currencies in a list.
    """
    symbols = rates.keys()
    list_of_symbols = list()
    for symbol in symbols:
        list_of_symbols.append(symbol)
    return list_of_symbols
