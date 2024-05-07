import logging


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="basic.log",
     )
    
    logging.debug("This message is a debug message.")
    logging.info("This message is an info message.")
    logging.warning("This message is a warning message.")
    logging.error("This message is an error message.")
    logging.critical("This message is a critical message.")
    

if __name__ == "__main__":
    main()
