import os
import numpy as np
import matplotlib.pyplot as plt
import gtrs.Thermal as Thermal

# File path
test_dir = '.test'
if not os.path.isdir(test_dir):
    os.mkdir(test_dir)
# test_source_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'test-plot')
# assert(os.path.isdir(test_source_dir)

# todo
def test_HalfSpaceT():
    '''
    Test halfspace temperature
    '''
    # constants
    seconds_in_year = 3.15e7
    T1 = 1600.
    T0 = 300.
    kappa = 1e-6
    # construct query array
    z = np.linspace(0,100e3,100) # list of depth values, in m
    t = np.linspace(0,50e6*seconds_in_year,200) # list of t values
    tt,zz = np.meshgrid(t,z)
    # get values at query points
    T = Thermal.HalfSpaceT(T0, T1, tt, zz, kappa=kappa)
    # plot figure with pcolor
    fig, ax = plt.subplots()
    h = ax.pcolormesh(tt/seconds_in_year/1e6,zz/1e3,T, shading='auto')
    ax.set_xlabel('Time (Myr)') 
    ax.set_ylabel('Depth (km)')
    plt.gca().invert_yaxis() # gca is a function that returns a 'handle' to the current axes
    plt.colorbar(h, label='T (K)', ax=ax)
    # save figure
    filename = os.path.join(test_dir, 'half_space_cooling.png')
    fig.savefig(filename)
    pass