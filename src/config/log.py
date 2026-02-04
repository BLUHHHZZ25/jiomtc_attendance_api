from fastapi.logger import logger as fastapi_logger
import logging
from logging.config import dictConfig

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class InterceptHandler(logging.Handler):
    def emit(self, record):
        fastapi_logger.opt(depth=6, exception=record.exc_info).log(record.levelname, record.getMessage())

fastapi_logger.handlers = [InterceptHandler()]

logger = logging.getLogger(__name__)