import pytest
from television import *

class Test:
    def setup_method(self):
        self.tvl = Television()

    def teardown_method(self):
        del self.tvl
    def test_init(self):
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_init(self):
        self.tvl.power()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tvl.power()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        pass
    def test_channel_up(self):
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tvl.power()
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.tvl.channel_up()
        self.tvl.channel_up()
        self.tvl.channel_up()
        assert self.tvl.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        pass



