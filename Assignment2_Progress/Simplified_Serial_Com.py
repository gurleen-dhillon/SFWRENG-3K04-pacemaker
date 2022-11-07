import serial
ser = serial.Serial("COM4",115200)

if ser.isOpen():
    ser.close()

ser.open()
sync = 0x10
data2 = 0x30
message = bytearray()
message.append(sync)
message.append(data2)
ser.write(message)
ser.close()
