import logging

# ANSI escape codes for colors
RESET = "\x1b[0m"
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = [f"\x1b[1;3{m}m" for m in range(8)]


LEVEL_COLORS = {
    logging.DEBUG: CYAN,
    logging.INFO: GREEN,
    logging.WARNING: YELLOW,
    logging.ERROR: RED,
    logging.CRITICAL: MAGENTA,
}

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_color = LEVEL_COLORS.get(record.levelno, WHITE)
        record.levelname = f"{log_color}{record.levelname.lower()}{RESET}:"
        record.msg = f"{record.msg}"
        return super().format(record)

def setup_logger(name: str, level=logging.INFO) -> logging.Logger:
    """Set up a logger with color support."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(level)

        formatter = ColoredFormatter(
            "%(levelname)-8s %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
