from bot.get_cfg import get_config

class Config(object):
    # You can keep this default
    SESSION_NAME = get_config("SESSION_NAME", "AHCompressorBot")
    # AHCompressBot....
    # sucks Dude
    APP_ID = '16732227' # Updated with your API ID
    API_HASH = "8b5594ad7ad37f3a0a7ddbfb3963bb51"  # Updated with your API HASH
    LOG_CHANNEL = -1002871989925  # Updated with your log channel ID
    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None) # Without `@` LOL
    # Get these values from my.telegram.org
    AUTH_USERS = {5868426717}
    # auth users jdk 
    TG_BOT_TOKEN = "7141984677:AAFztMNvuW-CYbsM1Ydq0zTZ6OQumWSEHTs"  # Updated with your bot token
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "/app/downloads")
    # Telegram maximum file upload size
    BOT_USERNAME = "hanime_encoding_bot"  # Updated with your bot username
    MAX_FILE_SIZE = 6440253535
    TG_MAX_FILE_SIZE = 6440253535
    FREE_USER_MAX_FILE_SIZE = 6440253535
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "☀️")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "☼")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
    # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", True)
