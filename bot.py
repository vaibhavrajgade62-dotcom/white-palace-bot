import asyncio
import datetime
import os
from aiohttp import web
from google import genai
from google.genai import types
import pytz
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Tokens
TELEGRAM_BOT_TOKEN = "8568639233:AAHTVzvDi3M9e8XkukJL37lHM4DH8wyW0Y4"
GEMINI_API_KEY = "AQ.Ab8RN6LF3kYL7IRm5W-RkRlnbCJQHrfGeNJ3DPWClzR9504rmg"

# Gemini Client Setup
client = genai.Client(api_key=GEMINI_API_KEY)
SYSTEM_PROMPT = (
    "Aap ek real human business partner aur sharp agarbatti market advisor hain. "
    "User ke sath natural, warm Hinglish me normal insaan ki tarah baat karein. "
    "Costing, raw materials (bamboo, DEP, fragrance), packaging aur business growth tips par realistic calculations aur strategies dein."
)

ADMIN_CHAT_ID = ""


# AI Response Generator (Auto-fallback to stable models)
def call_gemini(prompt_text):
    models_to_try = [
        "gemini-1.5-flash",
        "gemini-2.0-flash",
        "gemini-1.5-pro",
    ]
    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt_text,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT
                ),
            )
            if response and response.text:
                return response.text
        except Exception:
            continue
    return "Market update fetch nahi ho paya, kripya thodi der baad try karein."


# Daily Market Report Generator
def generate_agarbatti_report():
    today_str = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime(
        "%d %B %Y"
    )
    prompt = (
        f"Generate a sharp Daily Agarbatti Business & Market Analysis for date {today_str}. "
        "Include: 1. Raw Material Trends (Bamboo sticks, DEP, powders), "
        "2. Fragrance demand & dipping ratios, "
        "3. Packaging & margin insight, 4. 1 actionable tip. Keep it structured with emojis."
    )
    return call_gemini(prompt)


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global ADMIN_CHAT_ID
    ADMIN_CHAT_ID = str(update.effective_chat.id)

    welcome_text = (
        "Namaste! 👋 Main live hoon aur aapke business ke sath ready hoon.\n\n"
        "• Normal insaan ki tarah mujhse koi bhi sawal ya calculation pucho.\n"
        "• Roz shaam *9:00 PM* par market update main khud bhejunga.\n"
        "• Abhi market report dekhne ke liye: /report"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")


# /report command
async def report_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id, action="typing"
    )
    report = generate_agarbatti_report()
    await update.message.reply_text(report)


# Chat Handler
async def human_chat_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    global ADMIN_CHAT_ID
    ADMIN_CHAT_ID = str(update.effective_chat.id)

    user_query = update.message.text
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id, action="typing"
    )

    try:
        reply = call_gemini(user_query)
        await update.message.reply_text(reply)
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")


# Scheduled 9:00 PM Daily Push
async def send_daily_update(context: ContextTypes.DEFAULT_TYPE):
    if ADMIN_CHAT_ID:
        report = generate_agarbatti_report()
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=report)


# Web Server for Render Port Check
async def handle_ping(request):
    return web.Response(text="Bot is running active!")


async def run_web_server():
    server = web.Application()
    server.router.add_get("/", handle_ping)
    port = int(os.environ.get("PORT", 10000))
    runner = web.AppRunner(server)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()


async def main():
    await run_web_server()

    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("report", report_command))
    app.add_handler(
        MessageHandler(filters.TEXT & (~filters.COMMAND), human_chat_handler)
    )

    tz = pytz.timezone("Asia/Kolkata")
    target_time = datetime.time(hour=21, minute=0, second=0, tzinfo=tz)

    job_queue = app.job_queue
    if job_queue:
        job_queue.run_daily(send_daily_update, time=target_time)

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
                
