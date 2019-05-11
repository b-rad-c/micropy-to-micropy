from pyb import I2C

i2c = I2C(1)
i2c.init(I2C.SLAVE, addr=0x42)


def send():
    i2c.send('hello from pyboard', timeout=5000)


def recv():
    print(i2c.recv(16, timeout=5000))


print('initialized...')
