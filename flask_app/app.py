from flask import Flask, render_template, request
import summarizer
import os

app = Flask(__name__)

# Directory where the uploaded PDF files are stored.
PDF_File_Directory = '/Users/schumbar/Desktop/team_projects/CMPE256/CMPE256_Team_Project/flask_app/Data/PDF/'

def delete_all_files_in_directory(directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")


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
    delete_all_files_in_directory(PDF_File_Directory)
    # Check if the post request has the file part
    if 'files[]' not in request.files:
        return 'No file part in the request'

    files = request.files.getlist('files[]')
    
    # Check if the user has selected files
    if not files or files[0].filename == '':
        return 'No files selected'
    file_list_output = []

    for file in files:
        if file:
            # Save each file to a specific path
            filename = file.filename
            file_list_output.append(filename)
            save_path = os.path.join(PDF_File_Directory, filename)
            file.save(save_path)

    return render_template('index.html', files = file_list_output)

@app.route('/generate_summary', methods=['POST'])
def generate_summary():
    # Retrieve data from request

    summary_length_radio_input = request.form['length']
    if summary_length_radio_input == 'short':
        summary_length = "using 1-3 sentences"
    elif summary_length_radio_input == 'medium':
        summary_length = "using 3-6 sentences"
    elif summary_length_radio_input == 'long':
        summary_length = "using 6-10 sentences"
    else:
        summary_length = "using 15 sentences"
    response = summarizer.get_response("Generate a summary of the text " + summary_length + ".")
    print("generate summary done!")
    return response
    # return render_template('response.html', response=response)

if __name__ == '__main__':
    # app.run(debug=True)
    generate_summary()
