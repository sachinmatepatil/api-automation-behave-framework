import logging


def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler('framework.log'),  # Save logs to file
            logging.StreamHandler()  # Print logs on console
        ]
    )
    return logging.getLogger()

