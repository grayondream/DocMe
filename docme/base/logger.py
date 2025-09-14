import spdlog
from .singleton import SingletonBase

class Logger(SingletonBase):
    def __init__(self, level=spdlog.LogLevel.DEBUG, log_file=None):
        if not hasattr(self, 'initialized'):
            if log_file:
                self.logger = spdlog.FileLogger("file_logger", log_file)
            else:
                self.logger = spdlog.ConsoleLogger("console_logger")
            self.logger.set_level(level)
            self.logger.set_pattern("%Y-%m-%d %H:%M:%S [thread %t] %v")
            self.initialized = True

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

def logi(message):
    Logger().info(message)
    
def loge(message):
    Logger().error(message)
    
def logd(message):
    Logger().debug(message)
    
# 使用示例
if __name__ == "__main__":
    # 创建一个日志实例，输出到控制台
    logger1 = Logger()
    logger1.info("This is an info message from logger1.")
    logger1.error("This is an error message from logger1.")
    logger1.debug("This is a debug message from logger1.")

    # 创建一个新的日志实例，输出到文件
    # logger2 = Logger(spdlog.LogLevel.INFO, "logs.txt")
    # logger2.logi("This is an info message from logger2, written to file.")
    # logger2.loge("This is an error message from logger2, written to file.")

    