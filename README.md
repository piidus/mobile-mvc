# mobile-mvc
A basic Flet to check mvc in one_page_mvc.py

# My Flet App
## Description
    "My Flet App" is a simple application built using the Flet framework. It demonstrates a basic multi-page layout featuring a home page, login page, and settings page, with a responsive menu for navigation.

### Features
-   Home Page: Displays a welcome message to users.
-   Login Page: Contains input fields for username and password, and a login button.
-   Settings Page: Placeholder for future settings content.
-   Navigation Menu: Allows users to switch between the home, login, and settings pages.

### Project Structure
The project is organized into the following structure:

```plaintext
.
├── main.py
├── pages
│   ├── home.py
│   ├── login.py
│   ├── settings.py
├── components
│   └── menu.py
├── README.md
└── requirements.txt
```
-    main.py: The main entry point of the application, setting up the page and handling navigation.
-   pages/: Contains individual modules for each page (home, login, settings).
-   components/: Contains shared components like the navigation menu.

-   README.md: Documentation for the project.
-   requirements.txt: Lists the dependencies required to run the project.

### Installation
-   For ubuntu
`sudo apt update`

`sudo apt install libmpv-dev libmpv2`

`sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1`
-   clone
`git clone https://github.com/yourusername/my-flet-app.git`
`cd my-flet-app`

-   Activate
    `python -m venv .venv`
    -   window
        `.venv\Scripts\activate`
    -   On macOS/Linux:
        `source .venv/bin/activate`

### Install the dependencies:
    `python main.py`

Dependencies
Flet: A framework for building interactive web apps using Python.

Contributing
Contributions are welcome! Feel free to submit issues, fork the repository, and send pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

# DEPLOYMENT
1.  [Download flutter Sdk](https://docs.flutter.dev/release/archive)
    -   set into c: drive
    -   load path in windows env file
    -   verify installation `flutter --version`
2.  [Download & Install android Studio](https://developer.android.com/studio)
    -   add flutter in plugin

3.  Enable Windows Developer Mode 
    Enabling Developer Mode on Windows
        Here's how to enable Developer Mode on Windows:

        Open Developer Mode Settings:

        Press Win + R to open the Run dialog.
        Type ms-settings:developers and press Enter. This will open the Developer Mode settings.
        Enable Developer Mode:

        In the Developer Mode settings, find the "Developer Mode" section.
        Toggle the switch to enable Developer Mode.
        You might be prompted to confirm your choice and restart your computer. Follow any additional instructions to complete the setup.
        Confirm Developer Mode:

        Ensure that Developer Mode is turned on by returning to the Developer Mode settings page. The switch should be in the "On" position.

        Restart Computer.

4.  Run in cmd 
    `flet build apk`

Happy Flettings