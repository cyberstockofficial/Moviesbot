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
    START_TXT = environ.get("START_TXT", "<b><u>Hello {} I Am <u>Cyber Movie Bot</u> 😎</b>\n\n<b>Use Inline Features of This bot\n\n<i>Give Me Any <b>Movies, Anime, Web Series</b> Name I Will Giev You <b>Telegram Files</b> In All Quality!</i>")
    HELP_TXT = """Hey {}
<b>Here is Your help Guide.</b>"""
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
<i>1. Make Me The Admin Of Your Channel If It's Private.
2. Make Sure That Your Channel Does Not Contains Camrips, Porn And Fake Files.
3. Forward The Last Message To Me With Quotes.</i>
 <b>I'll Add All The Files In That Channel To My DB.</b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- <b><u>Used To Connect Bot To PM For Managing Filters.</b></u>
- <b><u>It Helps To Avoid Spamming In Groups.</b></u>

<b>NOTE:</b>
<i>1. Only Admins Can Add A Connection.
2. Send <code>/connect</code> For Connecting Me To Ur PM</i>

<b>Commands and Usage:</b>
• <code>/connect</code>  - <b>Connect A Particular Chat To Your PM</b>
• <code>/disconnect</code>  - <b>Disconnect From A Chat</b>
• <code>/connections</code> - <b>List All Your Connections</b>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
<b>These Are The Extra Features Only For Cyber Movie Bot</b>

<b>Commands And Usage:</b>
• <code>/id</code> - <b>Get Id Of A Specified User.</b>
• <code>/info</code>  - <b>Get Information About A User.</b>
• <code>/imdb</code>  - <b>Get The Film Information From IMDb Source.</b>
• <code>/search</code>  - <b>Get The Film Information From Various Sources.</b>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
<b><i>This Module Only Works For My Admins</i></b>

<b>Commands and Usage:</b>
• <code>/logs</code> - <b>To Get The Rescent Errors.</b>
• <code>/stats</code> - <b>To Get Status Of Files In Database.</b>
• <code>/delete</code> - <b>To Delete A Specific File From Database.</b>
• <code>/users</code> - <b>To Get List Of My User's And Ids.</b>
• <code>/chats</code> - <b>To Get List Of The My Chats And Ids</b>
• <code>/leave</code>  - <b>To Leave From A Chat.</b>
• <code>/disable</code>  -  <b>Do Disable A Chat.</b>
• <code>/ban</code> - <b>To Ban A User.</b>
• <code>/unban</code> - <b>To Unban A User.</b>
• <code>/channel</code> - <b>To Get List Of Total Connected Channels</b>
• <code>/broadcast</code> - <b>To Broadcast A Message To All Users</b>"""
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
