# This Repo was not fully owned by me. Some codes are scraped from respected DEVOLEPERS whom where mine friends. 
# check Readme.md For More. 

import logging
logger = logging.getLogger(__name__)
LOGGER = logging.getLogger(__name__)
import os, re, time, math, json, string, random, traceback, wget, asyncio, datetime, aiofiles, aiofiles.os, requests, youtube_dl, lyricsgenius
from config import Config
from random import choice 
import yt_dlp
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from pytube import YouTube
from youtubesearchpython import VideosSearch
from youtubesearchpython import SearchVideos
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid


Bot = Client(
    "Song Downloader Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)



START_TEXT = """ Hai {}, 
Iam a song download Bot 🙂
"""

CMDS_TEXT = """
Hey {} This are this bots power🌠
"""

ABOUT_TEXT = """
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰ 𝐀𝐁𝐎𝐔𝐓 ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣ 
║ 𝙈𝙔𝙉𝘼𝙈𝙀-𝐌𝐀𝐊𝐑𝐈_𝐒𝐎𝐍𝐆𝐁𝐎𝐓 
║┣⪼𝓓𝓮𝓿𝓸𝓵𝓸𝓹𝓮𝓻 -[𝐌𝐀𝐊𝐑𝐈](https://t.me/blesson_3)
║┣⪼ 𝓛𝓲𝓫𝓻𝓪𝓻𝓻𝔂 - [𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼](https://pyrogram.org)
║┣⪼ 𝓛𝓪𝓷𝓰𝓾𝓪𝓰𝓮 - [𝙿𝚈𝚃𝙷𝙾𝙽 𝟹](https://python.org)
║┣⪼ 𝓑𝓸𝓽 𝓼𝓮𝓻𝓿𝓮𝓻 -  [𝙷𝙴𝚁𝙾𝙺𝚄](https://heroku.com)
║┣⪼ 𝓑𝓾𝓲𝓵𝓭 𝓢𝓽𝓪𝓽𝓾𝓼 - v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
║╰━━━━━━━━━━━━━━━➣ ╚══════════════════❍⊱❁۪۪
"""
MUSIC = """ **🎧MUSIC**
You can also use this feature in group too
➩ /music <songname artist(optional)>: uploads the song in it's best quality available
You can also use these commands
➩/song
➩/s
➩/m
"""
 
VSONG = """ **📀VSONG📀**
You can also use this feature in group too
➩ /vsong <songname artist(optional)>: uploads the video song in it's best quality available
➩ /video <songname artist(optional)>: uploads the video song in it's best quality available
"""
  
LYRICS = """ **🎶LYRICS🎶**
You can also use this feature in group too
➩ /lyrics <songname>: uploads the lyrics of song
"""

YOUTUBE = """  **📽️YOUTUBE📽️**
You can also use this feature in group too

➩ /ytaudio <youtubelink>: uploads the audio of song in it's best quality available
➩ /ytvideo <youtubelink>: uploads the video of song in it's best quality available
you can also use inline for search YouTube video or song
"""


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Support📕', url=f"https://telegram.me/{Config.SUPPORT}"), 
        InlineKeyboardButton(text="SEARCH🔎", switch_inline_query_current_chat="")
        ],[
        InlineKeyboardButton('HELPℹ️', callback_data ='cmds'),        
        InlineKeyboardButton('ABOUT😁', callback_data='about')        
        ]]
    )
CMDS_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎧MUSIC🎧', callback_data='song'),
        InlineKeyboardButton('📀VSONG📀', callback_data='video')
        ],[
        InlineKeyboardButton('🎶LYRICS🎶', callback_data='lyrics'),
        InlineKeyboardButton('📽️YOUTUBE📽️', callback_data='youtube')
        ],[
        InlineKeyboardButton('🏠 Home', callback_data='home'),            
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('HOME🏡', callback_data='home'),
        InlineKeyboardButton('CLOSE🔐', callback_data='close')
        ]]
    )
MUSIC_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
    )
SOURCE_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='about')
        ]]
    )
YOUTUBE_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text="SEARCH🔎", switch_inline_query_current_chat=""),
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
    )
VSONG_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
    )
LYRICS_BUTTON = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('👩‍🦯 Back', callback_data='help')
        ]]
    )
        
@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "cmds":
        await update.message.edit_text(
            text=CMDS_TEXT.format(update.from_user.mention),
            reply_markup=CMDS_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "song":
        await update.message.edit_text(
            text=MUSIC,
            reply_markup=MUSIC_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "video":
        await update.message.edit_text(
            text=VSONG,
            reply_markup=VSONG_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "lyrics":
        await update.message.edit_text(
            text=LYRICS,
            reply_markup=LYRICS_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "youtube":
        await update.message.edit_text(
            text=YOUTUBE,
            reply_markup=YOUTUBE_BUTTON,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()




async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join(["🔴" for i in range(math.floor(percentage / 10))]),
            "".join(["🔘" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    "{}\n**File Name:** `{}`\n{}".format(type_of_ps, file_name, tmp)
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit("{}\n{}".format(type_of_ps, tmp))
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass


def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None
        
@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):    
    await update.reply_photo(
        photo="https://telegra.ph/file/a9522ca5294a086a5dbe8.jpg",
        caption=START_TEXT.format(update.from_user.mention),            
        reply_markup=START_BUTTONS
    )

@Bot.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_photo(
        photo="https://telegra.ph/file/a9522ca5294a086a5dbe8.jpg",
        caption=ABOUT_TEXT,        
        reply_markup=ABOUT_BUTTONS
    )



async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))




	
@Bot.on_inline_query()
async def inline(client: Client, query: InlineQuery):
    answers = []
    search_query = query.query.lower().strip().rstrip()

    if search_query == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text="Search your query here...🔎",
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        search = VideosSearch(search_query, limit=50)

        for result in search.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description="{}, {} views.".format(
                        result["duration"],
                        result["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "https://www.youtube.com/watch?v={}".format(
                            result["id"]
                        )
                    ),
                    thumb_url=result["thumbnails"][0]["url"]
                )
            )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out",
                switch_pm_parameter="",
            )
        

@Bot.on_message(filters.command("lyrics"))
async def lrsearch(_, message: Message):  
    m = await message.reply_text("Searching Lyrics")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("Lyrics not found..")
    xxx = f"""
**Lyrics Search Powered By Music Bot**
**Searched Song:-** __{query}__
**Found Lyrics For:-** __{S.title}__
**Artist:-** {S.artist}
**__Lyrics:__**
{S.lyrics}"""
    await m.edit(xxx)


def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


def download_youtube_audio(url: str):
    global is_downloading
    with yt_dlp.YoutubeDL(
        {
            "format": "bestaudio",
            "writethumbnail": True,
            "quiet": True,
        }
    ) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        if int(float(info_dict["duration"])) > 180:
            is_downloading = False
            return []
        ydl.process_info(info_dict)
        audio_file = ydl.prepare_filename(info_dict)
        basename = audio_file.rsplit(".", 1)[-2]
        if info_dict["ext"] == "webm":
            audio_file_opus = basename + ".opus"
            ffmpeg.input(audio_file).output(
                audio_file_opus, codec="copy", loglevel="error"
            ).overwrite_output().run()
            os.remove(audio_file)
            audio_file = audio_file_opus
        thumbnail_url = info_dict["thumbnail"]
        thumbnail_file = (
            basename + "." + get_file_extension_from_url(thumbnail_url)
        )
        title = info_dict["title"]
        performer = info_dict["uploader"]
        duration = int(float(info_dict["duration"]))
    return [title, performer, duration, audio_file, thumbnail_file]

def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


def download_youtube_audio(url: str):
    global is_downloading
    with yt_dlp.YoutubeDL(
        {
            "format": "bestaudio",
            "writethumbnail": True,
            "quiet": True,
        }
    ) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        if int(float(info_dict["duration"])) > 180:
            is_downloading = False
            return []
        ydl.process_info(info_dict)
        audio_file = ydl.prepare_filename(info_dict)
        basename = audio_file.rsplit(".", 1)[-2]
        if info_dict["ext"] == "webm":
            audio_file_opus = basename + ".opus"
            ffmpeg.input(audio_file).output(
                audio_file_opus, codec="copy", loglevel="error"
            ).overwrite_output().run()
            os.remove(audio_file)
            audio_file = audio_file_opus
        thumbnail_url = info_dict["thumbnail"]
        thumbnail_file = (
            basename + "." + get_file_extension_from_url(thumbnail_url)
        )
        title = info_dict["title"]
        performer = info_dict["uploader"]
        duration = int(float(info_dict["duration"]))
    return [title, performer, duration, audio_file, thumbnail_file]


def yt_search(song):
    videosSearch = VideosSearch(song, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url

@Bot.on_message(filters.command(['s']))
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('🔎 𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐭𝐡𝐞 𝐬𝐨𝐧𝐠...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            views = results[0]["views"]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('𝐅𝐨𝐮𝐧𝐝 𝐍𝐨𝐭𝐡𝐢𝐧𝐠. 𝐓𝐫𝐲 𝐂𝐡𝐚𝐧𝐠𝐢𝐧𝐠 𝐓𝐡𝐞 𝐒𝐩𝐞𝐥𝐥𝐢𝐧𝐠 𝐀 𝐋𝐢𝐭𝐭𝐥𝐞 😕')
            return
    except Exception as e:
        m.edit(
            "✖️ 𝐅𝐨𝐮𝐧𝐝 𝐍𝐨𝐭𝐡𝐢𝐧𝐠. 𝐒𝐨𝐫𝐫𝐲.\n\n𝐓𝐫𝐲 𝐀𝐧𝐨𝐭𝐡𝐞𝐫 𝐊𝐞𝐲𝐰𝐨𝐫𝐤 𝐎𝐫 𝐌𝐚𝐲𝐛𝐞 𝐒𝐩𝐞𝐥𝐥 𝐈𝐭 𝐏𝐫𝐨𝐩𝐞𝐫𝐥𝐲.\n\nEg.`/s Faded`"
        )
        print(str(e))
        return
    m.edit("🔎 𝐅𝐢𝐧𝐝𝐢𝐧𝐠 𝐀 𝐒𝐨𝐧𝐠 🎶 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 ⏳️ 𝐅𝐨𝐫 𝐅𝐞𝐰 𝐒𝐞𝐜𝐨𝐧𝐝𝐬 [🚀](https://telegra.ph/file/67f41ae52a85dfc0551ae.mp4)")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎧 𝐓𝐢𝐭𝐥𝐞 : [{title[:35]}]({link})\n⏳ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 : `{duration}`\n🎬 𝐒𝐨𝐮𝐫𝐜𝐞 : [Youtube](https://youtu.be/3pN0W4KzzNY)\n👁‍🗨 𝐕𝐢𝐞𝐰𝐬 : `{views}`\n\n💌 𝐁𝐲 : @SongPlayRoBot'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('❌ 𝐄𝐫𝐫𝐨𝐫\n\n Report This Erorr To Fix @TamilSupport ❤️')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

Bot.run()
