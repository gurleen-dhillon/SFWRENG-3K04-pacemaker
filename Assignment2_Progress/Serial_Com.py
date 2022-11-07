import serial
ser = serial.Serial("COM4",115200)

if ser.isOpen():
    ser.close()

ser.open()
sync = 0x10
mode = 0x15
lrl = 0x01
url = 0x01
Vent_PW = 0x01
Atr_PW = 0x01
Vent_RP = 0x01
Atr_RP = 0x01
Vent_Amp = 0x01
Atr_Amp = 0x01

message = bytearray()

message.append(sync)
message.append(mode)
message.append(lrl)
message.append(url)
message.append(Vent_PW)
message.append(Atr_PW)
message.append(Vent_RP)
message.append(Atr_RP)
message.append(Vent_Amp)
message.append(Atr_Amp)
ser.write(message)
ser.close()
