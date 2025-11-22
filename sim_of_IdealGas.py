#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# setting const
N_PARTICLES = 100
BOX_SIZE = 10.0
DT = 0.05 # Time increments
STEPS = 200 

class IdealGasSim:
	def __init__(self):
		self.positions = np.random.rand(N_PARTICLES, 2) * BOX_SIZE
		self.velocities = np.random.randn(N_PARTICLES, 2)
		
		self.fig, self.ax = plt.subplots()
		self.ax.set_xlim(0, BOX_SIZE)
		self.ax.set_ylim(0, BOX_SIZE)
		self.particles, = self.ax.plot([], [], 'bo', ms=5)
		self.temp_text = self.ax.text(0.5, 1.02, '', transform=self.ax.transAxes, ha='center')
	
	def step(self, frame):
		# Dynamics
		self.positions += self.velocities * DT

		# Bounce 
		for i in range(2):
			hit_lower = self.positions[:, i] < 0
			self.positions[hit_lower, i] *= -1	
			self.velocities[hit_lower, i] *= -1
			
			hit_upper = self.positions[:, i] > BOX_SIZE
			self.positions[hit_upper, i] = 2*BOX_SIZE - self.positions[hit_upper, i]
			self.velocities[hit_upper, i] *= -1

		# Thermodynamics
		v_squared = np.sum(self.velocities**2, axis=1)
		total_kinetic_energy = 0.5 * 1.0 * np.sum(v_squared)
		# get T. <K>= (2/2) * kB * T cuz 2dim
		# T = <K> = (Total K) / N
		current_temp = total_kinetic_energy / N_PARTICLES 
		
		self.particles.set_data(self.positions[:, 0], self.positions[:, 1])
		self.temp_text.set_text(f'Temperature(T): {current_temp:.2f}')
		return self.particles, self.temp_text

if __name__ == "__main__":
	# simulation
	sim = IdealGasSim()
	ani = animation.FuncAnimation(sim.fig, sim.step, frames=STEPS, interval=50, blit=True)
	plt.show()
