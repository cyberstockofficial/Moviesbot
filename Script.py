#### This Code Was Devloped By @AM_ROBOTS ####

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://cyberstockofficial.in')
    START_TXT = environ.get("START_TXT", "Hello Guys I Am Movie X Bot By @Movies_Unloaded2\n\nUse Inline Features of This bot\n\nGive Me Any Movies, Anime, Web Series Name I Will Giev You telegram Files In All Quality! {}")
    HELP_TXT = """Hey {}
Here is Your help Guide."""
    ABOUT_TXT = """<b>✯ My Name: {}</b>
<b>✮ Bot Own By: <a href=https://t.me/Movies_Unloaded2></b>
<b>✮ Liberay: Pyrogram</b>
<b>✮ language: khud he bana liya new</b>
<b>✮ database: Apne Ghar pe store hai sare</b>
<b>✮ Bot server: Ghar pe host hai</b>

<b>✮ Telegram Channel: <a href=https://t.me/Movies_Unloaded2</a></b>"""
    SOURCE_TXT = """<b>NOTE:</b>

Source - Kya Karega Bro Khud bana ek new bot

<b>DEVS:</b>
- <a href=https://t.me/Movies_Unloaded2>@Movies_Unloaded2</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- <b><u>Filter is the feature were users can set automated replies for a particular keyword.</u></b>

<b>NOTE:</b>
<i>1. only admins can <b>add filters in a chat.</b>
2. alert buttons have a limit of <b>64 characters.</b></i>

<b>Commands and Usage:</b>
• <code>/filter</code> - <b>add a filter in chat</b>
• <code>/filters</code> - <b>list all the filters of a chat</b>
• <code>/del</code> - <b>delete a specific filter in chat</b>
• <code>/delall</code> - <b>delete the whole filters in a chat (chat owner only)</b>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- <b><u>Supports both url and alert inline buttons.</b></u>

<b>NOTE:</b>
<i>1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format</i>

<b>URL buttons:</b>
<code>[UPDATE](buttonurl:https://t.me/Movies_Unloaded2)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
<i>1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.</i>
 <b>I'll add all the files in that channel to my db.</b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- <b><u>Used to connect bot to PM for managing filters.</b></u>
- <b><u>it helps to avoid spamming in groups.</b></u>

<b>NOTE:</b>
<i>1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM</i>

<b>Commands and Usage:</b>
• <code>/connect</code>  - <b>connect a particular chat to your PM</b>
• <code>/disconnect</code>  - <b>disconnect from a chat</b>
• <code>/connections</code> - <b>list all your connections</b>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
<b>these are the extra features Only For Cyber Movie Bot</b>

<b>Commands and Usage:</b>
• <code>/id</code> - <b>get id of a specified user.</b>
• <code>/info</code>  - <b>get information about a user.</b>
• <code>/imdb</code>  - <b>get the film information from IMDb source.</b>
• <code>/search</code>  - <b>get the film information from various sources.</b>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
<b><i>This module only works for my admins</i></b>

<b>Commands and Usage:</b>
• <code>/logs</code> - <b>to get the rescent errors.</b>
• <code>/stats</code> - <b>To get status of files in db.</b>
• <code>/delete</code> - <b>to delete a specific file from db.</b>
• <code>/users</code> - <b>to get list of my users and ids.</b>
• <code>/chats</code> - <b>To get list of the my chats and ids</b>
• <code>/leave</code>  - <b>to leave from a chat.</b>
• <code>/disable</code>  -  <b>do disable a chat.</b>
• <code>/ban</code> - <b>to ban a user.</b>
• <code>/unban</code> - <b>to unban a user.</b>
• <code>/channel</code> - <b>to get list of total connected channels</b>
• <code>/broadcast</code> - <b>to broadcast a message to all users</b>"""
    STATUS_TXT = """
★ <b>⚡ Total Files</b> : <code>{}</code>
★ <b>🤴 Total Users</b> : <code>{}</code>
★ <b>💻 Total Chats</b> : <code>{}</code>
★ <b>🤦‍♂️ Used Storage</b>: <code>{}</code>
★ <b>😊 Free Storage</b>: <code>{}</code>"""
    LOG_TEXT_G = """#newgroup
    
<b>᚛›🤼‍♂️ GROUP        ⪼ {}(<code>{}</code>)</b>
<b>᚛›👩‍👧‍👦 Total member ⪼ <code>{}</code></b>
<b>᚛›👨‍🦯 Added BY     ⪼ {}</b>
"""
    LOG_TEXT_P = """#newusers  
    
<b>᚛› ID   ⪼ <code>{}</code></b>
<b>᚛› Name ⪼ {}</b>
"""
