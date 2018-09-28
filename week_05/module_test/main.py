# from week_05.module_alex import say_hello

__author__ = "Alex Li"

# module_alex=all_code   module_alex.name module_alex.logger()
import os
import sys

x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(x)

import module_alex

print(sys.path)



print(sys.path)

module_alex.say_hello()
