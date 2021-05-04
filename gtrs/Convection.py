# -*- coding: utf-8 -*-
r"""Thermal convection

This exports: 

  -

This depends on:

  -  

Examples of usage:

  - default usage:

    compute velocity in a convectioning cell heated from basal

        python -m gtrs.Convection compute_cell_velocity -b 700e3 -T 1673 -d 3300 -e 1e21

descriptions
""" 
import numpy as np
import sys, os, argparse
# import json, re
# import pathlib
# import subprocess
from math import pi
# from matplotlib import cm
from matplotlib import pyplot as plt

# directory to the aspect Lab
ASPECT_LAB_DIR = os.environ['ASPECT_LAB_DIR']
RESULT_DIR = os.path.join(ASPECT_LAB_DIR, 'results')
# directory to shilofue
shilofue_DIR = os.path.join(ASPECT_LAB_DIR, 'shilofue')


def BasalRa(D, dT, rho_0, g, alpha, kappa, eta):
    '''
    compute rayleigh number, from basal heating
    Inputs:
        -
    Returns:
        -
    '''
    return alpha * rho_0 * dT * g * D**3.0 / (kappa * eta)


def BasalCellVelocity(b, dT, rho_0, eta, **kwargs):
    '''
    compute the approximate scale of velocity in a convection cell by basal heating
    Inputs:
        -
    Returns:
        -
    '''
    aspect_ratio = kwargs.get('aspect_ratio', 1)
    kappa = kwargs.get('kappa', 1e-6)
    alpha = kwargs.get('alpha', 3e-5)
    g = kwargs.get('g', 10.0)
    Ra = BasalRa(b, dT, rho_0, g, alpha, kappa, eta)
    # T&S eq 6.362, aspect_ratio = lambda / (2*b)
    velocity = kappa / b * aspect_ratio**(7.0/3.0) / (1 + aspect_ratio**4.0)**(2.0/3.0) * (Ra / (2 * pi**0.5))**(2.0/3.0)
    return velocity


def main():
    '''
    main function of this module
    Inputs:
        sys.arg[1](str):
            commend
        sys.arg[2, :](str):
            options
    '''
    _commend = sys.argv[1]
    # parse options
    parser = argparse.ArgumentParser(description='Parse parameters')
    parser.add_argument('-i', '--inputs', type=str,
                        default='',
                        help='Some inputs')
    parser.add_argument('-b', '--vertical_extent', type=float,
                        default=0.0,
                        help='vertical_extent')
    parser.add_argument('-T', '--temperature_scaling', type=float,
                        default=0.0,
                        help='temperature/temperature difference')
    parser.add_argument('-d', '--reference_density', type=float,
                        default=0.0,
                        help='reference_density')
    parser.add_argument('-e', '--reference_viscosity', type=float,
                        default=0.0,
                        help='reference_viscosity')
    _options = []
    try:
        _options = sys.argv[2: ]
    except IndexError:
        pass
    arg = parser.parse_args(_options)

    # commands
    if _commend == 'compute_cell_velocity':
        # example:
        velocity = BasalCellVelocity(arg.vertical_extent, arg.temperature_scaling, arg.reference_density, arg.reference_viscosity)
        yr_to_s = 365*24*3600
        print("Analytic solution of velocity in convection cell is: %.4e (m/s), %.4e (cm/yr)" % (velocity, velocity * yr_to_s * 100))

# run script
if __name__ == '__main__':
    main()