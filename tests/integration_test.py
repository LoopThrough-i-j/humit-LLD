import os
import sys

sys.path.append(os.getcwd())
import contextlib
import difflib

from Coffee_Machine import Coffee_Machine


class Integration_Test:
    def run_machine(self, test_id, input_sample, file_name):
        def diff(out, res):
            return "\n" + "\n".join(
                [
                    line
                    for line in difflib.unified_diff(
                        out, res, fromfile="output ", tofile="expected ", lineterm=""
                    )
                ]
            )

        with open(f"tests/output/{file_name}", "w") as o:
            with contextlib.redirect_stdout(o):
                Coffee_Machine.run(input_sample)
        with open(f"tests/output/{file_name}", "r") as o, open(
            f"tests/success/{file_name}", "r"
        ) as r:
            out = o.readlines()
            exp = r.readlines()
            assert out == exp, file_name + diff(out, exp)
        
        print(f"Test {test_id} Successfull")

    def test_1(self) -> None:
        inp_sample = {
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
        self.run_machine(1, inp_sample, "test1")
        

    def test_2(self) -> None:
        inp_sample = {
            "machine": {
                "outlets": {"count_n": 1},
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
        self.run_machine(2, inp_sample, "test2")

    def test_3(self) -> None:
        inp_sample = {
            "machine": {
                "outlets": {"count_n": 1},
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
                "total_items_quantity": {},
            }
        }
        self.run_machine(3, inp_sample, "test3")

    def test_4(self) -> None:
        inp_sample = {
            "machine": {
                "outlets": {"count_n": 10},
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
        self.run_machine(4, inp_sample, "test4")

    def test_5(self) -> None:
        inp_sample = {
            "machine": {
                "outlets": {"count_n": 10},
                "beverages": {
                    "hot_tea": {
                        "hot_milk": 100,
                        "hot_water": 200,
                        "sugar_syrup": 10,
                        "ginger_syrup": 10,
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
                    "black_tea": {
                        "hot_water": 300,
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
        self.run_machine(5, inp_sample, "test5")

    @staticmethod
    def run():
        I = Integration_Test()
        I.test_1()
        I.test_2()
        I.test_3()
        I.test_4()
        I.test_5()


if __name__ == "__main__":
    Integration_Test.run()
