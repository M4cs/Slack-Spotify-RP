from colorama import Fore as f
from os import system, name

PROMPT = f.RED + "[" + f.BLUE + "SSRP" + f.RED + "] " + f.RESET

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

def info(message):
    print(PROMPT + f.GREEN + "INFO | " + f.RESET + message)
    
def error(message):
    print(PROMPT + f.RED + "ERROR | " + f.RESET + message)
    
def warning(message):
    print(PROMPT + f.YELLOW + "WARNING | " + f.RESET + message)
    
def prompt(message):
    print(PROMPT + message)
    
def show_music(message):
    clear()
    print(PROMPT + "Running SSRP v1.0.0")
    print(PROMPT + message)
    print(PROMPT + "Press Ctrl + C to Quit")