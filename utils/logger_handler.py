import os

import logging

from datetime import datetime

from utils.path_tool import get_abs_path

# 日志保存的根目录
LOG_ROOT = get_abs_path("logs")

# 确保日志的目录存在
os.makedirs(LOG_ROOT, exist_ok=True)

# 日志的格式配置 error info debug
DEFAULT_LOG_FORMAT = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s -  %(filename)s:%(lineno)d - %(message)s',
)

def get_logger(
        name:str = "agent",
        console_level: int = logging.INFO, # 只有级别大于等于INFO的才会输出到控制台。
        file_level: int = logging.DEBUG,    # 只有级别大于等于DEBUG的才会输出到文件。
        log_file= None,
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 避免重复添加Handler，因为只要外面调用一次实例就会存在内存里，如果每个文件都要新的实例会很占内存。
    if logger.handlers:
        return logger

    # 控制台Handler
    console_handler = logging.StreamHandler()   # 设置为控制台的
    console_handler.setLevel(console_level)     # 设置输出等级
    console_handler.setFormatter(DEFAULT_LOG_FORMAT)        # 设置输出格式

    logger.addHandler(console_handler)

    if not log_file:        # 日志文件存放路径
        log_file = os.path.join(LOG_ROOT,f"{name}_{datetime.now().strftime('%Y%m%d')}.log")


    # 文件handler
    file_handler = logging.FileHandler(log_file,encoding="utf-8")
    file_handler.setLevel(file_level)
    file_handler.setFormatter(DEFAULT_LOG_FORMAT)

    logger.addHandler(file_handler)

    return logger

# 快速获取日志器
logger = get_logger()


if __name__ == "__main__":
    logger.info("信息日志")
    logger.error("错误日志")
    logger.warning("警报日志")
    logger.debug("调试日志")
