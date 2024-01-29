from colorama import init
from termcolor import colored

init()

argument = None

def error(message:str):
        print(colored("❌: " + message, "red"))
    
def warn(message:str):
    print(colored("⚠️: " + message, "yellow"))

def success(message:str):
    print(colored("✅: " + message, "green"))

def info(message:str):
    print(colored("ℹ️: ", "blue") + message)

def ask(message:str):
    data = input(colored(message, "magenta"))
    return data

def debug(message:str):
    if argument == "-d":
        print(colored("🪲: " + message, "grey"))

def inline(message:str):
    print(message, end="\r")