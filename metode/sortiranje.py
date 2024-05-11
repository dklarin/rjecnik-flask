'''import locale

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
        raise ValueError("Nepodržani način sortiranja: {}".format(jezik))'''

# definicija rječnika za sortiranje hrvatskih slova
croatian_alphabet_order = {
    'a': 0, 'b': 1, 'c': 2, 'č': 3, 'ć': 4, 'd': 5, 'dž': 6, 'đ': 7, 'e': 8, 'f': 9, 'g': 10, 'h': 11,
    'i': 12, 'j': 13, 'k': 14, 'l': 15, 'lj': 16, 'm': 17, 'n': 18, 'nj': 19, 'o': 20, 'p': 21, 'r': 22,
    's': 23, 'š': 24, 't': 25, 'u': 26, 'v': 27, 'z': 28, 'ž': 29
}

# funkcija za sortiranje riječi ili izraza prema hrvatskom abecednom poretku
def croatian_sort(word):
    temp_letters = []
    sorted_word = []
    # provjera za zarez kao dodatni razdjelnik
    words = word.replace(',', ' ').split()
    for w in words:
        i = 0
        while i < len(w):
            if i + 1 < len(w) and w[i:i+2].lower() in croatian_alphabet_order:
                temp_letters.append(croatian_alphabet_order[w[i:i+2].lower()])
                i += 2
            else:
                if temp_letters:
                    sorted_word.extend(sorted(temp_letters))
                    temp_letters = []
                sorted_word.append(croatian_alphabet_order[w[i].lower()])
                i += 1
        if temp_letters:
            sorted_word.extend(sorted(temp_letters))
    return sorted_word
