from flask import Flask,Request
import serial

app=Flask(__name__)

ser=serial.Serial('COM3',9600)
while True:
    ser.write("yes")
    data = ser.readline().decode().strip()
    print("Data from Arduino:", data)
    ser.write("yes")
    

ser.close()

@app.route('/')
def home():
    return "<h1>hello</h1>"



if __name__== "__main__":
    app.run(debug=True)