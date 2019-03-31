# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:08:01 2019

@author: Usuario
"""

import gym
from gym.spaces import *
import sys

# Tipo de espacios de acción

# BOX -> R^n {x1, x2, x3, ... xn}, xi{low, high}
# gym.spaces.box(low = -10, high = 10, shape = {2,})

# Discrete -> Numeros enteros entre 0 y n-1, {0, 1, 2, ..., n-1}
# gym.spaces.Discrete(5)

# Dict -> Diccionario de espacios más complejos
# gym.spaces.Dict({
#        "position" : gym.spaces.Discrete(3),
#        "velocity" : gym.spaces.Discrete(2)
#        })

# Multi Binary -> (0, 1)^n, {x1, x2, x3, ..., xn}, xi{1, 0}
# gym.spaces.multi_binary(3) # {x, y, z} = T|F

# Multi Discrete -> {a1, a2, a3, ..., b}
# gym.spaces.multi_discrete({-10, 10}, {0, 1})

# Tuple -> Producto de espacios simples
# gym.spaces.Tuple(gym.spaces.Discrete(3), gym.spaces.discrete(2))

# PRNG -> Random Seeds

def print_spaces(space):
    print(space)
    if isinstance(space, Box):
        print("\n Cota inferior: ", space.low)
        print("\n Cota superior: ", space.high)

if __name__ == "__main__":
    environment = gym.make(sys.argv[1])
    print("Espacio de observaciones: ")
    print_spaces(environment.observation_space)
    print("Espacio de acciones: ")
    print_spaces(environment.action_space)
    try:
        print("Descripción de las acciones: ", environment.wrapped.get_action_meanings())
    except AttributeError:
        pass