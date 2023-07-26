'''
REST API documentation:  https://developer.edamam.com/edamam-docs-recipe-api
'''
import random
import requests
import json
import random

from csvhandler import save_data


def get_content():
    data = get_data_url()
    results = extract_data(data)

    return results

def get_data_url():
    # Adres URL API Rest
    url = 'https://api.edamam.com/api/recipes/v2?type=public&app_id=41896ae7&app_key=%20ad8016fc0de5de69bab7d400a24cff52%09&mealType=Dinner&imageSize=LARGE&calories=0-3000&random=true'

    # Żądanie GET do API
    response = requests.get(url)

    data = response.json()
    return data


#wyciągnięcie odpowiednich danych ze słownika z Rest API
def extract_data(data):

    for element in data['hits']:
        image = element['recipe']['images']['LARGE']['url']
        name = element['recipe']['label']
        calories = int(element['recipe']['calories'])
        servings = int(element['recipe']['yield'])
        uri = element['recipe']['uri']
        rangevalues = slider_range(calories)
        extracted_data = {'id': id_extractor(uri),
            
                          'name_key': name,
                          'value_key': calories,
                          'servings_key': servings,
                          'top_range': rangevalues.get('top_range'),
                          'bottom_range': rangevalues.get('bottom_range'),
                          'image_key': image}
        save_data(extracted_data)

    return extracted_data

#ucięcie stringa uri, tylko do formy unique ID
def id_extractor(uri_id):
    distributor = 'www.edamam.com/ontologies/edamam.owl#recipe_'
    return (uri_id.split(distributor,1)[1])


def slider_range(calories_value):
    random.seed(5)
    bottom = calories_value - random.randint(100,500)
    if bottom <0:
        bottom = 0
    top = calories_value + random.randint(100,500)
    return {'top_range': top, 'bottom_range': bottom}


# def get_random_data(data):
#     achieved_data = data
#     # Pobranie wszystkich rekordów z listy "hits"
#     records = achieved_data['hits']
#     # Pobranie losowego rekordu
#     random_record = random.choice(records)
#
#     return random_record


print(get_content())
