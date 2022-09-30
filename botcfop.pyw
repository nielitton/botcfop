from playwright.sync_api import sync_playwright
from tkinter import *




# Ideia para o futuro é pegar automaticamente o arquivo no arquivei

def initBot():
    tableRow = 1
    final = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        pageBling = browser.new_page()
        pageBling.goto('https://www.bling.com.br/ctes.php#list')
        pageBling.wait_for_timeout(2000)
        pageBling.fill("input[id='username']", "") # Lembrar sempre de mascarar a senha e o e-mail pro GitHub...
        pageBling.wait_for_timeout(2000)
        pageBling.fill("input[id='senha']", "")
        pageBling.wait_for_timeout(2000)
        pageBling.click("button[name='enviar']")
        pageBling.wait_for_timeout(2000)
        pageBling.click("xpath=//html/body/div[5]/div[1]/div/i")
        pageBling.wait_for_timeout(2000)
        #FILTRANDO POR DATA DE PERÍODO -->
        pageBling.click("xpath=//html/body/div[6]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div[2]")
        pageBling.wait_for_timeout(2000)
        pageBling.click("xpath=//html/body/div[6]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/div[2]/ul/li[6]")
        pageBling.wait_for_timeout(2000)
        pageBling.fill("input[id='filtro-data-ini']", textInputData.get())
        pageBling.wait_for_timeout(2000)
        pageBling.click("xpath=//html/body/div[6]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/div[3]/div[2]")
        pageBling.wait_for_timeout(2000)
        while (final <= 10000):
            while (tableRow <= 100):
                pageBling.click(f"xpath=/html/body/div[6]/div[4]/div[2]/div[2]/table/tbody/tr[{tableRow}]")
                pageBling.wait_for_timeout(2000)
                ufEmit = pageBling.input_value("select[id=cte_emit_UF]")
                ufRem = pageBling.input_value("select[id=cte_rem_UF]")
                cfop = pageBling.input_value("input[id='cte_CFOP']")
                if (ufEmit == "ES" and ufRem == "ES" and cfop != "1353"):
                    final = 0
                    pageBling.fill("input[id='cte_CFOP']", "1353")
                    pageBling.wait_for_timeout(2000)
                    pageBling.click("button[id='botaoSalvar']")
                    tableRow += 1
                elif (ufEmit != "ES" or ufRem != "ES"):
                    final = 0
                    pageBling.fill("input[id='cte_CFOP']", "2353")
                    pageBling.wait_for_timeout(2000)
                    pageBling.click("button[id='botaoSalvar']")
                    pageBling.wait_for_timeout(2000)
                    tableRow += 1
                else:
                    final += 1
                    pageBling.click("button[id='botaoCancelar']")
                    pageBling.wait_for_timeout(2000)
                    tableRow += 1
                    if(final == 10000):
                        break
            pageBling.wait_for_timeout(2000)
            pageBling.click("xpath=//html/body/div[6]/div[4]/div[2]/div[2]/nav/ul/li[4]/span/span[1]")
            tableRow = 1
            pageBling.wait_for_timeout(2000)

        # finalizando quando ele encontrar 5 CFOP's corretos
        pageBling.wait_for_timeout(2000) 
        pageBling.close()


root = Tk()
root.title("BotCFOP")

Label(text='Digite uma data para iniciar o robô').grid(column=0, row=0)
textInputData = Entry(root)
textInputData.grid(column=0, row=1)
Button(text='Rodar robô', command=initBot).grid(column=0, row=2)


root.mainloop()


