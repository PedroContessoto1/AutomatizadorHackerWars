import time
from os import environ
import re
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

"""
Joker XD
"""

def env(key: str):
    """
    Carrega uma variavel de ambiente
    """
    return environ.get(key)


def id_return(html_table):
    """
    Filtra o html e retorna o ID do virus
    :param html_table: read_html
    :return: str
    """
    list_numerous_lines = []
    list_ids = []
    html_table = list(html_table)
    acc = 0
    for i in html_table:
        i.split("\n")
        acc += 1
        if i.split("\n") == ['Generic Warez.vwarez', '']:
            id_count = acc + 8
            list_numerous_lines.append(id_count)
    for i in list_numerous_lines:
        linha = html_table[i]
        html_id = str(linha).split("id")[1].split(">")[0]
        html_id = re.sub("[^0-9]", '', html_id)
        list_ids.append(html_id)
    return list_ids[0]


def posicao_virus(tabela):
    """
    Transforma tabela na posição do virus
    :param tabela: read_html
    :return: int
    """
    acc = 0
    for i in tabela:
        if i == 'Generic Warez.vwarez':
            return acc + 1
        else:
            acc += 1


def clicar_botao_xpath(xpath, navegador):
    botao = navegador.find_element_by_xpath(xpath)
    if EC.element_to_be_clickable((By.XPATH, xpath)):
        botao.click()


def pesquisa_site(ip, navegador):
    # clicar botao internet
    clicar_botao_xpath('//*[@id="menu-internet"]/a', navegador)
    # Colocando o link na url
    campo_url = navegador.find_element_by_xpath(
        '//*[@id="content"]/div[3]/div/div[1]/div[1]/div/div[1]/form/div/input[1]')
    campo_url.clear()
    campo_url.send_keys(ip)

    # clicar botao "go"
    clicar_botao_xpath('//*[@id="content"]/div[3]/div/div[1]/div[1]/div/div[1]/form/div/input[2]', navegador)


def entra_no_site(navegador, n, ip):
    # Se o ip ainda não estiver hackeado
    clicar_botao_xpath(f'//*[@id="content"]/div[3]/div/div[1]/div[{n}]/div[1]/ul/li[2]/a', navegador)
    time.sleep(0.5)
    if navegador.find_element_by_xpath('//*[@id="loginform"]/div[1]/div/div/input').get_attribute('value') == '':
        # clicar hack
        clicar_botao_xpath('//*[@id="content"]/div[3]/div/div[1]/div[2]/div[1]/ul/li[3]/a', navegador)
        time.sleep(1)
        # clicar crack
        clicar_botao_xpath('//*[@id="content"]/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]/a', navegador)
        time.sleep(4)

    # Entrar com acesso no computador hackeado
    clicar_botao_xpath('//*[@id="loginform"]/div[3]/span[3]/input', navegador)


def pc_tabela_software(navegador):
    # Tratamento do html para conseguir a posição do virus nos softwares
    html_meu_software = navegador.find_element_by_xpath(
        '//*[@id="content"]/div[3]/div/div/div/div[2]/div/table').get_attribute('outerHTML')
    soup = BeautifulSoup(html_meu_software, 'html.parser')
    table = soup.find(name='table')
    tabela_software = pd.read_html(str(table))[0]
    tabela_nomes = tabela_software['Software name']
    return tabela_nomes


def fazer_log_out(log_out, navegador):
    if log_out:
        # clicar no botao log out
        clicar_botao_xpath('//*[@id="content"]/div[3]/div/div[1]/div[2]/a', navegador)


def salvar_log(log: str):
    with open('logs.txt', 'a') as arquivo_saida:
        arquivo_saida.write(log)


def copiar_apagar_log_entrada(navegador):
    # Pegando o log e mandando para logs.txt
    game_campo_log = navegador.find_element_by_xpath(
        '//*[@id="content"]/div[3]/div[1]/div[3]/div[2]/div[1]/div/div/form/textarea[2]')
    salvar_log(game_campo_log.get_attribute("value"))
    # Limpando o Log
    game_campo_log.clear()
    game_botao_edit_log = navegador.find_element_by_xpath(
        '//*[@id="content"]/div[3]/div[1]/div[3]/div[2]/div[1]/div/div/form/input[2]')
    time.sleep(1)
    if EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="content"]/div[3]/div[1]/div[3]/div[2]/div[1]/div/div/form/input[2]')):
        game_botao_edit_log.click()
        time.sleep(5)


def copiar_apagar_log_saida(navegador):
    # Limpando os logs
    if EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[3]/div/div[3]/div[1]/ul/li[1]/a')):
        game_botao_log = navegador.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[3]/div[1]/ul/li[1]/a')
        game_botao_log.click()

    game_campo_log2 = navegador.find_element_by_xpath(
        '//*[@id="content"]/div[3]/div[1]/div[3]/div[2]/div[1]/div/div/form/textarea[2]')
    # Mandando os logs para logs.txt
    salvar_log(game_campo_log2.get_attribute("value"))
    game_campo_log2.clear()

    if EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="content"]/div[3]/div[1]/div[3]/div[2]/div[1]/div/div/form/input[2]')):
        game_botao_edit_log2 = navegador.find_element_by_xpath(
            '//*[@id="content"]/div[3]/div[1]/div[3]/div[2]/div[1]/div/div/form/input[2]')
        game_botao_edit_log2.click()
        time.sleep(5)


def instalar_virus(navegador, posicao):
    # Selecionando o virus
    game_botao_upload = navegador.find_element_by_xpath('//*[@id="link"]')
    time.sleep(3)
    game_botao_upload.click()
    time.sleep(3)

    # clicar botao de tabela de download
    clicar_botao_xpath('//*[@id="s2id_uploadSelect"]/a/span[1]', navegador)
    time.sleep(2)

    # clicar no virus na tabela
    clicar_botao_xpath(f'//*[@id="select2-drop"]/ul/li[{posicao}]/ul/li/div', navegador)

    # botao de upload
    clicar_botao_xpath('//*[@id="uploadForm"]/input', navegador)

    # Fazendo tratamento do Html para pegar o ID do virus
    tabela_software_internet = navegador.find_element_by_xpath(
        '//*[@id="content"]/div[3]/div/div[3]/div[2]/div/div[1]/table').get_attribute('outerHTML')
    soup_internet = BeautifulSoup(tabela_software_internet, 'html.parser')
    table_internet = soup_internet.find(name='table')
    arquivo = open("html_tabela.txt", "w")
    arquivo.write(str(table_internet))
    arquivo.close()
    arquivo = open("html_tabela.txt", "r")
    id_ = id_return(arquivo)
    clicar_botao_xpath(f'//*[@id="{id_}"]/td[5]/a[3]', navegador)
    # Instalando o virus
    arquivo.close()


def logar_conta(navegador, dados):
    # Escreve login e senha
    campo_login = navegador.find_element_by_xpath('//*[@id="login-username"]')
    campo_senha = navegador.find_element_by_xpath('//*[@id="password"]')
    campo_login.send_keys(dados.login)
    campo_senha.send_keys(dados.senha)
    # Passar do reCAPTCHA
    input("Caps feito :")
    # Logar na conta
    clicar_botao_xpath('//*[@id="login-submit"]', navegador)

def filtra_ips(lista_ips):
    ips_certo = []
    for i in lista_ips:
        ips_certo.append(i.split("[")[1].split("]")[0])
    return ips_certo
