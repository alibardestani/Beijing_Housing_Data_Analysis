import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import ConnectionStyle

housing_extended = pd.read_csv('housing_extended.csv', encoding='gbk')

# Create a sample of the data
housing_sample = housing_extended.iloc[:-100:100]

fig1, ax1 = plt.subplots(figsize=(10, 7))
housing_sample.plot(x='Lng', y='Lat', ax=ax1, kind='scatter', alpha=0.2)
ax1.axis('equal')
ax1.set_title('Scatter Plot of Housing Locations')

fig2, ax2 = plt.subplots(figsize=(10, 7))
housing_sample.plot(x='Lng', y='Lat', ax=ax2, kind='scatter', alpha=0.4,
                    c='pricePerSquare', cmap=plt.get_cmap("jet"), colorbar=True)
ax2.axis('equal')

# Annotate the center of Beijing
text_position = (116.6, 39.65)
arrow_position = (116.40, 39.90)
ax2.annotate('Center of Beijing', xy=arrow_position, xytext=text_position, 
             arrowprops=dict(arrowstyle='fancy', connectionstyle=ConnectionStyle("Arc3", rad=0.3)))

fig3, ax3 = plt.subplots(figsize=(10, 7))
housing_sample.plot(x='Lng', y='Lat', ax=ax3, kind='scatter', alpha=0.2,
                    s=housing_sample['distanceToCapital'] * 4)
ax3.axis('equal')

# Add a map as the background image
beijing_img = mpimg.imread('map1.jpg')
ax3.imshow(beijing_img, extent=[115.89777890444654, 116.90711309555346, 39.5957436, 40.2840444])

# Scatter plot with color based on district and size based on square footage
fig4, ax4 = plt.subplots(figsize=(12.5, 7))
scatter = ax4.scatter(
    housing_sample['Lng'], housing_sample['Lat'], c=housing_sample['district'], 
    s=housing_sample['square'] / 20, cmap='nipy_spectral', alpha=0.6
)
cbar = fig4.colorbar(scatter, ax=ax4)
cbar.set_label('District')

ax4.set_xlabel('Lng')
ax4.set_ylabel('Lat')
ax4.axis('equal')

beijing_img1 = mpimg.imread('map1.jpg')
ax4.imshow(beijing_img1, extent=[115.89777890444654, 116.90711309555346, 39.5957436, 40.2840444])

# Filter housing data by distance to capital and plot
housing_filtered = housing_sample[(housing_sample['distanceToCapital'] > 10) & (housing_sample['distanceToCapital'] < 30)]

fig5, ax5 = plt.subplots(figsize=(12.5, 7))
beijing_img2 = mpimg.imread('map2.jpg')
ax5.imshow(beijing_img2, extent=[115.89777890444654, 116.90711309555346, 39.5957436, 40.2840444])

scatter = ax5.scatter(
    housing_filtered['Lng'], housing_filtered['Lat'], c=housing_filtered['district'], 
    s=housing_filtered['square'] / 20, cmap='nipy_spectral', alpha=0.6
)
cbar = fig5.colorbar(scatter, ax=ax5)
cbar.set_label('District')

ax5.set_xlabel('Lng')
ax5.set_ylabel('Lat')
ax5.axis('equal')

plt.show()
