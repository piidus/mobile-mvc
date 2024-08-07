import flet as ft

class Model:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

class View:
    def __init__(self, model):
        self.model = model
        self.text = ft.Text(value=str(model.count))

    def update(self):
        self.text.value = str(self.model.count)
        self.text.update()  # Ensure the text widget updates

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.button = ft.ElevatedButton(text="Increment", on_click=self.on_click)

    def on_click(self, e):
        self.model.increment()
        self.view.update()

def main(page: ft.Page):
    model = Model()
    view = View(model)
    
    controller = Controller(model, view)

    page.add(view.text, controller.button)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    
    page.update()  # Ensure the initial UI state is rendered

ft.app(target=main)
