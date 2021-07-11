from typing import List
from Coffee_Machine.components.Outlet import Outlet


class Coffee_Machine:

    def __init__(self, outlet_count: int) -> None:
        self.outlets = []
        self.item_counter = 0
        for i in range(outlet_count):
            self.outlets.append(Outlet(i))

    def prepare(self, item_list: List[str]):
        
        for outlet in self.outlets:
            while self.item_counter < len(item_list) and outlet.get_ingredients is False:
                self.item_counter += 1

    def 
