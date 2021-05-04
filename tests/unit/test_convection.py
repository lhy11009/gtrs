# -*- coding: utf-8 -*-
r"""Test for Convection.py

This outputs:

  - test results to value of variable "test_dir"

This depends on:

  - source files written from the value of "source_dir"

Examples of usage:

  - default usage:

        python -m pytest test_foo.py

descriptions:
    every function is a separate test, combined usage with pytest module
""" 


import os
# import pytest
# import filecmp  # for compare file contents
# import numpy as np
from gtrs.Convection import *  # import test module
# from shilofue.Utilities import 
# from matplotlib import pyplot as plt
# from shutil import rmtree  # for remove directories

test_dir = ".test"
source_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'parse')


if not os.path.isdir(test_dir):
    # check we have the directory to store test result
    os.mkdir(test_dir)


def test_basal_ra():
    '''
    test the function of compute rayleigh number
    Asserts:
    '''
    tolerance = 1e-6

    # values from Zhang & ZHong 2010? paper, but I haven't got there
    # value for dT and eta
    # also note that there computation uses R, rather than D, so there value is 8-9
    # times bigger.
    D = 2890e3
    dT = 1673.0  # value for earth ?
    kappa = 1e-6
    alpha = 2e-5
    g = 9.8
    rho_0 = 3300
    eta = 1e21
    Ra_std = 2.61191765e9
    Ra = BasalRa(D, dT, rho_0, g, alpha, kappa, eta)
    assert((Ra - Ra_std)/Ra_std < tolerance)


    
# notes
    
# to check for error message
    # with pytest.raises(SomeError) as _excinfo:
    #    foo()
    # assert(r'foo' in str(_excinfo.value))

# assert the contents of file
    # assert(filecmp.cmp(out_path, std_path))

