import machine
import utime

potentiometer = machine.ADC(26) #deklarasi pin yg dipakai
#conversion_factor = 3.3 / (65535)
pam = machine.Pin(27, machine.Pin.OUT)
led = machine.Pin(6, machine.Pin.OUT)

while True:
    RH = potentiometer.read_u16() 
    kelembaban = (100-(RH/65535.00)*100) #perhitungan dalam persen
    print(kelembaban)
    utime.sleep(2)
    if kelembaban < 80:#kelembaban kurang dari 80% led menyala
        led.value(1)
        pam.value(1)
    else : #kelembaban lebih dari 80% led mati 
        led.value(0)
        pam.value(0)