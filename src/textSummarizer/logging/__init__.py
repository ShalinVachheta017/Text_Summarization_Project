import os
import sys
import logging

# Set up logging
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # Format of the log
log_dir = "logs" # Directory to store logs
log_filepath = os.path.join(log_dir,"running_logs.log") # File to store logs
os.makedirs(log_dir, exist_ok=True) # Create the directory if it does not exist


# Configure the logger
logging.basicConfig(  # Configure the logger 
    level= logging.INFO, # Set the logging level
    format= logging_str, # Set the format of the log

    # Set the handlers to write the logs to a file and to the console
    handlers=[ 
        logging.FileHandler(log_filepath), # Write the logs to a file
        logging.StreamHandler(sys.stdout)  # Write the logs to the console
    ]
)

# Create a logger
logger = logging.getLogger("textSummarizerLogger")