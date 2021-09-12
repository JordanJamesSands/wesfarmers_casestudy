from flask import *
from main import *

app = Flask(__name__)

@app.route("/")
def mainpage():
    return render_template('index.html',display_report=False)

@app.route("/report")
def report():
    report = generate_summary_report()
    return render_template('index.html',report=report,display_report=True)
    