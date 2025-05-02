from flask import Flask, render_template

# Create the Flask application.
# The 'template_folder' parameter explicitly tells Flask where to find HTML files.
app = Flask(__name__, template_folder="templates")

# Home route: Renders the index.html template.
@app.route("/")
def home():
    return render_template("index.html")

# Love route: Renders the love.html template.
@app.route("/love")
def love():
    return render_template("love.html")

if __name__ == "__main__":
    # Run the app on host "0.0.0.0", which makes it accessible on your local network.
    # The port is set to 5000 by default, and debug mode is enabled for development.
    app.run(host="0.0.0.0", port=5000, debug=True)