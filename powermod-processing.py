import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def read_csv_data(filename):
    df = pd.read_csv(filename)
    return df['Volt'].values

def plot_waveform(original_data, fs):
    time = np.arange(len(original_data)) / fs
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(time, original_data, label='Original Signal')
    plt.title('Signal Waveform')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')

    skip = 20000
    avg_data = np.array([np.average(original_data[skip*i:skip*i+2*skip]) for i in range(0, (len(original_data)) // skip - 2)])
    avg_t = np.arange(len(avg_data)) * skip / fs
    plt.subplot(2, 1, 2)
    plt.plot(avg_t, avg_data, label='Filtered Signal')
    plt.title('Signal Waveform')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()

filename = sys.argv[1]
fs = 2_000_000.0     # Sampling frequency
original_data = read_csv_data(filename)
plot_waveform(original_data, fs)