import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ISTKHARX import LOGGER, app, userbot
from ISTKHARX.core.call import ISTKHAR
from ISTKHARX.misc import sudo
from ISTKHARX.plugins import ALL_MODULES
from ISTKHARX.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ISTKHARX.plugins" + all_module)
    LOGGER("ISTKHARX.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴀʟʟ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await ISTKHAR.start()
    try:
        await ISTKHAR.stream_call("https://te.legra.ph/file/39b302c93da5c457a87e3.mp4")
    except NoActiveGroupCall:
        LOGGER("ISTKHARX").error(
            "ʙsᴅᴋ ᴠᴄ ᴛᴏ ᴏɴ ᴋᴀʀʟᴇ  ʟᴏɢ ɢʀᴏᴜᴘ\ᴄʜᴀɴɴᴇʟ ᴋɪ.\n\n ᴏɴ ᴋᴀʀᴋᴇ ᴀᴀ ᴛᴀʙ ᴛᴀᴋ ʙᴏᴛ ʙᴀɴᴅ ᴋᴀʀ ʀʜᴀ ʜᴏᴏɴ..."
        )
        exit()
    except:
        pass
    await ISTKHAR.decorators()
    LOGGER("ISTKHARX").info(
        "ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ, ɴᴏᴡ ɢɪʙ ʏᴏᴜʀ ɢɪʀʟғʀɪᴇɴᴅ ᴄʜᴜᴛ ɪɴ @ll_ISTKHAR_BABY_lll"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ISTKHARX").info("ᴍᴀᴀ ᴄʜᴜᴅᴀ ᴍᴀɪɴ ʙᴏᴛ ʙᴀɴᴅ ᴋᴀʀ ʀʜᴀ Lb Mᴜsɪᴄ Bᴏᴛ...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
