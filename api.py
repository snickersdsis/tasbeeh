from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# توكن البوت
TOKEN = "7813031936:AAFub_5iuyu-VZEsXY8ATc61g56jF_uNqVU"

# رابط المسبحة المصغر
webapp_url = "https://snickersdsis.github.io/tasbeeh/"  # استبدل هذا بالرابط الفعلي لتطبيق المسبحة الخاص بك

# دالة start التي سترد على الرسائل
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # زر لتحويل المستخدم إلى التطبيق المصغر
    keyboard = [
        [InlineKeyboardButton("افتح المسبحة", web_app=WebAppInfo(url=webapp_url))]  # استخدام WebAppInfo هنا
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "أهلاً وسهلاً! مرحباً بك في بوت المسَبِّحة. اضغط على الزر لفتح المسبحة.",
        reply_markup=reply_markup
    )

# إعداد البوت
def main():
    application = Application.builder().token(TOKEN).build()

    # إضافة الـ handler الخاص بأمر start
    application.add_handler(CommandHandler("start", start))

    # تشغيل البوت
    application.run_polling()

if __name__ == "__main__":
    main()
