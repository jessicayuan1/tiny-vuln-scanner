import os
import subprocess
import pickle

user_input = input("Enter command: ")
eval(user_input)  # risky
os.system(user_input)  # risky
subprocess.call(user_input, shell=True)  # risky

with open("data.pkl", "rb") as f:
    obj = pickle.load(f)  # risky

exec("print('hello world')")  # risky
