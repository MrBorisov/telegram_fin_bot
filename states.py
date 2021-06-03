from aiogram.utils.helper import Helper, HelperMode, ListItem


class MyStates(Helper):
    mode = HelperMode.snake_case

    HAND_STATE = ListItem()
    STAT_STATE = ListItem()
    CONF_STATE = ListItem()
