from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('converter.html')

@app.route('/convert', methods=['POST'])
def convert():
    conversion_type = request.form['conversion_type']
    value = float(request.form['value'])
    result = ""

    if conversion_type == "temperature":
        result = f"{value}°F is {(value - 32) * 5 / 9:.2f}°C"
    elif conversion_type == "weight":
        result = f"{value} lbs is {value * 0.453592:.2f} kg"
    elif conversion_type == "volume":
        result = f"{value} oz is {value * 29.5735:.2f} ml"
    elif conversion_type == "distance":
        result = f"{value} miles is {value * 1.60934:.2f} km"
    else:
        result = "Invalid conversion type."

    return render_template('converter.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
