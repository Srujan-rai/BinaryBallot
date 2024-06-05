from flask import Flask, request, jsonify
import serial
import time

app = Flask(__name__)

try:
    # Adjust the port to match your Arduino connection
    arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit(1)

@app.route('/send_yes', methods=['POST'])
def send_yes():
    arduino.write(b'yes\n')
    return jsonify({'status': 'yes sent'})

@app.route('/button_status', methods=['GET'])
def button_status():
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').strip()
        return jsonify({'button': data})
    return jsonify({'button': 'none'})

if __name__ == '__main__':
    app.run()
