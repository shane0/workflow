from flask import Flask, render_template
import os

# Define the path to the templates folder
template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
print(template_folder)

# Create the Flask app and specify the template folder
app = Flask(__name__, template_folder=template_folder)



@app.route('/<message>')
def index(message):
    return render_template('flask_tools.html', message=message)

@app.route('/two/<message1>/<message2>')
def two(message1, message2):
    return render_template('flask_tools.html', message1=message1, message2=message2)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)
