# Signal ICT Manthan Package

A comprehensive Python package for signal generation and operations in Digital Signal Processing (DSP) and Signals & Systems courses.

## Author
**Manthan**  
Enrollment No: 92510133003

## Package Overview

This package provides three main modules for signal processing operations:

### 1. `unitary_signals.py`
- `unit_step(n)` - Generates unit step signal
- `unit_impulse(n)` - Generates unit impulse (delta) signal  
- `ramp_signal(n)` - Generates ramp signal

### 2. `trigonometric_signals.py`
- `sine_wave(A, f, phi, t)` - Generates sine wave
- `cosine_wave(A, f, phi, t)` - Generates cosine wave
- `exponential_signal(A, a, t)` - Generates exponential signal

### 3. `operations.py`
- `time_shift(signal, k)` - Time shifts signal by k units
- `time_scale(signal, k)` - Time scales signal by factor k
- `signal_addition(signal1, signal2)` - Adds two signals
- `signal_multiplication(signal1, signal2)` - Multiplies two signals

## Installation

### From Local Wheel File
```bash
pip install dist/signal_ICT_Manthan_92510133003-1.0.0-py3-none-any.whl
```

### From TestPyPI
```bash
pip install -i https://test.pypi.org/simple/ signal-ICT-Manthan-92510133003
```

### From Source
```bash
git clone https://github.com/yourusername/signal_ICT_Manthan_92510133003.git
cd signal_ICT_Manthan_92510133003
pip install .
```

## Dependencies

- numpy >= 1.20.0
- matplotlib >= 3.3.0

## Usage Examples

### Basic Signal Generation
```python
import numpy as np
from signal_ICT_Manthan_92510133003 import unitary_signals, trigonometric_signals

# Generate discrete signals
n = np.arange(-10, 10)
step = unitary_signals.unit_step(n)
impulse = unitary_signals.unit_impulse(n)

# Generate continuous signals
t = np.linspace(0, 1, 500)
sine = trigonometric_signals.sine_wave(2, 5, 0, t)  # A=2, f=5Hz, phi=0
```

### Signal Operations
```python
from signal_ICT_Manthan_92510133003 import operations

# Time shift
shifted = operations.time_shift(sine, 5)

# Signal arithmetic
added = operations.signal_addition(signal1, signal2)
multiplied = operations.signal_multiplication(sine, cosine)
```

## Building the Package

### 1. Build Distribution Files
```bash
python setup.py sdist bdist_wheel
```

### 2. Upload to TestPyPI
```bash
twine upload --repository testpypi dist/*
```

### 3. Upload to PyPI (Production)
```bash
twine upload dist/*
```

## Project Structure
```
signal_ICT_Manthan_92510133003/
├── signal_ICT_Manthan_92510133003/
│   ├── __init__.py
│   ├── unitary_signals.py
│   ├── trigonometric_signals.py
│   └── operations.py
├── dist/
│   ├── *.whl
│   └── *.tar.gz
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
├── main.py
└── manthan.py
```

## Features Demonstrated

✅ Unit step, impulse, and ramp signal generation  
✅ Sine, cosine, and exponential signal generation  
✅ Time shifting and scaling operations  
✅ Signal addition and multiplication  
✅ Comprehensive plotting with matplotlib  
✅ Modular package design  
✅ PyPI distribution ready  

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and add tests
4. Submit a pull request

## Support

For issues and questions:
- Open an issue on GitHub
- Contact: your.email@example.com

## Changelog

### Version 1.0.0
- Initial release
- Basic signal generation functions
- Signal operation functions
- Complete documentation
- PyPI distribution setup