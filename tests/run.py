
from Coffee_Machine import Coffee_Machine

input_sample = {
    "machine": {
        "outlets": {"count_n": 3},
        "beverages": {
            "hot_tea": {
                "hot_milk": 100,
                "hot_water": 200,
                "sugar_syrup": 10,
                "ginger_syrup": 10,
                "tea_leaves_syrup": 30,
            },
            "black_tea": {
                "hot_water": 300,
                "sugar_syrup": 50,
                "ginger_syrup": 30,
                "tea_leaves_syrup": 30,
            },
            "green_tea": {
                "hot_water": 100,
                "sugar_syrup": 50,
                "ginger_syrup": 30,
                "green_mixture": 30,
            },
            "hot_coffee": {
                "hot_milk": 400,
                "hot_water": 100,
                "sugar_syrup": 50,
                "ginger_syrup": 30,
                "tea_leaves_syrup": 30,
            },
        },
        "total_items_quantity": {
            "hot_milk": 500,
            "hot_water": 500,
            "sugar_syrup": 100,
            "ginger_syrup": 100,
            "tea_leaves_syrup": 100,
        },
    }
}

Coffee_Machine.run(input_sample)
