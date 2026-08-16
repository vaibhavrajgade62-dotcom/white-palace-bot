import asyncio
import datetime
import os
import aiohttp
from aiohttp import web
import pytz
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Aapke Tokens
TELEGRAM_BOT_TOKEN = "8568639233:AAHTVzvDi3M9e8XkukJL37lHM4DH8wyW0Y4"
GEMINI_API_KEY = "AQ.Ab8RN6LF3kYL7IRm5W-RkRlnbCJQHrfGeNJ3DPWClzR9504rmg"

SYSTEM_PROMPT = (
    "Aap ek real human business partner aur sharp agarbatti market advisor hain. "
    "User ke sath natural, warm Hinglish me baat karein. "
    "Costing, raw materials (bamboo, DEP, fragrance), packaging aur business growth tips par realistic calculations dein."
)

ADMIN_CHAT_ID = ""


# Direct Google Gemini REST API Call
async def ask_gemini_direct(prompt_text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": prompt_text}]}],
        "systemInstruction": {"parts": [{"text": SYSTEM_PROMPT}]},
    }
    headers = {"Content-Type": "application/json"}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, json=payload, headers=headers, timeout=20
            ) as resp:
                data = await resp.json()
                if (
                    "candidates" in data
                    and len(data["candidates"]) > 0
                    and "content" in data["candidates"][0]
                ):
                    return data["candidates"][0]["content"]["parts"][0]["text"]
                elif "error" in data:
                    return f"API Error: {data['error'].get('message', 'Key issue')}"
                else:
                    return "Bhai, report process nahi ho saki. Dobara try karein."
    except Exception as e:
        return f"Connection issue: {str(e)}"


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
    today_str = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime(
        "%d %B %Y"
    )
    prompt = (
        f"Generate a sharp Daily Agarbatti Business & Market Analysis for date {today_str}. "
        "Include: 1. Raw Material Trends (Bamboo sticks, DEP, powders), "
        "2. Fragrance demand & dipping ratios, "
        "3. Packaging & margin insight, 4. 1 actionable tip. Keep it structured with emojis."
    )
    reply = await ask_gemini_direct(prompt)
    await update.message.reply_text(reply)


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

    reply = await ask_gemini_direct(user_query)
    await update.message.reply_text(reply)


# 9:00 PM Auto Send
async def send_daily_update(context: ContextTypes.DEFAULT_TYPE):
    if ADMIN_CHAT_ID:
        today_str = datetime.datetime.now(
            pytz.timezone("Asia/Kolkata")
        ).strftime("%d %B %Y")
        prompt = f"Generate a sharp Daily Agarbatti Market Analysis for {today_str}."
        report = await ask_gemini_direct(prompt)
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=report)


# Port Server for Render
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
