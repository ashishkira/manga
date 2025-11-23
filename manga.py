import numpy as np
import pandas as pd
import os
import random as rnd

def open_file():
    if not os.path.exists("data/data.csv"):
        print("file not found")
        return
        
    else:
        try:
            return pd.read_csv("data/data.csv")
        except:
            return

def creat_command(data):
    for seed in data["code number"]:
        command = f'start chrome --profile-directory="Profile 1" "https://hentaifox.com/gallery/{seed}/"'
        list.add(command)
                
    return list

def select_n_tab(smp, num):
    n_tab = rnd.sample(sorted(smp), num)
    return n_tab

def open_tab(tab):
    for x in tab:
        os.system(x)


list = {f'"start chrome --profile-directory="Profile 1" "https://hentaifox.com/""',}

def main():
    data = open_file()
    food = creat_command(data)
    number = int(input("enter number of tab : "))
    n_number_tab = select_n_tab(food, number)
    open_tab(n_number_tab)


if __name__ == "__main__":
    main()