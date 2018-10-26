# This is a basic application log generator
# It is used to simulate log file generation
# Features:
#   - generate 5 log levels messages 
#   - specify time frequency for each log level
#   - uses threads as timers for each log level
#   - log record includes the following fields:
#       timestamp
#       log level
#       log message
#       store id
#       app instance id (multiple app instances per store)
#       component name
#       source file name
#       function name
#       source line number
#   - rotating file logs (max size: 100kb, bkp count: 5)

import inspect
import logging
import logging.handlers
import random
from threading import Timer
import utility
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--storeId", required=False, help="Example: --storeId 36")
args = parser.parse_args()

environment = utility.Environment("config.json", args)

def function_logger(file_level, console_level = None):
    formatString = '[%(asctime)s][%(levelname)s] %(message)s - [id:%(storeId)s][instance:%(instanceId)s] - [%(component)s][%(sourceFile)s][%(functionName)s][ln:%(lineNumber)s]'
    function_name = "app" #inspect.stack()[1][3]
    logger = logging.getLogger(function_name)
    logger.setLevel(logging.DEBUG) #By default, logs all messages

    if console_level != None:
        ch = logging.StreamHandler() #StreamHandler logs to console
        ch.setLevel(console_level)
        ch_format = logging.Formatter(formatString)
        ch.setFormatter(ch_format)
        logger.addHandler(ch)

    fh = logging.handlers.RotatingFileHandler("{0}.log".format(function_name), maxBytes=100000, backupCount=5)
    fh.setLevel(file_level)
    fh_format = logging.Formatter(formatString)
    fh.setFormatter(fh_format)
    logger.addHandler(fh)

    return logger

f1_logger = function_logger(logging.DEBUG, logging.DEBUG)

def switch(x):
    return {
        'info': (0.025, 'info', 'any info message'),
        'debug': (0.25, 'debug', 'any debug message'),
        'warning': (0.5, 'warning', 'Here is a warning message'),
        'error': (1, 'error', 'It is an error message'),
        'critical': (2, 'critical', 'ATTENTION: This is a critical issue!')
    }.get(x, (0.1, 'info', 'any info message')) # 1 is default if x not found

def createLog(logType='info'):
    typeData = switch(logType)
    config = environment.configParser.config
    storeId = "1" if not 'storeId' in config else config['storeId']
    d = {
        'storeId': storeId,
        'instanceId': str(random.randrange(1, 8)),
        'component': 'COMP-' + str(random.randrange(1, 14)),
        'sourceFile': random.choice(['file-'+str(random.randrange(1, 14))+'.c' for i in range(20)]),
        'functionName': random.choice(['function-'+ str(random.randrange(1, 14)) for i in range(20)]),
        'lineNumber': str(random.randrange(1, 1000))
    }
    # duration is in seconds
    t = Timer(typeData[0] * 60, createLog, args=[logType])
    t.start()
    # example: f1_logger.warning('warn message')
    getattr(f1_logger, typeData[1])(typeData[2], extra=d)
    # wait for time completion
    #t.join()

def f1():
    createLog('info')
    createLog('debug')
    createLog('warning')
    createLog('error')
    createLog('critical')

def main():
    f1()
    logging.shutdown()

main()
