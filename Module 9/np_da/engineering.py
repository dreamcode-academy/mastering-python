import numpy as np



signal = np.array([...])  # Sensor data
filter = np.array([...])  # Filter applied to the signal

# Applying Fourier transform
fft_signal = np.fft.fft(signal)

# Filtering the signal in the frequency domain
filtered_fft_signal = fft_signal * filter


# Applying the inverse Fourier transform to get the filtered signal
filtered_signal = np.fft.ifft(filtered_fft_signal)

print("Filtered Signal:", filtered_signal)