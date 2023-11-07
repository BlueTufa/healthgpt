import logging
import os


# TODO: Parameterize logging format string
log_format = logging.Formatter("%(asctime)s [%(filename)s] [%(funcName)s] [%(levelname)s] [%(lineno)d] %(message)s")
log = logging.getLogger()
log.addHandler(logging.StreamHandler())

# TODO: change the default to WARN or INFO
log_level = os.environ.get("LOG_LEVEL", "DEBUG")
log.setLevel(log_level)
