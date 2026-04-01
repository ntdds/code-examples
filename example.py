# Define a function named NT_Serial with parameters "com" and "command".
def NT_Serial(com, command):

    # Import the serial class from the PySerial library, instantiate a serial class
    # object named "tep" and then load the "tep" object with serial port parameters.
    import serial
    tep = serial.Serial()
    tep.port = com
    tep.baudrate = 19200
    tep.parity = serial.PARITY_NONE
    tep.stopbits = serial.STOPBITS_ONE
    tep.timeout = 1

    # Open the "tep" serial port. If there is a problem opening the port, print an error message.
    try:
        tep.open()
    except Exception as e:
        print("error opening serial port: \n" + str(e))
        return

    # Write the contents of the "command" variable to the "tep" serial port. The encode() method
    # creates HEX values for these characters using the UTF-8 code set. Then tep.readline() stores
    # the first line returned from the COM port in the "temp" variable. The decode() method
    # converts the returned HEX values to text characters, also based on the UTF-8 code set.
    tep.write(command.encode())
    temp = tep.readline()
    temp = temp.decode()

    # Create a variable "c" and a variable "recentVal". The tep.readline() method stores the second
    # line returned from the COM port (if there was more than one line returned) in "recentVal".
    # The while loop checks to see if there was more than one line returned. If more than one line
    # was returned then the lines are stored in "temp" separated by a "c" string. The temp.split(c)
    # method removes the "c" strings, separates the lines with commas and prints them to the screen.
    c = "!$"
    recentVal = tep.readline()
    recentVal = recentVal.decode()
    while (recentVal != ""):
        temp = temp + c + recentVal
        recentVal = tep.readline()
        recentVal = recentVal.decode()
    Lines = temp.split(c)
    m = Lines
    print(m)
    tep.close()

# Load the NT_Serial() function with the correct COM port and 409B command.
# COM port and command can be passed as command-line arguments, e.g.:
#   python example.py COM3 "f0 15\n"
# If no arguments are provided, defaults to COM3 and "f0 15\n".
import sys
com_port = sys.argv[1] if len(sys.argv) > 1 else "COM3"
command  = (sys.argv[2] if len(sys.argv) > 2 else "f0 15") + "\n"
NT_Serial(com_port, command)
