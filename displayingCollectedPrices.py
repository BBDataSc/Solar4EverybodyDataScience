# This code will handle the collected prices and will add them to an aws repository

# imported packages
import pandas as pd
import numpy as np
import matplotlib as plt
from glob import glob


# variables
dataPageOne = []
dataPageTwo = []

main_file = "main.py"


# functions
def fetchFiles(files):
    x = dataPageOne  # add main file reference
    y = dataPageTwo  # add main_file reference
    plt.plot(files)
    return(x,y)


if __name__ == "__main__":
    data_x, data_y = fetchFiles(main_file)
    print(data_x, data_y)