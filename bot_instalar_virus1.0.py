from util import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Dados import Dados

if __name__ == '__main__':
    dados = Dados()
    log_out = False
    n = 2

    ch_options = Options()
    navegador = webdriver.Chrome(executable_path=dados.path_driver, options=ch_options)

    navegador.get(dados.link)
    navegador.maximize_window()
    navegador.implicitly_wait(20)

    logar_conta(navegador, dados)

    # Logar nos softwares do computador
    clicar_botao_xpath('//*[@id="menu-software"]/a', navegador)

    posicao = posicao_virus(pc_tabela_software(navegador))

    lista_ips = filtra_ips(open("lista_ips.txt", "r"))


    for ip in lista_ips:
        # Entra na internet e pesquisar site
        pesquisa_site(ip, navegador)
        # Se o log out for necessario
        fazer_log_out(log_out, navegador)
        # Entra no site
        entra_no_site(navegador, n, ip)
        # copiando e apagando logs
        copiar_apagar_log_entrada(navegador)
        # Entrando nos softwares
        clicar_botao_xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div[1]/ul/li[2]/a', navegador)

        try:
            instalar_virus(navegador, posicao)
        except:
            print(f"não instalou {ip}")
        copiar_apagar_log_saida(navegador)
        log_out = True
        if n != 3:
            n += 1

# Se o ip não estiver mais ativo
# if EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[3]/div/div[1]/div[2]/div[1]/a')):
#     botao_whost = navegador.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[1]/div[2]/div[1]/a')
#     botao_whost.click()
#     continue
