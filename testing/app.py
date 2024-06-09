from flask import Flask, jsonify, render_template, redirect, url_for
import serial
import threading

app = Flask(__name__)

button_status = "none"
current_page = 1
pages = ["index1.html", "index2.html", "index3.html"]

# Attempt to establish a serial connection
ser = None
try:
    ser = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
    print("Serial connection established.")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")

def read_from_serial():
    global button_status, current_page
    while True:
        if ser and ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            button_status = data
            print(f"Received: {data}")
            if data == "done":
                current_page = (current_page % len(pages)) + 1

if ser:
    thread = threading.Thread(target=read_from_serial)
    thread.daemon = True
    thread.start()

@app.route('/')
def index():
    return redirect(url_for('page', page_number=1))

@app.route('/page/<int:page_number>')
def page(page_number):
    global current_page
    current_page = page_number
    return render_template(pages[page_number - 1])

@app.route('/send_yes', methods=['POST'])
def send_yes():
    try:
        if ser:
            ser.write(b'yes\n')
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

@app.route('/next_page', methods=['POST'])
def next_page():
    global current_page
    current_page = (current_page % len(pages)) + 1
    return jsonify({'next_page': url_for('page', page_number=current_page)})

if __name__ == '__main__':
    app.run()
