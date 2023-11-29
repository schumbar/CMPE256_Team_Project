from flask import Flask, render_template, request
import summarizer
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def submit_query():
    user_query = request.form['user_query']
    response = summarizer.get_response(user_query)
    return render_template('response.html', response=response)

@app.route('/upload_files', methods=['POST'])
def upload_files():
    # Check if the post request has the file part
    if 'files[]' not in request.files:
        return 'No file part in the request'

    files = request.files.getlist('files[]')
    
    # Check if the user has selected files
    if not files or files[0].filename == '':
        return 'No files selected'

    for file in files:
        if file:
            # Save each file to a specific path
            filename = file.filename
            save_path = os.path.join('/Users/schumbar/Desktop/team_projects/CMPE256/CMPE256_Team_Project/flask_app/Data/PDF/', filename)
            file.save(save_path)

    return render_template('index.html')

@app.route('/generate_summary', methods=['POST'])
def generate_summary():
    # Retrieve data from request
    summary_length = request.form['length']
    if summary_length == 'short':
        summary_length = "using 1-3 sentences"
    elif summary_length == 'medium':
        summary_length = "using 3-6 sentences"
    elif summary_length == 'long':
        summary_length = "using 6-10 sentences"
    response = summarizer.get_response("Generate a summary of the text " + summary_length + ".")
    return response
    # return render_template('response.html', response=response)

if __name__ == '__main__':
    # app.run(debug=True)
    generate_summary()
