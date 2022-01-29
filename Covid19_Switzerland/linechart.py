import pandas as pd
from math import pi
import numpy as np
from bokeh.io import output_file, show, save
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool,FactorRange
import bokeh.palettes as bp

# Goal: Draw a line chart displaying averaged daily new cases for all cantons in Switzerland.

### Task 1: Data Preprocessing

## T1.1 Read data into a dataframe, set column "Date" to be the index
# Interpretation: value on row i, column j is either the cumulative covid-19 case number of canton j on date i or null value

url = 'https://github.com/daenuprobst/covid19-cases-switzerland/blob/master/covid19_cases_switzerland_openzh-phase2.csv'
url_raw = 'https://raw.githubusercontent.com/daenuprobst/covid19-cases-switzerland/master/covid19_cases_switzerland_openzh-phase2.csv'

raw = pd.read_csv(url_raw)
df = raw.set_index('Date')

# Initialize the first row with zeros, and remove the last column 'CH' from dataframe

df.iloc[0,:] = 0
drop_list = df.loc[:,'CH':]
df = df.drop(drop_list, axis=1)


# Fill null with the value of previous date from same canton
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html
df = df.fillna(method='ffill')

## T1.2 Calculate and smooth daily case changes

# Compute daily new cases (dnc) for each canton, e.g. new case on Tuesday = case on Tuesday - case on Monday;
# Fill null with zeros as well
dnc = df.diff()
dnc = dnc.fillna(0)


# Smooth daily new case by the average value in a rolling window, and the window size is defined by step
# Why do we need smoothing? How does the window size affect the result?
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html
#step = 3
dnc_avg = dnc.rolling(window =3).mean()
dnc = dnc_avg.fillna(0)


## T1.3 Build a ColumnDataSource

# Extract all canton names and dates
# NOTE: be careful with the format of date when it is used as x input for a plot
cantons = list(dnc)
date = df.index
date = date.tolist()

# Create a color list to represent different cantons in the plot, you can either construct your own color patette or use the Bokeh color pallete
color_palette = bp.turbo(26)

# Build a dictionary with date and each canton name as a key, i.e., {'date':[], 'AG':[], ..., 'ZH':[]}
# For each canton, the value is a list containing the averaged daily new cases

source_dict = {}
source_dict['date'] = date
for c in cantons:
    source_dict[c] = dnc_avg[c].tolist()

source = ColumnDataSource(data=source_dict)



### Task 2: Data Visualization

## T2.1: Draw a group of lines, each line represents a canton, using date, dnc_avg as x,y. Add proper legend.
# https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/line.html?highlight=line#bokeh.models.glyphs.Line
# https://docs.bokeh.org/en/latest/docs/user_guide/interaction/legends.html

p = figure(plot_width=1000, plot_height=800, x_axis_type="datetime")
p.title.text = 'Daily New Cases in Switzerland'

p = figure(plot_width=1000, plot_height=800, x_axis_type="datetime")
p.title.text = 'Daily New Cases in Switzerland'
source.data['date'] = pd.to_datetime(source.data['date'])


for canton, color in zip(cantons, color_palette):
    p.line(x = 'date', y = canton, line_width=2, color=color, alpha=0.8,legend_label=canton, name=canton, source=source)


# Make the legend of the plot clickable, and set the click_policy to be "hide"
p.legend.location = "top_left"
p.legend.click_policy="hide"


## T2.2 Add hovering tooltips to display date, canton and averaged daily new case

# (Hovertip doc) https://docs.bokeh.org/en/latest/docs/user_guide/tools.html#hovertool
# (Date hover)https://stackoverflow.com/questions/41380824/python-bokeh-hover-date-time

hover = HoverTool(
        tooltips=[
            ('date','@date{%F}'),
            ('canton', '$name'),
            ('case', '@$name{int}'),
        ],
        formatters={
        '@date' : 'datetime'}
    )

p.add_tools(hover)

show(p)
output_file("linechart.html")
save(p)

