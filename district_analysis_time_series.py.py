import pandas as pd
import matplotlib.pyplot as plt

housing_extended = pd.read_csv('housing_extended.csv', encoding='gbk')

# Calculate building age
housing_extended['building_age'] = 2021 - housing_extended['constructionTime']

# Aggregate data by district
districts_df = housing_extended.groupby('district').agg(
    **{
        'pricePerSquare mean': ('pricePerSquare', 'mean'),
        '% houses with elevator': ('elevator', lambda x: (x == 'has elevator').mean() * 100),
        '% houses with subway': ('subway', lambda x: (x == 'has subway').mean() * 100),
        'square mean': ('square', 'mean'),
        'building age mean': ('building_age', 'mean'),
        'frequent buildingStructure': ('buildingStructure', lambda x: x.mode()[0])
    }
).reset_index()

districts_df.set_index('district', inplace=True)

housing_extended['tradeTime'] = pd.to_datetime(housing_extended['tradeTime'])

# Plot the average price per square meter over time
fig1, ax1 = plt.subplots(figsize=(8, 8))
housing_extended.loc[housing_extended['tradeTime'] >= '2010'].resample('M', on='tradeTime')['pricePerSquare'].mean().plot(ax=ax1, color='crimson')
ax1.set_title('Price Per Square Meter Over Time')
ax1.set_xlabel('Trade Time')
ax1.set_ylabel('Price Per Square Meter')

plt.show()

# Filter data from 2010 onwards and plot the number of trades close to the city center over time
housing_filtered = housing_extended[housing_extended['tradeTime'].dt.year >= 2010]

fig2, ax2 = plt.subplots(figsize=(8, 8))
housing_filtered.resample('3M', on='tradeTime')['distanceToCapital'].apply(lambda x: (x < 15).sum()).plot(ax=ax2, color='orange')
ax2.set_title('Center City House Trades Over Time')
ax2.set_xlabel('Trade Time')
ax2.set_ylabel('Frequency')

plt.show()
