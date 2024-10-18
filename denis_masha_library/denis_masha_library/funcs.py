from functools import reduce
from datetime import date
import pandas as pd
from geopy.distance import geodesic

def count_simba(simba):
    return reduce(lambda acc, s: acc + s.lower().count('simba'), simba, 0)

strings = ["Simba and Nala are lions.", "I laugh in the face of danger.",
                 "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

print(count_simba(strings))

def get_day_month_year(dates):
    return pd.DataFrame(list(map(lambda d: {'day': d.day, 'month': d.month, 'year': d.year}, dates)))

dates_list = [date(2022, 10, 20), date(2023, 10, 23), date(2024, 10, 24)]
print(get_day_month_year(dates_list))

def compute_distance(coordinates):
    return list(map(lambda coords: geodesic(coords[0], coords[1]).kilometers, coordinates))

coordinates = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
print(compute_distance(coordinates))

def sum_general_int_list(l):
    return reduce(lambda acc, el: acc + (sum_general_int_list(el) if isinstance(el, list) else el), l, 0)

nlist = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
print(sum_general_int_list(nlist))