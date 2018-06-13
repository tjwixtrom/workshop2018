mslp = {}
for i in range(1, 21):
    data = Dataset('../2015020112/wrfprst_d01_2015020112_mem'+str(i)+'.nc')
    mslp['mem'+str(i)] = data.variables['mslp'][:].data

# Choose a time to plot
time = 5

# Set up the figure and add a map background
fig = plt.figure(1, figsize=(17., 12.))
ax = plt.subplot(111, projection=plotcrs)
ax.set_extent((-123, -74, 25, 51), ccrs.PlateCarree())
ax.coastlines('50m', edgecolor='black', linewidth=0.75)
ax.add_feature(states_provinces, edgecolor='black', linewidth=0.5)

# Plot the desired contours for each member
for i in range(1, 21):
    contours = np.array([1000, 1008, 1016])
    ax.contour(lon, lat, mslp['mem'+str(i)][time,], contours, colors=['tab:red', 'tab:orange', 'tab:green'],
               transform=ccrs.PlateCarree())

# Add each contour color to the legend
red_patch = mpatches.Patch(color='tab:red', label='1000 hPa')
orange_patch = mpatches.Patch(color='tab:orange', label='1008 hPa')
green_patch = mpatches.Patch(color='tab:green', label='1016 hPa')
plt.legend(handles=[red_patch, orange_patch, green_patch], loc=1)

# Make some titles
plt.title('Ensemble Mean Sea Level Pressure Spaghetti Plot', loc='left')
plt.title('VALID: %s' % (vtimes[time]), loc='right')
plt.show()
