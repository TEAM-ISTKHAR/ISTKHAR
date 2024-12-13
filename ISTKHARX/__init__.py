from ISTKHARX.core.bot import MUSARRAT
from ISTKHARX.core.dir import dirr
from ISTKHARX.core.git import git
from ISTKHARX.core.userbot import Userbot
from ISTKHARX.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = MUSARRAT()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
