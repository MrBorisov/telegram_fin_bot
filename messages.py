help_message = 'Для того, чтобы изменить текущее состояние пользователя, ' \
               'отправь команду "/hand ,/stat, /conf"' \
               'Чтобы сбросить текущее состояние, отправь "/setstate".'

start_message = 'Привет!\n' + help_message
invalid_key_message = 'Ключ "{key}" не подходит.\n' + help_message
hand_mode_msg = 'Введите сумму'
stat_mode_msg = 'Статистика'
config_mode_msg = 'Настройки'
state_reset_message = 'Состояние успешно сброшено'
state_change_success_message = 'Текущее состояние успешно изменено'

MESSAGES = {
    'start': start_message,
    'help': help_message,
    'invalid_key': invalid_key_message,
    'hand_mode': hand_mode_msg,
    'stat': stat_mode_msg,
    'state_change': state_change_success_message,
    'config': config_mode_msg,
    'state_reset': state_reset_message,

}
