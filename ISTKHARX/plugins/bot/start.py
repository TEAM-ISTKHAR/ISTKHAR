import time

from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from ISTKHARX import app
from ISTKHARX.misc import _boot_
from ISTKHARX.plugins.sudo.sudoers import sudoers_list
from ISTKHARX.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from ISTKHARX.utils import bot_sys_stats
from ISTKHARX.utils.decorators.language import LanguageStart
from ISTKHARX.utils.formatters import get_readable_time
from ISTKHARX.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string
from ISTKHARX.misc import SUDOERS


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                photo=config.START_IMG_URL,
                caption=_["help_1"].format(config.SUPPORT_GROUP),
                protect_content=True,
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOG_GROUP_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                    parse_mode=ParseMode.HTML
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_GROUP),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOG_GROUP_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                    parse_mode=ParseMode.HTML
                )
    else:
        out = private_panel(_)
        UP, CPU, RAM, DISK = await bot_sys_stats()
        await message.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOG_GROUP_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                parse_mode=ParseMode.HTML
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


welcome_group = 2
@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    try:
        chat_id = message.chat.id
        for member in message.new_chat_members:
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=member.first_name,  
                            user_id=member.id        
                        )
                    ]
                ]
            )

            if isinstance(config.OWNER_ID, int):
                if member.id == config.OWNER_ID:
                    owner = f"""
            <b>#BOT_OWNER</b>
            
            𝙎𝙩𝙖𝙮 𝘼𝙡𝙚𝙧𝙩 ⚠️
            
            {member.mention} <b>Owner Of</b> {app.mention} <b>just joined the group</b> <code>{message.chat.title}</code>.
            
            <b>Support Me Here 👇🏻🤭💕</b>
            
            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            ┣★ <b>Update</b> -: @Music_World_Update
            ┣★ <b>Support</b> -: @Music_World_Support
            ┣★ <b>Bot Username</b> -: @{app.username}
            ┣★ <b>Join Here</b> -: @DPZ_STYLES_WORLD
            ┣★ <b>Note</b> -: This Is Only For Welcome For My Owner {member.mention}
            """
                    sent_message = await message.reply_text(owner, reply_markup=buttons, parse_mode=ParseMode.HTML)
                    await asyncio.sleep(180)
                    await sent_message.delete()
                    return

            elif isinstance(config.OWNER_ID, (list, set)):
                if member.id in config.OWNER_ID:
                    owner = f"""
            <b>#BOT_OWNER</b>
            
            𝙎𝙩𝙖𝙮 𝘼𝙡𝙚𝙧𝙩 ⚠️
            
            {member.mention} <b>Owner Of</b> {app.mention} <b>just joined the group</b> <code>{message.chat.title}</code>.
            
            <b>Support Me Here 👇🏻🤭💕</b>
            
            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            ┣★ <b>Update</b> -: @Music_World_Update
            ┣★ <b>Support</b> -: @Music_World_Support
            ┣★ <b>Bot Username</b> -: @{app.username}
            ┣★ <b>Join Here</b> -: @DPZ_STYLES_WORLD
            ┣★ <b>Note</b> -: This Is Only For Welcome For My Owner {member.mention}
            """
                    sent_message = await message.reply_text(
                        owner, 
                        reply_markup=buttons,
                        parse_mode=ParseMode.HTML
                    )
                    await asyncio.sleep(180)
                    await sent_message.delete()
                    return
            
                    return
                except Exception as e:
                    print(f"Error in welcome handler: {e}")
                    return



@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_GROUP,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
