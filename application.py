from flask import Flask, render_template, url_for, request
from request_data import * # this script handles getting the data use get_jobs_municipality(search_key)
# EB looks for an 'application' callable by default.
application = Flask(__name__)
app = application

@app.route('/', methods=['GET', 'POST'])
def index():
    data = ""
    data_paragraph = "";
    if request.method == 'POST':
        """Here I will handle the data from the form"""
        data = get_jobs_municipality("IT underviser")
        form = request.form
    return render_template('index.html', divdata = data)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()