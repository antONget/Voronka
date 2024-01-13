# preprocessing
## подготовка списка зависимостей
```bash
pip freeze > requirements.txt
```

# Bot
## Разархивируйте проект в выбранную вами папку на сервере или склонируйте репозитарий из github выполнив команду
```bash
git clone https://github.com/antONget/LenInfoService.git
```
## Для разворачивания телеграм-бота последовательно выполните команды:
### Создайте виртуальное окружения для проекта
```bash
python -m venv venv
```
### Активируйте его
### Windows:
```bash
venv\Scripts\activate.bat
```
### Linux
```bash
venv/Scripts/activate
```
### Установите требуемы зависисмости для проекта
```bash 
pip install -r requirements.txt
```
### Необезательный пункт
Внесите изменения в файл .env в папке config (если требуется изменить токен бота или id канала)
```python 
BOT_TOKEN="token_your_telegam_bot"
ADMIN_IDS="telegram_id manager(or admin), who will receive messages with orders"
```
### Запустите бота
```bash 
python bot.py 
```

### PM2
Еще один способ запустить бота — использовать менеджер процессов PM2. PM2 автоматически перезапускает бота и сохраняет логи.
Установите следующие пакеты:
```bash 
sudo apt install nodejs
sudo apt install npm
```
Далее установите PM2:
```bash 
npm install pm2 -g
```
Для запуска бота перейдите в директорию с ботом и запустите его командой:
```bash 
pm2 start bot.py --interpreter=python3
```
# Инструкция по работе с телеграмм-ботом
Телеграмм бот выполнен по техническому заданию согласованного с заказчиком.
![Воронка.jpeg](resources%2F%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D0%BA%D0%B0.jpeg)

Бот имеет только пользовательский режим.
Представляет собой цепочку сообщений, отправляемые через указанные промежутки времени.
Каждое сообщение представляет собой полезный контент побуждающий пользователя к покупке основного продукта.
В случае если пользователь НЕ открыл видео или статью, то ему с заданной переодичностью поступают сообщения побуждающие это сделать (всего три сообщения для каждого элемента контента).
При запуске бота в нижней части экранв на протяжении всей работы присутствует кнопку купить, связанная со страницей покупки продукта.

