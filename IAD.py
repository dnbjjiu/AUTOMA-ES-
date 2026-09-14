import re
from pathlib import Path
from datetime import date
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    data = date.today().isoformat()

    pasta_downloads = Path(
        r"C:\Users\artur.dantas\Desktop\PowerBI Automacao"
        r"\Downloads\Índice de Atendimento à Demanda"
    )
    pasta_downloads.mkdir(parents=True, exist_ok=True)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        storage_state=r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Playwright dados\sessao.json"
    )
    page = context.new_page()

    page.goto("https://app.powerbi.com/groups/me/reports/275e19f2-81fc-4617-b8e7-7b1b8e1855f1/ReportSection78e554cea0bdb9000be7?experience=power-bi")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("combobox", name="grau").click()
    page.locator("div:nth-child(2) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="IAD por Unidade Judiciária").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download_info:
        page.get_by_test_id("export-btn").click()
    download = download_info.value
    download.save_as(pasta_downloads / f"{data}_G1.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/275e19f2-81fc-4617-b8e7-7b1b8e1855f1/ReportSection78e554cea0bdb9000be7?experience=power-bi")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("combobox", name="grau").click()
    page.locator("div:nth-child(3) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="IAD por Unidade Judiciária").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download1_info:
        page.get_by_test_id("export-btn").click()
    download1 = download1_info.value
    download1.save_as(pasta_downloads / f"{data}_G2.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/275e19f2-81fc-4617-b8e7-7b1b8e1855f1/ReportSection78e554cea0bdb9000be7?experience=power-bi")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.get_by_label("grau", exact=True).get_by_text("Todos").click()
    page.locator("div:nth-child(4) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="IAD por Unidade Judiciária").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download2_info:
        page.get_by_test_id("export-btn").click()
    download2 = download2_info.value
    download2.save_as(pasta_downloads / f"{data}_JE.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/275e19f2-81fc-4617-b8e7-7b1b8e1855f1/ReportSection78e554cea0bdb9000be7?experience=power-bi")
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="Limpar todas as segmentações").click(timeout=60000)
    page.get_by_role("combobox", name="grau").click()
    page.locator("div:nth-child(5) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="IAD por Unidade Judiciária").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download3_info:
        page.get_by_test_id("export-btn").click()
    download3 = download3_info.value
    download3.save_as(pasta_downloads / f"{data}_TR.xlsx")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
