import configparser


config = configparser.ConfigParser()
config.read('config.ini')

CONFIG_SECTION_LINE_BOT = 'line-bot'
CONFIG_SECTION_UNSPLASH = 'unsplash'


def get_config(section_name: str, key: str):
    return config.get(section_name, key)