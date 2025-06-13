import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

class Logger:
    def __init__(self, log_name="agentic_pm", log_level=logging.INFO):
        self.log_name = log_name
        self.log_level = log_level
        self.logger = self._setup_logger()
    
    def _setup_logger(self):
        # Create logs directory if it doesn't exist
        logs_dir = os.path.join(os.getcwd(), "logs")
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        
        # Create logger
        logger = logging.getLogger(self.log_name)
        logger.setLevel(self.log_level)
        
        # Clear existing handlers if any
        if logger.handlers:
            logger.handlers.clear()
        
        # Create file handler with rotating file
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        log_file = os.path.join(logs_dir, f"{self.log_name}_{today}.log")
        file_handler = RotatingFileHandler(
            log_file, maxBytes=10*1024*1024, backupCount=5
        )
        
        # Create console handler
        console_handler = logging.StreamHandler()
        
        # Create formatter and add it to the handlers
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def info(self, message):
        self.logger.info(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def debug(self, message):
        self.logger.debug(message)
    
    def critical(self, message):
        self.logger.critical(message)

# Create a default logger instance
logger = Logger()
