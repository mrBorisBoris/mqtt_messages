import logging

logging.basicConfig(level=logging.INFO,
                    filename="py_log.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

# logging.error('OSError: [Errno 51] Network is unreachable', exc_info=True)
# logging.error('--- Logging error ---', exc_info=True)