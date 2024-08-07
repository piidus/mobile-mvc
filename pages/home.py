import flet as ft

def home_page():
    """
    Returns a `ft.Column` widget containing the home page content.

    The `home_page` function creates a `ft.Column` widget with a `ft.Text` widget as its child. The `ft.Text` widget displays the text "Welcome to the home page". Additional content can be added to the `ft.Column` widget by appending more widgets to the list.

    Returns:
        ft.Column: The `ft.Column` widget containing the home page content.
    """
    return ft.Column([
        ft.Text("Welcome to the home page"),
        # ... other home page content
    ])
