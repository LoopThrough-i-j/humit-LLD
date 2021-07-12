import asyncio

from Coffee_Machine.components.Store import Store
from Coffee_Machine.lib.color_codes import ENDC, FAIL, OKBLUE, OKCYAN, OKGREEN
from Coffee_Machine.lib.Exceptions import IngredientNotFound, IngredientOutOfStock


class Outlet:
    """
    This is the outlet of a coffee machine.
    """

    def __init__(self, id: int) -> None:
        """
        Initializes with no recipe, isBuzy False and the counter id
        Params
        ------
        id: int
            Id of Outlet
        """
        self.recipe = None
        self.id = id
        self.isBusy = False

    def get_ingredients(self, recipe_name: str, store: Store) -> bool:
        """
        Initializes with no recipe, isBuzy False and the counter id
        Params
        ------
        recipe_name: str
            Name of Recipe
        store: Store
            Instance of Current Store
        Return
        ------
        bool
            Successfully got the Ingredients or not
        """
        try:
            # Fetch recipe and set it to current recipe
            self.recipe = store.fetch_recipe(recipe_name)
            assert self.recipe is not None, "Recipe not valid"
            ingreds = self.recipe.ingredients
            store.get_ingredients(ingreds)
            # If fetching ingredients is successfull set Outlet to busy
            self.isBusy = True
            print(OKBLUE + f"preparing {self.recipe.name}" + ENDC)
            return True
        except (AssertionError, IngredientOutOfStock, IngredientNotFound) as e:
            print(FAIL + str(e) + ENDC)
        except Exception as e:
            pass
        print(OKCYAN + f"{recipe_name} cannot be prepared" + ENDC)
        self.recipe = None
        return False

    async def prepare(self) -> None:
        """
        Simulate preparation, with preparation time as 5 sec.
        """
        await asyncio.sleep(5)
        self.isBusy = False
        assert self.recipe is not None
        print(OKGREEN + f"{self.recipe.name} prepared" + ENDC)
