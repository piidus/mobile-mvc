import flet as ft
from pages.home import home_page
from pages.login import login_page
from pages.settings import settings_page
from components.menu import menu

def main(page: ft.Page):
    """
    The main function that initializes the Flet app.

    Args:
        page (ft.Page): The Flet page object.

    Returns:
        None
    """

    page.title = "My Flet App"
    page.window.width = 400  # Updated to handle deprecation
    content_area = ft.Container()
    
    def show_page(page_content):
        content_area.content = page_content
        page.update()

    menu_bar = menu(show_page)  # Pass the show_page function to the menu

    # Add the content_area to the page first
    page.add(menu_bar, content_area)

    # Initial page
    show_page(home_page())

ft.app(target=main)

