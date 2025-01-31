# Fourier-Analysis-of-a-Coupled-Oscillator-System
This repository contains a numerical study of the Fourier transform of a three-coupled-oscillator system. The script extracts the frequency components of each oscillator's motion and generates frequency-intensity plots, revealing the dominant vibrational modes and their spectral characteristics.

## DoF Oscillator System with Fourier Transform
This project simulates a 3-degree-of-freedom (3-DoF) coupled oscillator system and performs a Fourier Transform (FT) on the displacement of the first oscillator. It uses numerical integration to solve the system's equations of motion and plots the Fourier spectrum.

### Requirements
- Python 3.x or higher
- Required libraries:
  - numpy
  - matplotlib
  - scipy

### Running the Project
To run the project locally, follow these steps:

Clone the repository to your local machine:
`git clone https://github.com/BatuhanKaganErhan/Fourier-Analysis-of-a-Coupled-Oscillator-System.git`

Navigate to the project directory:
`cd Fourier-Analysis-of-a-Coupled-Oscillator-System`

Install the required dependencies: `pip install numpy matplotlib scipy `

Run the script:
`python fourier_transform_analysis.py`

### Usage
Clone this repository or download the project files to your local machine.

In the main Python file (e.g., fourier_transform_analysis.py), ensure the initial conditions (yStart), spring constant (k), and mass (m) are set according to your simulation needs.

Run the Python script by executing the following command in your terminal:
`python fourier_transform_analysis.py`

The script will calculate the motion of the oscillators, perform the Fourier Transform, and display the FT intensity plot.

### Project Overview

This project investigates the behavior of a coupled oscillator system, applying numerical methods to solve the system's equations of motion and perform Fourier analysis on the displacement data. The system consists of multiple coupled oscillators, and the study explores the frequency components of each oscillator’s motion through the Fourier transform. Additionally, the motion of the oscillators is visualized to observe their dynamic interactions over time.

Key objectives include:

- Simulating the motion of a coupled oscillator system with variable boundary conditions (fixed or free ends).
- Performing Fourier transform analysis to extract the frequency-intensity spectrum of each oscillator's motion.
- Visualizing the displacement of each oscillator over time, highlighting their dynamic behavior.

Features:

- Fourier Analysis: The project uses the Fourier transform to analyze the frequency components of the system's oscillators.
- Oscillator Motion Visualization: In addition to Fourier analysis, the project provides plots showing the displacement of each oscillator over time.
- Flexible Boundary Conditions: The system allows for different boundary conditions, such as fixed or free ends, affecting the oscillators' behavior.

This project provides insights into the spectral properties of coupled oscillators, making it valuable for applications in mechanical systems, vibration analysis, and related fields.

### How It Works
The system consists of n coupled oscillators (with 3 in this example). The script solves the equations of motion using the `solve_ivp` function from the SciPy library. A Fourier Transform is then applied to the displacement of the first oscillator. The result is a plot showing the FT intensity vs. frequency, highlighting dominant frequency components.

### Code Explanation
1. integralTrapezoidal(data)
This function numerically computes the integral of the given data using the trapezoidal rule. It's useful for understanding how physical quantities like energy are distributed over time.

2. f_nosc(t, y, n, k, m, fixed_end)
This function models the coupled oscillators using Newton’s Second Law, calculating forces and accelerations for each oscillator. The motion is numerically solved using the Runge-Kutta method.

3. Fourier Transform (FT) Application
This function applies the Fourier transform to the oscillators’ displacement data over time, extracting the frequency-intensity spectrum, which helps analyze the system’s frequency components.

4. Visualization of Results
The Fourier spectrum is visualized by plotting the frequency vs. intensity, providing insight into how the oscillators' energy is distributed across different frequencies.

### Example Output
Below is a sample Fourier Transform spectrum for the three oscillators:

https://github.com/BatuhanKaganErhan/Fourier-Analysis-of-a-Coupled-Oscillator-System/blob/main/fourier_spectrum_plots.png

This plot visualizes the frequency components and their intensities for the three oscillators, providing insight into the oscillatory behavior and the interaction between them.

### Visualizing Oscillator Motion
The motion data for each oscillator is available in the file `oscillator_motion_plot.py`. This file contains the necessary code to generate the motion plots for the oscillators, which visually represent their behavior over time.

### License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
