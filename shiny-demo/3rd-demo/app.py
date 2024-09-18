from shiny.express import input, render, ui
from shiny import reactive

# step 2
from shared import tips

from shiny.express import input, render, ui
from shiny import reactive
from shared import tips


ui.page_opts(title="Scatter plot", fillable=True)


with ui.sidebar(open="desktop"):
    ui.input_slider("val", "Slider label 3", min=0, max=100, value=50)
    ui.input_select("var", "Variable", choices=tips.columns.tolist())

    @render.text
    def slider_val():
        return f"Slider value: {input.val()}"

    ui.input_action_button("btn_calc", "Calculate")

with ui.layout_columns(col_widths=[12, 6]):

    with ui.card(full_screen=True):
        ui.h4("Histogram of Selected Variable (click Calculate to update)")
        @render.plot
        def plot():
            from matplotlib import pyplot as plt
            if input.btn_calc():
                with reactive.isolate():
                    tips[input.var()].hist(grid=False)

                    plt.xlabel(input.var())
                    plt.ylabel("Count")

    with ui.card(full_screen=True):
        ui.h4("Tips Dataset")
        # Render the tips dataframe
        @render.data_frame
        def show_tips():
            return tips
