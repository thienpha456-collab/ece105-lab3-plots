"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt

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

def generate_data(seed):
    """Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int
        Random number generator seed for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    """
    rng = np.random.default_rng(seed=seed)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)
    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot scatter plot of sensor data on the given Axes.

    Parameters
    ----------
    sensor_a : array_like
        Temperature readings from Sensor A.
    sensor_b : array_like
        Temperature readings from Sensor B.
    timestamps : array_like
        Timestamps for the readings.
    ax : matplotlib.axes.Axes
        The Axes object to plot on.

    Returns
    -------
    None
        Modifies ax in place.
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.7)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.7)
    ax.set_xlabel('Timestamp (seconds)')
    ax.set_ylabel('Sensor Reading (°C)')
    ax.set_title('Sensor Data Scatter Plot')
    ax.legend()
    ax.grid(True)

# Create plot_histogram(sensor_a, sensor_b, ax) that draws
# the histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_histogram(sensor_a, sensor_b, ax):
    """Plot overlaid histogram of sensor temperature distributions on the given Axes.

    Parameters
    ----------
    sensor_a : array_like
        Temperature readings from Sensor A.
    sensor_b : array_like
        Temperature readings from Sensor B.
    ax : matplotlib.axes.Axes
        The Axes object to plot on.

    Returns
    -------
    None
        Modifies ax in place.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A', color='blue')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B', color='orange')
    ax.axvline(np.mean(sensor_a), color='blue', linestyle='--', linewidth=2, label='Sensor A Mean')
    ax.axvline(np.mean(sensor_b), color='orange', linestyle='--', linewidth=2, label='Sensor B Mean')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Overlaid Histogram of Sensor Temperature Distributions')
    ax.legend()
    ax.grid(True)

# Create plot_boxplot(sensor_a, sensor_b, ax) that draws
# the box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_boxplot(sensor_a, sensor_b, ax):
    """Plot side-by-side box plot of sensor distributions on the given Axes.

    Parameters
    ----------
    sensor_a : array_like
        Temperature readings from Sensor A.
    sensor_b : array_like
        Temperature readings from Sensor B.
    ax : matplotlib.axes.Axes
        The Axes object to plot on.

    Returns
    -------
    None
        Modifies ax in place.
    """
    ax.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'])
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(overall_mean, color='red', linestyle='--', linewidth=2, label=f'Overall Mean: {overall_mean:.2f}°C')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Side-by-Side Box Plot of Sensor Distributions')
    ax.legend()
    ax.grid(True, axis='y')

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.

def main():
    """Generate sensor data and create publication-quality plots.

    Generates synthetic sensor data, creates a 1x3 subplot figure with
    scatter plot, histogram, and box plot, and saves the figure as PNG.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    sensor_a, sensor_b, timestamps = generate_data(876)
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    plot_scatter(sensor_a, sensor_b, timestamps, axs[0])
    plot_histogram(sensor_a, sensor_b, axs[1])
    plot_boxplot(sensor_a, sensor_b, axs[2])
    plt.tight_layout()
    plt.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')

if __name__ == '__main__':
    main()