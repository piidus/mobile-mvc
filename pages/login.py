import flet as ft

def login_page():
    """
    Creates a login page using the Flet library.

    This function returns a `ft.Column` widget containing a username text field, a password text field, and a login button.
    The username and password text fields have labels "Username" and "Password" respectively.
    The login button has the text "Login".

    Returns:
        ft.Column: The `ft.Column` widget representing the login page.
    """

    return ft.Column([
        ft.TextField(label="Username"),
        ft.TextField(label="Password"),
        ft.ElevatedButton(text="Login"),
        # ... other login page content
    ])
