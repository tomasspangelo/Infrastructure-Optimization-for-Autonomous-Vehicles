import os

"""
Intermediate script for running plot script
"""
path = os.getcwd().replace(" ", "\ ")
os.system(f"python {path}/plot.py")
