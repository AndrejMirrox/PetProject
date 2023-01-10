import telebot
import requests


bot = telebot.TeleBot('5782002043:AAFQYfChULCUge8ihmhfWT4B9jVCNlLORtk')



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может показать информацию о видео с YouTube.")

def get_video_info(video_id):
    api_key = "AIzaSyBPKydE-ydIVuD0gZ8O1ooTWWMAvXkTqhw"
    api_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
    r = requests.get(api_url)
    data = r.json()
    return data["items"][0]["snippet"]

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text
    if "youtube.com" in text:
        # извлекаем идентификатор видео из ссылки
        video_id = text.split("v=")[-1]
        # получаем информацию о видео
        video_info = get_video_info(video_id)
        # формируем текст сообщения
        response = f"Название: {video_info['title']}\n"
        response += f"Описание: {video_info['description']}\n"
        bot.send_message(message.chat.id, response)
        print(message.text)
    else:
        bot.send_message(message.chat.id, "Это не ссылка на YouTube")
        print(message.text)

bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    print("Бот завершил работу")
