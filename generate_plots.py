"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

def generate_data(seed):
    """Generate synthetic temperature sensor data and timestamps.

    Parameters
    ----------
    seed : int
        Seed for the random number generator to ensure reproducibility.

    Returns
    -------
    sensor_a : ndarray of shape (200,)
        Temperature readings from Sensor A (mean 25°C, std 3°C).
    sensor_b : ndarray of shape (200,)
        Temperature readings from Sensor B (mean 27°C, std 4.5°C).
    timestamps : ndarray of shape (200,)
        Sorted timestamps uniformly distributed from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed)
    timestamps = np.sort(rng.uniform(0, 10, 200))
    sensor_a = rng.normal(25, 3, 200)
    sensor_b = rng.normal(27, 4.5, 200)
    return sensor_a, sensor_b, timestamps