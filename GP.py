import random
import numpy as np


class Tree(object):
    def __init__(self):
        self.Left = None
        self.Right = None
        self.state = None

# Chapter 4 solving the equation x^2 + x + 1

# Prep Steps

# Terminal Set
# T = {x,Reals}

# Function Set
# F = {+,-,*,%}
# % is protected division

# Fitness function
# Sum of absolute errors

# Run Parameters
# population size = 4
# 50% subtree crossover, 25% reproduction, 25% subtree mutation, no tree size limits

# Termination = individual w/ fitness < 0.1

parameters = {
    'pop_size':4,
    'crossover':0.5,
    'reproduction':0.25,
    'subtree_mutation':0.25
}

population = []

def choose_random_element(set_input):
    return set_input[np.random.randint(len(set_input))]

def generate_random_tree(func_set,term_set,max_d,method):

    if max_d == 0 or (method == 'grow' and random.random() < len(term_set)/(len(term_set) + len(func_set))):
        expr = choose_random_element(term_set)

    else:
        func = choose_random_element(func_set)

def init_pop():

    for i in range(parameters['pop_size']):

        program = True()
