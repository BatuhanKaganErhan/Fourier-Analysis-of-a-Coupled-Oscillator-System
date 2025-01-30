# Fourier-Analysis-of-a-Coupled-Oscillator-System
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
`git clone https://github.com/BatuhanKaganErhan/Fourier-Analysis-of-a-Single-Oscillator-System.git`

Navigate to the project directory:
`cd Fourier-Analysis-of-a-Coupled-Oscillator-System`

Install the required dependencies: `pip install numpy matplotlib scipy `

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
The result is a plot showing the FT intensity vs. frequency, highlighting dominant frequency components.

### Code Explanation
integral(data): This function approximates the integral of the given data using the trapezoidal rule.
f_nosc(t, y, n, k, m, fixed_end): This function defines the system of differential equations using Newton's Second Law.
The motion is solved numerically with the Runge-Kutta method (RK45).
The Fourier Transform is computed on the displacement data, and a frequency spectrum plot is generated.

### Example Output
The output will be a plot showing the frequency spectrum of the first oscillator, with intensity values corresponding to the frequency components. This can be useful for analyzing the energy distribution across different frequencies in the system.
![fourier_spectrum_plots (1)](https://github.com/user-attachments/assets/65e1ee84-9b2d-448e-af0e-e56d00987fa4)

### Visualizing Oscillator Motion
In addition to performing Fourier analysis on the coupled oscillator system, this project also provides a visualization of the motion of each individual oscillator over time. By plotting the displacement of each oscillator, you can observe their dynamics and how they evolve under the influence of their interactions.

The motion data for each oscillator is available in the file `oscillator_motion_data.py`. This file contains the necessary code to generate the motion plots for the oscillators, which visually represent their behavior over time.

### License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
