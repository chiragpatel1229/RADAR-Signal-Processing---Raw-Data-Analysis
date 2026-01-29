# RADAR Signal Processing and Raw Data Analysis

## 📡 Telecommunications and Digital Signal Processing Project

## Overview
This repository contains a comprehensive signal processing pipeline developed to analyze raw RADAR data. The project was conducted at Hochschule Wismar under the guidance of Prof. Dr. Ing. Toralf Renkwitz. The primary objective was to transform raw and noisy radar echoes into actionable data through multiple stages of spectral analysis, filtering, and spatial estimation.

## Key Features and Technical Tasks
A multi stage digital signal processing pipeline was implemented in Python using the Spyder environment. The following technical tasks were completed.

### Raw Data Analysis
Plotted power graphs of raw data for all range gates and temporal samples. Both polarizations were evaluated to identify the most suitable data segments for further analysis.

### Coherent Integration
Applied a low pass filter based coherent integration approach using fourteen integration steps to reduce noise while preserving target signal integrity.

### Spectral Width Derivation
Performed Gaussian distribution fitting to estimate Doppler shifts and spectral widths across multiple range gates.

### Correlation Processing
**Autocorrelation**  
Evaluated receiver self similarity across all ranges.

**Cross Correlation**  
Analyzed phase and amplitude relationships between receiver channels two three and four to identify signal maxima.

### Angle of Arrival Estimation
Calculated the angle of arrival for all range gates using a three antenna array configuration.

### SNR Cleaning
Implemented an eighteen decibel signal to noise ratio thresholding method to suppress noise and generate high clarity spectral visualizations.

## Technical Coursework
In addition to the final report this repository includes foundational digital signal processing implementations.

### Signal Modeling
Generation and FFT based analysis of triangular and rectangular time domain signals.

### Kinematics
Simulation of radial velocity for moving observers demonstrating the Doppler effect.

### Coding Theory
Implementation and evaluation of signal communication modulation schemes and coding techniques.

### Statistical Analysis
Development of custom histogram functions and Gaussian distribution fitting models.

## Technologies Used
- **Programming Language**: Python  
- **Development Environment**: Spyder  
- **Libraries**: NumPy, Matplotlib including pcolor and line plots, PyAstronomy
