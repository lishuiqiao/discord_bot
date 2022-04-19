import logging
import os

# 路径获取
cur_dir = os.path.abspath(__file__).rsplit("/", 2)[0]

dir_path = os.path.join(cur_dir, 'logs')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

log_path = os.path.join(dir_path, "bot.log")

# encoding='utf-8'
logging.basicConfig(filename=log_path, level=logging.INFO,
    filemode = 'a', format='%(levelname)s:%(asctime)s:%(message)s', datefmt='%Y-%d-%m %H:%M:%S')


def get_logger():
    return logging.getLogger()
