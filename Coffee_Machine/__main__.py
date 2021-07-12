import asyncio
from typing import List, Tuple

from components.Outlet import Outlet
from components.Store import Store
from lib.color_codes import *


class Coffee_Machine:
    def __init__(self, outlet_count: int) -> None:
        self.outlets = []
        self.item_counter = 0
        self._store = Store()
        for i in range(outlet_count):
            self.outlets.append(Outlet(i))

    async def prepare(self, item_list: List[str]):

        while item_list != []:
            for outlet in self.outlets:
                while (
                    self.item_counter < len(item_list)
                    and outlet.get_ingredients(
                        item_list[self.item_counter], self._store
                    )
                    is False
                ):
                    self.item_counter += 1
                else:
                    self.item_counter += 1

            job_list = []
            for outlet in self.outlets:
                if outlet.isBusy:
                    job_list.append(asyncio.create_task(outlet.prepare()))
            if job_list:
                await asyncio.wait(job_list)

            item_list = item_list[self.item_counter :]
            self.item_counter = 0

    def add_ingredient(self, name: str, quantity: int):
        self._store.add_ingredient(name, quantity)

    def add_recipe(self, name: str, ingreds: List[Tuple[str, int]]):
        try:
            self._store.add_recipe(name, ingreds)
        except Exception as e:
            print(FAIL + str(e) + ENDC)


if __name__ == "__main__":
    cm = Coffee_Machine(3)
    cm.add_ingredient("hot_milk", 700)
    cm.add_ingredient("hot_water", 700)
    cm.add_ingredient("sugar_syrup", 700)
    cm.add_ingredient("ginger_syrup", 700)
    cm.add_ingredient("tea_leaves_syrup", 700)

    cm.add_recipe(
        "hot_tea",
        [
            ("hot_milk", 100),
            ("hot_water", 200),
            ("sugar_syrup", 10),
            ("ginger_syrup", 10),
            ("tea_leaves_syrup", 30),
        ],
    )
    cm.add_recipe(
        "black_tea",
        [
            ("hot_water", 300),
            ("sugar_syrup", 50),
            ("ginger_syrup", 30),
            ("tea_leaves_syrup", 30),
        ],
    )
    # cm.add_recipe("green_tea", [("hot_water", 100),("sugar_syrup", 50),("ginger_syrup", 30),("green_mixture", 30)])
    cm.add_recipe(
        "hot_coffee",
        [
            ("hot_milk", 400),
            ("hot_water", 100),
            ("sugar_syrup", 50),
            ("ginger_syrup", 30),
            ("tea_leaves_syrup", 30),
        ],
    )

    asyncio.run(
        cm.prepare(
            ["hot_tea", "black_tea", "hot_coffee", "hot_tea", "black_tea", "hot_coffee"]
        )
    )
