uh = {}
for i in range(1, 21):
    data = Dataset('../2015020112/wrfprst_d01_2015020112_mem'+str(i)+'.nc')
    uh['mem'+str(i)] = data.variables['UH'][:].data

point_probs = ens_prob(25., operator.gt, *[uh[key] for key in uh.keys()])

nprobs_uh = neighborhood_prob(point_probs, 40000, tlons, tlats)

# Choose a time to plot
time = 2

# Set up the figure and add a map background
fig = plt.figure(1, figsize=(17., 12.))
ax = plt.subplot(111, projection=plotcrs)
ax.set_extent((-123, -74, 25, 51), ccrs.PlateCarree())
ax.coastlines('50m', edgecolor='black', linewidth=0.75)
ax.add_feature(states_provinces, edgecolor='black', linewidth=0.5)

# Plot the surface
contours = np.arange(0.1, 1.1, 0.1)
cf = ax.contourf(lon, lat, nprobs_uh[time,], contours, transform=ccrs.PlateCarree(), cmap=plt.cm.viridis)
plt.colorbar(cf, orientation='horizontal', shrink=0.5, pad=0.05)
# Make some titles
plt.title('NMEP of Updraft Helicity Greater Than 25 m$^2$s$^{-2}$ within 40 km', loc='left')
plt.title('VALID: %s' % (vtimes[time]), loc='right')
plt.show()