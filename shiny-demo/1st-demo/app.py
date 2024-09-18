from shiny.express import input, render, ui

# step 2
from shared import tips

ui.input_slider("val", "Slider label 3", min=0, max=100, value=50)


# step 2
ui.input_select("var", "Variable", choices=tips.columns.tolist())

@render.text
def slider_val():
    abc = input.val()
    return f"Slider value: {abc}"

@render.plot
def plot():
    from matplotlib import pyplot as plt

    tips[input.var()].hist(grid=False)

    plt.xlabel(input.var())
    plt.ylabel("Count")

# Render the tips dataframe
@render.data_frame
def show_tips():
    return tips
