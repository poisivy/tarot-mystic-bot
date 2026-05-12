dict_tarot = {
  0: ("0_the fool.jpg", "Шут"),
  1: ("1_the magician.jpg", "Маг"),
  2: ("2_the high priestess.jpg", "Верховная жрица"),
  3: ("3_the empress.jpg", "Императрица"),
  4: ("4_the emperor.jpg", "Император"),
  5: ("5_the_hierophant.jpg", "Верховный жрец"),
  6: ("6_the lovers.jpg", "Влюбленные"),
  7: ("7_the chariot.jpg", "Колесница"),
  8: ("8_strength.jpg", "Сила"),
  9: ("9_the hermit.jpg", "Отшельник"),
  10: ("10_wheel of fortune.jpg", "Колесо Фортуны"),
  11: ("11_justice.jpg", "Справедливость"),
  12: ("12_the hanged man.jpg", "Повешенный"),
  13: ("13_the death.jpg", "Смерть"),
  14: ("14_temperance.jpg", "Умеренность"),
  15: ("15_the evil.jpg", "Дьявол"),
  16: ("16_the tower.jpg", "Башня"),
  17: ("17_the star.jpg", "Звезда"),
  18: ("18_the moon.jpg", "Луна"),
  19: ("19_the sun.jpg", "Солнце"),
  20: ("20_judgement.jpg", "Суд"),
  21: ("21_the world.jpg", "Мир"),
  22: ("22_wands_1.jpg", "Туз Жезлов"),
  23: ("23_wands_2.jpg", "Двойка Жезлов"),
  24: ("24_wands_3.jpg", "Тройка Жезлов"),
  25: ("25_wands_4.jpg", "Четверка Жезлов"),
  26: ("26_wands_5.jpg", "Пятерка Жезлов"),
  27: ("27_wands_6.jpg", "Шестерка Жезлов"),
  28: ("28_wands_7.jpg", "Семерка Жезлов"),
  29: ("29_wands_8.jpg", "Восьмерка Жезлов"),
  30: ("30_wands_9.jpg", "Девятка Жезлов"),
  31: ("31_wands_10.jpg", "Десятка Жезлов"),
  32: ("32_wands_page.jpg", "Паж Жезлов"),
  33: ("33_wands_knight.jpg", "Рыцарь Жезлов"),
  34: ("34_wands_queen.jpg", "Королева Жезлов"),
  35: ("35_wands_king.jpg", "Король Жезлов"),
  36: ("36_swords_1.jpg", "Туз Мечей"),
  37: ("37_swords_2.jpg", "Двойка Мечей"),
  38: ("38_swords_3.jpg", "Тройка Мечей"),
  39: ("39_swords_4.jpg", "Четверка Мечей"),
  40: ("40_swords_5.jpg", "Пятерка Мечей"),
  41: ("41_swords_6.jpg", "Шестерка Мечей"),
  42: ("42_swords_7.jpg", "Семерка Мечей"),
  43: ("43_swords_8.jpg", "Восьмерка Мечей"),
  44: ("44_swords_9.jpg", "Девятка Мечей"),
  45: ("45_swords_10.jpg", "Десятка Мечей"),
  46: ("46_swords_page.jpg", "Паж Мечей"),
  47: ("47_swords_knight.jpg", "Рыцарь Мечей"),
  48: ("48_swords_queen.jpg", "Королева Мечей"),
  49: ("49_swords_king.jpg", "Король Мечей"),
  50: ("50_cups_1.jpg", "Туз Кубков"),
  51: ("51_cups_2.jpg", "Двойка Кубков"),
  52: ("52_cups_3.jpg", "Тройка Кубков"),
  53: ("53_cups_4.jpg", "Четверка Кубков"),
  54: ("54_cups_5.jpg", "Пятерка Кубков"),
  55: ("55_cups_6.jpg", "Шестерка Кубков"),
  56: ("56_cups_7.jpg", "Семерка Кубков"),
  57: ("57_cups_8.jpg", "Восьмерка Кубков"),
  58: ("58_cups_9.jpg", "Девятка Кубков"),
  59: ("59_cups_10.jpg", "Десятка Кубков"),
  60: ("60_cups_page.jpg", "Паж Кубков"),
  61: ("61_cups_knight.jpg", "Рыцарь Кубков"),
  62: ("62_cups_queen.jpg", "Королева Кубков"),
  63: ("63_cups_king.jpg", "Король Кубков"),
  64: ("64_pentacles_1.jpg", "Туз Пентаклей"),
  65: ("65_pentacles_2.jpg", "Двойка Пентаклей"),
  66: ("66_pentacles_3.jpg", "Тройка Пентаклей"),
  67: ("67_pentacles_4.jpg", "Четверка Пентаклей"),
  68: ("68_pentacles_5.jpg", "Пятерка Пентаклей"),
  69: ("69_pentacles_6.jpg", "Шестерка Пентаклей"),
  70: ("70_pentacles_7.jpg", "Семерка Пентаклей"),
  71: ("71_pentacles_8.jpg", "Восьмерка Пентаклей"),
  72: ("72_pentacles_9.jpg", "Девятка Пентаклей"),
  73: ("73_pentacles_10.jpg", "Десятка Пентаклей"),
  74: ("74_pentacles_page.jpg", "Паж Пентаклей"),
  75: ("75_pentacles_knight.jpg", "Рыцарь Пентаклей"),
  76: ("76_pentacles_queen.jpg", "Королева Пентаклей"),
  77: ("77_pentacles_king.jpg", "Король Пентаклей"),
}

import telebot
import random
import openai
import time
import webbrowser
from telebot import types
import requests
from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO
import datetime
import json
import time

def date_checker(message):
    try:
        datetime.datetime.strptime(message, '%d.%m.%Y')
        return True
    except ValueError:
        # Строка не является корректной датой в формате дд.мм.ГГГГ
        return False


def time_checker(message):
    try:
        datetime.datetime.strptime(message, '%H:%M')
        return True
    except ValueError:
        # Строка не является корректным временем в формате ЧЧ:ММ
        return False


def pars_natal_chart(user_name, day, month, year, hour=12, minute=0):
  query = {'fn': user_name,
         'fd': day,
         'fm': month,
         'fy': year,
         'fh': hour,
         'fmn': minute,
         'c1': "Москва, Россия",
         'ttz': 20,
         'tz': "Europe/Moscow",
         'tm': 3,
         'lt': 55.7522,
         'ln': 37.6155,
         'hs': 'P',
         'sb': 1}
  url = requests.get('https://geocult.ru/natalnaya-karta-onlayn-raschet', params=query).url
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, "html.parser")
  # Картинка натальной карты
  image_link_tag = soup.find("a", id="r660")
  image_link = image_link_tag.get("href").replace(' ','%20')
  response = requests.get(image_link)
  image = Image.open(BytesIO(response.content))
  # Картинка аспектов
  image_link_tag_2 = soup.find("a", id="r705")
  image_link_2 = image_link_tag_2.get("href").replace(' ','%20')
  response_2 = requests.get(image_link_2)
  image_2 = Image.open(BytesIO(response_2.content))
  # Объединяем картинки
  new_width = image_2.width  # ширина нижней картинки
  image = image.resize((new_width, int(image.height*(image_2.width/image.width))))
  res_img = Image.new('RGB', (max(image_2.width, image.width), image_2.height + image.height))
  res_img.paste(image, (0, 0))
  res_img.paste(image_2, (0, image.height))
  return res_img, url


def get_compatibility_message(compatibility_score):
  prompt = {
      "modelUri": "gpt://b1ghb2n1j9jhjg62oqmv/yandexgpt/rc",
      "completionOptions": {
          "stream": False,
          "temperature": 0.6,
          "maxTokens": "200"
      },
      "messages": [
          {
              "role": "system",
              "text": "Ты мудрая гадалка, помогающая узнать судьбу. Ты отвечаешь человеку обезличено, без указания пола"
          },
          {
              "role": "user",
              "text": f"Магический шар показал, что совместимость с моим избранником равна {compatibility_score}%. Что это значит? Есть ли у нас шансы на любовь?"
          }
      ]
  }

  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Api-Key YOUR_YANDEX_API_KEY"
  }

  response = requests.post(url, headers=headers, json=prompt)
  result = json.loads(response.text)
  message = result["result"]["alternatives"][0]["message"]["text"]
  message = message.replace('.','\.').replace('-','\-')
  return message


def get_magic_answer(question):
  prompt = {
      "modelUri": "gpt://b1ghb2n1j9jhjg62oqmv/yandexgpt/rc",
      "completionOptions": {
          "stream": False,
          "temperature": 0.6,
          "maxTokens": "200"
      },
      "messages": [
          {
              "role": "system",
              "text": "Ты мудрая гадалка, помогающая узнать свое будущее и судьбу. Ты отвечаешь на вопросы о будущем без указания пола. Давай ответы в пределах 6 предложений"
          },
          {
              "role": "user",
              "text": "Привет! Мне нужна твоя помощь! Я хочу узнать немного о своем будущем."
          },
        {
            "role": "assistant",
            "text": "Будущее скрыто завесой тайны, но я обладаю даром приоткрывать ее. Задай мне любой вопрос о твоей судьбе, и я воспользуюсь своими древними знаниями и интуицией, чтобы пролить свет на твой путь."
        },
        {
            "role": "user",
            "text": f"{question}"
        }
      ]
  }

  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Api-Key YOUR_YANDEX_API_KEY"
  }

  response = requests.post(url, headers=headers, json=prompt)
  result = json.loads(response.text)
  message = result["result"]["alternatives"][0]["message"]["text"]
  message = message.replace('.','\.').replace('-','\-')
  return message

def get_taro_answer(card, method):
  prompt = {
      "modelUri": "gpt://b1ghb2n1j9jhjg62oqmv/yandexgpt/rc",
      "completionOptions": {
          "stream": False,
          "temperature": 0.6,
          "maxTokens": "200"
      },
      "messages": [
          {
              "role": "system",
              "text": "Ты гадалка, интерпретирующая результаты раскладов таро. Ты интерпретируешь без указания пола. Давай ответы в пределах 8 предложений. Начинай повествование с непосредственной интерпретации карты"
          },
          {
              "role": "user",
              "text": f"Привет! В раскладе таро '{method}'. Выпало следующее: {card}. Расскажи что это значит?"
          }
      ]
  }

  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Api-Key YOUR_YANDEX_API_KEY"
  }

  response = requests.post(url, headers=headers, json=prompt)
  result = json.loads(response.text)
  message = result["result"]["alternatives"][0]["message"]["text"]
  message = message.replace('.','\.').replace('-','\-')
  return message


def get_taro_situation_answer(card):
  prompt = {
      "modelUri": "gpt://b1ghb2n1j9jhjg62oqmv/yandexgpt/rc",
      "completionOptions": {
          "stream": False,
          "temperature": 0.6,
          "maxTokens": "300"
      },
      "messages": [
          {
              "role": "system",
              "text": "Ты интерпретируешь результаты раскладов таро на ситуацию. Расклад на ситуацию имеет следующую логику: Из колоды вытягиваются семь карт. Первые три символизируют события прошлого, настоящего и будущего. Четвертая означает страхи и надежды, пятая — то, что может изменить ситуацию, которая привела человека к тарологу, шестая — конкретный совет, а седьмая — возможный исход ситуации. Ты интерпретируешь карты  без указания пола. Ты описываешь каждую карту по одному предложению. Начинай повествование с непосредственной интерпретации карты"
          },
          {
              "role": "user",
              "text": f"Привет! В раскладе таро на ситуацию. Выпали следующие карты: {card}. Расскажи что это значит?"
          }
      ]
  }

  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Api-Key YOUR_YANDEX_API_KEY"
  }

  response = requests.post(url, headers=headers, json=prompt)
  result = json.loads(response.text)
  message = result["result"]["alternatives"][0]["message"]["text"]
  message = message.replace('.','\.').replace('-','\-').replace('(','\(').replace(')','\)')
  return message


def get_taro_love_answer(card):
  prompt = {
      "modelUri": "gpt://b1ghb2n1j9jhjg62oqmv/yandexgpt/rc",
      "completionOptions": {
          "stream": False,
          "temperature": 0.6,
          "maxTokens": "300"
      },
      "messages": [
          {
              "role": "system",
              "text": "Ты интерпретируешь результаты раскладов таро на любовь. Расклад на любовь имеет следующую логику: Из колоды вытягиваются восемь карт. Первая и пятая позиции — что разделяет партнеров. Вторая и шестая — намерения и желания.Третья и седьмая позиция — точка соприкосновения, общее у партнеров. Четвертая и восьмая — движущая сила отношений. Ты интерпретируешь карты без указания пола. Ты описываешь каждую карту по одному предложению. Начинай повествование с непосредственной интерпретации карты"
          },
          {
              "role": "user",
              "text": f"Привет! В раскладе на любовь Леминската. Выпали следующие карты: {card}. Расскажи что это значит? Опиши кратко"
          }
      ]
  }

  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Api-Key YOUR_YANDEX_API_KEY"
  }

  response = requests.post(url, headers=headers, json=prompt)
  result = json.loads(response.text)
  message = result["result"]["alternatives"][0]["message"]["text"]
  message = message.replace('.','\.').replace('-','\-').replace('(','\(').replace(')','\)')
  return message






bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# Приветственная функция
@bot.message_handler(commands=['start'])
def main_start(message):
  global user_name
  user_name=message.from_user.first_name
  bot.send_message(message.chat.id, f'Доброго времени суток, {user_name}!')

# Команда ask - ответ на любой вопрос
@bot.message_handler(commands=['ask'])
def main_ask(message):
  global user_name
  user_name=message.from_user.first_name
  bot.send_message(message.chat.id, f'''Будущее скрыто завесой тайны, но я обладаю даром приоткрывать ее.
Задай мне любой вопрос о своей судьбе, и я воспользуюсь своими древними знаниями и интуицией, чтобы пролить свет на твой путь''', parse_mode = 'html')
  @bot.message_handler(content_types=["text"])
  def main_answer(message):
    bot.send_message(message.chat.id, 'Хм.. это любопытный вопрос. Дай мне немного времени, и я вернусь к тебе с откровениями')
    bot.send_chat_action(message.chat.id, 'typing')
    answer = get_magic_answer(message.text)
    if "Посмотрите, что нашлось в поиске" in answer:
      answer = "Власть Судьбы сегодня окутана туманом\. Я не могу пробиться сквозь завесу тайны, чтобы дать вам четкий ответ\. Возможно получиться узнать ответ на другой вопрос\."
    bot.send_message(message.chat.id, f'''||{answer}||''', parse_mode = 'MarkdownV2')
    markup_ask = types.InlineKeyboardMarkup()
    markup_ask.row(types.InlineKeyboardButton('Да', callback_data='yes_ask'), types.InlineKeyboardButton('Нет', callback_data='no_ask'))
    bot.send_message(message.chat.id, 'Хочешь спросить меня о чём-то ещё?', reply_markup=markup_ask)


# Команда compatibility - расчет совместимости с пользователем
@bot.message_handler(commands=['compatibility'])
def main_compatibility(message):
  global user_name
  user_name=message.from_user.first_name
  bot.send_message(message.chat.id, f'''Хочешь узнать совместимость?
Пришли фото избранника и я открою тебе тайну''', parse_mode = 'html')
  @bot.message_handler(content_types=['photo'])
  def main_photo(message):
    bot.send_message(message.chat.id, 'Хмм.. посмотрим, что покажет магический шар!')
    video = open('/content/Магический шар.gif', 'rb')
    bot.send_document(message.chat.id, video)
    bot.send_chat_action(message.chat.id, 'typing')
    compatibility_qty = random.randint(0,100)
    compatibility_answer = get_compatibility_message(compatibility_qty)
    bot.send_message(message.chat.id, f'''Ваша совместимость \- ||*{compatibility_qty}%*||

||{compatibility_answer}||''', parse_mode = 'MarkdownV2')


# Команда natal_chart - расчет и отправка пользователю натальной карты
@bot.message_handler(commands=['natal_chart'])
def main_chart(message):
    global user_name
    user_name=message.from_user.first_name
    bot.send_message(message.chat.id, 'Чтобы расчитать натальную карту мне потребуется чуть больше информации о тебе.')
    bot.send_message(message.chat.id, 'Пожалуйста, укажи свою дату рождения в формате дд.мм.гггг. Например, 19.09.1999.')
    bot.register_next_step_handler(message, date_func)

def date_func(message):
    date = message.text
    if date_checker(date):
        global day, month, year
        day, month, year = date.split('.')
        year = int(year)  # Преобразуем год в целое число
        if year < 1801 or year > 2099:
            bot.send_message(message.chat.id, 'Год должен быть между 1801 и 2099. Пожалуйста, укажи корректную дату.')
            bot.register_next_step_handler(message, date_func)
            return

        # Вывод вопроса про точное время рождения
        markup_time = types.InlineKeyboardMarkup()
        markup_time.row(types.InlineKeyboardButton('Да', callback_data='yes'), types.InlineKeyboardButton('Нет', callback_data='no'))
        bot.send_message(message.chat.id, 'Подскажи, знаешь ли ты точное время своего рождения?', reply_markup=markup_time)

    else:
        bot.send_message(message.chat.id, 'Пожалуйста, укажи *корректную дату* рождения в формате дд\.мм\.гггг\. Например, 19\.09\.1999\.', parse_mode='MarkdownV2')
        bot.register_next_step_handler(message, date_func)

def send_natal_card(chat_id, result_image, url):
    markup_natal_card = types.InlineKeyboardMarkup()
    markup_natal_card.add(types.InlineKeyboardButton('Изучить подробнее', url=url))
    bot.send_photo(chat_id, result_image)
    bot.send_message(chat_id, 'Космограмма твоей натальной карты готова! Дополнительно ты можешь ознакомиться с таблицей сформировавшихся аспектов. По ссылке ниже ты можешь ознакомиться с результатами более детально', reply_markup=markup_natal_card)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    chat_id = callback.message.chat.id
    if callback.data == 'yes':
        bot.send_message(chat_id, 'Пожалуйста, укажи точное время рождения в формате чч:мм. Например, 13:45')
        bot.register_next_step_handler(callback.message, time_func, True)  # True означает, что время нужно
    elif callback.data == 'no':
        bot.send_message(chat_id, 'Дай мне немного времени на расчеты...')
        bot.send_chat_action(chat_id, 'upload_photo')
        result_image, url = pars_natal_chart(user_name, day, month, year)
        send_natal_card(chat_id, result_image, url)
    elif callback.data == 'yes_ask':
        bot.send_message(chat_id, 'Напиши свой вопрос')
        bot.register_next_step_handler(callback.message, main_answer, True)
    elif callback.data == 'no_ask':
        bot.send_message(chat_id, 'Хорошо, если вдруг у тебя появятся вопросы, просто используй команду /ask')
    elif callback.data == 'day_card':
      markup_day_card = types.InlineKeyboardMarkup()
      markup_day_card.row(types.InlineKeyboardButton('Да', callback_data='yes_day_card'),types.InlineKeyboardButton('Нет', callback_data='no_day_card'))
      bot.send_message(chat_id, f'''Отличный выбор! Давай посмотрим, что грядет тебе наступающий день.
Будем использовать младшие арканы в гадании?''', reply_markup=markup_day_card)
    elif callback.data in ['yes_day_card', 'no_day_card']:
        is_full_arcana = callback.data == 'yes_day_card'
        day_card(chat_id, is_full_arcana)
    elif callback.data == 'past_present_future':
      markup_past_present_future = types.InlineKeyboardMarkup()
      markup_past_present_future.row(types.InlineKeyboardButton('Да', callback_data='yes_past_present_future'),types.InlineKeyboardButton('Нет', callback_data='no_past_present_future'))
      bot.send_message(chat_id, f'''Отличный выбор! Давай посмотрим, что покажут карты.
Будем использовать младшие арканы в гадании?''', reply_markup=markup_past_present_future)
    elif callback.data in ['yes_past_present_future', 'no_past_present_future']:
        is_full_arcana = callback.data == 'yes_past_present_future'
        past_present_future(chat_id, is_full_arcana)
    elif callback.data == 'situation':
        bot.send_message(chat_id, f'''Отличный выбор! Давай посмотрим, что скажут карты о твоей ситуации.''')
        situation(chat_id)
    elif callback.data == 'love':
        bot.send_message(chat_id, f'''Отличный выбор! Давай посмотрим, как сложатся твои отношения.''')
        love(chat_id)


def day_card(chat_id, is_full_arcana):
    bot.send_message(chat_id, '''Давай начнем, сосредоточься и почувствуй энергию карт 🃏''')
    method = 'Карта дня'
    video_message = bot.send_animation(chat_id, open('/content/tarot card.gif', 'rb'))
    video_message_id = video_message.message_id
    bot.send_chat_action(chat_id, 'typing')
    num = random.randint(0, 77 if is_full_arcana else 21)
    card_path, card_name = dict_tarot[num][0], dict_tarot[num][1]
    card = open(f'/content/{card_path}', 'rb')
    time.sleep(5)  # Задержка перед отправкой карты
    bot.send_photo(chat_id, card)
    bot.delete_message(chat_id, video_message_id)
    bot.send_message(chat_id, f'''Твоя карта дня \- *{card_name}*

*Интерпретация:*
{get_taro_answer(card_name, method)}''', parse_mode='MarkdownV2')

def past_present_future(chat_id, is_full_arcana):
    bot.send_message(chat_id, '''Давай начнем, мысленно или вслух попроси карты показать три важные периода в твоей жизни''')
    method = 'Прошлое, настоящее и будущее'
    video_message = bot.send_animation(chat_id, open('/content/tarot card.gif', 'rb'))
    video_message_id = video_message.message_id
    bot.send_chat_action(chat_id, 'typing')
    num1, num2, num3 = random.sample(range(0, 78 if True else 22), 3)
    card_info = [dict_tarot[num][0] for num in [num1, num2, num3]]
    card_names = [dict_tarot[num][1] for num in [num1, num2, num3]]
    cards = [Image.open(f'/content/{card_path}') for card_path in card_info]
    combined_image = Image.new('RGB', (sum(card.width for card in cards), max(card.height for card in cards)))
    x_offset = 0
    for card in cards:
        combined_image.paste(card, (x_offset, 0))
        x_offset += card.width
    bytes_io = BytesIO()
    combined_image.save(bytes_io, format='jpeg')
    bytes_io.seek(0)
    time.sleep(5)
    bot.send_photo(chat_id, bytes_io)
    bot.delete_message(chat_id, video_message_id)
    bot.send_message(chat_id, f'''Прошлое \- *{card_names[0]}*\. Настоящее \- *{card_names[1]}*\. Будущее \- *{card_names[2]}*\.

*Интерпретация:*
{get_taro_answer(', '.join(card_names), method)}''', parse_mode='MarkdownV2')


def situation(chat_id):
    bot.send_message(chat_id, '''Постарайся сконцентрироваться на интересущей тебя ситуации.''')
    video_message = bot.send_animation(chat_id, open('/content/tarot card.gif', 'rb'))
    video_message_id = video_message.message_id
    bot.send_chat_action(chat_id, 'typing')
    num1, num2, num3, num4, num5, num6, num7 = random.sample(range(0, 78), 7)
    card_info = [dict_tarot[num][0] for num in [num1, num2, num3, num4, num5, num6, num7]]
    card_names = [dict_tarot[num][1] for num in [num1, num2, num3, num4, num5, num6, num7]]
    cards = [Image.open(f'/content/{card_path}') for card_path in card_info]
    combined_image = Image.new('RGB', (sum(card.width for card in cards[:3]), max(card.height for card in cards)))
    x_offset = 0
    for card in cards[:3]:
        combined_image.paste(card, (x_offset, 0))
        x_offset += card.width
    combined_image2 = Image.new('RGB', (sum(card.width for card in cards[3:]), max(card.height for card in cards)))
    x_offset = 0
    for card in cards[3:]:
        combined_image2.paste(card, (x_offset, 0))
        x_offset += card.width
    new_width = combined_image2.width
    combined_image = combined_image.resize((new_width, int(combined_image.height*(combined_image2.width/combined_image.width))))
    res_img = Image.new('RGB', (max(combined_image2.width, combined_image.width), combined_image2.height + combined_image.height))
    res_img.paste(combined_image, (0, 0))
    res_img.paste(combined_image2, (0, combined_image.height))
    bytes_io = BytesIO()
    res_img.save(bytes_io, format='jpeg')
    bytes_io.seek(0)
    time.sleep(5)
    bot.send_photo(chat_id, bytes_io)
    bot.delete_message(chat_id, video_message_id)
    bot.send_message(chat_id, f'''Твои карты: *{', '.join(card_names)}*

{get_taro_situation_answer(', '.join(card_names))}''', parse_mode='MarkdownV2')

def love(chat_id):
    bot.send_message(chat_id, '''Постарайся сконцентрироваться на интересующем тебя человеке.''')
    video_message = bot.send_animation(chat_id, open('/content/tarot card.gif', 'rb'))
    video_message_id = video_message.message_id
    bot.send_chat_action(chat_id, 'typing')
    num1, num2, num3, num4, num5, num6, num7, num8 = random.sample(range(0, 78), 8)
    card_info = [dict_tarot[num][0] for num in [num1, num2, num3, num4, num5, num6, num7, num8]]
    card_names = [dict_tarot[num][1] for num in [num1, num2, num3, num4, num5, num6, num7, num8]]
    cards = [Image.open(f'/content/{card_path}') for card_path in card_info]
    combined_image = Image.new('RGB', (6*max(card.width for card in cards), 3*max(card.height for card in cards)), '#FFEBCD')
    combined_image.paste(cards[0], (0, cards[0].height))
    combined_image.paste(cards[1], (cards[0].width, 0))
    combined_image.paste(cards[2], (2*cards[0].width, cards[0].height))
    combined_image.paste(cards[3], (4*cards[0].width, 2*cards[0].height))
    combined_image.paste(cards[4], (5*cards[0].width, cards[0].height))
    combined_image.paste(cards[5], (4*cards[0].width, 0))
    combined_image.paste(cards[6], (3*cards[0].width, cards[0].height))
    combined_image.paste(cards[7], (cards[0].width, 2*cards[0].height))
    bytes_io = BytesIO()
    combined_image.save(bytes_io, format='jpeg')
    bytes_io.seek(0)
    time.sleep(5)
    bot.send_photo(chat_id, bytes_io)
    bot.delete_message(chat_id, video_message_id)
    bot.send_message(chat_id, f'''Твои карты: *{', '.join(card_names)}*

{get_taro_love_answer(', '.join(card_names))}''', parse_mode='MarkdownV2')

def time_func(message, needs_time):
    time = message.text
    if needs_time and time_checker(time):
        hour, minute = time.split(':')
        bot.send_message(message.chat.id, 'Дай мне немного времени на расчеты...')
        bot.send_chat_action(message.chat.id, 'upload_photo')
        result_image, url = pars_natal_chart(user_name, day, month, year, hour, minute)
        send_natal_card(message.chat.id, result_image, url)
    elif needs_time:
        bot.send_message(message.chat.id, 'Пожалуйста, укажи *корректное* время рождения в формате чч:мм\. Например, 13:45\.', parse_mode='MarkdownV2')
        bot.register_next_step_handler(message, time_func, needs_time)


# Команда tarot - расклад карт таро
@bot.message_handler(commands=['tarot'])
def main_tarot(message):
  global user_name
  user_name=message.from_user.first_name
  markup_tarot = types.InlineKeyboardMarkup()
  markup_tarot.row(types.InlineKeyboardButton('Карта дня', callback_data='day_card'))
  markup_tarot.row(types.InlineKeyboardButton('Прошлое, настоящее и будущее', callback_data='past_present_future'))
  markup_tarot.row(types.InlineKeyboardButton('Расклад на ситуацию', callback_data='situation'))
  markup_tarot.row(types.InlineKeyboardButton('Лемниската (расклад на любовь)', callback_data='love'))
  bot.send_message(message.chat.id, f'''О, ты хочешь обратиться к картам? Я помогу тебе!
Выбери вариант расклада карт Таро:''', parse_mode = 'html', reply_markup=markup_tarot)


bot.infinity_polling()
