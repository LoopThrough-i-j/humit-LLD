import asyncio

from components.Store import Store
from lib.color_codes import *
from lib.Exceptions import *


class Outlet:
    """
    This is the outlet of a coffee machine.
    """

    def __init__(self, id: int) -> None:
        self.recipe = None
        self.id = id
        self.isBusy = False

    def get_ingredients(self, recipe_name: str, store: Store):
        try:
            self.recipe = store.fetch_recipe(recipe_name)
            assert self.recipe is not None, "Recipe not valid"
            ingreds = self.recipe.ingredients
            for ingred_id in ingreds:
                store.get_ingredient(ingred_id, ingreds[ingred_id])

            self.isBusy = True
            print(OKBLUE + f"preparing {self.recipe.name}" + ENDC)
            return True
        except (AssertionError, IngredientOutOfStock, IngredientNotFound) as e:
            print(FAIL + str(e) + ENDC)
        except Exception as e:
            pass
        print(OKCYAN + f"{self.recipe.name} cannot be prepared" + ENDC)
        return False

    async def prepare(self):
        await asyncio.sleep(2)
        self.isBusy = False
        print(OKGREEN + f"{self.recipe.name} prepared" + ENDC)
