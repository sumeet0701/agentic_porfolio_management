import logging
import os
from datetime import datetime

def setup_logging(log_dir='logs'):
    """
    Set up logging configuration with a timestamped log file.

    Args:
        log_dir (str): Directory to store log files. Defaults to 'agentic_pm/logs'.
    """
    # Create log directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)

    # Generate log file name with current timestamp
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    logs_path = os.path.join(log_dir, LOG_FILE)

    # Configure logging
    logging.basicConfig(
        filename=logs_path,
        format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )

    # Return a logger object
    return logging.getLogger(__name__)