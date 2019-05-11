###Micropy to Micropy
A simple example of i2c 2-way communication between two micropython enabled microcontrollers.
In this example I am using a pyboard v1.1 as the slave and a lopy4 from pycom as the master.
According to this page https://learn.adafruit.com/micropython-hardware-i2c-devices/i2c-slave
the pyboard is the only micropython enabled controller that can act in slave mode currently.

pyboard is on v1.10 of micropython, lopy4 is on v1.18.1.r1 firmware

### usage
After loading the code and doing a soft-reset, run the following examples by opening repl sessions on each.

**lopy4 to pyboard**

on the pyboard run:

    recv()

then within the set timeout (5 seconds) run this on the lopy4:

    send()
    
the pyboard will show:

    >>> recv()
    b'hello from lopy4'
    
**pyboard to lopy4**

on the pyboard run:

    send()

then within the set timeout (5 seconds) run this on the lopy4:

    recv()
    
the lopy4 will show:
    
    >>> recv()
    b'hello from pyboard'
    
### errors
on the pyboard, if you call send or recv without running the corresponding functions on the lopy4 the i2c class will raise an OSError after the timeout period.

    >>> send()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "main.py", line 8, in send
    OSError: [Errno 110] ETIMEDOUT
    >>> recv()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "main.py", line 12, in recv
    OSError: [Errno 110] ETIMEDOUT
    
The lopy4 behaves slightly differently because it does not have the timeout parameter that the pyboard does.
The send function will raise the exception immediately if the slave is not already waiting, and the
recv function will raise the exception after ~25 seconds (timeout period does not appear to be configurable) 

    >>> send()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "main.py", line 7, in send
    OSError: I2C bus error
    >>> recv()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "main.py", line 10, in recv
    OSError: I2C bus error
