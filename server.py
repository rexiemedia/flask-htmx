from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  # Enable Cross-Origin Resource Sharing (optional)

@app.route("/")
def home():
    return render_template(
        'home/index.html',
        request=request,
        title="Home - Welcome to Silverback Security Solutions"
    )


@app.route("/about")
def about():
    return render_template('about/index.html', request=request,
        title="About US | Silverback Security Solutions")

@app.route("/blog")
def blog():
    return render_template('blog/index.html')

@app.route("/contact")
def contact():
    return render_template('contact/index.html', request=request,
        title="Contact US | Silverback Security Solutions")