import os

"""
Intermediate script for running subset script
"""
path = os.getcwd().replace(" ", "\ ")
os.system(f"python {path}/subset_script.py")
