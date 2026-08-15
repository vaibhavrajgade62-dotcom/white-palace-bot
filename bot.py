import datetime
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
BOT_TOKEN = "8568639233:AAHTVzvDi3M9e8XkukJL37lHM4DH8wyW0Y4"

# Daily auto-report ke liye chat ID
ADMIN_CHAT_ID = ""


def generate_agarbatti_report():
    today_str = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime(
        "%d %B %Y"
    )
    report = f"""📊 *DAILY AGARBATTI INDUSTRY & MARKET DIGEST*
📅 *Date:* {today_str} | *Time:* 09:00 PM IST

━━━━━━━━━━━━━━━━━━━━━
🌿 *1. RAW MATERIAL & COST TRENDS*
• *Bamboo Sticks (8" / 9"):* ₹115 – ₹130 / kg (Supply stable).
• *Jigat Powder (Quality A):* ₹65 – ₹80 / kg.
• *Charcoal Powder / Sawdust:* ₹18 – ₹28 / kg.
• *DEP Oil (Carrier):* ₹140 – ₹160 / kg.
• *Raw Agarbatti (Count ~950-1000):* ₹72 – ₹85 / kg.

🌸 *2. FRAGRANCE & CONSUMER DEMAND*
• *Top Scents:* Sandalwood, Rose, Mogra, Lavender, Sambrani Dhoop.
• *Trending:* Citronella (Mosquito repellent demand), Flora Bathi.
• *Dipping Target Ratio:* 1:3 ya 1:4 (Perfume : DEP).

📦 *3. PACKAGING & RETAIL MARGIN ANALYSIS*
• *Zipper Pouches (150g - 250g):* Maximum volume retail driver.
• *Box Packaging (₹10 / ₹20 MRP):* High turnover in retail/kirana.
• *Estimated Manufacturing Cost:* ₹140 – ₹180 / kg.
• *Wholesale Selling Price:* ₹220 – ₹280 / kg.
• *Average Gross Margin:* 30% – 45%.

━━━━━━━━━━━━━━━━━━━━━
💡 *Daily Tip:* Check dipping absorption percentage daily to prevent scent leakage and weight variance.
"""
    return report


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    global ADMIN_CHAT_ID
    ADMIN_CHAT_ID = str(chat_id)

    welcome_text = (
        f"🙏 *Namaste! White Palace AI Assistant Active hai!*\n\n"
        f"Aapki Chat ID register ho gayi hai: `{chat_id}`\n\n"
        f"• Roz sham *9:00 PM* par auto research update yahi milega.\n"
        f"• Agarbatti report dekhne ke liye type karein: /report\n"
        f"• Aap mujhse koi bhi sawal ya baat kar sakte hain!"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")


# /report command
async def report_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report = generate_agarbatti_report()
    await update.message.reply_text(report, parse_mode="Markdown")


# Normal chat reply handler (baat karne ke liye)
async def chat_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text.lower()

    if "agarbatti" in user_msg or "rate" in user_msg or "cost" in user_msg:
        reply = (
            "Agarbatti raw material aur market report dekhne ke liye /report command dabayein, "
            "ya mujhe specific item ka naam batayein (jaise bamboo stick, DEP oil, fragrance)."
        )
    elif "kaise ho" in user_msg or "hello" in user_msg or "hi" in user_msg:
        reply = "Main bilkul badiya hun! Batao aaj business ya research me kya help chahiye?"
    else:
        reply = f"Aapka message mil gaya: '{update.message.text}'. Main aapke sawal par research update ready kar raha hun. Latest market update ke liye /report type karein."

    await update.message.reply_text(reply)


# Roz sham 9 PM auto message
async def send_daily_update(context: ContextTypes.DEFAULT_TYPE):
    if ADMIN_CHAT_ID:
        report = generate_agarbatti_report()
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID, text=report, parse_mode="Markdown"
        )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Commands & Chat Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("report", report_command))
    app.add_handler(
        MessageHandler(filters.TEXT & (~filters.COMMAND), chat_handler)
    )

    # 9:00 PM IST Timer
    tz = pytz.timezone("Asia/Kolkata")
    target_time = datetime.time(hour=21, minute=0, second=0, tzinfo=tz)

    job_queue = app.job_queue
    if job_queue:
        job_queue.run_daily(send_daily_update, time=target_time)

    app.run_polling()


if __name__ == "__main__":
    main()
 
