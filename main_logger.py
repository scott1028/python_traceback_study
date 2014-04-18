# coding:utf-8

import logging

logger = logging.getLogger(__name__)

def some_method():
    logger.debug('begin of some_method')

def main():
	# 當 logger 設定為最高級別的時候上面所有的 debug 級別的 log 訊息就不會顯示！
    # logging.basicConfig(level=logging.CRITICAL)
    logging.basicConfig(level=logging.DEBUG)
    some_method()
 
if __name__ == '__main__':
    main()
