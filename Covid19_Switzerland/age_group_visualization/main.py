import pandas as pd 
from math import pi
from bokeh.io import output_file, show, save
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool,FactorRange,CustomJS
# import bokeh.palettes as bp # uncomment it if you need special colors that are pre-defined

 
### Task 1: Data Preprocessing
 

## T1.1 Read online .csv file into a dataframe using pandas
# Reference links: 
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
# https://stackoverflow.com/questions/55240330/how-to-read-csv-file-from-github-using-pandas 

original_url = 'https://github.com/daenuprobst/covid19-cases-switzerland/blob/master/demographics_switzerland_bag.csv'
url="https://raw.githubusercontent.com/daenuprobst/covid19-cases-switzerland/master/demographics_switzerland_bag.csv"
df=pd.read_csv(url)

## T1.2 Prepare data for a grouped vbar_stack plot
# Reference link, read first before starting: 
# https://docs.bokeh.org/en/latest/docs/user_guide/categorical.html#stacked-and-grouped


# Filter out rows containing 'CH' 
idx_ch = df.loc[df['canton'] == 'CH'].index
df = df.drop(idx_ch)


# Extract unique value lists of canton, age_group and sex
canton = df.canton.unique()
age_group = df.age_group.unique()
sex = df.sex.unique()


# Create a list of categories in the form of [(canton1,age_group1), (canton2,age_group2), ...]
factors = []
for i in canton:
    for j in age_group:
        factors.append((i,j),)

# Use genders as stack names
stacks = ['male','female']

# Calculate total population size as the value for each stack identified by canton,age_group and sex
male_pop = []
female_pop = []


for i in canton:
    can_df = df.loc[(df['canton']== i)]
    for j in age_group:
        age_df = can_df.loc[(can_df['age_group'] == j)]
        for k in sex:
            if k == sex[0]:
                male_df = age_df.loc[(age_df['sex'] == k),['pop_size']]
                sum_male = male_df.sum()
                male_pop.append(sum_male.values[0])
            else :
                female_df = age_df.loc[(age_df['sex'] == k),['pop_size']]
                sum_female = female_df.sum()
                female_pop.append(sum_female.values[0])


# Build a ColumnDataSource using above information
source = ColumnDataSource(data=dict(
    x = factors,
    male = male_pop,
    female = female_pop,
))



### Task 2: Data Visualization


## T2.1: Visualize the data using bokeh plot functions
p = figure(x_range=FactorRange(*factors), plot_height=500, plot_width=800, title='Canton Population Visualization')
p.yaxis.axis_label = "Population Size"
p.xaxis.axis_label = "Canton"
p.xaxis.major_label_text_font_size = '5px'
p.xaxis.major_label_orientation = pi/2
p.sizing_mode = "stretch_both"
p.xgrid.grid_line_color = None

p.vbar_stack(stacks, x='x', width=0.9, alpha=0.5, color=["blue", "red"], source=source, legend_label=stacks)



## T2.2 Add the hovering tooltips to the plot using HoverTool
# To be specific, the hover tooltips should display “gender”, canton, age group”, and “population” when hovering.
# https://docs.bokeh.org/en/latest/docs/user_guide/tools.html#hovertool
# read more if you want to create fancy hover text: https://stackoverflow.com/questions/58716812/conditional-tooltip-bokeh-stacked-chart


hover = HoverTool(
        tooltips=[
            ("canton and agegroup", "@x"),  
            ("gender", "$name"),
            ("population", "@$name"),
        ]
    )

p.add_tools(hover)
show(p)


## T2.3 Save the plot as "dvc_ex1.html" using output_file

output_file("dvc_ex1.html")

