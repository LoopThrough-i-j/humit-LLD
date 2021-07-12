from typing import Dict, List, Optional, Tuple

from lib.Exceptions import IngredientOutOfStock, InvalidIngredientQuantity


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

    def __init__(self, id: str, name: str, quantity: int) -> None:
        self.id = id
        self.name = name
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

    def __init__(self, id: str, name: str, ingredients: Dict[str, int]) -> None:
        self.id = id
        self.name = name
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

    def __init__(self) -> None:
        """
        Set ingredients and recipies in a store to empty
        """
        self.ingredients: Dict[str, Ingredient] = {}
        self.recipes: Dict[str, Recipe] = {}

    @staticmethod
    def name_to_id(name: str) -> str:
        """
        chnage name of an item to id
        """
        return name.replace(" ", "_").lower()

    def add_ingredient(self, name: str, quantity: int) -> Ingredient:
        """
        Add Ingredients to store
        Params
        ------
        name: str
            Name of Ingredient
        quantity: int
            Quantity of Ingrredient to be added to store
        Return
        ------
        Ingredient
            New Ingredient generated
        """
        if quantity < 0:
            raise InvalidIngredientQuantity()
        ing_id = Store.name_to_id(name)
        if ing_id in self.ingredients:
            self.ingredients[ing_id].quantity += quantity
        else:
            self.ingredients[ing_id] = Ingredient(ing_id, name, quantity)

        return self.ingredients[ing_id]

    def add_recipe(self, name: str, ingreds: Dict[str, int]) -> Recipe:
        """
        Add Recipe to store
        Params
        ------
        name: str
            Name of Recipe
        ingreds: Dict[str, int]
            Dict of Ingredients with name and quantity
        Return
        ------
        Recipe
            New Recipe generated
        """
        recipe_id = Store.name_to_id(name)
        recipe_name = name
        recipe_ingreds: Dict[str, int] = {}
        for ing_name in ingreds:
            ing_quan = ingreds[ing_name]
            ing_id = Store.name_to_id(ing_name)
            if ing_id not in self.ingredients:
                self.add_ingredient(ing_name, 0)
            recipe_ingreds[ing_id] = ing_quan
        self.recipes[recipe_id] = Recipe(recipe_id, recipe_name, recipe_ingreds)
        return self.recipes[recipe_id]

    def fetch_recipe(self, recipe_name: str) -> Optional[Recipe]:
        """
        Fetch Recipe from store
        Params
        ------
        recipie_name: str
            Name of Recipe
        Return
        ------
        Optional[Recipe]
            Recipie if found
        """
        recipe_id = Store.name_to_id(recipe_name)
        if recipe_id in self.recipes:
            return self.recipes[recipe_id]

    def get_ingredient(self, ingred_id: str, ingred_quant: int) -> None:
        """
        Get Ingredient from store, throws Exception if not found
        Params
        ------
        ingred_id: str
            Id of Ingredient
        ingred_quant: int
            Quantity of Ingredient
        """
        if ingred_quant < 0:
            raise InvalidIngredientQuantity()

        ingred = self.ingredients[ingred_id]
        if ingred.quantity < ingred_quant:
            raise IngredientOutOfStock(
                f"{ingred.name} running Low: {ingred.quantity} ml."
            )
        else:
            ingred.quantity -= ingred_quant
