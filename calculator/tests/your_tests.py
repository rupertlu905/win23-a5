#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
# Checks that the program outputs "1" for an input of "5 - 4"
assert run("5 - 4").output == "1"
# Checks that the program outputs "2" for an input of "8 / 4"
assert run("8 / 4").output == "2"
# Checks that the program exits successfully (no error) for input "5 - 4"
assert run("5 - 4").exit_status == 0
# Checks that the program fails (correctly errors) for input "4 & 8"
assert run("4 & 8").exit_status != 0

print("All tests passed!")
