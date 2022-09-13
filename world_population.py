import json
from pygal_maps_world import i18n
import pygal
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

def get_country_code(country_name):
    """Возвращает для заданной страны ее код из 2 букв"""

    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
        
    # если страна не найдена, вернуть none
    return None
    
# print(i18n.COUNTRIES)

# заполняем список данными
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# построение словаря с данными численности и населения
cc_population = {}

# вывод населения стран за 2010 год
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)

        if code:
            cc_population[code] = population
        
        else:
            print('Error - ' + country_name)

# группировка стран по 3 уровням населения
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
# wm.add('2010', cc_population)

wm.render_to_file('world_population.svg')
