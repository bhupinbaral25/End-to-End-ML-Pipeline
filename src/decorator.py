import io
import sys
import pickle
import logging
import pandas as pd
from functools import wraps
import warnings

from src.utils import CONFIG, get_today_date

today_date = get_today_date()
log_file = f"./log/{today_date}_{CONFIG['log_file']}"

logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def data_error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")

        except pd.errors.ParserError:
            print("Error: Unable to parse data. Please check the file format.")

        except pd.errors.EmptyDataError:
            print("Error: The file is empty. Please provide data in the file.")

        except Exception as e:
            print(f"Error: An unexpected error occurred: {e}")

    return wrapper


def loger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        warnings.filterwarnings("ignore")
        logger = logging.getLogger(func.__name__)

        class LogFileHandler(logging.StreamHandler):
            def emit(self, record):
                try:
                    msg = self.format(record)
                    with open(log_file, 'a') as log:
                        log.write(f"{msg}\n")
                except (KeyboardInterrupt, SystemExit):
                    raise
                except:
                    self.handleError(record)

        stdout_handler = LogFileHandler(sys.stdout)
        stderr_handler = LogFileHandler(sys.stderr)
        logger.addHandler(stdout_handler)
        logger.addHandler(stderr_handler)

        logger.info("Function %s was called with arguments: %s, %s", func.__name__, args, kwargs)

        try:
           
            stdout_io = io.StringIO()
            sys.stdout = stdout_io

            result = func(*args, **kwargs)
            printed_output = stdout_io.getvalue()
            sys.stdout = sys.__stdout__
            if printed_output:
                with open(log_file, 'a') as log:
                    log.write(f"{printed_output}\n")

            logger.info("Function %s returned: %s", func.__name__, result)

            return result
        
        except Exception as e:
            logger.exception("Function %s raised an exception: %s", func.__name__, e)
            sys.stdout = sys.__stdout__

    return wrapper


def pickle_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print(f"Error: File not found at '{args[0]}'.")
        except pickle.PickleError:
            print("Error: Unable to load pickled data.")
        except Exception as e:
            print("An unexpected error occurred:", e)

    return wrapper


