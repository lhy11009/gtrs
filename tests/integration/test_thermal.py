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
    # check values
    assert(abs(T[1,1]-560.539702)<1e-5)
    assert(abs(T[50,50]-1505.5986503)<1e-5)
    # plot figure with pcolor
    filename = os.path.join(test_dir, 'half_space_cooling.png')
    if os.path.isfile(filename):
        os.remove(filename)
    fig, ax = plt.subplots()
    h = ax.pcolormesh(tt/seconds_in_year/1e6,zz/1e3,T, shading='auto')
    ax.set_xlabel('Time (Myr)') 
    ax.set_ylabel('Depth (km)')
    plt.gca().invert_yaxis() # gca is a function that returns a 'handle' to the current axes
    plt.colorbar(h, label='T (K)', ax=ax)
    # save figure
    fig.savefig(filename)
    assert(os.path.isfile(filename))
    pass


def test_TemperaturePeriodicChange():
    '''
    Test periodic change temperature
    '''
    # make the mesh
    seconds_in_year = 3.15e7  # 3.15*10**7
    z = np.linspace(0,10.0,100) # list of depth values, in m
    t = np.linspace(0,5.0*seconds_in_year,200) # list of t values
    # print these out on your own to see what happens:
    tt,zz = np.meshgrid(t,z)

    # assign values to the variables
    T0 = 300.0  # surface temperature, K
    dT = 10.0 # Temperature change in model, K
    omega = 2 * np.pi / seconds_in_year  # w = 2 * pi / T, s^(-1), T equals 1 year
    kappa = 1e-6  # m^2 / s

    # call function
    T = Thermal.TemperaturePeriodicChange(T0, dT, tt, omega, zz, kappa=kappa)

    # check values
    assert(abs(T[1,1]-309.609289893017)<1e-5)
    assert(abs(T[50,50]-302.02889455036365)<1e-5)
    
    # plot figure with pcolor
    filename = os.path.join(test_dir, 'temperature_periodic_change_T_minus_T0.png')
    if os.path.isfile(filename):
        os.remove(filename)
    fig, ax = plt.subplots()
    h = ax.pcolormesh(tt/seconds_in_year/1e6,zz/1e3,T-T0, shading='auto')
    ax.set_xlabel('Time (Myr)') 
    ax.set_ylabel('Depth (km)')
    plt.gca().invert_yaxis() # gca is a function that returns a 'handle' to the current axes
    plt.colorbar(h, label='T (K)', ax=ax)
    # save figure
    fig.savefig(filename)
    assert(os.path.isfile(filename))
    pass