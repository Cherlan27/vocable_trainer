import logging

logging.basicConfig(
    filename="backend_logs.log",
    level=logging.DEBUG,
    format="{asctime} - {levelname} - {message}",
    filemode="a",
    encoding="utf-8",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(
    logging.Formatter(
        "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
)

logger = logging.getLogger(__name__)
logger.addHandler(console_handler)
