# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
from my_api import functions
# touchAPP(0.1,0.9)
# login('13422883445','123456')
