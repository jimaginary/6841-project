import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import sys

if (len(sys.argv) < 2):
    print("format: get_brightness.py input.mp4")
    exit(1)

# Open the video file
cap = cv2.VideoCapture(sys.argv[1])

if not cap.isOpened():
    print("Error: Could not open video.")
    exit(1)

brightness = []

print("processing frames...")

while True:
    ret, frame = cap.read()  # Read a frame from the video
    if not ret:
        break  # Exit the loop if there are no more frames

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the average brightness of the grayscale frame
    avg_brightness = np.mean(gray_frame)

    # Accumulate brightness and frame count
    brightness.append(avg_brightness)

# Release the video capture object
cap.release()


Fs = 30
brightness = np.array(brightness)
t = np.linspace(0, len(brightness)/Fs, len(brightness))
centre_brightness = brightness-np.average(brightness)
plt.plot(t, centre_brightness)
plt.show()

moving_average_brightness = np.array(
    [np.average(centre_brightness[i:i+5]) for i in range(len(centre_brightness)-5)]
)
normal_brightness = np.sign(moving_average_brightness)
plt.plot(t[:-5], normal_brightness)
plt.plot(t[:-5], moving_average_brightness)
plt.show()