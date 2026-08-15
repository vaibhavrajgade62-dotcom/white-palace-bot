import datetime
import google.generativeai as genai
import pytz
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Aapka Telegram Bot Token
TELEGRAM_BOT_TOKEN = "8568639233:AAHTVzvDi3M9e8XkukJL37lHM4DH8wyW0Y4"

# Aapki Gemini API Key
GEMINI_API_KEY = "AQ.Ab8RN6LF3kYL7IRm5W-RkRInbC"

# Gemini AI Setup
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=(
        "Aap ek real insaan, business partner aur sharp market analyst ki tarah behave karein. "
        "User ke sath natural Hinglish me baat karein, koi robotic tone nahi. "
        "Agarbatti manufacturing, raw materials, fragrance trends, packaging costing aur branding me aap expert hain. "
        "General baaton ka friendly jawab dein, aur business sawalon par realistic numbers aur practical calculation batayein."
    ),
)

ADMIN_CHAT_ID = ""


# Daily Market Report
def generate_agarbatti_report():
    today_str = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime(
        "%d %B %Y"
    )
    prompt = (
        f"Generate a sharp Daily Agarbatti Business & Market Analysis for date {today_str}. "
        "Include: 1. Raw Material Trends (Bamboo sticks, DEP, powders), "
        "2. Fragrance demand, 3. Packaging & margin insight, 4. 1 actionable tip. Keep it structured with emojis."
    )
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Report fetch issue: {str(e)}"


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global ADMIN_CHAT_ID
    ADMIN_CHAT_ID = str(update.effective_chat.id)

    welcome_text = (
        "Namaste! 👋 Main live hoon aur aapke business ke sath ready hoon.\n\n"
        "• Mujhse normal insaan ki tarah koi bhi sawal ya calculation pucho.\n"
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
        response = model.generate_content(user_query)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")


# Scheduled 9:00 PM Daily Push
async def send_daily_update(context: ContextTypes.DEFAULT_TYPE):
    if ADMIN_CHAT_ID:
        report = generate_agarbatti_report()
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=report)


def main():
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

    app.run_polling()


if __name__ == "__main__":
    main()
