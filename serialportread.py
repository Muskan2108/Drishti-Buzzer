import serial

ser = serial.Serial('COM6','38400')
ser.write('0')
while True:
    if ser.inWaiting():
        txt=ser.read()
        print txt
        fi=open('buzzer.txt','a')
        fi.write(txt)
        if txt=='B' or txt=='b':
            fi.write('\n')
        fi.close()
    f=open('test.txt','r')
    lines=f.readlines()
    if lines[len(lines)-1]=='0':
        ser.write('0')
    if lines[len(lines)-1]=='1':
        ser.write('1')
    f.close()  
