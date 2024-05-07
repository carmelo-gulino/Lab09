import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        try:
            d_minima = int(self._view._txtIn.value)
            self._model.build_graph(d_minima)
            self._view.print_graph(self._model._airports_graph)
        except ValueError:
            self._view.print_error()
