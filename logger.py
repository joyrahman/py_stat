import logging


def get_logger(file_name):
    
    # logging configuration
    logger = logging.getLogger('pid_application')
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = logging.FileHandler(file_name)
    fh.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)


    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    #### START OF EXECUTION  #####
    #logger.info('execution started')

    # return the logger

    return logger
