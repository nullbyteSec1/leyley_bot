import json
import threading
from modules.brincadeiras import calc_gay,calc_lesbica,calc_nacionalidade,calc_casal,calc_gostosa,calc_pobre,get_perfil
from modules.geral import menu,start,button_handler
from modules.dowloads import dowload_and_send
from modules.puxadas import puxada_ip,puxada_cep,puxada_cnpj
from modules.hentai import rule34,hentai_video
from dev.main import install,cls,load_config
try:
  from telegram import Update
  from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,CallbackQueryHandler,MessageHandler,filters
  import httpx
except ModuleNotFoundError:
  install()


TOKEN,OWNER_ID  = load_config()

COMMANDS = {}
def command(name):
  def wrapper(func):
     COMMANDS[name] = func
     return func
  return wrapper

@command("start")
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await start(update,context)

@command("menu")
async def menu_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
   await  menu(update,context)

@command("gay")
async def calc_gay_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
     return  await calc_gay(context.args[0],update,context) 

@command("gostosa")
async def calc_gotosa_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    return await calc_gostosa(context.args[0],update,context)

@command("get_perfil")
async def get_perfil_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    return await get_perfil(context.args[0],update,context) 

@command("pobre")
async def calc_pobre_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    return await calc_pobre(context.args[0],update,context)

@command("lesbica")
async def calc_lesbica_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await calc_lesbica(context.args[0],update,context)

@command("nacionalidade")
async def calc_nacionalidade_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await calc_nacionalidade(context.args[0],update,context)

@command("casal")
async def calc_casal_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await calc_casal(context.args[0],context.args[1],update,context)

@command("tiktok")
async def dowload_and_send_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await dowload_and_send(context.args[0],update,context)

@command("instagram")
async def instagram(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await dowload_and_send(context.args[0],update,context)

@command("ip")
async def puxada_ip_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await puxada_ip(context.args[0],update,context)

@command("cep")
async def puxada_cep_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await puxada_cep(context.args[0],update,context)

@command("cnpj")
async def puxada_cnpj_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await puxada_cnpj(context.args[0],update,context)

@command("rule34")
async def rule34_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await rule34(context.args[0],update,context)

@command("hentai_video")
async def hentai_video_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await hentai_video(context.args[0],update,context)

if __name__ == "__main__":
     app = ApplicationBuilder().token(TOKEN).build()    
     for cmd, func in COMMANDS.items():       
        app.add_handler(CommandHandler(cmd, func)) 
     app.add_handler(CallbackQueryHandler(button_handler))

     cls()
     ascii_banner = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣵⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⣿⣿⣦⡀⠀⠀⠀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠟⠁⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣦⡀⠀⠀⠈⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠇⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⢙⡧⠠⣄⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⣠⠏⠀⢠⠏⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠈⢷⢦⠀⠀⣠⣾⣿⡆⢸⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢰⠃⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⡽⠲⡀⠀⠀⢀⣼⣾⣀⠔⢭⣿⡿⢳⣼⠀⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠮⣷⣄⡀⠀⢷⣄⠀⠀⠀⢀⡞⠁⠀⡼⣀⠴⣫⠶⠛⢧⡀⣸⣿⡔⢺⡇⢀⠇⠀⠀⠀⠀⠀⣰⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠋⠓⠾⠏⠳⣄⣀⡜⠀⠀⠚⠋⢡⠞⢁⡤⣶⣾⡟⣿⣟⠀⢸⠄⢸⠀⠀⠀⠀⢀⣼⡿⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢿⡗⠒⠢⣄⡀⠀⠉⠀⠀⠀⠀⣠⡿⠚⠙⣷⡿⠟⢸⣿⠙⠀⣸⠀⡇⠀⠀⠀⢀⣾⠟⡠⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⢸⡿⣋⣹⣟⣷⣄⠀⠀⠀⠀⠀⠛⠒⠒⠉⠁⠀⠀⡾⣿⣇⡴⠁⠀⡇⠀⠀⢀⣾⡟⡔⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣶⡄⣀⣼⠁⠀⣿⠁⠉⠁⠀⠀⠀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡿⠁⠀⠀⢸⠀⠀⠀⣼⡿⡰⠁⠀⠀⠀⠀
   ⠀⠀⠀⠀⢿⣿⣿⣿⣿⠃⠀⠀⡟⢦⠀⠀⠀⠀⠺⠄⠀⠀⠀⣠⡞⠀⠀⠀⠀⢠⡇⡇⠀⠀⠀⢸⠀⠀⢰⣿⠃⠀⠀⠀⠀
   ⠀⠀⠀⠀⠈⠉⢸⣿⠏⠀⠀⣸⠀⡏⠑⢦⡀⠀⠀⠐⣾⣿⣿⡿⠁⠀⠀⣀⠴⠉⡇⢹⠀⠀⠀⢸⠀⠀⣸⣿⠘⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⢀⣯⡤⠄⢴⠇⣸⣀⡀⠀⠉⠓⠦⣀⡉⠉⠉⠀⢀⡤⡾⠁⠀⣰⡇⢸⣷⣦⠤⠞⠒⠒⠺⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⢀⡎⢠⠃⠀⠉⠙⠒⠂⠤⠤⣽⠓⠒⠊⠉⠀⣧⣀⣼⣿⡇⠀⣿⣿⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⢀⡞⢠⠇⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⡇⠀⡿⠃⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⠋⡼⠀⠀⠀⡞⢠⠏⠀⠀⠈⠑⠦⡀⠀⠀⠀⢀⣀⣤⣴⣶⣿⣿⣿⣿⣿⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠟⠁⢠⠇⠀⠀⡸⣰⣯⠏⠀⠀⠀⢀⣀⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡇⢀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀
⠀⢀⡼⠧⠶⠦⠾⠦⠤⠤⠷⠿⠥⠤⠤⠶⠿⠋⣸⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⡇⡜⠀⠀⠀⠀⠀⠀⣸⣄⠀⠀⠀⠀⠀
⠀⣾⡄⠀⠀⠀⠀⠀⠀⠀⠀⡀⠰⣤⣤⣤⣴⣾⣿⣦⣈⠙⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠤⠼⣟⠁⠀⠀⠀⠀⠀⢠⠟⢏⠻⠷⣦⣀⣀
⠞⡏⠳⣄⡀⠀⠀⠀⠀⠘⡆⢹⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⢀⡞⠀⠈⢆⠀⠀⠀⠀
⠀⡇⠀⠀⠈⡏⠹⡟⣆⠀⢃⢸⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⡴⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⢸⠆⠀⠀⠀⡼⠁⠀⠀⠈⢆⠀⠀⠀
⠀⠀⠀⠀⠀⢧⠀⠹⢶⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⠋⡰⠋⢁⣠⢤⣤⣤⡴⠚⠁⠀⡼⠀⠀⠀⢰⠃⠀⠀⠀⠀⠈⡆⠀⠀
⠀⠀⠀⠀⠀⢸⡀⠀⠈⡆⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⣉⣴⣾⣿⡟⠀⠀⠀⠀⡇⠀⠀⢀⠟⡇⠀⠀⠀⠀⠀⠸⠀⠀
⠀⠀⠀⠀⠀⠀⢧⠀⠀⡇⢸⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⢠⠇⠀⠀⡼⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠘⡆⠀⣣⢸⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⢸⠀⠀⣰⠁⠀⠈⣇⠀⠀⠀⠀⠀
------------------------------------------------------------
|  _          __  .__                 ___.           __     |
| |  |   _____/  |_|  |   ____ ___.__. \_ |__   _____/  |_  |
| |  | _/ __ \   __\  | _/ __ <   |  |  | __ \ /  _ \   __\ |
| |  |_\  ___/|  | |  |_\  ___/\___  |  | \_\ (  <_> )  |   |
| |____/\___   __| |____/\___    ____|  |___  /\____/|__|   |
|  \/               \/\/           \/                       |
-------------------------------------------------------------
     """
     print(ascii_banner)
     app.run_polling()
