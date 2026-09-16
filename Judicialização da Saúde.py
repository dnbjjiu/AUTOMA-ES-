import re
from datetime import datetime
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    caminho = r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Downloads\Judicialização da Saúde"
    data = datetime.now().strftime("%Y-%m-%d")

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="C:\\Users\\artur.dantas\\Desktop\\PowerBI Automacao\\Playwright dados\\sessao.json")
    page = context.new_page()
    page.goto("https://app.powerbi.com/groups/me/reports/e89c8572-40b5-4e0c-ad63-97751a54ea0c/59f7b69802b252be24e8?experience=power-bi")
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.get_by_role("checkbox", name="G1").click()
    page.get_by_role("link", name="Indicador . Clique para").first.click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Tempo médio (dias) por").nth(1).click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download6_info:
        page.get_by_test_id("export-btn").click()
    download6 = download6_info.value
    download6.save_as(f"{caminho}\\Judicialização da Saúde_G1_{data}.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/e89c8572-40b5-4e0c-ad63-97751a54ea0c/59f7b69802b252be24e8?experience=power-bi&bookmarkGuid=a5965c20c2a9057243e6")
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.get_by_role("checkbox", name="G2").click()
    page.get_by_role("heading", name="Tempo médio (dias) por").nth(1).click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Tempo médio (dias) por").nth(1).click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download7_info:
        page.get_by_test_id("export-btn").click()
    download7 = download7_info.value
    download7.save_as(f"{caminho}\\Judicialização da Saúde_G2_{data}.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/e89c8572-40b5-4e0c-ad63-97751a54ea0c/59f7b69802b252be24e8?experience=power-bi")
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.get_by_role("checkbox", name="JE").click()
    page.get_by_role("link", name="Indicador . Clique para").first.click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Tempo médio (dias) por").nth(1).click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download8_info:
        page.get_by_test_id("export-btn").click()
    download8 = download8_info.value
    download8.save_as(f"{caminho}\\Judicialização da Saúde_JE_{data}.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/e89c8572-40b5-4e0c-ad63-97751a54ea0c/59f7b69802b252be24e8?experience=power-bi&bookmarkGuid=a5965c20c2a9057243e6")
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.get_by_role("checkbox", name="TR").click()
    page.get_by_role("heading", name="Tempo médio (dias) por").nth(1).click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Tempo médio (dias) por").nth(1).click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download9_info:
        page.get_by_test_id("export-btn").click()
    download9 = download9_info.value
    download9.save_as(f"{caminho}\\Judicialização da Saúde_TR_{data}.xlsx")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)