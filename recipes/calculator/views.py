from django.shortcuts import render
from django.http import HttpResponse
import copy

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'cheesecake': {
        'творог, г': 350,
        'яйца, шт': 2,
        'мука, ст.ложка': 6,
        'сахар, ст.ложка': 2,
        'масло, ст.ложка': 5,
    }
}


def index(request):
    dish_name_list = []
    for dish_name_for_list in DATA.keys():
        dish_name_list.append(dish_name_for_list)
    context = {
        'dish_name_list': dish_name_list,
    }
    return render(request, 'index/index.html', context)

def dish(request, dish):
    dish_name = dish
    servings = int(request.GET.get('servings', 1))
    recipe = copy.copy(DATA[dish_name])
    for ingredient, amount in recipe.items():
        recipe[ingredient] = amount * servings
    dish_name_list = []
    for dish_name_for_list in DATA.keys():
        dish_name_list.append(dish_name_for_list)

    context = {
        'dish_name': dish_name,
        'recipe': recipe,
        'servings': servings,
        'dish_name_list': dish_name_list,
    }
    return render(request, 'calculator/index.html', context)
