from scraping34 import Scraping34
from telegram import Update
from telegram.ext import ContextTypes
import os


async def rule34(character:str,update:Update,context:ContextTypes.DEFAULT_TYPE):
    if not character:
        await update.message.reply_text("❌Erro use /rule34 <personagem> \n exemplo /rule34 tsunade naruto")

    scraping = Scraping34(character,"./dowloads/rule34.jpg","photo")
    scraping.run()
    await update.message.reply_photo(
        photo="./dowloads/rule34.jpg",
        caption=f"{character} rule34 \n by leyleybot"
    )
    os.system("rm ./dowloads/rule34.jpg")


async def hentai_video(character:str,update:Update,context:ContextTypes.DEFAULT_TYPE):
    if not character:
        await update.message.reply_text("❌Erro use /rule34 <personagem> \n exemplo /hentai_video tsunade naruto")
    await update.message.reply_text("🕷️baixando o seu video pode demorar um pouco")
    scraping = Scraping34(character,"./dowloads/hentai.mp4","video")
    scraping.run()
    with open("./dowloads/hentai.mp4","rb") as video:
         await update.message.reply_video(
               video=video,
               caption=f"video hentai de {character} encontrado"
          )
    os.system("rm ./dowloads/hentai.mp4")

