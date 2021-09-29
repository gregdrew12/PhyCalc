import random
import numpy as np

variable_list = []
formula_dict = {
    ''.join(sorted(['x', 'x0', 'v', 't'])): "x = x0 + vt",
    ''.join(sorted(['s', 'd', 't'])): "s = d/t",
    ''.join(sorted(['v', 'v0', 'a', 't'])): "v = v0 + at",
    ''.join(sorted(['x', 'x0', 'v0', 't', 'a'])): "x = x0 + v0t + at^2/2",
    ''.join(sorted(['v', 'v0', 'a', 'x', 'x0'])): "v^2 = v0^2 + 2a(x - x0)",
    ''.join(sorted(['x', 'x0', 't', 'v', 'v0'])): "x = x0 + t(v + v0)/2",
    ''.join(sorted(['x', 'x0', 'v', 't', 'a'])): "x = x0 + vt - at^2/2",
    ''.join(sorted(['a', 'g'])): "a = -g",
    ''.join(sorted(['v', 'v0', 'g', 't'])): "y = y0 - gt",
    ''.join(sorted(['y', 'y0', 'v0', 't', 'g'])): "y = y0 + v0t - gt^2/2",
    ''.join(sorted(['Opp', 'Hyp', 'Θ'])): "Opp = Hyp*sinΘ",
    ''.join(sorted(['Adj', 'Hyp', 'Θ'])): "Adj = Hyp*cosΘ",
    ''.join(sorted(['Opp', 'Adj', 'Θ'])): "Opp = Adj*tanΘ",
    ''.join(sorted(['Opp', 'Hyp', 'Θ'])): "Opp = Hyp*sinΘ",
    ''.join(sorted(['Opp', 'Hyp', 'Θ'])): "Opp = Hyp*sinΘ",
    ''.join(sorted(['Opp', 'Hyp', 'Θ'])): "Opp = Hyp*sinΘ",
    ''.join(sorted(['Opp', 'Hyp', 'Θ'])): "Opp = Hyp*sinΘ",
    ''.join(sorted(['Opp', 'Hyp', 'Θ'])): "Opp = Hyp*sinΘ"
    }

given = input("Input given variables: ")
unkown = input("Input unkown variable: ")
given_list = given.split(" ")
variable_list = sorted((given + " " + unkown).split(" "))
print(variable_list)
print(formula_dict[''.join(variable_list)])