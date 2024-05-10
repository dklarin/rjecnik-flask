from flask import Blueprint, render_template

from metode.sortiranje import *
from metode.sheets import plahte

rijeci = Blueprint('rijeci', __name__,
                   template_folder='templates')

wks = plahte()

# lista apartmana
skupina = ['šolski pribor', 
           'moja družina',
           'kaj je to kdo je to']

link = ['/rijeci/slovenski:solski_pribor:', 
        '/rijeci/slovenski:moja_druzina:',
        '/rijeci/slovenski:kaj_je_to_kdo_je_to:']

kljucevi_json = ['link', 'skupina']
linkovi = [{kljuc: vrijednost for kljuc, vrijednost in zip(kljucevi_json, vrijednosti)} 
                for vrijednosti in zip(link, skupina)] 

@rijeci.route('/rijeci/<jezik_skupina_sort>/')
def rjecnik(jezik_skupina_sort):  

    splitani_string = jezik_skupina_sort.split(":")

    jezik = splitani_string[0]
    skupina = splitani_string[1]
    sort = splitani_string[2]
   
    retci = wks.get_all_records()
    
    if skupina == 'moja_druzina':
        retci = [item for item in retci if item['skupina'] == 'moja družina']
    elif skupina == 'solski_pribor':
        retci = [item for item in retci if item['skupina'] == 'šolski pribor']   
    elif skupina == 'kaj_je_to_kdo_je_to':
        retci = [item for item in retci if item['skupina'] == 'kaj je to kdo je to']
    elif skupina == 'sve':
        retci = retci         
    else:
        print('Ne postoji takva riječ!')
        return render_template('404.html'), 404

    if sort == 'sortiraj':
        # sortiranje niza riječi koristeći prilagođenu funkciju za sortiranje
        sortirane_rijeci = sorted(retci, key=lambda x: custom_sort_key(x, jezik)) 
    else:
        sortirane_rijeci = retci
    
    print(skupina)

    return render_template('rijeci_sve.html', retci=sortirane_rijeci, linkovi=linkovi, skupina=skupina)
