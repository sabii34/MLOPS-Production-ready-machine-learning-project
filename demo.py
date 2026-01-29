from Us_Visa.logger import logging
import sys


from Us_Visa.exception import USvisaException, UsVisaException

#  logging.info("Demo file is being run")
try:
    a = 2 / 100
except Exception as e:
    raise USvisaException(e, sys)


