import logging
import os
from os import path
from from_root import from_root

from datetime import datetime
LOG_FILE_NAME = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

log_dir = "logs"
log_path = path.join(from_root(), log_dir, LOG_FILE_NAME)
os.makedirs(path.dirname(log_path), exist_ok=True)


logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)
