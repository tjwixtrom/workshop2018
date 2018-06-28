# Read in the data for timestep precipitation (timestep_pcp)
pcp = {}
for i in range(1, 21):
    data = Dataset('../2015020112/wrfprst_d01_2015020112_mem'+str(i)+'.nc')
    pcp['mem'+str(i)] = data.variables['timestep_pcp'][:].data
    
# Create the thresholded fields (greater than 10 mm)
pcp_paintballs = paintballs(10, op.gt, *[pcp[key] for key in pcp.keys()])

# Plot the paintballs
# Choose a time to plot
time = 3

# Set up the figure and add a map background
fig = plt.figure(1, figsize=(17., 12.))
ax = plt.subplot(111, projection=plotcrs)
ax.set_extent((-123, -74, 25, 51), ccrs.PlateCarree())
ax.coastlines('50m', edgecolor='black', linewidth=0.75)
ax.add_feature(states_provinces, edgecolor='black', linewidth=0.5)

# Plot the paintballs
for i in range(len(pcp_paintballs)):
    data = pcp_paintballs[i][time,]
    ax.scatter(lon[data == 1], lat[data == 1], data[data == 1], transform=ccrs.PlateCarree(), label='mem'+str(i+1))

# Make some titles and legend
plt.title('Ensemble Member Paintballs Timestep Precipitation > 10 mm', loc='left')
plt.title('VALID: {0:%Y-%m-%d %H:%M:%S}'.format(vtimes[time]), loc='right')
plt.legend(loc=4)
plt.show()
