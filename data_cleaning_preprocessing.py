import pandas as pd

housing = pd.read_csv('housing_data.csv', encoding='gbk')

# Create a copy of the data and drop unnecessary columns
housing_dropped = housing.copy()
housing_dropped = housing_dropped.drop(['Unnamed: 0', 'Cid', 'id', 'url'], axis=1)

# Check for missing values and create a summary
housing_null = pd.DataFrame()
housing_null['Missing Values'] = housing_dropped.isna().sum()
housing_null = housing_null.set_index(pd.Index(housing_dropped.columns.tolist()))

housing_dropped['DOM'].plot(kind='box')

# Handle missing values
housing_no_missing = housing_dropped.copy()
housing_no_missing['DOM'].fillna(housing_no_missing['DOM'].mode()[0], inplace=True)
housing_no_missing.dropna(subset=['elevator', 'subway'], inplace=True)

housing_no_missing.to_csv('housing_no_missing.csv', encoding='gbk', index=False)
