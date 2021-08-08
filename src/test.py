import os
import glob
import datetime
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import traceback
from logging import getLogger, StreamHandler, FileHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.addHandler(handler)
logger.setLevel(DEBUG)
logger.propagate = False

def get_timestamp() -> str:
    '''!
    @brief タイムスタンプ取得メソッド
    @return タイムスタンプ(str)
    '''
    timestamp = datetime.datetime.strftime(
        datetime.datetime.now(), "%Y/%m/%d %H:%M:%S")
    return f"[{timestamp}] {os.path.basename(__file__)}"


if __name__=="__main__":

    # Logger
    file_handler = FileHandler("./log/log.txt")
    file_handler.setLevel(DEBUG)
    logger.addHandler(file_handler)
    logger.debug(get_timestamp())

    logger.debug("test")
