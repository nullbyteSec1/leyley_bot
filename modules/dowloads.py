from yt_dlp import YoutubeDL
from telegram import Update
from telegram.ext import ContextTypes
import os


DOWNLOAD_PATH = "./dowloads"
os.makedirs(DOWNLOAD_PATH,exist_ok=True)

async def dowload_and_send(url:str,update: Update,context:ContextTypes) -> None:
    if not url:
        await update.message.reply_text("❌Error url não definida \n\n use /yt <url>")
        return
    if not url.startswith(("http://","https://")):
        await update.message.reply_text("❌error link inválido")
        return 


    msg = await update.message.reply_text("⏳baixando video pode demorar um pouco")

    try:
        ydl_opts = {
            "format":"bestvideo+bestaudio/best",
            'merge_output_format': 'mp4',
            'outtmpl': f'{DOWNLOAD_PATH}/%(title)s.%(ext)s',
            'noplaylist': True, 
            'quiet': True,
            'no_warnings': True,
            'format': 'best[height<=720]',  
        }
        with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

        with open(filename, 'rb') as video_file:
            await context.bot.send_video(
                chat_id=update.effective_chat.id,
                video=video_file,
                caption=f"🎥 {info.get('title', 'Vídeo')}\n🔗 {url}",
                supports_streaming=True,   
                read_timeout=300,          
                write_timeout=300,
                connect_timeout=300,
                                                                                                    )
            msg.delete()
    except Exception as e:
        await update.message.reply_text(f"❌ {e}")
        return 
    finally:
        try:
            if 'filename' in locals() and os.path.exists(filename):
                os.remove(filename)
        except Exception:
                pass



