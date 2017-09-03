"""
Author: JiaHui (Jeffrey) Lu
Student ID: 25944800
"""
import numpy as np
import matplotlib.pyplot as plt

def parse_coordinates(file_name):
    file = open(file_name).readlines()
    print(file)

parse_coordinates("A.pdb")