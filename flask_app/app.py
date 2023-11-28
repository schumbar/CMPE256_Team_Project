from flask import Flask, render_template, request
import script_272 # Replace with your actual script name

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def submit_query():
    user_query = request.form['user_query']
    response = script_272.get_response(user_query)  # Replace with the actual function call
    return render_template('response.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
