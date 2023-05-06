# bibliotecas
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# declaração de variáveis
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)

contato = ['Contato Aqui']
mensagem = "Mensagem Aqui"

#busca 
def buscar_contato(contato):
    #achar contato
    campo_pesquisa = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]")
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    #digitar/enviar mensagem
def enviar_mensagem(mensagem):

    int c
    for c in range(15000):
        enviar_mensagem = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
        enviar_mensagem.send_keys(Keys.ENTER)
        enviar_mensagem.send_keys(mensagem)
        enviar_mensagem = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span")
        enviar_mensagem.click()

for contato in contato:
    buscar_contato(contato)
    enviar_mensagem(mensagem)


#  testar
