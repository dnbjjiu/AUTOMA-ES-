import re
from pathlib import Path
from datetime import date
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    data = date.today().isoformat()

    pasta_downloads = Path(r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Downloads\Ações Penais")
    pasta_downloads.mkdir(parents=True, exist_ok=True)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Playwright dados\sessao.json")
    page = context.new_page()

    page.goto("https://app.powerbi.com/groups/me/reports/ebc6fba5-0ed5-4869-8190-994a61b2f205/e83338934a0be8733270?experience=power-bi")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Tempo médio (dias) por").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download3_info:
        page.get_by_test_id("export-btn").click()
    download3 = download3_info.value
    download3.save_as(pasta_downloads / f"{data}_Ações Penais.xlsx")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)