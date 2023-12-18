# CMPE 256 Team Project

## Project Title: Research Paper Summarization

This is the README for the team project for the CMPE256 class. This submission is for the Bay Area Rockers team, which consists of the following team members:

1. Shawn Chumbar
2. Sajal Agarwal
3. Dhruval Shah

## Project Description

This project introduces a flask-based web application designed for the summarizzation of complex PDF documents using Natural Language Processing (NLP) techniques. The application leverages machine learning models to parse, interpret, and condense extensive textual data, aiming for high-precision summaries. Some Challenges include extracting relevant information from unstructured text and condensing it without losing essential meaning.

### Project Deliverables

Please see below for the list of deliverables related to this project.

1. **README.md**: README file detailing this project.
2. **CMPE256_team project.ipynb**: Google Colab python notebook containing the code for this project.
3. **flask_app**: Folder containing the files for the flask app.
4. **Dataset**: Folder containing the Research PDFs used for this project.
5. **256_RPS_Presentation.pptx**: PowerPoint presentation for this project.
6. **CMPE256 Team Project Demo.ipynb**: Google Colab python notebook containing the code for the demo. Please note that we have transferred the code in here to the flask_app.
7. **CMPE 256 Project Report.pdf**: PDF file of the project report.

### Installation Instructions

The following installation instructions are specific to MacOS. Please note that the instructions may vary depending on your operating system.
The instructions below assume that you have python installed on your machine and have the python pip package manager installed.

To get the project running, please follow the steps below:

1. Clone the repository
2. `cd flask_app`
3. `pip install -r requirements.txt`
4. Change the `directory_path` and `OPENAI_API_KEY` variables within the `summarizer.py` file.
5. Change the `PDF_File_Directory` variable in the `app.py` file.
6. `flask run`