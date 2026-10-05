# Stars and Exoplanets

This is a small Flask web application built around astronomy, covering stars, exoplanets and some interesting objects in space. I used Flask for routing and server-side logic, Jinja templates for dynamic content, and HTML/CSS for the presentation layer.

## What it does

The website contains separate pages for:

- Stars and their properties
- Exoplanets and their discovery
- Interesting astronomical objects
- A simple contact form

The pages are connected through Flask routes and `url_for()`. Astronomical data is passed from Python to the templates and rendered using Jinja variables, loops and conditional statements.
The contact page handles GET and POST requests and processes submitted form data through Flask's `request.form`.

## Implementation

Flask routes handle the different pages and pass data to the corresponding Jinja templates. Lists of astronomical objects are rendered dynamically using Jinja loops, while conditional rendering is used where required. Static CSS is served through Flask's `static` directory.

## Tools

- Python
- Flask
- Jinja2
- HTML
- CSS
- VS Code

## Running locally

Install the dependencies:
`pip install -r requirements.txt`

Start the application:
`python main.py`

Open `http://127.0.0.1:5000` in a browser.

## Notes

This small project was built while working with Flask and experimenting with the connection between Python backend logic, Jinja templates and HTML/CSS. The astronomy content is used as the subject matter for the application, with the main focus being the Flask implementation and server-side template rendering.