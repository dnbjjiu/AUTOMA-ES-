import re
from pathlib import Path
from datetime import date
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    data = date.today().isoformat()

    pasta_downloads = Path( r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Downloads\Conciliação Saúde")
    pasta_downloads.mkdir(parents=True, exist_ok=True)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Playwright dados\sessao.json")
    page = context.new_page()

    page.goto("https://app.powerbi.com/groups/me/reports/60290229-c07c-4fe1-8577-8eb113a685fa/350de3d9e78a083d0c64?experience=power-bi")
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="Indicador . Clique aqui para").click(timeout=60000)
    page.get_by_role("link", name="Indicador . Clique aqui para").click(timeout=60000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("combobox", name="Grau").click()
    page.locator("div:nth-child(2) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Índice de Conciliação por").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Compartilhar").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download_info:
        page.get_by_test_id("export-btn").click()
    download = download_info.value
    download.save_as(pasta_downloads / f"{data}_Conciliação Saúde_G1.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/60290229-c07c-4fe1-8577-8eb113a685fa/350de3d9e78a083d0c64?experience=power-bi")
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="Indicador . Clique aqui para").click(timeout=60000)
    page.get_by_role("link", name="Indicador . Clique aqui para").click(timeout=60000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("combobox", name="Grau").click()
    page.locator("div:nth-child(3) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Índice de Conciliação por").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Compartilhar").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download1_info:
        page.get_by_test_id("export-btn").click()
    download1 = download1_info.value
    download1.save_as(pasta_downloads / f"{data}_Conciliação Saúde_G2.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/60290229-c07c-4fe1-8577-8eb113a685fa/350de3d9e78a083d0c64?experience=power-bi")
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="Indicador . Clique aqui para").click(timeout=60000)
    page.get_by_role("link", name="Indicador . Clique aqui para").click(timeout=60000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("combobox", name="Grau").click()
    page.locator("div:nth-child(4) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Índice de Conciliação por").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download2_info:
        page.get_by_test_id("export-btn").click()
    download2 = download2_info.value
    download2.save_as(pasta_downloads / f"{data}_Conciliação Saúde_JE.xlsx")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)