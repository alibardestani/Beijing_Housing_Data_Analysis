---

# Beijing Housing Data Analysis

## Overview

This repository contains a comprehensive analysis of Beijing's housing market data. The project involves various steps including data cleaning, categorical transformation, outlier detection and removal, feature engineering, and advanced visualizations. The analysis provides insights into price trends, the impact of proximity to amenities like subways and elevators, and district-level housing market dynamics.

## Project Structure

- **data_cleaning_preprocessing.py**: Handles initial data cleaning, removal of unnecessary columns, and basic preprocessing tasks such as filling missing values.
  
- **categorical_transformation_outlier_removal.py**: Transforms categorical variables, removes outliers from the dataset, and ensures data integrity for further analysis.

- **feature_engineering_visualization.py**: Focuses on creating new features such as distance to the city center and price per square meter, followed by basic visualizations to explore the data.

- **advanced_visualization.py**: Contains scripts for detailed geospatial visualizations, including scatter plots overlaid on maps and annotated visual insights.

- **district_analysis_time_series.py**: Analyzes housing data at the district level and explores time-series trends, particularly focusing on housing prices post-2010.

## Key Features

- **Data Cleaning**: Efficient handling of missing data and irrelevant features.
- **Feature Engineering**: Creation of new, meaningful variables for deeper insights.
- **Outlier Detection**: Identifying and removing outliers to ensure accurate analysis.
- **Geospatial Analysis**: Visualization of housing data on a map of Beijing.
- **Time Series Analysis**: Tracking housing price trends over time.
- **District-Level Insights**: Aggregated statistics and trends by district.

## Dependencies

The project is built using Python and the following libraries:
- pandas
- numpy
- matplotlib
- seaborn
- datetime

To install the required packages, use:
```bash
pip install -r requirements.txt
```

## Usage

1. **Data Cleaning and Preprocessing**: Start with `data_cleaning_preprocessing.py` to clean the raw data.
2. **Categorical Transformation and Outlier Removal**: Run `categorical_transformation_outlier_removal.py` to transform categorical variables and remove outliers.
3. **Feature Engineering**: Use `feature_engineering_visualization.py` to generate new features and initial visualizations.
4. **Advanced Visualization**: Dive deeper with `advanced_visualization.py` to create detailed plots and maps.
5. **District Analysis and Time Series**: Explore trends at the district level using `district_analysis_time_series.py`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or issues, please feel free to open an issue on this repository or contact the maintainer.

---
