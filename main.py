# import numpy as np
# import matplotlib.pyplot as plt
# from unitary_signals import unit_step, unit_impulse, ramp_signal
# from trigonometric_signals import sine_wave, cosine_wave
# from operations import time_shift, signal_addition, signal_multiplication

# # 1. Generate and plot unit step & unit impulse
# n = np.arange(-10, 10, 1)
# step = unit_step(n)
# impulse = unit_impulse(n)

# # 2. Generate sine wave (A=2, f=5Hz, phi=0, t=0..1 sec)
# t = np.linspace(0, 1, 500)
# sine = sine_wave(2, 5, 0, t)

# # 3. Perform time shifting on sine wave by +5 units
# shifted_sine = time_shift(sine, 5)
# plt.plot(sine, label="Original Sine")
# plt.plot(shifted_sine, label="Shifted Sine (+5)")
# plt.legend()
# plt.title("Time Shifting")
# plt.show()

# # 4. Add unit step and ramp signal
# ramp = ramp_signal(n)
# added = signal_addition(step, ramp)
# plt.stem(n, added, use_line_collection=True)
# plt.title("Addition: Unit Step + Ramp")
# plt.show()

# # 5. Multiply sine and cosine of same frequency
# cosine = cosine_wave(2, 5, 0, t)
# multiplied = signal_multiplication(sine, cosine)
# plt.plot(t, multiplied)
# plt.title("Multiplication: Sine * Cosine")
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from signal_ICT_Manthan_92510133003 import unitary_signals, trigonometric_signals, operations

# --- 1. Generate and plot unit step & unit impulse ---
n = np.arange(-10, 10)
step = unitary_signals.unit_step(n)
impulse = unitary_signals.unit_impulse(n)

# --- 2. Generate sine wave ---
t = np.linspace(0, 1, 500)
sine = trigonometric_signals.sine_wave(2, 5, 0, t)
cosine = trigonometric_signals.cosine_wave(2, 5, 0, t)

# --- 3. Time shifting sine wave ---
shifted_sine = operations.time_shift(sine, 5)
plt.figure()
plt.plot(t, sine, label="Original Sine")
plt.plot(t, shifted_sine, label="Shifted Sine (+5)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Time Shifting")
plt.legend()
plt.grid(True)
plt.show()

# --- 4. Add unit step and ramp ---
ramp = unitary_signals.ramp_signal(n)
added = operations.signal_addition(step, ramp)
plt.figure()
plt.stem(n, added)
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Addition: Unit Step + Ramp")
plt.grid(True)
plt.show()

# --- 5. Multiply sine and cosine ---
multiplied = operations.signal_multiplication(sine, cosine)
plt.figure()
plt.plot(t, multiplied)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Multiplication: Sine * Cosine")
plt.grid(True)
plt.show()