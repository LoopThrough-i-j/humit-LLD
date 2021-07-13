import os
import sys

sys.path.append(os.getcwd())
import contextlib
import difflib

from Coffee_Machine import Coffee_Machine


def run_machine(input_sample, file_name):

    with open(f"tests/output/{file_name}", "w") as o:
        with contextlib.redirect_stdout(o):
            Coffee_Machine.run(input_sample)
    with open(f"tests/output/{file_name}", "r") as o, open(
        f"tests/success/{file_name}", "r"
    ) as r:
        out = o.read()
        exp = r.read()
        return out, exp


def test_1() -> None:
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
    out, exp = run_machine(inp_sample, "test1")
    assert out == exp


def test_2() -> None:
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
    out, exp = run_machine(inp_sample, "test2")
    assert out == exp


def test_3() -> None:
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
    out, exp = run_machine(inp_sample, "test3")
    assert out == exp


def test_4() -> None:
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
    out, exp = run_machine(inp_sample, "test4")
    assert out == exp


def test_5() -> None:
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
    out, exp = run_machine(inp_sample, "test5")
    assert out == exp
