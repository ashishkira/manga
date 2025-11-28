import numpy as np
import pandas as pd
import os
import random as rnd
import time
import subprocess



def creat_command(data, list):
    for num in data:
        command = f'start chrome --profile-directory="Profile 1" "file:///C:/Users/Ashish_kira/Videos/SHIT/manga/{num:02}/main.html"'
        list.add(command)
    return list

def select_n_tab(smp):
    n_tab = rnd.sample(sorted(smp), 1)
    return n_tab

def open_tab(tab, log, num):
    
    if tab[0] in log:
        print("not opened")
        return num
    else:
        os.system(tab[0])
        print("opened")
        log.add(tab[0])
        num += 1
        return num
    
def if_com(com):
    if com == 100:
        return False
    else:
        return True

def main():
    list = {f'"start chrome --profile-directory="Profile 1" "https://hentaifox.com/""',}
    log_stored ={"00"}
    num_meter = 0
    data = range(0,99)
    run = True
    raw_command = creat_command(data, list)
    while run:
        print(num_meter)
        # number_oftab = int(input("enter number : "))
        final_commands = select_n_tab(raw_command)
        num_meter = open_tab(final_commands, log_stored, num_meter)
        run = if_com(num_meter)
        time.sleep(5)
        subprocess.run([
            "powershell",
            "Get-Process chrome | ForEach-Object { $_.CloseMainWindow() }"
        ])


    
    
    
    
    

if __name__ == "__main__":
    
    main()