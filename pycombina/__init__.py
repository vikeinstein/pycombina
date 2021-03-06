#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This file is part of pycombina.
#
# Copyright 2017-2018 Adrian Bürger, Clemens Zeile, Sebastian Sager, Moritz Diehl
#
# pycombina is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pycombina is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pycombina. If not, see <http://www.gnu.org/licenses/>.

import os

try:

    if os.environ["PYCOMBINA_PROMPTS_SHOWN"] == "True":
        
        prompt_init_message = False

except KeyError:
    
    os.environ["PYCOMBINA_PROMPTS_SHOWN"] = "True"
    prompt_init_message = True
            
if prompt_init_message:

    print("\n-----------------------------------------------------------")
    print("|                                                         |")
    print("|                     You are using                       |")
    print("|                                                         |")
    print("|                       pycombina                         |")
    print("|                                                         |")
    print("|     A collection of methods for binary approximation    |")
    print("|       by A. Buerger, C. Zeile, S. Sager, M. Diehl       |")
    print("|                                                         |")
    print("-----------------------------------------------------------\n")


from ._binary_approximation import BinApprox

try:
    import gurobipy

    if gurobipy.gurobi.version() < (8, 0, 0):
        raise ImportError

    from ._combina_milp import CombinaMILP
except ImportError:
    print("- gurobipy version > 8.0.0 not found, CombinaMILP disabled.\n")

try:
    from ._combina_bnb import CombinaBnB
except ImportError:
    print("- BnB solver extension not found, CombinaBnB disabled.\n")

try:
    from ._combina_sur import CombinaSUR
except ImportError:
    print("- Sum-Up-Rounding solver extension not found, CombinaSUR disabled.\n")
