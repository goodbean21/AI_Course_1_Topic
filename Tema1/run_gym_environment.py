# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:34:34 2019

@author: Usuario
"""

import gym

## ArgV 1st value: name of the environment
environment = gym.make("Qbert-v0")
MAX_NUM_EPISODES = 10
MAX_STEPS_PER_EPISODES = 500

for episode in range(MAX_NUM_EPISODES):
    obs = environment.reset() # Primer instancia del entorno
    
    for step in range(MAX_STEPS_PER_EPISODES):
        environment.render()
        action = environment.action_space.sample() # Decision Aleatoria
        
        # Environment step retorna 4 valores:
        # x.step(arg) = { 
            # Next_State    -> Object,
            # Reward        -> float, 
            # Done          -> bool, 
            # Info          -> Dictionary
        # }
        
        next_state, reward, done, info = environment.step(action)
        obs = next_state
        
        if done or step == (MAX_STEPS_PER_EPISODES - 1):
            print("\n Episodes #{} terminado en {} steps".format(episode,step+1))
            break     
    
environment.close()
