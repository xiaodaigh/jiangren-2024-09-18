# install the shiny extension

from shiny import App, render, ui
import matplotlib.pyplot as plt
import numpy as np

app_ui = ui.page_fluid(
    ui.input_slider("n", "Number of points", 10, 100, 50),
    ui.output_plot("plot")
)

def server(input, output, session):
    @output
    @render.plot
    def plot():
        n = input.n()
        x = np.random.rand(n)
        y = np.random.rand(n)
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        return fig

app = App(app_ui, server)
