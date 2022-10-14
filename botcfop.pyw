from playwright.sync_api import sync_playwright
from tkinter import *


# Ideia para o futuro é pegar automaticamente o arquivo no arquivei
def initBot():
    dataInicio = textInputData.get()
    root.destroy()
    tableRow = 1
    final    = 0
    with sync_playwright() as p:
        browser   = p.chromium.launch(headless=False)
        pageBling = browser.new_page()
        pageBling.goto('https://www.bling.com.br/ctes.php#list')
        pageBling.wait_for_timeout(2000)
        email                 = pageBling.locator("input[id='username']") # Lembrar sempre de mascarar a senha e o e-mail pro GitHub...
        email.fill("assuntosdiversos1998@gmail.com")
        pageBling.wait_for_timeout(2000)
        senha                 = pageBling.locator("input[id='senha']")
        senha.fill("Tfm1234@")
        pageBling.wait_for_timeout(2000)
        button_enviar         = pageBling.locator("button[name='enviar']")
        button_enviar.click()
        pageBling.wait_for_timeout(2000)
        warning_armazenamento = pageBling.locator("xpath=//html/body/div[4]/div[1]/div/i")
        warning_armazenamento.click()
        pageBling.wait_for_timeout(2000)
        #FILTRANDO POR DATA DE PERÍODO ->
        button_calendar       = pageBling.locator("xpath=//html/body/div[5]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button")
        button_calendar.click()
        pageBling.wait_for_timeout(2000)
        select_month          = pageBling.locator("xpath=//html/body/div[5]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/div[2]/ul/li[6]")
        select_month.click()
        pageBling.wait_for_timeout(2000)
        input_data_filter     = pageBling.locator("input[id='filtro-data-ini']")
        input_data_filter.fill(dataInicio) 
        pageBling.wait_for_timeout(2000)
        filter_data           = pageBling.locator("xpath=//html/body/div[5]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/button")
        filter_data.click()
        pageBling.wait_for_timeout(2000)
        while (final <= 10):
            while (tableRow <= 100):
                row_cte = pageBling.locator(f"xpath=//html/body/div[5]/div[4]/div[2]/div[2]/table/tbody/tr[{tableRow}]")
                row_cte.click()
                pageBling.wait_for_timeout(1000)
                ufEmit  = pageBling.input_value("select[id=cte_emit_UF]")
                ufRem   = pageBling.input_value("select[id=cte_rem_UF]")
                cfop    = pageBling.input_value("input[id='cte_CFOP']")
                if (ufEmit == "ES" and ufRem == "ES" and cfop != "1353"):
                    final  = 0
                    cte_input = pageBling.locator("input[id='cte_CFOP']")
                    cte_input.fill("1353")
                    pageBling.wait_for_timeout(1000)
                    pageBling.click("button[id='botaoSalvar']")
                    tableRow += 1
                elif (ufEmit != "ES" or ufRem != "ES"):
                    final    = 0
                    cte_input_2353 = pageBling.locator("input[id='cte_CFOP']")
                    cte_input_2353.fill("2353")
                    pageBling.wait_for_timeout(1000)
                    pageBling.click("button[id='botaoSalvar']")
                    pageBling.wait_for_timeout(1000)
                    tableRow += 1
                else:
                    final    += 1
                    pageBling.click("button[id='botaoCancelar']")
                    pageBling.wait_for_timeout(1000)
                    tableRow += 1
                    if(final == 10000):
                        break
            pageBling.wait_for_timeout(1000)

            next_page = pageBling.locator("xpath=//html/body/div[5]/div[4]/div[2]/div[2]/nav/ul/li[4]/span")
            next_page.click()
            tableRow  = 1
            pageBling.wait_for_timeout(1000)

        # finalizando quando ele encontrar 5 CFOP's corretos
        pageBling.wait_for_timeout(2000) 
        pageBling.close()


root = Tk()
root.title("BotCFOP")

Label(text    = 'Digite uma data para iniciar o robô').grid(column = 0, row = 0)
textInputData = Entry(root)
textInputData.grid(column = 0, row = 1)
Button(text   = 'Rodar robô', command = initBot).grid(column = 0, row = 2)


root.mainloop()