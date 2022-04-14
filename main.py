
import sys
import glob
import time
import serial
import serial.tools.list_ports
import shutil


def get_list_of_serial_ports():
    return [comport.device for comport in serial.tools.list_ports.comports()]

def exit():
    sys.exit("done with the crowbar")

def main():
    # loop 10 times
    for t in range(0,11):
        #update list of all com ports
        ports = get_list_of_serial_ports()
        print(ports)
        #iterate through each port
        for port in ports:
            print('trying port: ',port)
            #connect to the port at 1200bps
            serial_port = serial.Serial()
            serial_port.baudrate = 1200
            serial_port.port = port        
            if serial_port.is_open:
                #if it is already open, then try to close it
                serial_port.close()
            
            serial_port.open() # try to open the port
            time.sleep(0.5) # wait 1/2 a second
            
            #disconnect from serial port to trigger bootloader mode
            serial_port.close()
    
    #exit
    exit()

if __name__ == '__main__':
    main()
    