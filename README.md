# Fourier-Analysis-of-a-Single-Oscillator-System
This repository contains a numerical study of the Fourier transform of a three-coupled-oscillator system. The script extracts the frequency components of each oscillator's motion and generates frequency-intensity plots, revealing the dominant vibrational modes and their spectral characteristics.

## DoF Oscillator System with Fourier Transform
This project simulates a 3-degree-of-freedom (3-DoF) coupled oscillator system and performs a Fourier Transform (FT) on the displacement of the first oscillator. It uses numerical integration to solve the system's equations of motion and plots the Fourier spectrum.

### Requirements
- Python 3.7 or higher
- Required libraries:
  - numpy
  - matplotlib
  - scipy

## Running the Project
To run the project locally, follow these steps:

Clone the repository to your local machine:
`git clone https://github.com/yourusername/projectname.git`

Navigate to the project directory:
`cd projectname`

Install the required dependencies:
`pip install -r requirements.txt`

Run the script:
`python my_script.py`

### Usage
Clone this repository or download the project files to your local machine.

In the main Python file (e.g., oscillator_simulation.py), ensure the initial conditions (yStart), spring constant (k), and mass (m) are set according to your simulation needs.

Run the Python script by executing the following command in your terminal:
`python my_script.py`

The script will calculate the motion of the oscillators, perform the Fourier Transform, and display the FT intensity plot.

### How It Works
The system consists of n coupled oscillators (with 3 in this example).
The script solves the equations of motion using the solve_ivp function from the SciPy library.
A Fourier Transform is then applied to the displacement of the first oscillator.
The result is a plot showing the FT intensity vs. frequency.

### Code Explanation
integral(data): This function approximates the integral of the given data using the trapezoidal rule.
f_nosc(t, y, n, k, m, fixed_end): This function defines the system of differential equations describing the motion of the coupled oscillators.
The motion is solved numerically with the Runge-Kutta method (RK45).
The Fourier Transform is computed on the displacement of the first oscillator and plotted.

### Example Output
The output will be a plot showing the frequency spectrum of the first oscillator, with intensity values corresponding to the frequency components. This can be useful for analyzing the energy distribution across different frequencies in the system.
