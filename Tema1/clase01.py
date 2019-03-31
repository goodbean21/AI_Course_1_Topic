# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:24:28 2018
Este un programa para testear Open AI 
@author: Usuario
"""

import gym

environment = gym.make("SpaceInvaders-v0") # Instancia del juego
environment.reset() # Limpia el entorno del VG para la toma de decisiones

for _ in range(2000):
    environment.render() # Pintar en pantalla la acción
    environment.step(environment.action_space.sample()) # Toma de decisión - Aleatoria
    
environment.close() # Terminar la sesión