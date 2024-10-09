from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def generate_home_page():
    """Make home page, showing prompts for story"""
    words = story.prompts

    return render_template("prompts.html", prompts=words)

@app.route("/story")
def show_story():
    """Show final story"""
    text = story.generate(request.args)
    return render_template("stories.html", text=text)