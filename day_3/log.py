# import logging

# logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
# logging.debug("this indicates the debugging information")
# logging.info("this indicates the important information")
# logging.error("this indicates error information")
# logging.warning("this indicates the warining information")
# logging.critical("this indicates the critical information")


import logging
logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
try:
    a=int(input("enter number a: "))
    b=int(input("enter number b: "))
    print(a/b)
except(ZeroDivisionError,ValueError) as message:
    print(message)
    logging.exception(message)
print("logging level is set up. check newfile.txt for log details")