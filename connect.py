from serial import Serial
import time
print("Libraries OK")

'''set the serial to connect to the arduino (you should change the port)'''
ser =Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    timeout=None)
def adddata(data):
    '''a function to add the data to the text file'''
    date=time.time()
    h=str(data)+','+str(date)+'\n'
    fh = open('example.txt', 'a')
    fh.write(h) 
    fh.close 
while True:
    ''' infinit loop'''
    while(ser.inWaiting()==0):
        '''wait for the data from serial'''
        a=float(ser.readline().decode('utf-8'))
         '''read and decode the data'''
        print(a)
        print("emre")
         '''ahe data to the txt file'''

