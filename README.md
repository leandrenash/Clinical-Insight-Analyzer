# Clinical Trial Data Analysis Platform

A comprehensive web-based platform designed to support medical researchers in processing, analyzing, and visualizing complex clinical trial datasets. This tool provides statistical analysis capabilities, data visualization, and insights generation for clinical trial data.

## Features

- **Data Management**
  - Upload and validate clinical trial datasets
  - Automated data preprocessing and cleaning
  - Support for CSV file formats
  - Secure data handling and validation

- **Statistical Analysis**
  - Basic statistical measures
  - T-tests and ANOVA analysis
  - Effect size calculations
  - Chi-square tests
  - Factor analysis

- **Data Visualization**
  - Treatment outcome comparisons
  - Box plots for distribution analysis
  - Scatter plots with trend lines
  - Time series analysis
  - Correlation heatmaps

- **Advanced Analytics**
  - Principal Component Analysis (PCA)
  - Correlation analysis
  - Treatment effectiveness visualization
  - Factor analysis

## Getting Started

### Prerequisites

- Python 3.11
- Required Python packages (automatically installed):
  - streamlit
  - pandas
  - numpy
  - scipy
  - plotly
  - scikit-learn
  - statsmodels

### Installation

1. Clone the repository
2. Install the required packages:
```bash
pip install streamlit pandas numpy scipy plotly scikit-learn statsmodels
```

### Running the Application

Run the following command:
```bash
streamlit run main.py
```

The application will be available at `http://localhost:5000`

## Usage Guide

1. **Data Upload**
   - Navigate to the Data Upload page
   - Upload your CSV file containing clinical trial data
   - The system will validate and preprocess the data automatically

2. **Statistical Analysis**
   - Choose from various statistical tests
   - Select variables for analysis
   - View detailed statistical results and interpretations

3. **Visualization**
   - Select from multiple visualization types
   - Customize plots based on your requirements
   - Export visualizations for reports and presentations

4. **Factor Analysis**
   - Perform correlation analysis
   - Execute Principal Component Analysis
   - Analyze component loadings and explained variance

## Project Structure

```
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── pages/
│   ├── data_upload.py   # Data upload and validation
│   ├── statistical_analysis.py
│   ├── factor_analysis.py
│   └── visualization.py
├── utils/
│   ├── data_processor.py
│   ├── statistics.py
│   └── visualizations.py
└── main.py              # Main application file
```

## Technologies Used

- **Streamlit**: Web interface and application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **SciPy**: Statistical computations
- **Plotly**: Interactive data visualization
- **Scikit-learn**: Machine learning and data analysis
- **Statsmodels**: Statistical modeling and hypothesis tests

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
