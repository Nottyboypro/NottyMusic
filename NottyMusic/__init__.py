from NottyMusic.core.bot import Notty
from NottyMusic.core.dir import dirr
from NottyMusic.core.git import git
from NottyMusic.core.userbot import Userbot
from NottyMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Notty()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
