import os

class Checker:
    def __init__(self, config):
        self.config = config
        self.models_existence()
        self.telegram_api_token_existence()

    def models_existence(self):
        if not os.path.exists(self.config["VOSK_MODEL_PATH"]):
            print("[!] Can not find VOSK model :(")
            exit(1)
        print("[*] Passed test 'Models existence'")

    def telegram_api_token_existence(self):
        if self.config["TELEGRAM_API_TOKEN"] == "":
            print("[!] Can not find Bot token for Telegram :(")
            exit(1)
        print("[*] Passed test 'Telegram API Token existence'")