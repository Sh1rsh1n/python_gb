from random import randint

def get_temprature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)

def get_preassure(sensor):
    return randint(730, 750) if sensor else randint(750, 770)

def get_wind_speed(sensor):
    return randint(0, 10) if sensor == 1 else randint(10, 20)

def data_collect(sensor = 1):
    return (get_temprature(sensor), get_preassure(sensor), get_wind_speed(sensor))

