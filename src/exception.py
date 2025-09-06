# src/exception.py
import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys = None):
    try:
        if error_detail is None:
        
            return f"Error: {str(error)}"
        
        _, _, exc_tb = error_detail.exc_info()
        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            return f"Error occurred in python script name [{file_name}] line number [{line_number}] error message[{str(error)}]"
        else:
            return str(error)
    except Exception:
        return str(error)

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys = None):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
    
    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)