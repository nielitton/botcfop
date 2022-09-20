from select import select
from playwright.sync_api import sync_playwright
tableRow = 98

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    pageBling = browser.new_page()
    pageBling.goto('https://www.bling.com.br/ctes.php#list')
    pageBling.wait_for_timeout(2000)
    pageBling.fill("input[id='username']", "nieliton@maxcoatacado.com.br")
    pageBling.wait_for_timeout(2000)
    pageBling.fill("input[id='senha']", "Psfm1234@")
    pageBling.wait_for_timeout(2000)
    pageBling.click("button[name='enviar']")
    pageBling.wait_for_timeout(2000)
    while (tableRow < 101):
        pageBling.locator(f"xpath=/html/body/div[5]/div[4]/div[2]/div[2]/table/tbody/tr[{tableRow}]/td[2]").click()
        pageBling.wait_for_timeout(2000)
        ufEmit = pageBling.input_value("select[id=cte_emit_UF]")
        ufRem = pageBling.input_value("select[id=cte_rem_UF]")
        cfop = pageBling.input_value("input[id='cte_CFOP']")
        if (ufEmit == "ES" and ufRem == "ES" and cfop != "1354"):
            pageBling.fill("input[id='cte_CFOP']", "1354")
            pageBling.click("button[id='botaoCancelar']")
            tableRow += 1
        else:
            pageBling.close()
    pageBling.wait_for_timeout(5000)
    pageBling.click("span[class='border-right']")
    pageBling.wait_for_timeout(50000)