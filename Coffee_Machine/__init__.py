import asyncio
from typing import Any, Dict, List, Tuple

from Coffee_Machine.components.Outlet import Outlet
from Coffee_Machine.components.Store import Store


class Coffee_Machine:
    """
    The Coffee_Machine is responsible for interacting with the user
    """

    def __init__(self, outlet_count: int) -> None:
        """
        Initializes the store and the list of Outlets for the Coffee_Machine
        Params
        ------
        outlet_count: int
            Number of Outlets of the Coffee_Machine
        """
        self.outlets = []
        self.item_counter = 0
        self._store = Store()
        for i in range(outlet_count):
            self.outlets.append(Outlet(i))

    async def prepare(self, bev_list: List[str]) -> None:
        """
        Prepares Beverages
        Params
        ------
        bev_list: List[str]
            List of names of the beverages
        """
        while bev_list:
            job_list = []
            for outlet in self.outlets:
                if self.item_counter >= len(bev_list):
                    break

                while self.item_counter < len(bev_list) and not outlet.get_ingredients(
                    bev_list[self.item_counter], self._store
                ):  # The while loop runs till we find an item that can be assigned to the current outlet
                    self.item_counter += 1
                else:
                    self.item_counter += 1
                # if outlet isBusy i.e. got the ingredients, it starts preparing
                if outlet.isBusy:
                    job_list.append(asyncio.create_task(outlet.prepare()))

            # Wait for all outlets to complete
            if job_list:
                await asyncio.wait(job_list)

            # Remove the beverages from the queue that are parsed
            bev_list = bev_list[self.item_counter :]
            self.item_counter = 0

    def add_ingredient(self, name: str, quantity: int) -> None:
        """
        Add ingredients to store
        Params
        ------
        name: str
            Name of the Ingredient
        quantity: int
            Quantity of Ingredient to be Added
        """
        self._store.add_ingredient(name, quantity)

    def add_recipe(self, name: str, ingreds: Dict[str, int]) -> None:
        """
        Add recipe to store
        Params
        ------
        name: str
            Name of the Recipe
        ingreds: List[Tuple[str, int]]
            List of Ingredients and quantity in a tuple
        """
        self._store.add_recipe(name, ingreds)

    @staticmethod
    def run(inp: Dict[str, Any]) -> None:
        machine: Dict[str, Any] = inp["machine"]
        num_outlets: int = machine["outlets"]["count_n"]
        beverages: Dict[str, Dict[str, int]] = machine["beverages"]
        total_items_quantity: Dict[str, int] = machine["total_items_quantity"]

        coffee_machine = Coffee_Machine(num_outlets)
        for item in total_items_quantity:
            coffee_machine.add_ingredient(item, total_items_quantity[item])
        for beverage in beverages:
            coffee_machine.add_recipe(beverage, beverages[beverage])
        asyncio.run(coffee_machine.prepare(list(beverages.keys())))
