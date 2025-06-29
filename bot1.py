# AI Telegram Bot: Home Decor Assistant (Lithuania market)
# Target audience: Women 23-40+, language: Lithuanian
# Monetization: AliExpress affiliate links

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random

# --- PROMPTS & RESPONSES ---
decor_styles = [
    "minimalistinis skandinaviškas interjeras",
    "boho stiliaus dekoro sprendimai",
    "elegantiškas auksinis/veidrodinis stilius",
    "natūralus medžio ir lino derinys",
    "modernus industrinis stilius"
]

product_keywords = ["sienų dekoras", "lempos", "pagalvėlės", "žvakidės", "kilimai"]

film_items = [
    {
        "title": "Friends: Monikos sofa",
        "desc": "Geltona sofa kaip seriale \"Friends\"",
        "img": "https://i.imgur.com/nS9dF3y.jpg",
        "link": "https://rzekl.com/g/your-tag?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fitem%2F1005005902013682.html"
    },
    {
        "title": "Stranger Things: Lemputės",
        "desc": "Retro lemputės su raidėmis kaip seriale",
        "img": "https://i.imgur.com/KXLmZdB.jpg",
        "link": "https://rzekl.com/g/your-tag?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fitem%2F1005004149581144.html"
    },
    {
        "title": "Harry Potter: Pagalvėlės",
        "desc": "Gryffindor stiliaus dekoro elementai",
        "img": "https://i.imgur.com/D0t9vPo.jpg",
        "link": "https://rzekl.com/g/your-tag?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fitem%2F4001291526934.html"
    },
    {
        "title": "Wednesday: Gotikinė žvakidė",
        "desc": "Juoda gotikinė žvakidė kaip Enid ir Wednesday kambaryje",
        "img": "https://i.imgur.com/GkOLpMD.jpg",
        "link": "https://rzekl.com/g/your-tag?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fitem%2F1005005927261671.html"
    },
    {
        "title": "Bridgerton: Barokiniai veidrodžiai",
        "desc": "Veidrodžiai su auksiniais ornamentais kaip dvaro interjere",
        "img": "https://i.imgur.com/VujDd3v.jpg",
        "link": "https://rzekl.com/g/your-tag?ulp=https%3A%2F%2Fwww.aliexpress.com%2Fitem%2F1005005671463667.html"
    }
]

# Affiliate link (example)
affiliate_link = "https://rzekl.com/g/your-tag?ulp=https%3A%2F%2Fwww.aliexpress.com"

# --- Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [["1️⃣"], ["2️⃣"], ["3️⃣"]]
    await update.message.reply_text(
        "🛋️ Sveika! Aš esu tavo AI namų dekoro asistentė.\n"
        "Padėsiu tau rasti stilingus daiktus tavo namams 🪄\n\n"
        "Pasirink:\n"
        "1️⃣ Interjero stiliaus įkvėpimas\n"
        "2️⃣ Rasti konkretų produktą\n"
        "3️⃣ Filmai ir serialai 🎬",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True)
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.strip()

    if msg in ["1", "1️⃣"]:
        style = random.choice(decor_styles)
        await update.message.reply_text(f"Šiandien AI rekomenduoja: *{style}* – žiūrėk tinkamus daiktus čia: {affiliate_link}", parse_mode="Markdown")

    elif msg in ["2", "2️⃣"]:
        buttons = [[k] for k in product_keywords]
        await update.message.reply_text("Kokio produkto ieškai?", reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))

    elif msg.lower() in product_keywords:
        await update.message.reply_text(f"Ieškau „{msg}“... štai geriausias pasiūlymas: {affiliate_link}")

    elif msg in ["3", "3️⃣"]:
        for item in film_items:
            await update.message.reply_photo(
                photo=item["img"],
                caption=f"*{item['title']}*\n{item['desc']}\n[Peržiūrėti]({item['link']})",
                parse_mode="Markdown"
            )

    else:
        await update.message.reply_text("Parašyk 1️⃣, 2️⃣ arba 3️⃣, kad galėčiau padėti!")

# --- Init ---
app = ApplicationBuilder().token("8011999115:AA...tvojtoken").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

if __name__ == '__main__':
    app.run_polling()
