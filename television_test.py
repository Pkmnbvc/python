import pytest
from television import *

class Test:
    def setup_method(self):
        self.tvl = Television()

    def teardown_method(self):
        del self.tvl

