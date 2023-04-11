from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Connect to MindsDB
# mdb = mindsdb_sdk.Mindsdb()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the data from the POST request.
        data = request.form.to_dict()
        # Use MindsDB to make predictions based on historical data frrom docs/main.csv file

        print(data)
        return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)
