import re
from pathlib import Path
from datetime import date
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    pasta_downloads = Path(r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Downloads\Atos Infracionais")
    pasta_downloads.mkdir(parents=True, exist_ok=True)
    data = date.today().isoformat()

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Playwright dados\sessao.json")
    page = context.new_page()

    page.goto("https://app.powerbi.com/groups/me/reports/7f3b523f-86b3-4f58-b3ed-dd9c278db641/2347c669099ae50e7e00")
    page.get_by_role("button", name="Limpar todas as segmentações").click()
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Tempo Liquido dos Processos (").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download5_info:
        page.get_by_test_id("export-btn").click()
    download5 = download5_info.value
    download5.save_as(pasta_downloads / f"{data}_Atos Infracionais.xlsx")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)