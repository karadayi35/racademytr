import telegram
import schedule
import asyncio
import time
from telegram import Bot

# Telegram bot token ve kanal ID'si
TOKEN = "8173433982:AAGacqHiXWLYxAcYL8eiGsiiEx-QGvLwpJ4"  # BotFather'dan aldığınız API token
CHAT_ID = "-1002214510803"  # Kanal ID'niz

# Botu başlatın
bot = Bot(token=TOKEN)


# Asenkron mesaj gönderme fonksiyonu
async def send_message_with_image():
    try:
        # Resim dosyasının yolunu belirtin (daha önce yüklediğiniz resimler)
        image_path = "turke.png"  # Resim dosyasının yolu
        with open(image_path, 'rb') as image:
            # Mesaj metni
            crown_emoji = "👑"
            message_text = f"{crown_emoji} EN İYİ CASİNO SİTELERİ - TÜRKİYE\n\n" \


            # Butonlar
            buttons = [
                [telegram.InlineKeyboardButton(text="👑Stake 10 USDT Bonus Al", url="https://stake.com/?c=9dd9dbc553")],
                [telegram.InlineKeyboardButton(text="👑Slottica %200 Yatırım Bonusu",
                                               url="https://gopartner.link/?a=205678&c=184089&s1=6028")],
                [telegram.InlineKeyboardButton(text="👑Mostbet Toplam 150,000 TL Bonus", url="https://t.ly/eAL_1")],
                [telegram.InlineKeyboardButton(text="👑Marbahis %30 Kripto Yatırım Bonusu",
                                               url="https://bit.ly/3RF81eI")],
            ]

            # Inline keyboard ile butonlar

            reply_markup = telegram.InlineKeyboardMarkup(buttons)

            # Asenkron olarak mesaj gönder
            await bot.send_photo(chat_id=CHAT_ID, photo=image, caption=message_text, reply_markup=reply_markup)
            print("Mesaj gönderildi!")
    except Exception as e:
        print(f"Hata oluştu: {e}")


# Schedule kullanımı için asenkron işlevi sarmalayan bir fonksiyon
def job_wrapper():
    asyncio.ensure_future(send_message_with_image())


# Her 5 saniyede bir mesaj paylaşımı için:
schedule.every(3).hours.do(job_wrapper)


# Asenkron döngüyü sürekli çalıştır
async def run_schedule():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)


# Ana asenkron döngü
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run_schedule())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
