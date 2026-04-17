# ECE 105 Lab 3: Sensor Data Plots

Generate publication-quality visualizations of synthetic temperature sensor data.

## Installation

1. Activate the `ece105` conda environment:
   ```bash
   conda activate ece105
   ```

2. Install required dependencies:
   ```bash
   conda install numpy matplotlib
   ```
   
   Or using mamba:
   ```bash
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the command line:

```bash
python generate_plots.py
```

The script will generate synthetic temperature readings from two sensors and create a visualization figure.

## Example Output

The script produces `sensor_analysis.png`, a figure containing three subplots:

1. **Scatter Plot** (left): Temperature readings from both sensors plotted over time. Sensor A (blue) has a mean of 25°C with standard deviation of 3°C, while Sensor B (orange) has a mean of 27°C with standard deviation of 4.5°C. Both sensors have 200 readings spread uniformly across 0–10 seconds.

2. **Histogram** (center): Overlaid histograms showing the distribution of temperature readings from both sensors (30 bins, 50% transparency). Vertical dashed lines indicate the mean temperature for each sensor.

3. **Box Plot** (right): Side-by-side box plots comparing the distributions of the two sensors. A horizontal dashed line shows the overall mean temperature across both sensors.

## AI Tools Used and Disclosure

[Placeholder: Describe the AI tools used to generate this project, including GitHub Copilot and any other asistants.]