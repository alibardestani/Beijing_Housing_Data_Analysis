import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import radians

housing_no_outlier = pd.read_csv('housing_no_outlier.csv', encoding='gbk')

# Calculate distance to the capital using the Haversine formula
capital_lng = radians(116.4074)
capital_lat = radians(39.9042)

housing_capital = housing_no_outlier.copy()
housing_capital['Lng'] = np.radians(housing_capital['Lng'])
housing_capital['Lat'] = np.radians(housing_capital['Lat'])

housing_capital['distanceToCapital'] = np.arccos(
    np.sin(housing_capital['Lat']) * np.sin(capital_lat) +
    np.cos(housing_capital['Lat']) * np.cos(capital_lat) *
    np.cos(housing_capital['Lng'] - capital_lng)
) * 6371.0088  # Radius of the Earth in km

# Calculate price per square meter
housing_PPS = housing_capital.copy()
housing_PPS['pricePerSquare'] = (housing_PPS['totalPrice'] * 1000) / housing_PPS['square']

fig, ax = plt.subplots()
fig.set_size_inches(15, 15)
housing_PPS['pricePerSquare'].hist(ax=ax, bins=20)

# Plot the effect of distance to capital on 'pricePerSquare'
fig, ax = plt.subplots(figsize=(8, 8))
sns.regplot(ax=ax, data=housing_PPS, x='distanceToCapital', y='pricePerSquare', 
            line_kws={'color': 'red'}, scatter_kws={'alpha': 0.1})

# KDE plot to show the effect of elevator availability on 'pricePerSquare'
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title("Effect of Elevator on Price", color="red")
ax.set_facecolor('#ffffcc')
plt.gcf().set_facecolor('khaki')

housing_PPS[housing_PPS['elevator'] == 'no elevator']['pricePerSquare'].plot(kind='kde', ax=ax, label='no elevator', color='blue')
housing_PPS[housing_PPS['elevator'] == 'has elevator']['pricePerSquare'].plot(kind='kde', ax=ax, label='has elevator', color='orange')

ax.set_xlabel('pricePerSquare')
ax.set_ylabel('Density')
plt.legend()

# Save the extended data to a new CSV file
housing_PPS.to_csv('housing_extended.csv', encoding='gbk', index=False)
