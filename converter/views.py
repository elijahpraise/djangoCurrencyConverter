from django.shortcuts import render
from converter.functions import rate_display, symbols_display
from  import CurrencySymbols

rates = rate_display('https://api.exchangerate.host/latest')
symbols = symbols_display(rates)


def index(request):
    """
    evaluates if the page is submitting the required form or just returning a page.
    """
    if request.method == 'POST':
        amount = request.POST['amount']
        current_currency = request.POST['current_currency']
        desired_currency = request.POST['desired_currency']
        # if  current currency is not equal to euros then convert to euros before converting to desired currency.
        if current_currency != 'EUR':
            amount_in_euro = int(amount) / rates.get(current_currency)
            result = amount_in_euro * rates.get(desired_currency)
        # or if current currency is equal to euros then convert to desired currency.
        elif str(current_currency) == 'EUR':
            result = int(amount) * rates.get(current_currency)
        # getting the symbol for both the current and desired currency.
        current_currency_symbol = CurrencySymbols.get_symbol(current_currency)
        desired_currency_symbol = CurrencySymbols.get_symbol(desired_currency)
        context = {
            'result': result,
            'amount': amount,
            'current_currency_symbol': current_currency_symbol,
            'desired_currency_symbol': desired_currency_symbol
        }
        return render(request, 'converter/result.html', context=context)
    else:
        return render(request, 'converter/index.html', {'symbols': symbols})
