from shiny.express import input, render, ui

from shiny import reactive
# step 2
from shared import tips

ui.input_slider("val", "Slider label 3", min=0, max=100, value=50)


# step 2
ui.input_select("var", "Variable", choices=tips.columns.tolist())

ui.input_action_button("btn_calc", "Calculate")

@render.text
def slider_val():
    return f"Slider value: {input.val()}"


@render.plot
def plot():
    from matplotlib import pyplot as plt
    if input.btn_calc():
        with reactive.isolate():
            tips[input.var()].hist(grid=False)

            plt.xlabel(input.var())
            plt.ylabel("Count")


# Render the tips dataframe
@render.data_frame
def show_tips():
    return tips
