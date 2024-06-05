from flask import Flask, request, jsonify, render_template
import serial
import threading

app = Flask(__name__)

# Shared variable to store button status
button_status = "none"
can_press_button = False

# Initialize the serial connection
ser = None
try:
    ser = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
    print("Serial connection established.")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")

# Function to read from serial in a separate thread
def read_from_serial():
    global button_status
    while True:
        if ser and ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            button_status = data
            print(f"Received: {data}")

# Start the serial reading thread
if ser:
    thread = threading.Thread(target=read_from_serial)
    thread.daemon = True
    thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_yes', methods=['POST'])
def send_yes():
    global can_press_button
    try:
        if ser:
            ser.write(b'yes\n')
            can_press_button = True
            return jsonify({'status': 'yes sent'})
        else:
            return jsonify({'error': 'Serial connection not established'})
    except serial.SerialException as e:
        return jsonify({'error': str(e)})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/button_status', methods=['GET'])
def button_status_route():
    return jsonify({'button': button_status})

if __name__ == '__main__':
    app.run()
