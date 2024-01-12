# _Немой [Lite]_
**Приложение для перевода голосовых в текст для Telegram**
> Это лёгкая версия бота Nemoi STT, которая использует VOSK

# Особенное спасибо разработчикам:
- **Aiogram: https://github.com/aiogram/aiogram**
- **VOSK: https://alphacephei.com/vosk/**

# Установка и запуск:
1. Установливаем системные зависимости:
```shell
# Arch Linux
sudo pacman -Sy python python-pip ffmpeg
```
2. Клонируем репозиторий:
```shell
git clone URL
```
3. Добавляем токен (регистрируем у BotFather) в /usr/share/nemoi-stt-lite/run/src/config.json
4. Запускаем бота:
```shell
sudo systemctl daemon-reload
sudo systemctl start nemoi-stt-lite
```

## Платформы
> Поддержка остальных платформ не планируется в будущем
- **Arch Linux**

## TODO:
- **Скрипт для изменения конфигурационного файла**