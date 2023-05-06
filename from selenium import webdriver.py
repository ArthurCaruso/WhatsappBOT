from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Rebeca é chata!"
        self.chats1 = ["Rebeca Kook"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)
        for campo_grupo in self.chats1:
            campo_grupo = self.driver.find_element("class name", "//span[@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr']")
            time.sleep(2)
            campo_grupo.click()
            chat_box = self.driver.find_element("xpath", "//div[@class='p3_M1']")
            time.sleep(2)


            for con in range[0,15000]:
                chat_box.click()
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element("xpath",
                    "//span[@data-icon='send']")
                botao_enviar.click()

bot = WhatsappBot()
bot.EnviarMensagens()