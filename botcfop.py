from playwright.sync_api import sync_playwright
tableRow = 98
fim = 1

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
    pageBling.wait_for_timeout(5000)
    pageBling.locator("//html/body/div[4]/div[1]/div/i").click()
    pageBling.wait_for_timeout(2000)
    while (fim <= 3):
        while (tableRow <= 100):
            pageBling.locator(f"xpath=/html/body/div[5]/div[4]/div[2]/div[2]/table/tbody/tr[{tableRow}]/td[2]").click()
            pageBling.wait_for_timeout(2000)
            ufEmit = pageBling.input_value("select[id=cte_emit_UF]")
            ufRem = pageBling.input_value("select[id=cte_rem_UF]")
            cfop = pageBling.input_value("input[id='cte_CFOP']")
            if (ufEmit == "ES" and ufRem == "ES" and cfop != "1354"):
                pageBling.fill("input[id='cte_CFOP']", "1354")
                pageBling.click("button[id='botaoCancelar']")
                tableRow += 1
        pageBling.wait_for_timeout(2000)
        pageBling.locator("//html/body/div[5]/div[4]/div[2]/div[2]/nav/ul/li[4]/span").click()
        tableRow = 98
        pageBling.wait_for_timeout(2000)
        fim += 1