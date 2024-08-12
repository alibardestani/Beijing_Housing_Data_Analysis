import pandas as pd
import numpy as np

housing_no_missing = pd.read_csv('housing_no_missing.csv', encoding='gbk')

# Transform categorical variables using mapping
housing_categorical = housing_no_missing.copy()
housing_categorical["elevator"] = housing_categorical["elevator"].map({1: "has elevator", 0: "no elevator"})
housing_categorical["subway"] = housing_categorical["subway"].map({1: "has subway", 0: "no subway"})
housing_categorical["buildingStructure"] = housing_categorical["buildingStructure"].map(
    {1: "unknown", 2: "mixed", 3: "brick and wood", 4: "concrete", 5: "steel", 6: "steel-concrete composite"}
)
housing_categorical["renovationCondition"] = housing_categorical["renovationCondition"].map(
    {1: "other", 2: "rough", 3: "simplicity", 4: "hardcover"}
)

# Display unique values for 'constructionTime' and 'floor'
print('constructionTime:', housing_categorical['constructionTime'].unique())
print('floor:', housing_categorical['floor'].unique())

# Filter out rows with unknown 'constructionTime' and convert to integer
housing_construction = housing_categorical[housing_categorical['constructionTime'].str.contains('未知') == False]
housing_construction['constructionTime'] = housing_construction['constructionTime'].astype('int32')

housing_floor = housing_construction.copy()
housing_floor['floor'] = housing_floor['floor'].str.extract('(\d+)').astype('int32')

housing_floor['totalPrice'].plot(kind='box')

# Calculate the IQR and remove outliers in 'totalPrice'
Q1 = housing_floor['totalPrice'].quantile(.25)
Q3 = housing_floor['totalPrice'].quantile(.75)
IQR = Q3 - Q1

lower_band = Q1 - 1.5 * IQR
upper_band = Q3 + 1.5 * IQR

housing_no_outlier = housing_floor[(housing_floor['totalPrice'] >= lower_band) & (housing_floor['totalPrice'] <= upper_band)]

# Print the number of outliers removed and plot the cleaned data
print('Number of removed outliers:', housing_floor.shape[0] - housing_no_outlier.shape[0])
housing_no_outlier['totalPrice'].plot(kind='box')

housing_no_outlier.to_csv('housing_no_outlier.csv', encoding='gbk', index=False)
