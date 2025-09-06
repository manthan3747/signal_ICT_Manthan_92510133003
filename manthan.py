from signal_ICT_Manthan_92510133003 import unitary_signals, trigonometric_signals, operations
import numpy as np
import matplotlib.pyplot as plt

# --- Unitary signals ---
n1 = np.arange(-10, 10)   # Discrete index values
step = unitary_signals.unit_step(n1)
impulse = unitary_signals.unit_impulse(n1)
ramp = unitary_signals.ramp_signal(n1)

# --- Trigonometric signals ---
t = np.linspace(0, 1, 500)  # time vector from 0 to 1 sec
sine = trigonometric_signals.sine_wave(2, 5, 0, t)       # A=2, f=5Hz, phi=0
cosine = trigonometric_signals.cosine_wave(2, 5, 0, t)
expo = trigonometric_signals.exponential_signal(1, -2, t)  # example exponential

# --- Operations ---

# Time shifting sine wave by +5
shifted_sine = operations.time_shift(sine, 5)
plt.figure(figsize=(10, 6))
plt.plot(t, sine, label="Original Sine", linewidth=2)
plt.plot(t, shifted_sine, label="Shifted Sine (+5)", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Time Shift Example")
plt.legend()
plt.grid(True)
plt.show()

# Time scaling sine wave by factor 2
n2 = np.arange(0, 20, 0.1)
sine_n2 = np.sin(n2)

scaled_time, scaled_sine = operations.time_scale(sine_n2, 2)

plt.figure(figsize=(10, 6))
plt.plot(n2, sine_n2, label="Original Sine", linewidth=2)
plt.plot(scaled_time, scaled_sine, label="Time Scaled (k=2)", linewidth=2)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Time Scaling Example")
plt.legend()
plt.grid(True)
plt.show()

# Addition: step + ramp (Fixed - using correct variables)
added = operations.signal_addition(step, ramp)
plt.figure(figsize=(10, 6))
plt.stem(n1, added, basefmt=" ")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Addition: Unit Step + Ramp")
plt.grid(True)
plt.show()

# Multiplication: sine * cosine
multiplied = operations.signal_multiplication(sine, cosine)
plt.figure(figsize=(10, 6))
plt.plot(t, multiplied, linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Multiplication: Sine * Cosine")
plt.grid(True)
plt.show()