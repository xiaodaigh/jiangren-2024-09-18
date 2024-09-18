from shiny.express import input, render, ui
from shiny import reactive

# step 2
from shared import tips

from shiny.express import input, render, ui
from shiny import reactive
from shared import tips


ui.input_slider("val", "Slider label 3", min=0, max=100, value=50)
ui.input_select("var", "Variable", choices=tips.columns.tolist())


@reactive.calc
def histogram_data():
    return tips[input.var()]


ui.h4("Histogram of Selected Variable")
@render.plot
def plot1():
    from matplotlib import pyplot as plt
    a = histogram_data()
    a.hist(grid=False)

    plt.xlabel(input.var())
    plt.ylabel("Count")

ui.h4("Histogram2 of Selected Variable")
@render.plot
def plot2():
    from matplotlib import pyplot as plt
    histogram_data().hist(grid=True)
    plt.xlabel(input.var())
    plt.ylabel("Count")

ui.h4("Tips Dataset")
# Render the tips dataframe
@render.data_frame
def show_tips():
    return tips
