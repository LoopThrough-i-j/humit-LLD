from Coffee_Machine.components.Store import Store
from time import sleep

class Outlet:
    """
    This is the outlet of a coffee machine.
    """
    def __init__(self, store: Store, id: int) -> None:
        self.recipe = None
        self.id = id
        self.isBusy = False
        self.store = store

    def get_ingredients(self, recipe_name: str):
        try:
            self.recipe = self.store.fetch_recipe(recipe_name)
            assert self.recipe is not None, "Recipe not valid"
            ingreds = self.recipe.ingredients
            for ingred_id in ingreds:
                self.store.get_ingredient(ingred_id, ingreds[ingred_id])
            
            self.isBusy = True
            return True
        except:
            pass
        return False
    
    def prepare(self):
        sleep(10)
        self.isBusy = False
