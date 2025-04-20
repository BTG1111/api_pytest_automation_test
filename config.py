import logging
import os

""" LOGGER """
LOG_FILE_DIRECTORY = "log"  # 定義log存放資料夾的資料夾名稱
LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), LOG_FILE_DIRECTORY)  # 定義log存放資料夾的完整路徑
if not os.path.exists(LOG_DIR_PATH):  # 確認log存放的資料夾是否存在， 不存在則創建
    os.makedirs(LOG_DIR_PATH)
LOG_NAME = "api_test.log"  # 定義log檔案名稱
LOG_PATH = os.path.join(LOG_DIR_PATH, LOG_NAME)
LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"  # 定義log各式
DEFAULT_LOG_LEVEL = logging.DEBUG  # 預設logging level

logger = logging.getLogger("my_logger")  # 創建一個 logger
logger.setLevel(DEFAULT_LOG_LEVEL)

if not logger.handlers:
    file_handler = logging.FileHandler(LOG_PATH, mode='w', encoding='utf-8')
    formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
