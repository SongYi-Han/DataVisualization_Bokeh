`age_group_visualization`
<br/>
* Dataset : https://github.com/daenuprobst/covid19-cases-switzerland/blob/master/demographics_switzerland_bag.csv
* Goal : Visualize the population size distribution across all age groups in Switzerland, grouped by different cantons.
* Data preprocessing : Read the online .csv file into a DataFrame using pandas and Prepare data source for plotting (ColumnDataSource)
* Data Visualization : Add hovering tooltips to the plot in order to provide more detailed information. The hover tooltips display “gender”, “canton, age group”, and “population” when hovering.
<img width="800" alt="image" src="https://user-images.githubusercontent.com/40763359/170133115-0270437e-2cb0-4cae-bb5d-81d7602d9da7.png">
<br/><br/>

`daily_cases_visualization`
<br/>
* Dataset : https://github.com/daenuprobst/covid19-cases-switzerland/blob/master/covid19_cases_switzerland_openzh-phase2.csv
* Goal: Visualize and compare the daily cases increase for each of the cantons, such that people can better assess the situation in different cantons.
* Data preprocessing : Calculate daily new cases for each canton and smooth it with a rolling window
* Data Visualization : Add a clickable legend and hovering tooltips to the plot in order to provide more detailed information.
<img width="700" alt="image" src="https://user-images.githubusercontent.com/40763359/170132787-d5f9019a-b254-4f56-bc79-825ae98e11d8.png">
<br/><br/>

`daily_test_visualization`
<br/>
* Dataset - https://github.com/daenuprobst/covid19-cases-switzerland/blob/master/covid19_tests_switzerland_bag.csv
* Goal : display and link daily total tests numbers together with positive cases numbers in two plots; user can drag the shaded overlay in the second plot and the range of the first plot will be automatically
* Data preprocessing : Define a colormap and map the range of positive rate to a colormap linearly
* Data visalization : 
  * plot1 display the daily tests numbers in a scatter plot, and add a hover tool to display the date and the corresponding total test number. The scattered point color is mapped to the positive rate from the data.
  * plot2 consists of a basic line glyph that displays the
general trend of positive cases, and add a RangeTool, with which user can observe detailed scatter
points distribution in the plot1. Add a hover tool to display the date and the corresponding
positive number.
<img width="700" alt="image" src="https://user-images.githubusercontent.com/40763359/170132572-942c85b9-6429-494f-b0c6-990375f98f08.png">
<br/><br/>

`bed_per_capita_visualization`
<br/>
* Dataset : 
  * 'https://raw.githubusercontent.com/daenuprobst/covid19-cases-switzerland/master/demographics.csv'
  * 'https://raw.githubusercontent.com/daenuprobst/covid19-cases-switzerland/master/covid_19_cases_switzerland_standard_format.csv'
  * 'https://github.com/daenuprobst/covid19-cases-switzerland/blob/master/covid19_cases_switzerland_openzh-phase2.csv'

* Goal : Visualize daily new cases statistics and available beds per catita on the map of Switzerland
* Data preprocessing: read geometry data and build a GeoJSONDataSource
* Data visualization:
  * two linear color mappers for attributes “Density” and “BedsPerCapita”
  * The color of each canton encodes the “Density” by default. When hovering over one canton, it should display canton, density, beds per capita, and daily new cases per capita in the hovertool.
  * Add circles at the locations of capital cities for each canton, and the sizes are proportional to daily new cases per capita.
  * Create a radio button group with labels ‘Density’ and ‘BedsPerCapita’. Clicking on one button will trigger to update map displaying corresponding information, and the color bar will be changed as well.
  * Add a date slider to control which per capita daily new cases information to show and complete the callback function.
  * Add a play button to change slider value and update the map plot dynamically.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/40763359/170132527-4cdb14cc-0e8f-4c2d-8817-0d39023f650a.png">
<br/>

