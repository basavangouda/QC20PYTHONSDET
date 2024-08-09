"""
It's Highly recommended for us to store the complete application flow and exception
information to the file. This Process is called Logging

Logging Levels
CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
"""
import logging
logging.basicConfig(filename="abc.txt",filemode='w',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
print("Logging Demo")

logging.debug("Debug information")
logging.info("Info Information")
logging.warning("Warning information")
logging.error("Error Information")
logging.critical("Critical Information")
logging.info("********************************************")
logging.info("New request is coming")
try:
    x=int(input("Enter the Fnumber"))
    y=int(input("Enter the Snumber"))
    print("The Result is =:",x/y)

except ZeroDivisionError as msg:
    print("Can't divide by zero")
    logging.exception(msg)

except ValueError as msg:
    print("Please provide a Valid Value")
    logging.exception(msg)

logging.info("Request Processing is completed")

