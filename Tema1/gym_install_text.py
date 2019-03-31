# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:04:57 2019

@author: Usuario
"""

import gym

environment = gym.make("MountainCar-v0")
environment.reset()

for _ in range(2000):
    environment.render()
    environment.step(environment.action_space.sample())
    
environment.close() 