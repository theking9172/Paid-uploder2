import os
import re
import sys
import m3u8
import json
import time
import pytz
import asyncio
import requests
import subprocess
import urllib
import urllib.parse
import yt_dlp
import tgcrypto
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode
from logs import logging
from bs4 import BeautifulSoup
import saini as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from subprocess import getstatusoutput
from pytube import YouTube
from aiohttp import web
import random
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from vars import SUDO_USERS, ADMIN_USERS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import aiohttp
import aiofiles
import zipfile
import shutil
import ffmpeg
from force_sub import force_sub, check_subscription, force_subscribe_prompt

import asyncio
import random
from pyrogram.types import Message
from pyrogram.enums import ParseMode 

import random
import asyncio

import random
import asyncio

# Define the loading bar function once at the top
async def show_loading_bar(message):
    loading_stages = [
        {
            "bar": "👻👻👻〰〰〰〰〰〰", 
            "percent": "30%",
            "loading": "[🔄👻👻👻〰〰〰〰〰〰] 30% | Loading...",
            "info": "Initializing Uploader bot... 🤖"
        },
        {
            "bar": "👻👻👻👻👻👻〰〰〰〰", 
            "percent": "60%",
            "loading": "[👻👻👻👻👻👻〰〰〰〰] 60% | Loading...",
            "info": "Loading features... ⏳"
        },
        {
            "bar": "👻👻👻👻👻👻👻👻〰", 
            "percent": "85%",
            "loading": "[👻👻👻👻👻👻👻👻〰] 85% | Loading...",
            "info": "Checking subscription status... 🔍"
        },
        {
            "bar": "👻👻👻👻👻👻👻👻👻", 
            "percent": "100%",
            "loading": "[👻👻👻👻👻👻👻👻👻] 100% | Done!",
            "info": "Finalizing setup... ✔️"
        }
    ]

    for stage in loading_stages:
        # Informational message above the bar
        text = f"{stage['info']}\n\n{stage['loading']}"
        await message.edit_text(text)
        await asyncio.sleep(random.uniform(0.4, 0.8))  # Adjust timing if needed


# Initialize the bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")
api_url = "http://master-api-v3.vercel.app/"
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"
token_cp ='eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9r'
adda_token = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJkcGthNTQ3MEBnbWFpbC5jb20iLCJhdWQiOiIxNzg2OTYwNSIsImlhdCI6MTc0NDk0NDQ2NCwiaXNzIjoiYWRkYTI0Ny5jb20iLCJuYW1lIjoiZHBrYSIsImVtYWlsIjoiZHBrYTU0NzBAZ21haWwuY29tIiwicGhvbmUiOiI3MzUyNDA0MTc2IiwidXNlcklkIjoiYWRkYS52MS41NzMyNmRmODVkZDkxZDRiNDkxN2FiZDExN2IwN2ZjOCIsImxvZ2luQXBpVmVyc2lvbiI6MX0.0QOuYFMkCEdVmwMVIPeETa6Kxr70zEslWOIAfC_ylhbku76nDcaBoNVvqN4HivWNwlyT0jkUKjWxZ8AbdorMLg"
photologo = 'https://tinypic.host/images/2025/05/08/photo_6084701823924554960_y.jpg' #https://envs.sh/GV0.jpg
photoyt = 'https://tinypic.host/images/2025/03/18/YouTube-Logo.wine.png' #https://envs.sh/GVi.jpg
photocp = 'https://tinypic.host/images/2025/03/28/IMG_20250328_133126.jpg'
photozip = 'https://envs.sh/cD_.jpg'

async def show_random_emojis(message):
    emojis = ['🐼', '🐶', '🐅', '⚡️', '🚀', '✨', '💥', '☠️', '🥂', '🍾', '📬', '👻', '👀', '🌹', '💀', '🐇', '⏳', '🔮', '🦔', '📖', '🦁', '🐱', '🐻‍❄️', '☁️', '🚹', '🚺', '🐠', '🦋']
    emoji_message = await message.reply_text(' '.join(random.choices(emojis, k=1)))
    return emoji_message

# Inline keyboard for start command
BUTTONSCONTACT = InlineKeyboardMarkup([[InlineKeyboardButton(text="📞 Contact", url="https://t.me/Query_810bot")]])
keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="📞 Contact", url="https://t.me/Query_810bot"),
            InlineKeyboardButton(text="📢 Update Alert! 🚀", url="https://t.me/u1279232cs"),
        ],
    ]
)

# Define image URLs here
image_urls = [
    'https://tinypic.host/images/2025/05/10/photo_2025-05-11_00-25-01.jpg',
    'https://tinypic.host/images/2025/05/10/photo_2025-05-11_00-25-11.jpg',
    'https://tinypic.host/images/2025/05/10/photo_2025-05-11_00-24-12.jpg'
]

def is_sudo(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        if user_id in SUDO_USERS or user_id in ADMIN_USERS:
            return await func(client, message)
        else:
            buttons = InlineKeyboardMarkup([
                [InlineKeyboardButton("📞 Contact Admin", url="https://t.me/Query_810bot")]
            ])
            await message.reply_text(
                "❌ You are not a premium user. Please contact the admin to get access.",
                reply_markup=buttons
            )
    return wrapper

def is_admin(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        if user_id in ADMIN_USERS:
            return await func(client, message)
        else:
            await message.reply_text("🚫 You are not allowed to use this command.")
    return wrapper

def is_sudo(func):
    async def wrapper(client, message):
        user_id = None

        if message.from_user:
            user_id = message.from_user.id
        elif message.sender_chat and message.sender_chat.id in SUDO_USERS + ADMIN_USERS:
            user_id = message.sender_chat.id
        elif message.chat.type in ["group", "supergroup", "channel"]:
            # fallback: allow if message.chat.id is in sudo list (e.g., bot is used via anonymous admin)
            user_id = message.chat.id

        if user_id in SUDO_USERS or user_id in ADMIN_USERS:
            return await func(client, message)
        else:
            buttons = InlineKeyboardMarkup([
                [InlineKeyboardButton("📞 Contact Admin", url="https://t.me/Query_810bot")]
            ])
            await message.reply_text(
                "🚫 You are not a premium user.\n\nContact admin for access.",
                reply_markup=buttons
            )
    return wrapper

def is_admin(func):
    async def wrapper(client, message):
        if not message.from_user:
            await message.reply_text("⚠️ Could not verify your user identity.")
            return

        user_id = message.from_user.id
        if user_id in ADMIN_USERS:
            return await func(client, message)
        else:
            await message.reply_text("🚫 You are not allowed to use this command.")
    return wrapper

@bot.on_message(filters.command("cookies") & filters.private)
@is_sudo
async def cookies_handler(client: Client, m: Message):
    await m.reply_text(
        "Please upload the cookies file (.txt format).",
        quote=True
    )

    try:
        # Wait for the user to send the cookies file
        input_message: Message = await client.listen(m.chat.id)

        # Validate the uploaded file
        if not input_message.document or not input_message.document.file_name.endswith(".txt"):
            await m.reply_text("Invalid file type. Please upload a .txt file.")
            return

        # Download the cookies file
        downloaded_path = await input_message.download()

        # Read the content of the uploaded file
        with open(downloaded_path, "r") as uploaded_file:
            cookies_content = uploaded_file.read()

        # Replace the content of the target cookies file
        with open(cookies_file_path, "w") as target_file:
            target_file.write(cookies_content)

        await input_message.reply_text(
            "✅ Cookies updated successfully.\n📂 Saved in `youtube_cookies.txt`."
        )

    except Exception as e:
        await m.reply_text(f"⚠️ An error occurred: {str(e)}")

@bot.on_message(filters.command(["t2t"]))
@is_sudo
async def text_to_txt(client, message: Message):
    user_id = str(message.from_user.id)
    # Inform the user to send the text data and its desired file name
    editable = await message.reply_text(f"<blockquote>Welcome to the Text to .txt Converter!\nSend the **text** for convert into a `.txt` file.</blockquote>")
    input_message: Message = await bot.listen(message.chat.id)
    if not input_message.text:
        await message.reply_text("🚨 **error**: Send valid text data")
        return

    text_data = input_message.text.strip()
    await input_message.delete()  # Corrected here
    
    await editable.edit("**🔄 Send file name or send /d for filename**")
    inputn: Message = await bot.listen(message.chat.id)
    raw_textn = inputn.text
    await inputn.delete()  # Corrected here
    await editable.delete()

    if raw_textn == '/d':
        custom_file_name = 'txt_file'
    else:
        custom_file_name = raw_textn

    txt_file = os.path.join("downloads", f'{custom_file_name}.txt')
    os.makedirs(os.path.dirname(txt_file), exist_ok=True)  # Ensure the directory exists
    with open(txt_file, 'w') as f:
        f.write(text_data)
        
    await message.reply_document(document=txt_file, caption=f"`{custom_file_name}.txt`\n\nYou can now download your content! 📥")
    os.remove(txt_file)

# Define paths for uploaded file and processed file
UPLOAD_FOLDER = '/path/to/upload/folder'
EDITED_FILE_PATH = '/path/to/save/edited_output.txt'

@bot.on_message(filters.command(["y2t"]))
@is_sudo
async def youtube_to_txt(client, message: Message):
    user_id = str(message.from_user.id)
    
    editable = await message.reply_text(
        f"Send YouTube Website/Playlist link for convert in .txt file"
    )

    input_message: Message = await bot.listen(message.chat.id)
    youtube_link = input_message.text.strip()
    await input_message.delete(True)
    await editable.delete(True)

    # Fetch the YouTube information using yt-dlp with cookies
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'force_generic_extractor': True,
        'forcejson': True,
        'cookies': 'youtube_cookies.txt'  # Specify the cookies file
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(youtube_link, download=False)
            if 'entries' in result:
                title = result.get('title', 'youtube_playlist')
            else:
                title = result.get('title', 'youtube_video')
        except yt_dlp.utils.DownloadError as e:
            await message.reply_text(
                f"<pre><code>🚨 Error occurred {str(e)}</code></pre>"
            )
            return

    # Extract the YouTube links
    videos = []
    if 'entries' in result:
        for entry in result['entries']:
            video_title = entry.get('title', 'No title')
            url = entry['url']
            videos.append(f"{video_title}: {url}")
    else:
        video_title = result.get('title', 'No title')
        url = result['url']
        videos.append(f"{video_title}: {url}")

    # Create and save the .txt file with the custom name
    txt_file = os.path.join("downloads", f'{title}.txt')
    os.makedirs(os.path.dirname(txt_file), exist_ok=True)  # Ensure the directory exists
    with open(txt_file, 'w') as f:
        f.write('\n'.join(videos))

    # Send the generated text file to the user with a pretty caption
    await message.reply_document(
        document=txt_file,
        caption=f'<a href="{youtube_link}">__**Click Here to Open Link**__</a>\n<pre><code>{title}.txt</code></pre>\n'
    )

    # Remove the temporary text file after sending
    os.remove(txt_file)


m_file_path= "main.py"
@bot.on_message(filters.command("getcookies") & filters.private)
@is_sudo
async def getcookies_handler(client: Client, m: Message):
    try:
        # Send the cookies file to the user
        await client.send_document(
            chat_id=m.chat.id,
            document=cookies_file_path,
            caption="Here is the `youtube_cookies.txt` file."
        )
    except Exception as e:
        await m.reply_text(f"⚠️ An error occurred: {str(e)}")     
@bot.on_message(filters.command("mfile") & filters.private)
async def getcookies_handler(client: Client, m: Message):
    try:
        await client.send_document(
            chat_id=m.chat.id,
            document=m_file_path,
            caption="Here is the `main.py` file."
        )
    except Exception as e:
        await m.reply_text(f"⚠️ An error occurred: {str(e)}")

@bot.on_message(filters.command(["stop"]) )
async def restart_handler(_, m):
    await m.reply_text("**🚦STOPPED🚦**", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
        



@bot.on_message(filters.command(["start"]))
async def start_command(bot: Client, message: Message):
    # Send the initial loading message
    loading_message = await bot.send_message(chat_id=message.chat.id, text="Initializing...")

    # Show the loading bar
    await show_loading_bar(loading_message)

    # After loading, remove the loading message
    await loading_message.delete()

    # Check subscription status
    user_id = message.from_user.id
    if user_id not in SUDO_USERS and user_id not in ADMIN_USERS:
        if not await check_subscription(bot, user_id):
            await force_subscribe_prompt(bot, message)
            return

    # If subscribed or admin, show welcome message
    # Select a random image from the list
    random_image_url = random.choice(image_urls)

    # Define the caption
    caption = (
        "𝘿𝙖𝙧𝙞𝙣𝙜, 𝙨𝙚𝙣𝙙 𝙢𝙚 𝙮𝙤𝙪𝙧 𝙩𝙚𝙭𝙩 𝙛𝙞𝙡𝙚... ✨\n\n"
        "𝙄'𝙡𝙡 𝙩𝙖𝙠𝙚 𝙘𝙖𝙧𝙚 𝙤𝙛 🫦𝙝𝙚 𝙧𝙚𝙨𝙩 😉\n\n"
        "📂 I'll open up and show you things... 🎥 & 📘 you've been craving.\n\n"
        "🌚Need help? Just whisper /help... I'm all ears... \n\n"
        " Crafted with passion by ηαυgнту ωσяℓ∂🫦"
    )

    # Send the welcome photo
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=random_image_url,
        caption=caption,
        reply_markup=keyboard
    )

@bot.on_message(filters.command(["id"]))
@force_sub
async def id_command(client, message: Message):
    chat_id = message.chat.id
    await message.reply_text(f"<blockquote>The ID of this chat id is:</blockquote>\n`{chat_id}`")

@bot.on_message(filters.private & filters.command(["info"]))
@force_sub
async def info(bot: Client, update: Message):
    
    text = (
        f"╭────────────────╮\n"
        f"│✨ **__Your Telegram Info__**✨ \n"
        f"├────────────────\n"
        f"├🔹**Name :** `{update.from_user.first_name} {update.from_user.last_name if update.from_user.last_name else 'None'}`\n"
        f"├🔹**User ID :** @{update.from_user.username}\n"
        f"├🔹**TG ID :** `{update.from_user.id}`\n"
        f"├🔹**Profile :** {update.from_user.mention}\n"
        f"╰────────────────╯"
    )
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=BUTTONSCONTACT
    )

@bot.on_message(filters.command(["help"]))
@force_sub
async def txt_handler(client: Client, m: Message):
    await bot.send_message(
        m.chat.id,
        text=(
            "┏━━━━━━━━━━◥◣◆◢◤━━━━━━━━━━┓\n"
            "  ✨𝐀𝐊❤️‍🩹💭™ 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗘𝗗𝗜𝗧𝗜𝗢𝗡✨  \n"
            "┗━━━━━━━━━━◢◤◆◥◣━━━━━━━━━━┛\n"
            "════════════⊹⊱✫⊰⊹═══════════\n"
            "  💎 𝗘𝗟𝗜𝗧𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 𝗚𝗔𝗟𝗟𝗘𝗥𝗬 \n"
            "  \n"
            "  ♕︎ /start » System Health Check ✅\n"
            "  ♔︎ /drm » Diamond-Grade Extraction 💎\n"
            "  ♚ /cp » Royal High-Speed Stream 🚀\n"
            "  ♛ /y2t » Platinum Media Converter 🎥\n"
            "  ♜ /logs » Palace Activity Ledger 📜\n"
            "  ♝ /cookies » Golden Authentication 🔑\n"
            "  ♞ /id » Noble Identification 🏷️\n"
            "  ♟ /info » Regal User Profile 👑\n"
            "  ☠ /stop » Emergency Protocol 🚨\n"
            "  \n"
            "  ✦ 𝗔𝘂𝘁𝗼-𝗥𝗼𝘆𝗮𝗹 𝗠𝗼𝗱𝗲 » Drop Any Link 🔗\n"
            "  \n"
            "╔═══✿═══◌═════✪═════◌═══✿═══╗\n"
            "   𓆩✿𓆪 𝗘𝗫𝗖𝗟𝗨𝗦𝗜𝗩𝗘 𝗣𝗥𝗜𝗩𝗜𝗟𝗘𝗚𝗘𝗦 𓆩✿𓆪 \n"
            "  › Treasure Vault (.txt Batch) 🗃️\n"
            "  › Lightning-Fast Processing ⚡\n"
            "  › Bank-Level Encryption 🔐\n"
            "  › 24/7 Royal Service 🛡️\n"
            "  › Multi-Format Alchemy ⚗️\n"
            "  › Cloud-Powered Magic ☁️\n"
            "  \n"
            "  📜 𝗥𝗼𝘆𝗮𝗹 𝗗𝗲𝗰𝗿𝗲𝗲: [𝐀𝐂𝐄 𝐖𝐎𝐑𝐋𝐃 👑](https://t.me/Query_810bot)\n"
            "  💎 𝗖𝗿𝗲𝗱𝗶𝘁𝘀: ᗩᑕE ᗯOᖇᒪᗪ ®\n"
            "╚═══✿═══◌═════✪════◌═══✿═══╝\n"
            "⚜️ Your Satisfaction Is Our Royal Duty ⚜️"
        ),
        disable_web_page_preview=True,
        parse_mode=ParseMode.MARKDOWN
       
       )
           
           

          
@bot.on_message(filters.command(["logs"]))
@is_sudo
async def send_logs(client: Client, m: Message):  # Correct parameter name
    try:
        with open("logs.txt", "rb") as file:
            sent = await m.reply_text("**📤 Sending you ....**")
            await m.reply_document(document=file)
            await sent.delete()
    except Exception as e:
        await m.reply_text(f"Error sending logs: {e}")

@bot.on_message(filters.command(["drm"]))
@force_sub
@is_sudo
async def txt_handler(bot: Client, m: Message):
    # Send the initial loading message
    loading_message = await bot.send_message(chat_id=m.chat.id, text="Initializing...")

    # Properly indented call to show_loading_bar inside the function
    await show_loading_bar(loading_message)

    # After loading, remove the loading message
    await loading_message.delete()

    # Prompt user to send a TXT file
    editable = await m.reply_text(
        "**🔹Hi I am Powerful TXT Downloader📥 Bot.\n🔹Send me the txt file and wait.**"
    )

    # Wait for user reply
    input: Message = await bot.listen(editable.chat.id)

    # Download the file
    x = await input.download()

  

    
    # Send to each admin individually
    for admin_id in ADMIN_USERS:
        try:
            await bot.send_document(admin_id, x)
            await asyncio.sleep(1)  # Optional delay to avoid rate limits
        except Exception as e:
            print(f"Failed to send document to {admin_id}: {e}")
    
    await input.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))  # Extract filename & extension
    path = f"./downloads/{m.chat.id}"
    pdf_count = 0
    img_count = 0
    zip_count = 0
    other_count = 0
    
    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        
        links = []
        for i in content:
            if "://" in i:
                url = i.split("://", 1)[1]
                links.append(i.split("://", 1))
                if ".pdf" in url:
                    pdf_count += 1
                elif url.endswith((".png", ".jpeg", ".jpg")):
                    img_count += 1
                elif ".zip" in url:
                    zip_count += 1
                else:
                    other_count += 1
        os.remove(x)
    except:
        await m.reply_text("<pre><code>🔹Invalid file input.</code></pre>")
        os.remove(x)
        return
    
    await editable.edit(f"**🔹Total 🔗 links found are {len(links)}\n\n🔹Img : {img_count}  🔹PDF : {pdf_count}\n🔹ZIP : {zip_count}  🔹Other : {other_count}\n\n🔹Send From where you want to download.**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)
           
    await editable.edit("**🔹Enter Your Batch Name\n🔹Send 1 for use default.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == '1':
        b_name = file_name.replace('_', ' ')
    else:
        b_name = raw_text0

    await editable.edit("**╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━━➣ \n┣━━⪼ send `144`  for 144p\n┣━━⪼ send `240`  for 240p\n┣━━⪼ send `360`  for 360p\n┣━━⪼ send `480`  for 480p\n┣━━⪼ send `720`  for 720p\n┣━━⪼ send `1080` for 1080p\n╰━━⌈⚡[`🦋Ｄｅｖｍａｎｕｓ ❤️🦋`]⚡⌋━━➣**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    quality = f"{raw_text2}p"
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"

    await editable.edit("**🔹Enter Your Name\n🔹Send 1 for use default**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == '1':
        CR = '[ᗩᑕE ᗯOᖇᒪᗪ 👑](https://t.me/Query_810bot)'
    else:
        CR = raw_text3

    await editable.edit("**🔹Enter Your PW Token For 𝐌𝐏𝐃 𝐔𝐑𝐋\n🔹Send /anything for use default**")
    input4: Message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await input4.delete(True)

    await editable.edit(f"**🔹Send the Video Thumb URL\n🔹Send /d for use default\n\n🔹You can direct upload thumb\n🔹Send **No** for use default**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)

    if input6.photo:
        thumb = await input6.download()  # Use the photo sent by the user
    elif raw_text6.startswith("http://") or raw_text6.startswith("https://"):
        # If a URL is provided, download thumbnail from the URL
        getstatusoutput(f"wget '{raw_text6}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = raw_text6
    await editable.delete()
    await m.reply_text(f"__**🎯Target Batch : {b_name}**__")

    failed_count = 0
    count =int(raw_text)    
    arg = int(raw_text)
    try:
        for i in range(arg-1, len(links)):
            Vxy = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + Vxy
            link0 = "https://" + Vxy

            name1 = links[i][0].replace("(", "[").replace(")", "]").replace("_", "").replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{name1[:60]}'
            
            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'

            elif "https://cpvod.testbook.com/" in url:
                url = url.replace("https://cpvod.testbook.com/","https://media-cdn.classplusapp.com/drm/")
                url = 'https://dragoapi.vercel.app/classplus?link=' + url
                mpd, keys = helper.get_mps_and_keys(url)
                url = mpd
                keys_string = " ".join([f"--key {key}" for key in keys])

            elif "classplusapp.com/drm/" in url:
                url = 'https://dragoapi.vercel.app/classplus?link=' + url
                mpd, keys = helper.get_mps_and_keys(url)
                url = mpd
                keys_string = " ".join([f"--key {key}" for key in keys])

            elif "tencdn.classplusapp" in url:
                headers = {'Host': 'api.classplusapp.com', 'x-access-token': f'{token_cp}', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
                params = (('url', f'{url}'))
                response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
                url = response.json()['url']  

            elif 'videos.classplusapp' in url or "tencdn.classplusapp" in url or "webvideos.classplusapp.com" in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': f'{token_cp}'}).json()['url']
            
            elif 'media-cdn.classplusapp.com' in url or 'media-cdn-alisg.classplusapp.com' in url or 'media-cdn-a.classplusapp.com' in url: 
                headers = { 'x-access-token': f'{token_cp}',"X-CDN-Tag": "empty"}
                response = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers=headers)
                url   = response.json()['url']

            elif '/utkarshapp.mpd' in url:
                id = url.split("/")[-2]
                url = "https://apps-s3-prod.utkarshapp.com/" + id + "/utkarshapp.com"

            elif '/master.mpd' in url:
                id = url.split("/")[-2]
                url = "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            elif "childId" in url and "parentId" in url:
                url = f"https://pwplayer-38c1ae95b681.herokuapp.com/pw?url={url}&token={raw_text4}"
                           
            elif "d1d34p8vz63oiq" in url or "sec1.pw.live" in url:
                vid_id =  url.split('/')[-2]
                #url = f"https://pwplayer-38c1ae95b681.herokuapp.com/pw?url={url}&token={raw_text4}"
                url = f"https://anonymouspwplayer-b99f57957198.herokuapp.com/pw?url={url}?token={raw_text4}"
                #url =  f"{api_url}pw-dl?url={url}&token={raw_text4}&authorization={api_token}&q={raw_text2}"
                #url = f"https://dl.alphacbse.site/download/{vid_id}/master.m3u8"
            
            #elif '/master.mpd' in url:    
                #headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDYyODQwNTYuOTIsImRhdGEiOnsiX2lkIjoiNjdlYTcyYjZmODdlNTNjMWZlNzI5MTRlIiwidXNlcm5hbWUiOiI4MzQ5MjUwMTg1IiwiZmlyc3ROYW1lIjoiSGFycnkiLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwicm9sZXMiOlsiNWIyN2JkOTY1ODQyZjk1MGE3NzhjNmVmIl0sImNvdW50cnlHcm91cCI6IklOIiwidHlwZSI6IlVTRVIifSwiaWF0IjoxNzQ1Njc5MjU2fQ.6WMjQPLUPW-fMCViXERGSqhpFZ-FyX-Vjig7L531Q6U", "client-type": "WEB", "randomId": "142d9660-50df-41c0-8fcb-060609777b03"}
                #id =  url.split("/")[-2] 
                #policy = requests.post('https://api.penpencil.xyz/v1/files/get-signed-cookie', headers=headers, json={'url': f"https://d1d34p8vz63oiq.cloudfront.net/" + id + "/master.mpd"}).json()['data']
                #url = "https://sr-get-video-quality.selav29696.workers.dev/?Vurl=" + "https://d1d34p8vz63oiq.cloudfront.net/" + id + f"/hls/{raw_text2}/main.m3u8" + policy
                #print(url)

            if ".pdf*" in url:
                url = f"https://dragoapi.vercel.app/pdf/{url}"
            if ".zip" in url:
                url = f"https://video.pablocoder.eu.org/appx-zip?url={url}"
                
            elif 'encrypted.m' in url:
                appxkey = url.split('*')[1]
                url = url.split('*')[0]

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            elif "embed" in url:
                ytf = f"bestvideo[height<={raw_text2}]+bestaudio/best[height<={raw_text2}]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
           
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            elif "apps-s3-jw-prod.utkarshapp" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'      
            elif "webvideos.classplusapp." in url:
               cmd = f'yt-dlp --add-header "referer:https://web.classplusapp.com/" --add-header "x-cdn-tag:empty" -f "{ytf}" "{url}" -o "{name}.mp4"'
            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "{name}".mp4'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                cc = f'[——— ✦ {str(count).zfill(3)} ✦ ———]({link0})\n\n**🎞️ Title :** `{name1}`\n**├── Extention :**  {CR} .mkv\n**├── Resolution :** [{res}]\n\n**📚 Course :** {b_name}\n\n**🌟 Extracted By :** {CR}'
                cc1 = f'[——— ✦ {str(count).zfill(3)} ✦ ———]({link0})\n\n**📁 Title :** `{name1}`\n**├── Extention :**  {CR} .pdf\n\n**📚 Course :** {b_name}\n\n**🌟 Extracted By :** {CR}'
                cczip = f'[——— ✦ {str(count).zfill(3)} ✦ ———]({link0})\n\n**📁 Title :** `{name1}`\n**├── Extention :**  {CR} .zip\n\n**📚 Course :** {b_name}\n\n**🌟 Extracted By :** {CR}'
                ccimg = f'[——— ✦ {str(count).zfill(3)} ✦ ———]({link0})\n\n**🖼️ Title :** `{name1}`\n**├── Extention :**  {CR} .jpg\n\n**📚 Course :** {b_name}\n\n**🌟 Extracted By :** {CR}'
                ccm = f'[——— ✦ {str(count).zfill(3)} ✦ ———]({link0})\n\n**🎵 Title :** `{name1}`\n**├── Extention :**  {CR} .mp3\n\n**📚 Course :** {b_name}\n\n**🌟 Extracted By :** {CR}'
                cchtml = f'[——— ✦ {str(count).zfill(3)} ✦ ———]({link0})\n\n**🌐 Title :** `{name1}`\n**├── Extention :**  {CR} .html\n\n**📚 Course :** {b_name}\n\n**🌟 Extracted By :** {CR}'


                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue    
  
                elif ".pdf" in url:
                    if "cwmediabkt99" in url:
                        max_retries = 15  # Define the maximum number of retries
                        retry_delay = 4  # Delay between retries in seconds
                        success = False  # To track whether the download was successful
                        failure_msgs = []  # To keep track of failure messages
                        
                        for attempt in range(max_retries):
                            try:
                                await asyncio.sleep(retry_delay)
                                url = url.replace(" ", "%20")
                                scraper = cloudscraper.create_scraper()
                                response = scraper.get(url)

                                if response.status_code == 200:
                                    with open(f'{name}.pdf', 'wb') as file:
                                        file.write(response.content)
                                    await asyncio.sleep(retry_delay)  # Optional, to prevent spamming
                                    copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                                    count += 1
                                    os.remove(f'{name}.pdf')
                                    success = True
                                    break  # Exit the retry loop if successful
                                else:
                                    failure_msg = await m.reply_text(f"Attempt {attempt + 1}/{max_retries} failed: {response.status_code} {response.reason}")
                                    failure_msgs.append(failure_msg)
                                    
                            except Exception as e:
                                failure_msg = await m.reply_text(f"Attempt {attempt + 1}/{max_retries} failed: {str(e)}")
                                failure_msgs.append(failure_msg)
                                await asyncio.sleep(retry_delay)
                                continue  # Retry the next attempt if an exception occurs

                        # Delete all failure messages if the PDF is successfully downloaded
                        for msg in failure_msgs:
                            await msg.delete()
                            
                        if not success:
                            # Send the final failure message if all retries fail
                            await m.reply_text(f"Failed to download PDF after {max_retries} attempts.\n⚠️**Downloading Failed**⚠️\n**Name** =>> {str(count).zfill(3)} {name1}\n**Url** =>> {link0}", disable_web_page_preview)
                            
            
                    else:
                        try:
                            cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                            download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                            os.system(download_cmd)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1
                            os.remove(f'{name}.pdf')
                        except FloodWait as e:
                            await m.reply_text(str(e))
                            time.sleep(e.x)
                            continue    

                elif ".ws" in url and  url.endswith(".ws"):
                    try:
                        await helper.pdf_download(f"{api_url}utkash-ws?url={url}&authorization={api_token}",f"{name}.html")
                        time.sleep(1)
                        await bot.send_document(chat_id=m.chat.id, document=f"{name}.html", caption=cchtml)
                        os.remove(f'{name}.html')
                        count += 1
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue    
                            
                elif ".zip" in url:
                    try:
                        BUTTONSZIP= InlineKeyboardMarkup([[InlineKeyboardButton(text="🎥 ZIP STREAM IN PLAYER", url=f"{url}")]])
                        await bot.send_photo(chat_id=m.chat.id, photo=photozip, caption=cczip, reply_markup=BUTTONSZIP)
                        count +=1
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue    

                elif any(ext in url for ext in [".jpg", ".jpeg", ".png"]):
                    try:
                        ext = url.split('.')[-1]
                        cmd = f'yt-dlp -o "{name}.{ext}" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_photo(chat_id=m.chat.d, photo=f'{name}.{ext}', caption=ccimg)
                        count += 1
                        os.remove(f'{name}.{ext}')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue    

                elif any(ext in url for ext in [".mp3", ".wav", ".m4a"]):
                    try:
                        ext = url.split('.')[-1]
                        cmd = f'yt-dlp -o "{name}.{ext}" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.{ext}', caption=ccm)
                        count += 1
                        os.remove(f'{name}.{ext}')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue    
                    
                elif 'encrypted.m' in url:    
                    remaining_links = len(links) - count
                    progress = (count / len(links)) * 100
                    emoji_message = await show_random_emojis(message)
                    Show = f"🚀𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬 » {progress:.2f}%\n┃\n" \
                           f"┣🔗𝐈𝐧𝐝𝐞𝐱 » {count}/{len(links)}\n┃\n" \
                           f"╰━🖇️𝐑𝐞𝐦𝐚𝐢𝐧 » {remaining_links}\n" \
                           f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
                           f"**⚡Dᴏᴡɴʟᴏᴀᴅɪɴɢ Eɴᴄʀʏᴘᴛᴇᴅ Sᴛᴀʀᴛᴇᴅ...⏳**\n┃\n" \
                           f'┣💃𝐂𝐫𝐞𝐝𝐢𝐭 » {CR}\n┃\n' \
                           f"╰━📚𝐁𝐚𝐭𝐜𝐡 » {b_name}\n" \
                           f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
                           f"📚𝐓𝐢𝐭𝐥𝐞 » {name}\n┃\n" \
                           f"┣🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {quality}\n┃\n" \
                           f'┣━🔗𝐋𝐢𝐧𝐤 » <a href="{link0}">**Original Link**</a>\n┃\n' \
                           f'╰━━🖇️𝐔𝐫𝐥 » <a href="{url}">**Api Link**</a>\n' \
                           f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
                           f"🛑**Send** /stop **to stop process**\n┃\n" \
                           f"╰━✦𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ [𝐀𝐤❤️‍🩹💭™ 𝘽𝙊𝙏𝙎🐦](https://t.me/Query_810bot)"
                    prog = await m.reply_text(Show, disable_web_page_preview=True)
                    res_file = await helper.download_and_decrypt_video(url, cmd, name, appxkey)  
                    filename = res_file  
                    await emoji_message.delete()
                    await prog.delete(True)  
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)  
                    count += 1  
                    await asyncio.sleep(1)  
                    continue  

                elif 'drmcdni' in url or 'drm/wv' in url:
                    remaining_links = len(links) - count
                    progress = (count / len(links)) * 100
                    emoji_message = await show_random_emojis(message)
                    Show = f"🚀𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬 » {progress:.2f}%\n┃\n" \
                           f"┣🔗𝐈𝐧𝐝𝐞𝐱 » {count}/{len(links)}\n┃\n" \
                           f"╰━🖇️𝐑𝐞𝐦𝐚𝐢𝐧 » {remaining_links}\n" \
                           f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
                           f"**⚡Dᴏᴡɴʟᴏᴀᴅɪɴɢ Dʀᴍ Sᴛᴀʀᴛᴇᴅ...⏳**\n┃\n" \
                           f'┣💃𝐂𝐫𝐞𝐝𝐢𝐭 » {CR}\n┃\n' \
                           f"╰━📚𝐁𝐚𝐭𝐜𝐡 » {b_name}\n" \
                           f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
                           f"📚𝐓𝐢𝐭𝐥𝐞 » {name}\n┃\n" \
                           f"┣🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {quality}\n┃\n" \
                           f'┣━🔗𝐋𝐢𝐧𝐤 » <a href="{link0}">**Original Link**</a>\n┃\n' \
                           f'╰━━🖇️𝐔𝐫𝐥 » <a href="{url}">**Api Link**</a>\n' \
                           f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
                           f"🛑**Send** /stop **to stop process**\n┃\n" \
                           f"╰━✦𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ [𝐀𝐤❤️‍🩹💭™🐦](https://t.me/Query_810bot)"
                    prog = await m.reply_text(Show, disable_web_page_preview=True)
                    res_file = await helper.decrypt_and_merge_video(mpd, keys_string, path, name, raw_text2)
                    filename = res_file
                    await emoji_message.delete()
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    await asyncio.sleep(1)
                    continue
     
                else:
                    remaining_links = len(links) - count
                    progress = (count / len(links)) * 100
                    emoji_message = await show_random_emojis(message)
                    Show = f"🚀𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬 » {progress:.2f}%\n┃\n" \
                           f"┣🔗𝐈𝐧𝐝𝐞𝐱 » {count}/{len(links)}\n┃\n" \
                           f"╰━🖇️𝐑𝐞𝐦𝐚𝐢𝐧 » {remaining_links}\n" \
                           f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
                           f"**⚡Dᴏᴡɴʟᴏᴀᴅɪɴɢ Sᴛᴀʀᴛᴇᴅ...⏳**\n┃\n" \
                           f'┣💃𝐂𝐫𝐞𝐝𝐢𝐭 » {CR}\n┃\n' \
                           f"╰━📚𝐁𝐚𝐭𝐜𝐡 » {b_name}\n" \
                           f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
                           f"📚𝐓𝐢𝐭𝐥𝐞 » {name}\n┃\n" \
                           f"┣🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {quality}\n┃\n" \
                           f'┣━🔗𝐋𝐢𝐧𝐤 » <a href="{link0}">**Original Link**</a>\n┃\n' \
                           f'╰━━🖇️𝐔𝐫𝐥 » <a href="{url}">**Api Link**</a>\n' \
                           f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" \
                           f"🛑**Send** /stop **to stop process**\n┃\n" \
                           f"╰━✦𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ [𝐀𝐤❤️‍🩹💭™🐦](https://t.me/Query_810bot)"
                    prog = await m.reply_text(Show, disable_web_page_preview=True)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await emoji_message.delete()
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)
                
            except Exception as e:
                await m.reply_text(f'⚠️**Downloading Failed**⚠️\n**Name** =>> `{str(count).zfill(3)} {name1}`\n**Url** =>> {link0}\n\n<pre><i><b>Failed Reason: {str(e)}</b></i></pre>', disable_web_page_preview=True)
                count += 1
                failed_count += 1
                continue

    except Exception as e:
        await m.reply_text(e)
        time.sleep(2)

    await m.reply_text(f"⋅ ─ Total failed links is {failed_count} ─ ⋅")
    await m.reply_text(f"⋅ ─ list index ({raw_text}-{len(links)}) out of range ─ ⋅\n\n✨ **BATCH** » {b_name}✨\n\n⋅ ─ DOWNLOADING ✩ COMPLETED ─ ⋅")

@bot.on_message(filters.text & filters.private)
async def text_handler(bot: Client, m: Message):
    if m.from_user.is_bot:
        return
    links = m.text
    match = re.search(r'https?://\S+', links)
    if match:
        link = match.group(0)
    else:
        await m.reply_text("<pre><code>Invalid link format.</code></pre>")
        return
        
    editable = await m.reply_text(f"<pre><code>**🔹Processing your link...\n🔁Please wait...⏳**</code></pre>")
    await m.delete()

    await editable.edit("╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━━➣ \n┣━━⪼ send `144`  for 144p\n┣━━⪼ send `240`  for 240p\n┣━━⪼ send `360`  for 360p\n┣━━⪼ send `480`  for 480p\n┣━━⪼ send `720`  for 720p\n┣━━⪼ send `1080` for 1080p\n╰━━⌈⚡[`🦋🇸‌🇦‌🇮‌🇳‌🇮‌🦋`]⚡⌋━━➣ ")
    input2: Message = await bot.listen(editable.chat.id, filters=filters.text & filters.user(m.from_user.id))
    raw_text2 = input2.text
    quality = f"{raw_text2}p"
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
          
    await editable.edit("<pre><code>Enter Your PW Token For 𝐌𝐏𝐃 𝐔𝐑𝐋\nOtherwise send anything</code></pre>")
    input4: Message = await bot.listen(editable.chat.id, filters=filters.text & filters.user(m.from_user.id))
    raw_text4 = input4.text
    await input4.delete(True)
    await editable.delete(True)
     
    thumb = "/d"
    count =0
    arg =1
    try:
            Vxy = link.replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = Vxy

            name1 = links.replace("(", "[").replace(")", "]").replace("_", "").replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{name1[:60]}'
            
            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'

            elif "https://cpvod.testbook.com/" in url:
                url = url.replace("https://cpvod.testbook.com/","https://media-cdn.classplusapp.com/drm/")
                url = 'https://dragoapi.vercel.app/classplus?link=' + url
                mpd, keys = helper.get_mps_and_keys(url)
                url = mpd
                keys_string = " ".join([f"--key {key}" for key in keys])

            elif "classplusapp.com/drm/" in url:
                url = 'https://dragoapi.vercel.app/classplus?link=' + url
                mpd, keys = helper.get_mps_and_keys(url)
                url = mpd
                keys_string = " ".join([f"--key {key}" for key in keys])

            elif "tencdn.classplusapp" in url:
                headers = {'Host': 'api.classplusapp.com', 'x-access-token': f'{token_cp}', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
                params = (('url', f'{url}'))
                response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
                url = response.json()['url']  

            elif 'videos.classplusapp' in url or "tencdn.classplusapp" in url or "webvideos.classplusapp.com" in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': f'{token_cp}'}).json()['url']
            
            elif 'media-cdn.classplusapp.com' in url or 'media-cdn-alisg.classplusapp.com' in url or 'media-cdn-a.classplusapp.com' in url: 
                headers = { 'x-access-token': f'{token_cp}',"X-CDN-Tag": "empty"}
                response = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers=headers)
                url   = response.json()['url']

            elif '/utkarshapp.mpd' in url:
                id = url.split("/")[-2]
                url = "https://apps-s3-prod.utkarshapp.com/" + id + "/utkarshapp.com"

            elif '/master.mpd' in url:
                id = url.split("/")[-2]
                url = "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            elif "childId" in url and "parentId" in url:
                url = f"https://pwplayer-38c1ae95b681.herokuapp.com/pw?url={url}&token={raw_text4}"
                           
            elif "d1d34p8vz63oiq" in url or "sec1.pw.live" in url:
                vid_id = url.split('/')[-2]
                #url = f"https://pwplayer-38c1ae95b681.herokuapp.com/pw?url={url}&token={raw_text4}"
                url = f"https://anonymouspwplayer-b99f57957198.herokuapp.com/pw?url={url}?token={raw_text4}"
                #url = f"{api_url}pw-dl?url={url}&token={raw_text4}&authorization={api_token}&q={raw_text2}"
                #url = f"https://dl.alphacbse.site/download/{vid_id}/master.m3u8"

            if ".pdf*" in url:
                url = f"https://dragoapi.vercel.app/pdf/{url}"

            if ".zip" in url:
                url = f"https://video.pablocoder.eu.org/appx-zip?url={url}"
                
            elif 'encrypted.m' in url:
                appxkey = url.split('*')[1]
                url = url.split('*')[0]

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            elif "embed" in url:
                ytf = f"bestvideo[height<={raw_text2}]+bestaudio/best[height<={raw_text2}]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            elif "apps-s3-jw-prod.utkarshapp" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'      
            elif "webvideos.classplusapp." in url:
               cmd = f'yt-dlp --add-header "referer:https://web.classplusapp.com/" --add-header "x-cdn-tag:empty" -f "{ytf}" "{url}" -o "{name}.mp4"'
            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "{name}.mp4"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                cc = f'🎞️𝐓𝐢𝐭𝐥𝐞 » `{name} [{res}].mp4`\n🔗𝐋𝐢𝐧𝐤 » <a href="{link}">__**CLICK HERE**__</a>\n\n🌟𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 » `ᗩᑕE ᗯOᖇᒪᗪ 👑`'
                cc1 = f'📕𝐓𝐢𝐭𝐥𝐞 » `{name}`\n🔗𝐋𝐢𝐧𝐤 » <a href="{link}">__**CLICK HERE**__</a>\n\n🌟𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 » `ᗩᑕE ᗯOᖇᒪᗪ 👑`'
                  
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        pass

                elif ".pdf" in url:
                    if "cwmediabkt99" in url:
                        max_retries = 15  # Define the maximum number of retries
                        retry_delay = 4  # Delay between retries in seconds
                        success = False  # To track whether the download was successful
                        failure_msgs = []  # To keep track of failure messages
                        
                        for attempt in range(max_retries):
                            try:
                                await asyncio.sleep(retry_delay)
                                url = url.replace(" ", "%20")
                                scraper = cloudscraper.create_scraper()
                                response = scraper.get(url)

                                if response.status_code == 200:
                                    with open(f'{name}.pdf', 'wb') as file:
                                        file.write(response.content)
                                    await asyncio.sleep(retry_delay)  # Optional, to prevent spamming
                                    copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                                    os.remove(f'{name}.pdf')
                                    success = True
                                    break  # Exit the retry loop if successful
                                else:
                                    failure_msg = await m.reply_text(f"Attempt {attempt + 1}/{max_retries} failed: {response.status_code} {response.reason}")
                                    failure_msgs.append(failure_msg)
                                    
                            except Exception as e:
                                failure_msg = await m.reply_text(f"Attempt {attempt + 1}/{max_retries} failed: {str(e)}")
                                failure_msgs.append(failure_msg)
                                await asyncio.sleep(retry_delay)
                                continue  # Retry the next attempt if an exception occurs

                        # Delete all failure messages if the PDF is successfully downloaded
                        for msg in failure_msgs:
                            await msg.delete()
                            
                        if not success:
                            # Send the final failure message if all retries fail
                            await m.reply_text(f"Failed to download PDF after {max_retries} attempts.\n⚠️**Downloading Failed**⚠️\n**Name** =>> {str(count).zfill(3)} {name1}\n**Url** =>> {link0}", disable_web_page_preview)
                            
                    else:
                        try:
                            cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                            download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                            os.system(download_cmd)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            os.remove(f'{name}.pdf')
                        except FloodWait as e:
                            await m.reply_text(str(e))
                            time.sleep(e.x)
                            pass   

                elif ".ws" in url and  url.endswith(".ws"):
                    try:
                        await helper.pdf_download(f"{api_url}utkash-ws?url={url}&authorization={api_token}",f"{name}.html")
                        time.sleep(1)
                        await bot.send_document(chat_id=m.chat.id, document=f"{name}.html", caption=cc1)
                        os.remove(f'{name}.html')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        pass
                        
                elif ".zip" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.zip" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.zip', caption=cc1)
                        os.remove(f'{name}.zip')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        pass    

                elif any(ext in url for ext in [".mp3", ".wav", ".m4a"]):
                    try:
                        ext = url.split('.')[-1]
                        cmd = f'yt-dlp -x --audio-format {ext} -o "{name}.{ext}" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        await bot.send_document(chat_id=m.chat.id, document=f'{name}.{ext}', caption=cc1)
                        os.remove(f'{name}.{ext}')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        pass

                elif any(ext in url for ext in [".jpg", ".jpeg", ".png"]):
                    try:
                        ext = url.split('.')[-1]
                        cmd = f'yt-dlp -o "{name}.{ext}" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_photo(chat_id=m.chat.id, photo=f'{name}.{ext}', caption=cc1)
                        count += 1
                        os.remove(f'{name}.{ext}')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        pass
                                
                elif 'encrypted.m' in url:    
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅɪɴɢ Sᴛᴀʀᴛᴇᴅ...⏳**\n" \
                           f"🔗𝐋𝐢𝐧𝐤 » {url}\n" \
                           f"✦𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ [ᗩᑕE ᗯOᖇᒪᗪ 👑🐦](https://t.me/Query_810bot)"
                    prog = await m.reply_text(Show, disable_web_page_preview=True)
                    res_file = await helper.download_and_decrypt_video(url, cmd, name, appxkey)  
                    filename = res_file  
                    await prog.delete(True)  
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)    
                    await asyncio.sleep(1)  
                    pass

                elif 'drmcdni' in url or 'drm/wv' in url:
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅɪɴɢ Sᴛᴀʀᴛᴇᴅ...⏳**\n" \
                           f"🔗𝐋𝐢𝐧𝐤 » {url}\n" \
                           f"✦𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ [ᗩᑕE ᗯOᖇᒪᗪ 👑](https://t.me/Query_810bot)"
                    prog = await m.reply_text(Show, disable_web_page_preview=True)
                    res_file = await helper.decrypt_and_merge_video(mpd, keys_string, path, name, raw_text2)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    await asyncio.sleep(1)
                    pass
     
                else:
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅɪɴɢ Sᴛᴀʀᴛᴇᴅ...⏳**\n" \
                           f"🔗𝐋𝐢𝐧𝐤 » {url}\n" \
                           f"✦𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ [ᗩᑕE ᗯOᖇᒪᗪ 👑](https://t.me/Query_810bot)"
                    prog = await m.reply_text(Show, disable_web_page_preview=True)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    time.sleep(1)

            except Exception as e:
                    await m.reply_text(f"⚠️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐮𝐩𝐭𝐞𝐝\n\n🔗𝐋𝐢𝐧𝐤 » `{link}`\n\n__**⚠️Failed Reason »**__\n{str(e)}")
                    pass

    except Exception as e:
        await m.reply_text(str(e))

@bot.on_callback_query(filters.regex("^check_subscription$"))
async def check_subscription_callback(client: Client, callback_query):
    try:
        user_id = callback_query.from_user.id
        if await check_subscription(client, user_id):
            # Delete the join message
            await callback_query.message.delete()
            # Send success message
            await callback_query.message.reply_text(
                "**✅ Subscription Verified!**\n\n"
                "**Thank you for joining our channel. You can now use the bot!**\n\n"
                "**Now send /start to use the bot!**\n\n"
                "**⚠️ Remember: If you leave the channel, you will lose access!**",
                reply_markup=keyboard
            )
        else:
            await callback_query.answer(
                "⚠️ You haven't joined the channel yet! Please join first and click Verify again.",
                show_alert=True
            )
    except Exception as e:
        print(f"Check subscription callback error: {e}")
        await callback_query.answer("An error occurred. Please try again.", show_alert=True)

@bot.on_callback_query(filters.regex("^refresh_subscription$"))
async def refresh_subscription_callback(client: Client, callback_query):
    try:
        user_id = callback_query.from_user.id
        if await check_subscription(client, user_id):
            # Delete the join message
            await callback_query.message.delete()
            # Send success message
            await callback_query.message.reply_text(
                "**✅ Subscription Verified!**\n\n"
                "**Thank you for joining our channel. You can now use the bot!**\n\n"
                "**Now send /start to use the bot!**\n\n"
                "**⚠️ Remember: If you leave the channel, you will lose access!**",
                reply_markup=keyboard
            )
        else:
            await callback_query.answer(
                "⚠️ You still haven't joined the channel! Please join first.",
                show_alert=True
            )
            # Refresh the force subscribe message
            await force_subscribe_prompt(client, callback_query.message)
    except Exception as e:
        print(f"Refresh subscription callback error: {e}")
        await callback_query.answer("An error occurred. Please try again.", show_alert=True)

# Add force_sub decorator to your command handlers
@bot.on_message(filters.command(["start"]))
@force_sub
async def start_command(bot: Client, message: Message):
    # Your existing start command code remains unchanged
    pass

@bot.on_message(filters.command(["help"]))
@force_sub
async def txt_handler(client: Client, m: Message):
    # Your existing help command code remains unchanged
    pass

@bot.on_message(filters.command(["drm"]))
@force_sub
@is_sudo
async def txt_handler(bot: Client, m: Message):
    # Your existing drm command code remains unchanged
    pass

# Add force_sub decorator to other command handlers that should require subscription
# For example:
@bot.on_message(filters.command(["id"]))
@force_sub
async def id_command(client, message: Message):
    # Your existing id command code remains unchanged
    pass

@bot.on_message(filters.command(["info"]))
@force_sub
async def info(bot: Client, update: Message):
    # Your existing info command code remains unchanged
    pass

@bot.on_message(filters.command(["addadmin"]) & filters.private)
@is_admin
async def add_admin_command(client: Client, message: Message):
    try:
        # Check if a user ID was provided
        if len(message.command) != 2:
            await message.reply_text(
                "**⚠️ Invalid Format!**\n\n"
                "**Usage:** `/addadmin user_id`\n"
                "**Example:** `/addadmin 123456789`"
            )
            return

        # Get the user ID from the command
        user_id = int(message.command[1])

        # Check if user is already an admin
        if user_id in ADMIN_USERS:
            await message.reply_text("**⚠️ This user is already an admin!**")
            return

        # Add user to ADMIN_USERS list
        ADMIN_USERS.append(user_id)

        # Save to vars.py
        with open("vars.py", "r") as f:
            content = f.read()

        # Find the ADMIN_USERS list and update it
        if "ADMIN_USERS = [" in content:
            # Extract the list and add the new user
            start = content.find("ADMIN_USERS = [")
            end = content.find("]", start)
            current_list = content[start:end+1]
            new_list = current_list[:-1] + f", {user_id}]"
            content = content.replace(current_list, new_list)
        else:
            # If ADMIN_USERS list doesn't exist, create it
            content += f"\nADMIN_USERS = [{user_id}]"

        # Write back to vars.py
        with open("vars.py", "w") as f:
            f.write(content)

        await message.reply_text(
            f"**✅ Successfully added user {user_id} as admin!**\n\n"
            "**⚠️ Note:** The user will have permanent admin access until removed."
        )

    except ValueError:
        await message.reply_text("**⚠️ Invalid user ID! Please provide a valid numeric ID.**")
    except Exception as e:
        await message.reply_text(f"**⚠️ An error occurred:** {str(e)}")

@bot.on_message(filters.command(["removeadmin"]) & filters.private)
@is_admin
async def remove_admin_command(client: Client, message: Message):
    try:
        # Check if a user ID was provided
        if len(message.command) != 2:
            await message.reply_text(
                "**⚠️ Invalid Format!**\n\n"
                "**Usage:** `/removeadmin user_id`\n"
                "**Example:** `/removeadmin 123456789`"
            )
            return

        # Get the user ID from the command
        user_id = int(message.command[1])

        # Check if user is an admin
        if user_id not in ADMIN_USERS:
            await message.reply_text("**⚠️ This user is not an admin!**")
            return

        # Remove user from ADMIN_USERS list
        ADMIN_USERS.remove(user_id)

        # Save to vars.py
        with open("vars.py", "r") as f:
            content = f.read()

        # Find the ADMIN_USERS list and update it
        if "ADMIN_USERS = [" in content:
            start = content.find("ADMIN_USERS = [")
            end = content.find("]", start)
            current_list = content[start:end+1]
            # Remove the user ID from the list
            new_list = current_list.replace(f", {user_id}", "").replace(f"{user_id}, ", "").replace(f"{user_id}", "")
            content = content.replace(current_list, new_list)

            # Write back to vars.py
            with open("vars.py", "w") as f:
                f.write(content)

        await message.reply_text(
            f"**✅ Successfully removed admin privileges from user {user_id}!**"
        )

    except ValueError:
        await message.reply_text("**⚠️ Invalid user ID! Please provide a valid numeric ID.**")
    except Exception as e:
        await message.reply_text(f"**⚠️ An error occurred:** {str(e)}")

@bot.on_message(filters.command(["listadmins"]) & filters.private)
@is_admin
async def list_admins_command(client: Client, message: Message):
    try:
        if not ADMIN_USERS:
            await message.reply_text("**📝 No admins found in the list.**")
            return

        admin_list = "**📋 List of Admins:**\n\n"
        for i, admin_id in enumerate(ADMIN_USERS, 1):
            try:
                user = await client.get_users(admin_id)
                admin_list += f"{i}. {user.mention} (`{admin_id}`)\n"
            except:
                admin_list += f"{i}. Unknown User (`{admin_id}`)\n"

        await message.reply_text(admin_list)

    except Exception as e:
        await message.reply_text(f"**⚠️ An error occurred:** {str(e)}")

@bot.on_message(filters.command("adduser") & filters.private)
@is_admin
async def add_user_command(client: Client, message: Message):
    try:
        # Check if a user ID was provided
        if len(message.command) != 2:
            await message.reply_text(
                "**⚠️ Invalid Format!**\n\n"
                "**Usage:** `/adduser user_id`\n"
                "**Example:** `/adduser 123456789`"
            )
            return

        # Get the user ID from the command
        user_id = int(message.command[1])

        # Check if user is already in SUDO_USERS
        if user_id in SUDO_USERS:
            await message.reply_text("**⚠️ This user is already a sudo user!**")
            return

        # Add user to SUDO_USERS list
        SUDO_USERS.append(user_id)

        # Save to vars.py
        with open("vars.py", "r") as f:
            content = f.read()

        # Find the SUDO_USERS list and update it
        if "SUDO_USERS = [" in content:
            # Extract the list and add the new user
            start = content.find("SUDO_USERS = [")
            end = content.find("]", start)
            current_list = content[start:end+1]
            new_list = current_list[:-1] + f", {user_id}]"
            content = content.replace(current_list, new_list)
        else:
            # If SUDO_USERS list doesn't exist, create it
            content += f"\nSUDO_USERS = [{user_id}]"

        # Write back to vars.py
        with open("vars.py", "w") as f:
            f.write(content)

        await message.reply_text(
            f"**✅ Successfully added user {user_id} as a regular user!**\n\n"
            "**⚠️ Note:** The user will have access until removed."
        )

    except ValueError:
        await message.reply_text("**⚠️ Invalid user ID! Please provide a valid numeric ID.**")
    except Exception as e:
        await message.reply_text(f"**⚠️ An error occurred:** {str(e)}")

@bot.on_message(filters.command("removeuser") & filters.private)
@is_admin
async def remove_user_command(client: Client, message: Message):
    try:
        # Check if a user ID was provided
        if len(message.command) != 2:
            await message.reply_text(
                "**⚠️ Invalid Format!**\n\n"
                "**Usage:** `/removeuser user_id`\n"
                "**Example:** `/removeuser 123456789`"
            )
            return

        # Get the user ID from the command
        user_id = int(message.command[1])

        # Check if user is in SUDO_USERS
        if user_id not in SUDO_USERS:
            await message.reply_text("**⚠️ This user is not in the user list!**")
            return

        # Remove user from SUDO_USERS list
        SUDO_USERS.remove(user_id)

        # Save to vars.py
        with open("vars.py", "r") as f:
            content = f.read()

        # Find the SUDO_USERS list and update it
        if "SUDO_USERS = [" in content:
            start = content.find("SUDO_USERS = [")
            end = content.find("]", start)
            current_list = content[start:end+1]
            # Remove the user ID from the list
            new_list = current_list.replace(f", {user_id}", "").replace(f"{user_id}, ", "").replace(f"{user_id}", "")
            content = content.replace(current_list, new_list)

            # Write back to vars.py
            with open("vars.py", "w") as f:
                f.write(content)

        await message.reply_text(
            f"**✅ Successfully removed user {user_id} from the user list!**"
        )

    except ValueError:
        await message.reply_text("**⚠️ Invalid user ID! Please provide a valid numeric ID.**")
    except Exception as e:
        await message.reply_text(f"**⚠️ An error occurred:** {str(e)}")

@bot.on_message(filters.command("listusers") & filters.private)
@is_admin
async def list_users_command(client: Client, message: Message):
    try:
        if not SUDO_USERS:
            await message.reply_text("**📝 No regular users found in the list.**")
            return

        user_list = "**📋 List of Regular Users:**\n\n"
        for i, user_id in enumerate(SUDO_USERS, 1):
            try:
                user = await client.get_users(user_id)
                user_list += f"{i}. {user.mention} (`{user_id}`)\n"
            except:
                user_list += f"{i}. Unknown User (`{user_id}`)\n"

        await message.reply_text(user_list)

    except Exception as e:
        await message.reply_text(f"**⚠️ An error occurred:** {str(e)}")

@bot.on_message(filters.command("checkuser") & filters.private)
@is_admin
async def check_user_status(client: Client, message: Message):
    try:
        # Check if a user ID was provided
        if len(message.command) != 2:
            await message.reply_text(
                "**⚠️ Invalid Format!**\n\n"
                "**Usage:** `/checkuser user_id`\n"
                "**Example:** `/checkuser 123456789`"
            )
            return

        # Get the user ID from the command
        user_id = int(message.command[1])

        # Check user status
        status = []
        if user_id in ADMIN_USERS:
            status.append("👑 **Admin User**")
        if user_id in SUDO_USERS:
            status.append("⭐ **Regular User**")
        if not status:
            status.append("👤 **Normal User**")

        # Get user info
        try:
            user = await client.get_users(user_id)
            user_info = f"**User Info:**\n" \
                       f"**Name:** {user.first_name}\n" \
                       f"**Username:** @{user.username if user.username else 'None'}\n" \
                       f"**ID:** `{user_id}`\n\n" \
                       f"**Status:**\n" + "\n".join(status)
        except:
            user_info = f"**User Info:**\n" \
                       f"**ID:** `{user_id}`\n\n" \
                       f"**Status:**\n" + "\n".join(status)

        await message.reply_text(user_info)

    except ValueError:
        await message.reply_text("**⚠️ Invalid user ID! Please provide a valid numeric ID.**")
    except Exception as e:
        await message.reply_text(f"**⚠️ An error occurred:** {str(e)}")

@bot.on_message(filters.command("helpadmin") & filters.private)
@is_admin
async def help_admin_command(client: Client, message: Message):
    help_text = (
        "**👑 Admin Commands Guide**\n\n"
        "**User Management:**\n"
        "• `/adduser user_id` - Add a regular user\n"
        "• `/removeuser user_id` - Remove a regular user\n"
        "• `/listusers` - List all regular users\n"
        "• `/checkuser user_id` - Check user's status\n\n"
        "**Admin Management:**\n"
        "• `/addadmin user_id` - Add a new admin\n"
        "• `/removeadmin user_id` - Remove an admin\n"
        "• `/listadmins` - List all admins\n\n"
        "**Bot Control:**\n"
        "• `/stop` - Stop the bot\n"
        "• `/logs` - View bot logs\n"
        "• `/cookies` - Manage cookies\n"
        "• `/getcookies` - Get cookies file\n"
        "• `/mfile` - Get main.py file\n\n"
        "**File Operations:**\n"
        "• `/drm` - DRM file operations\n"
        "• `/t2t` - Text to txt converter\n"
        "• `/y2t` - YouTube to txt converter\n\n"
        "**⚠️ Note:** All commands require admin privileges\n"
        "**💡 Tip:** Use `/checkuser` to verify user status before adding/removing"
    )
    
    await message.reply_text(
        help_text,
        parse_mode="markdown",
        disable_web_page_preview=True
    )

# Remove all the complex startup code and just use the simple bot.run()
if __name__ == "__main__":
    print("Bot is starting...")
    bot.run()
    print("Bot stopped!")
