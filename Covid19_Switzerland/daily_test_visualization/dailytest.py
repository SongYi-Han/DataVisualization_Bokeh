import pandas as pd
import numpy as np
import bokeh.palettes as bp
from bokeh.plotting import figure
from bokeh.io import output_file, show, save
from bokeh.models import ColumnDataSource, HoverTool, ColorBar, RangeTool
from bokeh.transform import linear_cmap
from bokeh.layouts import gridplot


# ==========================================================================
# Goal: Visualize Covid-19 Tests statistics in Switzerland with linked plots
# Dataset: covid19_tests_switzerland_bag.csv
# Data Interpretation:
# 		n_negative: number of negative cases in tests
# 		n_positive: number of positive cases in tests
# 		n_tests: number of total tests
# 		frac_negative: fraction of POSITIVE cases in tests
# ==========================================================================



### Task1: Data Preprocessing


## T1.1 Read the data to the dataframe "raw"
# You can read the latest data from the url, or use the data provided in the folder (update Nov.3, 2020)

url = 'https://github.com/daenuprobst/covid19-cases-switzerland/blob/master/covid19_tests_switzerland_bag.csv'
data = pd.read_csv("covid19_tests_switzerland_bag.csv")


## T1.2 Create a ColumnDataSource containing: date, positive number, positive rate, total tests
# All the data can be extracted from the raw dataframe.

date = np.array(list(data.iloc[:,1]), dtype=np.datetime64)
pos_num = list(data.iloc[:,3])
pos_rate = list(data.iloc[:,5])
test_num = list(data.iloc[:,4])

source = ColumnDataSource(data=dict(
    date = date,
    pos_num = pos_num,
    pos_rate = pos_rate,
    test_num = test_num
))


## T1.3 Map the range of positive rate to a colormap using module "linear_cmap"
# "low" should be the minimum value of positive rates, and "high" should be the maximum value

mapper = linear_cmap(field_name = 'pos_rate', palette = bp.Magma256 ,low = min(pos_rate) ,high = max(pos_rate))


### Task2: Data Visualization
# Reference link:
# (range tool example) https://docs.bokeh.org/en/latest/docs/gallery/range_tool.html?highlight=rangetool


## T2.1 Covid-19 Total Tests Scatter Plot
# x axis is the time, and y axis is the total test number.
# Set the initial x_range to be the first 30 days.

TOOLS = "box_select,lasso_select,wheel_zoom,pan,reset,help"

p = figure(plot_height = 300, plot_width = 1000, tools = TOOLS,
           x_axis_type = "datetime", background_fill_color = (255,255,255), x_range = (date[0],date[30]))

p.scatter('date', 'test_num', source = source, size = 10, color = mapper, line_color='blue')

p.title.text = 'Covid-19 Tests in Switzerland'
p.yaxis.axis_label = "Total Tests"
p.xaxis.axis_label = "Date"
p.sizing_mode = "stretch_both"

# Add a hovertool to display date, total test number
hover = HoverTool( tooltips = [
        ('date', '@date{%F}'),
        ('test', '@test_num')
    ],
     formatters = {'@date':'datetime'})

p.add_tools(hover)

## T2.2 Add a colorbar to the above scatter plot, and encode positve rate values with colors; please use the color mapper defined in T1.3

color_bar = ColorBar(color_mapper = mapper['transform'], width = 20, location = (0,0), title = 'P_Rate')
p.add_layout(color_bar,'right')


## T2.3 Covid-19 Positive Number Plot using RangeTool
# In this range plot, x axis is the time, and y axis is the positive test number.

select = figure(title = "Drag the middle and edges of the selection box to change the range above",
            plot_height = 300, plot_width = 1000, x_axis_type = "datetime", tools = "", toolbar_location = None, background_fill_color = (255,255,255))

# Define a RangeTool to link with x_range in the scatter plot
range_tool = RangeTool(x_range = p.x_range)
range_tool.overlay.fill_color = "green"
range_tool.overlay.fill_alpha = 0.2


# Draw a line plot and add the RangeTool to the plot
select.line('date','pos_num', source = source)
select.yaxis.axis_label = "Positive Cases"
select.xaxis.axis_label = "Date"
select.ygrid.grid_line_color = None
select.add_tools(range_tool)
select.toolbar.active_multi = range_tool



# Add a hovertool to the range plot and display date, positive test number
hover2 = HoverTool(
         tooltips=[
                    ('date','@date{%F}'),
                    ('positive','@pos_num')
         ],
         formatters={'@date':'datetime'})
select.add_tools(hover2)


## T2.4 Layout arrangement and display

linked_p = gridplot([p, select], ncols=1)
show(linked_p)
output_file("dvc_ex3.html")
save(linked_p)

