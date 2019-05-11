from machine import I2C
i2c = I2C(0, pins=('P9', 'P10'))
i2c.init(I2C.MASTER, baudrate=20000)


def send():
    i2c.writeto(0x42, 'hello from lopy4')

def recv():
    print(i2c.readfrom(0x42, 18))


print('initialized...')
