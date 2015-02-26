if __name__ == '__main__':
    import os.path
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
import json
import pickle
from admclient.adm import *


class ADMClientTest(unittest.TestCase):
    """ API tests. """

    def setUp(self):
        self.adm = ADM('client_id', 'client_secret')
        #TODO


if __name__ == '__main__':
    unittest.main()
