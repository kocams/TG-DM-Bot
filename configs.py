import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", 12345))

    API_HASH = str(os.environ.get("API_HASH", ""))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", ""))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1428968542))

    START = str(os.environ.get("START_TEXT", "Bu botu kullanarak benimle iletişime geçebilirsin"))

    HELP = str(os.environ.get("HELP_TEXT", "Faydalı linkler 🤙"))

    DONATE = str(os.environ.get("DONATE_TEXT", ""))

    DONATE_LINK = str(os.environ.get("DONATE_LINK", ""))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", "https://muhendisherif.com/"))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", "https://discord.com/invite/grovestreet07"))

