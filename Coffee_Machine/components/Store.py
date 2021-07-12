from typing import Dict, List, Tuple

from lib.color_codes import *
from lib.Exceptions import (
    IngredientNotFound,
    IngredientOutOfStock,
    InvalidIngredientQuantity,
)


class Ingredient:
    """
    The Ingredients in any Recipe.
    Params:
    -------
    id: str:
        Id of an ingredient
    name: str
        Name unique to every Ingredient
    quantity: int
        Quantity of an Ingredient in ml
    """

    def __init__(self, id: str, name: str, quantity: int):
        self.id = id
        self.name = name.title()
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"{self.id}: {self.quantity}\n"


class Recipe:
    """
    The Recipe of any beverage.

    Params:
    -------
    id: str:
        Id of a recipe
    name: str
        Name unique to every recipe
    Ingredients: Dict[str, int]
        A Map of Ingredient id and quantity in ml
    """

    def __init__(self, id: str, name: str, ingredients: Dict[str, int]):
        self.id = id
        self.name = name.title()
        self.ingredients = ingredients

    def __repr__(self) -> str:
        res = f"------------\n{self.id}. {self.name}:\n"
        for ing_id in self.ingredients:
            res += f"{ing_id}: {self.ingredients[ing_id]}\n"
        res += "------------"
        return res


class Store:
    """
    The Store is responsible for Holding and Supplying the Ingredients, and the Recipe.
    """

    def __init__(self):
        self.ingredients: Dict[str, Ingredient] = {}
        self.recipes: Dict[str, Recipe] = {}

    def name_to_id(self, name):
        return name.replace(" ", "_").lower()

    def add_ingredient(self, name: str, quantity: int):
        if quantity <= 0:
            raise InvalidIngredientQuantity()
        ing_id = self.name_to_id(name)
        if ing_id in self.ingredients:
            self.ingredients[ing_id].quantity += quantity
        else:
            self.ingredients[ing_id] = Ingredient(ing_id, name, quantity)

        return self.ingredients[ing_id]

    def add_recipe(self, name: str, ingreds: List[Tuple[str, int]]):
        recipe_id = self.name_to_id(name)
        recipe_name = name
        recipe_ingreds: Dict[str, int] = {}
        for ing_name, ing_quan in ingreds:
            ing_id = self.name_to_id(ing_name)
            if ing_id not in self.ingredients:
                raise IngredientNotFound(f"{ing_name} not Found in Store")
            if ing_id in recipe_ingreds:
                recipe_ingreds[ing_id] += ing_quan
            else:
                recipe_ingreds[ing_id] = ing_quan
        self.recipes[recipe_id] = Recipe(recipe_id, recipe_name, recipe_ingreds)
        return self.recipes[recipe_id]

    def fetch_recipe(self, recipe_name: str):
        recipe_id = self.name_to_id(recipe_name)
        if recipe_id in self.recipes:
            return self.recipes[recipe_id]

    def get_ingredient(self, ingred_id: str, ingred_quant: int):
        if ingred_quant <= 0:
            raise InvalidIngredientQuantity()
        if ingred_id in self.ingredients:
            ingred = self.ingredients[ingred_id]
            if ingred.quantity < ingred_quant:
                raise IngredientOutOfStock(
                    f"{ingred.name} running Low: {ingred.quantity} ml."
                )
            else:
                ingred.quantity -= ingred_quant
            return ingred_quant
        else:
            raise IngredientNotFound(f"{ingred_id} not Found in Store")
