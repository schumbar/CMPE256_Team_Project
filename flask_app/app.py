from flask import Flask, render_template, request
import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def submit_query():
    user_query = request.form['user_query']
    response = summarizer.get_response(user_query)
    return render_template('response.html', response=response)

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
