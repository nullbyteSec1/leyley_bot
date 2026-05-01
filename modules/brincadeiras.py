import random
import httpx

try:
    from telegram import Update
    from telegram.ext import ContextTypes
except ModuleNotFoundError:
    print("""
    Use: python run.py --install
    para baixar as dependências e usar o bot.
    """)


async def calc_gay(target: str, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pct = random.randint(0, 100)
    with open("./media/imagens/lgbt.jpg", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=f"🏳️‍🌈 O {target} é {pct}% gay\n\n> by leyley_404 bot"
        )


async def calc_lesbica(target: str, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pct = random.randint(0, 100)
    with open("./media/imagens/lgbt.jpg", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=f"✂️ A {target} é {pct}% lésbica\n\n> by leyley_404 bot"
        )


async def calc_gostosa(target: str, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pct = random.randint(0, 100)
    with open("./media/imagens/gostosa.jpg", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=f"🍑 A {target} é {pct}% gostosa\n\n> by leyley_404 bot"
        )


async def calc_pobre(target: str, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pct = random.randint(0, 100)
    with open("./media/imagens/pobre.jpg", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=f"💸 O(a) {target} é {pct}% pobre\n\n> by leyley_404 bot"
        )


async def calc_casal(target1: str, target2: str, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not target1 or not target2:
        await update.message.reply_text("❌ Use: /casal @amigo1 @amigo2")
        return

    pct = random.randint(0, 100)
    with open("./media/imagens/casal.jpg", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=f"❤️ {target1} e {target2} combinam {pct}% como casal\n\n> by leyley_404 bot"
        )


async def calc_nacionalidade(target: str, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        resp = httpx.get(f"https://api.nationalize.io/?name={target}", timeout=5.0)
        resp.raise_for_status()
        data = resp.json()

        if data.get("country") and len(data["country"]) > 0:
            country = data["country"][0]["country_id"]
            with open("./media/imagens/icon.jpg", "rb") as photo:
                await update.message.reply_photo(
                    photo=photo,
                    caption=f"🌍 Nacionalidade de {target}: {country}\n\n> by leyley_404 bot"
                )
        else:
            await update.message.reply_text(f"Não foi possível determinar a nacionalidade de {target}.")
    except Exception:
        await update.message.reply_text("❌ Erro ao consultar a API de nacionalidade.")


async def get_perfil(target: str, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not target:
        await update.message.reply_text("❌ Use: /perfil @amigo", quote=True)
        return

    patrimonio = random.randint(0, 9999)
    programa = random.randint(0, 9999)

    template = f"""
╔══════════════════════╗
║     PERFIL DE {target.upper()}     ║
╠══════════════════════╣
║ 🤑 PATRIMÔNIO: ${patrimonio:04d}    ║
║ 🫦 VALOR DO PROGRAMA: ${programa:04d} ║
╚══════════════════════╝
    """.strip()

    try:
        with open("./media/imagens/icon.jpg", "rb") as photo:
            await update.message.reply_photo(
                photo=photo,
                caption=template
            )
    except Exception:
        await update.message.reply_text(template)
