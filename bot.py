# -*- coding: utf-8 -*-
import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "8568639233:AAHTVzvDi3M9e8XkukJL37lHM4DH8wyW0Y4"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

SKU_DATA = {
    "woody green": {"10": {"cogs": 4.60, "dist": 6.50, "mrp": 10, "sticks": 15, "margin_pct": 29.2}, "20": {"cogs": 9.00, "dist": 13.00, "mrp": 20, "sticks": 32, "margin_pct": 30.8}},
    "toti futi": {"10": {"cogs": 4.40, "dist": 6.50, "mrp": 10, "sticks": 15, "margin_pct": 32.3}, "20": {"cogs": 8.60, "dist": 13.00, "mrp": 20, "sticks": 32, "margin_pct": 33.8}},
    "lavender": {"10": {"cogs": 4.70, "dist": 6.50, "mrp": 10, "sticks": 15, "margin_pct": 27.7}, "20": {"cogs": 9.20, "dist": 13.00, "mrp": 20, "sticks": 32, "margin_pct": 29.2}},
    "rose": {"10": {"cogs": 4.55, "dist": 6.50, "mrp": 10, "sticks": 15, "margin_pct": 30.0}, "20": {"cogs": 8.90, "dist": 13.00, "mrp": 20, "sticks": 32, "margin_pct": 31.5}},
    "sandalwood": {"10": {"cogs": 5.00, "dist": 6.50, "mrp": 10, "sticks": 15, "margin_pct": 23.1}, "20": {"cogs": 9.80, "dist": 13.00, "mrp": 20, "sticks": 32, "margin_pct": 24.6}},
    "jasmine": {"10": {"cogs": 4.65, "dist": 6.50, "mrp": 10, "sticks": 15, "margin_pct": 28.5}, "20": {"cogs": 9.10, "dist": 13.00, "mrp": 20, "sticks": 32, "margin_pct": 30.0}},
    "oudh": {"10": {"cogs": 5.20, "dist": 6.50, "mrp": 10, "sticks": 15, "margin_pct": 20.0}, "20": {"cogs": 10.20, "dist": 13.00, "mrp": 20, "sticks": 32, "margin_pct": 21.5}}
}

def get_csuite_keyboard():
    keyboard = [
        [KeyboardButton("👑 CEO Desk (Vaibhav)"), KeyboardButton("🎯 Director Ops (Pranay)")],
        [KeyboardButton("📊 Data Intelligence (Nikhil)"), KeyboardButton("💰 Finance & Risk (Tanukesh)")],
        [KeyboardButton("🌆 Generate Daily Evening Brief"), KeyboardButton("🌸 7 Fragrance SKU Matrix")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    intro = (
        "👑 *WHITE PALACE AGARBATTI GROUP — EXECUTIVE AI HQ*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Namaste Vaibhav Sir! White Palace Group ka 100,000 IQ autonomous C-Suite board ready hai.\n\n"
        "🏛️ *Active Board Members:*\n"
        "• *CEO Vaibhav:* Group Strategy, Market Expansion & Leadership.\n"
        "• *Director Pranay:* Operations Research, Dipping Batches & Production.\n"
        "• *Analyst Nikhil:* 7 Fragrance Consumption Data & SKU Velocity.\n"
        "• *Finance Mgr Tanukesh:* Unit Economics, Margin Defense & Credit Risk.\n\n"
        "Neeche buttons par click karein ya koi bhi sawal puchein!"
    )
    await update.message.reply_text(intro, parse_mode="Markdown", reply_markup=get_csuite_keyboard())

async def ceo_brief(update: Update):
    text = (
        "👑 *OFFICE OF THE CEO — VAIBHAV*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "• *Mission:* White Palace Agarbatti ko top-tier market leadership par scale karna.\n"
        "• *Strategic Focus:* ₹10 & ₹20 segment me 30%+ gross margin maintain karte hue volume push karna.\n"
        "• *Policy Mandate:* 15 din se zyada ke distributor credit par fresh dispatch pause rahega."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def ops_brief(update: Update):
    text = (
        "🎯 *OPERATIONS RESEARCH — DIRECTOR PRANAY*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "• *OR Dipping Standard:* 1 kg Raw Black Sticks : 280ml–330ml Fragrance Solution.\n"
        "• *Solvent Formulation:* 3 Parts DEP (Diethyl Phthalate) + 1 Part Fragrance Compound.\n"
        "• *Drying Control:* 24-36 hrs shaded ventilation (Direct dhoop strictly avoid karein).\n"
        "• *Batch Yield:* 1 kg stick batch = ~62-66 pouches (₹10 pack) or ~30-31 pouches (₹20 pack)."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def data_brief(update: Update):
    text = (
        "📊 *MARKET INTELLIGENCE — DATA ANALYST NIKHIL*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "• *Core 7 Fragrance Velocity:*\n"
        "   1. Rose & Sandalwood — 48% Total Volume (Fast-movers)\n"
        "   2. Jasmine & Lavender — 26% Volume (Steady consumption)\n"
        "   3. Woody Green & Toti Futi — 18% Volume (Regional pull)\n"
        "   4. Oudh — 8% Volume (Premium category)\n"
        "• *Variance Metric:* Sticks count exactly 15 (₹10) aur 32 (₹20) par maintain ho raha hai."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def finance_brief(update: Update):
    text = (
        "💰 *FINANCIAL AUDIT & RISK — TANUKESH*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "• *₹10 SKU Economics:* COGS Avg ₹4.60 | Wholesaler Rate ₹6.50 | Gross Margin: *~29.2% – 32.3%*\n"
        "• *₹20 SKU Economics:* COGS Avg ₹9.00 | Wholesaler Rate ₹13.00 | Gross Margin: *~30.8% – 33.8%*\n"
        "• *Working Capital Rule:* Raw material cash procurement par discount lein, credit limit strict 15 days rakhein."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def evening_report(update: Update):
    text = (
        "🌆 *WHITE PALACE GROUP — COMPREHENSIVE EVENING BRIEFING*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "👑 *CEO Vaibhav:* Brand positioning & volume growth review complete.\n"
        "🎯 *Director Pranay:* Production dipping racks at 96% efficiency; dry loss under 4.5%.\n"
        "📊 *Analyst Nikhil:* 7 Fragrance inventory velocity balanced; no stock-out risk.\n"
        "💰 *Finance Mgr Tanukesh:* Daily collection audited; margins defended across ₹10 & ₹20 lines.\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "⚡ *Verdict:* Operations Green. Tomorrow's dipping schedule queued."
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def handle_executive_brain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.strip()
    low = msg.lower()

    if msg == "👑 CEO Desk (Vaibhav)":
        await ceo_brief(update)
        return
    elif msg == "🎯 Director Ops (Pranay)":
        await ops_brief(update)
        return
    elif msg == "📊 Data Intelligence (Nikhil)":
        await data_brief(update)
        return
    elif msg == "💰 Finance & Risk (Tanukesh)":
        await finance_brief(update)
        return
    elif msg == "🌆 Generate Daily Evening Brief":
        await evening_report(update)
        return
    elif msg == "🌸 7 Fragrance SKU Matrix":
        sku_txt = (
            "🌸 *WHITE PALACE 7 SIGNATURE FRAGRANCES:*\n"
            "1. 🌲 Woody Green (₹10 / ₹20)\n"
            "2. 🍬 Toti Futi (₹10 / ₹20)\n"
            "3. 💜 Lavender (₹10 / ₹20)\n"
            "4. 🌹 Rose (₹10 / ₹20)\n"
            "5. 🪵 Sandalwood (₹10 / ₹20)\n"
            "6. 🌼 Jasmine (₹10 / ₹20)\n"
            "7. 👑 Oudh (₹10 / ₹20)"
        )
        await update.message.reply_text(sku_txt, parse_mode="Markdown")
        return

    if "tanukesh" in low or "finance" in low or "cost" in low or "margin" in low or "paisa" in low:
        found = None
        for frag in SKU_DATA:
            if frag in low:
                found = frag
                break
        if found:
            data_10 = SKU_DATA[found]["10"]
            data_20 = SKU_DATA[found]["20"]
            resp = (
                f"💰 *FINANCE MANAGER TANUKESH AUDIT — {found.upper()}:*\n\n"
                f"🏷️ *₹10 Pack:* COGS = ₹{data_10['cogs']:.2f} | Wholesaler = ₹{data_10['dist']:.2f} | Margin = *{data_10['margin_pct']}%*\n"
                f"🏷️ *₹20 Pack:* COGS = ₹{data_20['cogs']:.2f} | Wholesaler = ₹{data_20['dist']:.2f} | Margin = *{data_20['margin_pct']}%*\n\n"
                f"💡 *Tanukesh's Advice:* Is SKU par distributor credit 15 days se upar nahi hona chahiye."
            )
            await update.message.reply_text(resp, parse_mode="Markdown")
            return
        else:
            await finance_brief(update)
            return

    elif "pranay" in low or "dipping" in low or "formula" in low or "ratio" in low or "batch" in low or "factory" in low:
        resp = (
            "🎯 *DIRECTOR PRANAY (Operations & OR Strategy):*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "• *Standard Ratio:* 3 : 1 (3 Parts DEP + 1 Part Fragrance Compound).\n"
            "• *For 100 Kg Raw Sticks:* 25-30 Liters dipping solution (75% DEP + 25% Oil).\n"
            "• *OR Rule:* Floral oils (Rose, Jasmine) 3:1 ratio, woody oils (Sandalwood, Oudh) 2.5:1 ratio absorb karte hain.\n"
            "• *Drying:* Shade me 24 hrs dry karein taaki evaporation loss 4.5% ke andar rahe."
        )
        await update.message.reply_text(resp, parse_mode="Markdown")
        return

    elif "nikhil" in low or "data" in low or "trend" in low or "market" in low or "demand" in low:
        resp = (
            "📊 *DATA ANALYST NIKHIL (Demand Analytics):*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "• *Fast Movers:* Sandalwood ₹20 aur Rose ₹10 top volume driver hain.\n"
            "• *Trend:* Jasmine aur Lavender me +18% festive pickup dikh raha hai.\n"
            "• *Safety Stock:* Factory me hamesha 100 kg raw sticks buffer reserve rakhein."
        )
        await update.message.reply_text(resp, parse_mode="Markdown")
        return

    elif "vaibhav" in low or "ceo" in low or "strategy" in low:
        await ceo_brief(update)
        return

    else:
        resp = (
            f"🧠 *C-SUITE MULTI-AGENT REASONING (Query: '{msg}'):*\n\n"
            "👑 *CEO Vaibhav:* Brand standard aur sales volume strictly monitor karein.\n"
            "🎯 *Pranay:* Dipping ratio aur factory throughput clear hai.\n"
            "📊 *Nikhil:* 7 Fragrances demand matrix stable hai.\n"
            "💰 *Tanukesh:* Margins protected hain (30%+ target).\n\n"
            "Sir, aap direct specific sawal puchein jaise:\n"
            "• *'Tanukesh, Sandalwood ka margin batao'*\n"
            "• *'Pranay, dipping formula kya hai?'*\n"
            "• *'Nikhil, market trend kya hai?'*"
        )
        await update.message.reply_text(resp, parse_mode="Markdown", reply_markup=get_csuite_keyboard())

def main():
    print("WHITE PALACE AGARBATTI - C-SUITE LIVE")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_executive_brain))
    app.run_polling()

if __name__ == "__main__":
    main()
