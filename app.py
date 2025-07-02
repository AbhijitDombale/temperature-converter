from flask import Flask, render_template, request

app = Flask(__name__)

def convert_single_temperature(value, from_unit, to_unit):
    value = float(value)

    # Convert input to Celsius first
    if from_unit == 'Fahrenheit':
        value = (value - 32) * 5/9
    elif from_unit == 'Kelvin':
        value = value - 273.15

    # Convert from Celsius to target unit
    if to_unit == 'Fahrenheit':
        return f"{(value * 9/5) + 32:.2f} °F"
    elif to_unit == 'Kelvin':
        return f"{value + 273.15:.2f} K"
    else:
        return f"{value:.2f} °C"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        temp_value = request.form['temp_value']
        from_unit = request.form['temp_unit']
        to_unit = request.form['convert_to']

        try:
            result = convert_single_temperature(temp_value, from_unit, to_unit)
        except ValueError:
            result = {"Error": "Please enter a valid number!"}

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
