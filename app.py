from itertools import combinations
import json
import pandas as pd


def get_data(path): # обработка входных данных
    with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    return data

def generate_combs(line): # генерация всевозможных комбинаций для одной строки признаков
    res = []
    for i in range(1,len(line.values())+1):
        value_comb = []
        key_comb = []
        for comb in combinations(line.values(), r = i):
            value_comb.append(list(comb))
        for comb in combinations(line.keys(), r = i):
            key_comb.append(list(comb))
        for  j in range(len(key_comb)):
            res.append(dict(list(zip(key_comb[j], value_comb[j])))) # сохраняем в удобном формате словаря, кладя все комбинации в массив
    return res
        
def main(data): # основная функция
    res = generate_combs(data[0])
            
    for uniq_comb in res: # просматриваем каждую комбинацию
        flag = True
        checked_obj = []
        for i in range(1, len(data)): # сравниваем ее по ключам с остальными в нашем массиве данных
            json_obj = data[i]
            comb_obj = dict()
            for key in uniq_comb.keys():
                try:
                    comb_obj[key] = json_obj[key]
                except:
                    comb_obj[key] = None
            
            if comb_obj == uniq_comb: # если есть полное совпадение значит не уникальная комбинация
                flag = False
                break
            elif comb_obj in checked_obj: # если комбинация встречается не впервые то она не уникальна
                flag=False
                break
            else:
                checked_obj.append(comb_obj) # сохранение в массив комбинаций чтобы не пропустить совпадение
        if flag:
            fields = list(uniq_comb.keys()) #вывод первой уникальной комбинации, т.к по алгоритму она и будет являться наименьшей по количеству признаков
            break

    return pd.Series(fields)

data = get_data('./pr1.json')
print(main(data))



        
    
