from playwright.sync_api import sync_playwright

tableRow = 1
fim = 1
final = 0


# Para pegar os arquivos do arquivei no futuro
# today = datetime.date.today()
# hoje = today.strftime("%d%m%y")
# lastDate = "150922"
# pageArquivei = browser.new_page()
#     pageArquivei.goto("https://app.arquivei.com.br/cte/list")
#     pageArquivei.fill("input[name='email']", "sac@maxcoatacado.com.br")
#     pageArquivei.wait_for_timeout(2000)
#     pageArquivei.fill("input[name='password']", "ce220281")
#     pageArquivei.wait_for_timeout(2000)
#     pageArquivei.click("button[name='login']")
#     pageArquivei.wait_for_timeout(2000)
#     pageArquivei.fill("input[id='createdStart']", lastDate)
#     pageArquivei.wait_for_timeout(2000)
#     pageArquivei.fill("input[id='createdEnd']", hoje)
#     pageArquivei.wait_for_timeout(2000)
#     pageArquivei.click("div[class='Select-value']")
#     pageArquivei.wait_for_timeout(2000)
#     pageArquivei.mouse.click(x=550, y=310)
#     pageArquivei.wait_for_timeout(2000)
#     pageArquivei.click("button[class='btn-sm']")
#     pageArquivei.wait_for_timeout(50000)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    pageBling = browser.new_page()
    pageBling.goto('https://www.bling.com.br/ctes.php#list')
    pageBling.wait_for_timeout(2000)
    pageBling.fill("input[id='username']", "******@*****atacado.com.br")
    pageBling.wait_for_timeout(2000)
    pageBling.fill("input[id='senha']", "**************")
    pageBling.wait_for_timeout(2000)
    pageBling.click("button[name='enviar']")
    pageBling.wait_for_timeout(2000)
    while (final <= 5):
        while (tableRow <= 100):
            pageBling.locator(f"xpath=/html/body/div[5]/div[4]/div[2]/div[2]/table/tbody/tr[{tableRow}]/td[2]").click()
            pageBling.wait_for_timeout(2000)
            ufEmit = pageBling.input_value("select[id=cte_emit_UF]")
            ufRem = pageBling.input_value("select[id=cte_rem_UF]")
            cfop = pageBling.input_value("input[id='cte_CFOP']")
            if (ufEmit == "ES" and ufRem == "ES" and cfop != "1353"):
                pageBling.fill("input[id='cte_CFOP']", "1353")
                pageBling.wait_for_timeout(2000)
                pageBling.click("button[id='botaoSalvar']")
                tableRow += 1
            elif (ufEmit != "ES" or ufRem != "ES"):
                pageBling.fill("input[id='cte_CFOP']", "2353")
                pageBling.wait_for_timeout(2000)
                pageBling.click("button[id='botaoSalvar']")
                pageBling.wait_for_timeout(2000)
                tableRow += 1
            elif (cfop == "2353" or cfop == "1553"):
                final += 1
                tableRow += 1
        pageBling.wait_for_timeout(2000)
        pageBling.locator("//html/body/div[5]/div[4]/div[2]/div[2]/nav/ul/li[4]/span").click()
        tableRow = 1
        pageBling.wait_for_timeout(2000)