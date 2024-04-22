from flask import Flask,Request
import serial

app=Flask(__name__)

#ser=serial.Serial('COM3',9600)



@app.route('/')
def home():
    #ser.write("yes")
    #data = ser.readline().decode().strip()
    print("Data from Arduino:")
    #ser.close()
    return "<h1>testing</h1>"



if __name__== "__main__":
    app.run(debug=True)