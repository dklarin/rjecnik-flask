import locale

# funkcija za generiranje ključeva sortiranja
def custom_sort_key_hr(podatak):
    # definiranje lokalnih postavki za hrvatski jezik
    locale.setlocale(locale.LC_ALL, 'hr_HR.UTF-8')
    return locale.strxfrm(podatak['hrvatski'])

# funkcija za generiranje ključeva sortiranja
def custom_sort_key_sl(podatak):
    # definiranje lokalnih postavki za slovenski jezik
    locale.setlocale(locale.LC_ALL, 'sl_SL.UTF-8')
    return locale.strxfrm(podatak['slovenski'])

def custom_sort_key(podatak, jezik):
    if jezik == 'hrvatski':
        return custom_sort_key_hr(podatak)
    elif jezik == 'slovenski':
        return custom_sort_key_sl(podatak)
    else:
        raise ValueError("Nepodržani način sortiranja: {}".format(jezik))

