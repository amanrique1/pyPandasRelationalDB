import logging
from pyPandasRelationalDB.test import testCase1

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    logging.debug('Starting package execution')
    testCase1()
    logging.debug('Ending package execution')