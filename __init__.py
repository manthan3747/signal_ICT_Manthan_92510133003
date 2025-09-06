"""
Signal ICT Manthan Package
==========================

A comprehensive Python package for signal generation and operations 
in Digital Signal Processing (DSP) and Signals & Systems.

Author: Manthan
Enrollment: 92510133003

Modules:
--------
- unitary_signals: Unit step, impulse, and ramp signals
- trigonometric_signals: Sine, cosine, and exponential signals  
- operations: Time shifting, scaling, addition, multiplication

Example Usage:
--------------
>>> import numpy as np
>>> from signal_ICT_Manthan_92510133003 import unitary_signals
>>> n = np.arange(-5, 6)
>>> step = unitary_signals.unit_step(n)
"""

__version__ = "1.0.0"
__author__ = "Manthan"
__email__ = "manthandobariya3747@gmail.com"
__enrollment__ = "92510133003"

# Import all modules for easy access
from . import unitary_signals
from . import trigonometric_signals
from . import operations

# Define what gets imported with "from package import *"
__all__ = [
    'unitary_signals',
    'trigonometric_signals', 
    'operations',
    '__version__',
    '__author__',
    '__enrollment__'
]