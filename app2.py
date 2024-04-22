from flask import Flask, render_template, jsonify, request
import serial
import time

app = Flask(__name__)

# Initialize serial communication with Arduino
ser = serial.Serial('COM3', 9600)

# Define global variables to keep track of button presses and responses
button_pressed = False
button_response = None

# Define routes for each webpage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response')
def response():
    global button_pressed, button_response
    if button_pressed:
        return render_template('response.html', response=button_response)
    else:
        return "No response yet"

@app.route('/nextpage')
def next_page():
    return render_template('next_page.html')

# Route to receive button press from frontend
@app.route('/button_press', methods=['POST'])
def button_press():
    global button_pressed, button_response
    button_pressed = True
    # Send signal to Arduino
    ser.write(b"yes\n")
    # Wait for response from Arduino
    time.sleep(2)  # Adjust the delay as needed
    button_response = ser.readline().decode().strip()
    return jsonify({'success': True})

if __name__ == "__main__":
    app.run(debug=True)
