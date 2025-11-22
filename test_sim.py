import matplotlib
matplotlib.use('Agg') # Use non-interactive backend for testing
import sys
import os
sys.path.append(os.getcwd())
from sim_of_IdealGas import IdealGasSim

try:
    sim = IdealGasSim()
    sim.step(0)
    print("Test Passed: Simulation step ran without error.")
except Exception as e:
    print(f"Test Failed: {e}")
    exit(1)
