# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:02:16 2019

@author: Abel Aguilar
"""

from gym import envs

envs_names = [env.id for env in envs.registry.all()]

for name in sorted(envs_names):
    print(name)
    
