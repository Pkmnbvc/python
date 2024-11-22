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
        self.tvl.power()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 0'

        self.tvl.volume_up()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 1'

        self.tvl.mute()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 0'


        self.tvl.mute()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 1'

        # Test when TV is off and mute is invoked
        self.tvl.power()
        self.tvl.mute()
        assert str(self.tvl) == 'Power = False, Channel = 0, Volume = 0'

        # Test unmute when TV is off
        self.tvl.mute()
        assert str(self.tvl) == 'Power = False, Channel = 0, Volume = 0'

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
        self.tvl.channel_down()
        assert str(self.tvl) == 'Power = False, Channel = 0, Volume = 0'


        self.tvl.power()
        self.tvl.channel_down()
        assert str(self.tvl) == 'Power = True, Channel = 99, Volume = 0'


        self.tvl.channel_down()
        assert str(self.tvl) == 'Power = True, Channel = 98, Volume = 0'

    def test_volume_up(self):


        self.tvl.volume_up()
        assert str(self.tvl) == 'Power = False, Channel = 0, Volume = 0'


        self.tvl.power()
        self.tvl.volume_up()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 1'


        for _ in range(100):
            self.tvl.volume_up()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 100'


        self.tvl.mute()
        self.tvl.volume_up()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 1'

    def test_volume_down(self):

        # TV off, no change
        self.tvl.volume_down()
        assert str(self.tvl) == 'Power = False, Channel = 0, Volume = 0'


        self.tvl.power()
        self.tvl.volume_up()
        self.tvl.volume_up()
        self.tvl.volume_down()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 1'


        self.tvl.volume_down()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 0'


        self.tvl.mute()
        self.tvl.volume_down()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 0'

    def test_power_and_channel(self):

        self.tvl.channel_up()
        assert str(self.tvl) == 'Power = False, Channel = 0, Volume = 0'


        self.tvl.power()
        self.tvl.channel_up()
        assert str(self.tvl) == 'Power = True, Channel = 1, Volume = 0'


        for _ in range(100):
            self.tvl.channel_up()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 0'

    def test_power_and_volume(self):
        self.tvl.volume_up()
        assert str(self.tvl) == 'Power = False, Channel = 0, Volume = 0'


        self.tvl.power()
        self.tvl.volume_up()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 1'


        for _ in range(100):
            self.tvl.volume_up()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 100'


        self.tvl.mute()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 0'

    def test_power_and_mute(self):

        self.tvl.power()
        self.tvl.mute()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 0'

        self.tvl.mute()
        assert str(self.tvl) == 'Power = True, Channel = 0, Volume = 1'

        self.tvl.power()
        self.tvl.mute()
        assert str(self.tvl) == 'Power = False, Channel = 0, Volume = 0'



