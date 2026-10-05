from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    title = "Stars and Exoplanets"
    return render_template("index.html", title=title)

# Stars page
@app.route("/stars")
def stars():
    stars_list = ["Sun", "Sirius", "Betelgeuse", "Vega", "Polaris"]
    return render_template("stars.html",stars=stars_list)

# Exoplanets page
@app.route("/exoplanets")
def exoplanets():
    planets = ["51 Pegasi b", "Proxima Centauri b", "TRAPPIST-1e", "Kepler-452b", "WASP-12b"]
    return render_template( "exoplanets.html", planets=planets)

# Interesting objects page
@app.route("/interesting")
def interesting():
    object_name = "Betelgeuse"
    is_supergiant = True
    return render_template("interesting.html",object_name=object_name,is_supergiant=is_supergiant)

# Contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        user_message = request.form.get("message")

        print("Name:", name)
        print("Message:", user_message)

        message = "Hello " + name + "! Your message has been received."

    return render_template("contact.html",message=message)

if __name__ == "__main__":
    # debug=True automatically reloads the server when changes are made to the code.
    app.run(debug=True)
