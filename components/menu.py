import flet as ft
from pages.home import home_page
from pages.login import login_page
from pages.settings import settings_page

def menu(show_page):
    """
    Creates a menu for the application with three actions: Home, Login, and Settings.
    
    Args:
        show_page (function): A function that takes a page content as an argument and displays it.
        
    Returns:
        ft.AppBar: An AppBar widget with a title, leading icon, and three actions: Home, Login, and Settings.
    """

    def show_home(e):
        show_page(home_page())

    def show_login(e):
        show_page(login_page())

    def show_settings(e):
        show_page(settings_page())

    return ft.AppBar(
        title=ft.Text("My App"),
        leading=ft.Icon(name=ft.icons.MENU),  # Move leading to the center
        actions=[
            ft.IconButton(icon=ft.icons.HOME, on_click=show_home),
            ft.IconButton(icon=ft.icons.LOGIN, on_click=show_login),
            ft.IconButton(icon=ft.icons.SETTINGS, on_click=show_settings),
        ]
    )

