"""

test_slab.py

Author: Jordan Mirocha
Affiliation: University of Colorado at Boulder
Created on: Sun May 10 13:51:54 MDT 2015

Description: 

"""

import ares
import matplotlib.pyplot as pl

sim = ares.simulations.RaySegment(problem_type=3.1, initial_timestep=1e-15,
    epsilon_dt=0.0001, grid_cells=256, isothermal=1, tables_dlogN=[0.01])
sim.run()

anl = ares.analysis.RaySegment(sim)

ax1 = anl.RadialProfile('Tk', t=[0], color='k')
anl.RadialProfile('Tk', t=[1,5,15], ax=ax1, color='b', ls='--', lw=4)

ax2 = anl.RadialProfile('h_1', t=[0], fig=2, color='k')
anl.RadialProfile('h_1', t=[1,5,15], color='b', ax=ax2, ls='--', lw=4)

