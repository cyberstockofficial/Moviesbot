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
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}</b>
<b>✮ Bot Own By: <a href=https://t.me/Movies_Unloaded2></b>
<b>✮ linrary: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</b>
<b>✮ language: khud he bana liya new</b>
<b>✮ database: Apne Ghar pe store hai sare</b>
<b>✮ Bot server: Ghar pe host hai</b>

<b>✮ Telegram Channel: <a href=https://t.me/Movies_Unloaded2</a></b>"""
    SOURCE_TXT = """<b>NOTE:</b>

Source - Kya Karega Bro Khud bana ek new bot

<b>DEVS:</b>
- <a href=https://t.me/Movies_Unloaded2>@Movies_Unloaded2</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword.

<b>NOTE:</b>
1. only admins can add filters in a chat.
2. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• <code>/filter</code> - **add a filter in chat**
• <code>/filters</code> - **list all the filters of a chat**
• <code>/del</code> - **delete a specific filter in chat**
• <code>/delall</code> - **delete the whole filters in a chat (chat owner only)**"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[UPDATE](buttonurl:https://t.me/Movies_Unloaded2)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• <code>/connect</code>  - **connect a particular chat to your PM**
• <code>/disconnect</code>  - **disconnect from a chat**
• <code>/connections</code> - **list all your connections**"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features Only For Movie X Bot

<b>Commands and Usage:</b>
• <code>/id</code> - **get id of a specified user.**
• <code>/info</code>  - **get information about a user.**
• <code>/imdb</code>  - **get the film information from IMDb source.**
• <code>/search</code>  - **get the film information from various sources.**"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• <code>/logs</code> - **to get the rescent errors**
• <code>/stats</code> - **To get status of files in db.**
• <code>/delete</code> - **to delete a specific file from db.**
• <code>/users</code> - **to get list of my users and ids.**
• <code>/chats</code> - **To get list of the my chats and ids**
• <code>/leave</code>  - **to leave from a chat.**
• <code>/disable</code>  -  **do disable a chat.**
• <code>/ban</code> - **to ban a user.**
• <code>/unban</code> - **to unban a user.**
• <code>/channel</code> - **to get list of total connected channels**
• <code>/broadcast</code> - **to broadcast a message to all users**"""
    STATUS_TXT = """
★**⚡ Total Files**     : <code>{}</code>
★ <b>🤴 Total Users</b> : <code>{}</code>
★ <b>💻 Total Chats</b> : <code>{}</code>
★ <b>🤦‍♂️ Used Storage</b>: <code>{}</code>
★ <b>😊 Free Storage</b>: <code>{}</code>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛›🤼‍♂️ GROUP        ⪼ {}(<code>{}</code>)</b>
<b>᚛›👩‍👧‍👦 Total member ⪼ <code>{}</code></b>
<b>᚛›👨‍🦯 Added BY     ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫  
    
<b>᚛› ID   ⪼ <code>{}</code></b>
<b>᚛› Name ⪼ {}</b>
"""
