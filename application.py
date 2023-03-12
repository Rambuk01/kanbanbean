from flask import Flask, render_template, url_for, request, jsonify
from request_data import * # this file handles getting the data - use get_jobs_municipality(search_key)
# EB looks for an 'application' callable by default.
application = Flask(__name__)
app = application

@app.route('/', methods=['GET', 'POST'])
def index():
    city_jobs_dict = {}
    total_jobs = 0;
    if request.method == 'POST':
        
        # the job category is search_key.
        search_key = request.form.get('search_key')
        """Here I will handle the data from the form"""
        city_jobs_dict, total_jobs = get_jobs_municipality(search_key)
        
        form = request.form
    return render_template('index.html', divdata = city_jobs_dict, total=total_jobs)

# HANDLE AJAX REQUEST POST
@app.route('/ajax', methods = ['POST'])
def ajax_request():
    search_key = request.form['search_word']
    city_jobs_dict, total_jobs = get_jobs_municipality(search_key)
    return jsonify(ajax_results=city_jobs_dict)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()