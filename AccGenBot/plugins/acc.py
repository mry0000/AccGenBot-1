from . import *
from .. import *
from Configs import Config
from telethon import Button, events
from telethon.tl.functions.users import GetFullUserRequest
import random

btn =[
 [Button.url("Join Channel", Config.CHANNEL_URL)],
 [Button.inline("Back", data="gen")]
]

@AccGenBot.on(events.callbackquery.CallbackQuery(data="zee5"))
async def zee5(event):

    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.reply("**Join my channel to use me :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
           return

    hehe = await event.edit("<b><i>Generating Account</i></b>", parse_mode="HTML")

    with open('zee5.txt') as ha:
        sedloif = ha.read().splitlines()
    sed = random.choice(sedloif)
    user_s = await AccGenBot.get_me()
    user_us = user_s.username
    email, password = sed.split(":")

    await hehe.edit(f"<b><u>Zee5 Account</u></b>\n\n<b>Combo:</b> <code>{email}:{password}</code>\n<b>Email:</b> <code>{email}</code>\n<b>Password:</b> <code>{password}</code>\n\nGenerated By: @{event.sender.username}\nUser-ID: {event.sender_id}", buttons=btn, parse_mode="HTML")


@AccGenBot.on(events.callbackquery.CallbackQuery(data="voot"))
async def voot(event):

    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.reply("**Join my channel to use me :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
           return

    hehe = await event.edit("<b><i>Generating Account</i></b>", parse_mode="HTML")

    with open('voot.txt') as ha:
        sedloif = ha.read().splitlines()
    sed = random.choice(sedloif)
    user_s = await AccGenBot.get_me()
    user_us = user_s.username
    email, password = sed.split(":")

    await hehe.edit(f"<b><u>Voot Account</u></b>\n\n<b>Combo:</b> <code>{email}:{password}</code>\n<b>Email:</b> <code>{email}</code>\n<b>Password:</b> <code>{password}</code>\n\nGenerated By: @{event.sender.username}\nUser-ID: {event.sender_id}", buttons=btn, parse_mode="HTML")


@AccGenBot.on(events.callbackquery.CallbackQuery(data="wish"))
async def wish(event):

    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.reply("**Join my channel to use me :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
           return

    hehe = await event.edit("<b><i>Generating Account</i></b>", parse_mode="HTML")

    with open('wish.txt') as ha:
        sedloif = ha.read().splitlines()
    sed = random.choice(sedloif)
    user_s = await AccGenBot.get_me()
    user_us = user_s.username
    email, password = sed.split(":")

    await hehe.edit(f"<b><u>Wish Account</u></b>\n\n<b>Combo:</b> <code>{email}:{password}</code>\n<b>Email:</b> <code>{email}</code>\n<b>Password:</b> <code>{password}</code>\n\nGenerated By: @{event.sender.username}\nUser-ID: {event.sender_id}", buttons=btn, parse_mode="HTML")


@AccGenBot.on(events.callbackquery.CallbackQuery(data="shud"))
async def shud(event):

    soul = await verify(Config.CHANNEL_US, event, AccGenBot)
    if soul is False:
           await event.reply("**Join my channel to use me :)**", buttons=[[Button.url("Join Channel", Config.CHANNEL_URL)]])
           return

    hehe = await event.edit("<b><i>Generating Account</i></b>", parse_mode="HTML")

    with open('shud.txt') as ha:
        sedloif = ha.read().splitlines()
    sed = random.choice(sedloif)
    user_s = await AccGenBot.get_me()
    user_us = user_s.username
    email, password = sed.split(":")

    await hehe.edit(f"<b><u>Shudder Account</u></b>\n\n<b>Combo:</b> <code>{email}:{password}</code>\n<b>Email:</b> <code>{email}</code>\n<b>Password:</b> <code>{password}</code>\n\nGenerated By: @{event.sender.username}\nUser-ID: {event.sender_id}", buttons=btn, parse_mode="HTML")
