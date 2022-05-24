this is interactive map visualization based on statistics data
of Switzerland. The visualization mainly consists of two layers, a map as the base layer, and circles
encoding daily new cases per capita as the top layer. There are four data sources involved to provide
different information, three of them should be accessible online, and the geographical shape file is provided
as “data.zip” file.  
  
### Data Preprocessing
- In order to read and filter geometry data, install `geopandas`
- Merge data and build a GeoJSONDataSource

### Data Visualization 
- Two linear color mappers from attributes “Density” and “BedsPerCapita”
- The color of each
canton encodes the “Density” by default. When hovering over one canton, it should display canton,
density, beds per capita, and daily new cases per capita in the hovertool.
- circles represent the locations of capital cities for each canton, and the sizes are proportional to
daily new cases per capita.
- a radio button is grouped with labels ‘Density’ and ‘BedsPerCapita’. Clicking on one button
will trigger to update map displaying corresponding information, and the color bar will be changed
as well. Note that the circles will remain the same for both Density map and BedsPerCapita map.
-date slider controls which per capita daily new cases information to show 
-play button to change slider value and update the map plot dynamically.