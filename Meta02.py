import re
from pathlib import Path
from datetime import date
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    data = date.today().isoformat()

    pasta_meta02 = Path(r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Downloads\Metas\Meta 02\Meta 02")
    pasta_antigos = Path(r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Downloads\Metas\Meta 02\Mais antigos (Processos)")

    pasta_meta02.mkdir(parents=True, exist_ok=True)
    pasta_antigos.mkdir(parents=True, exist_ok=True)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="C:\\Users\\artur.dantas\\Desktop\\PowerBI Automacao\\Playwright dados\\sessao.json")
    page = context.new_page()

    page.goto("https://app.powerbi.com/groups/me/reports/97121c89-885c-4cac-971e-c3e8a28426d2/6f6168df79608b215c75?experience=power-bi")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Limpar todas as segmentações", exact=True).click(timeout=60000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.locator("span").filter(has_text="Meta 2").click()
    page.get_by_role("combobox", name="Instância").click()
    page.locator(".glyphicon.checkbox").first.click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Meta por Unidade Judiciária").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download_info:
        page.get_by_test_id("export-btn").click()
    download = download_info.value
    download.save_as(pasta_meta02 / f"{data}_G1.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/97121c89-885c-4cac-971e-c3e8a28426d2/6f6168df79608b215c75?experience=power-bi")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Limpar todas as segmentações", exact=True).click(timeout=60000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("combobox", name="Instância").click()
    page.locator("div:nth-child(2) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Meta por Unidade Judiciária").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download1_info:
        page.get_by_test_id("export-btn").click()
    download1 = download1_info.value
    download1.save_as(pasta_meta02 / f"{data}_G2.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/97121c89-885c-4cac-971e-c3e8a28426d2/6f6168df79608b215c75?experience=power-bi")
    page.wait_for_timeout(2000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("button", name="Limpar todas as segmentações", exact=True).click(timeout=60000)
    page.get_by_role("combobox", name="Instância").click()
    page.locator("div:nth-child(3) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Meta por Unidade Judiciária").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download2_info:
        page.get_by_test_id("export-btn").click()
    download2 = download2_info.value
    download2.save_as(pasta_meta02 / f"{data}_JE.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/97121c89-885c-4cac-971e-c3e8a28426d2/6f6168df79608b215c75?experience=power-bi")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Limpar todas as segmentações", exact=True).click(timeout=60000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("combobox", name="Instância").click()
    page.locator("div:nth-child(4) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Meta por Unidade Judiciária").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download4_info:
        page.get_by_test_id("export-btn").click()
    download4 = download4_info.value
    download4.save_as(pasta_meta02 / f"{data}_TR.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/97121c89-885c-4cac-971e-c3e8a28426d2/6f6168df79608b215c75?experience=power-bi")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Limpar todas as segmentações", exact=True).click(timeout=60000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_text("Mais Antigos", exact=True).click()
    page.get_by_role("combobox", name="Instância").click()
    page.locator(".glyphicon.checkbox").first.click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Meta por Unidade Judiciária").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download5_info:
        page.get_by_test_id("export-btn").click()
    download5 = download5_info.value
    download5.save_as(pasta_antigos / f"{data}_G1.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/97121c89-885c-4cac-971e-c3e8a28426d2/6f6168df79608b215c75?experience=power-bi")
    page.wait_for_timeout(4000)
    page.get_by_role("button", name="Limpar todas as segmentações", exact=True).click(timeout=60000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("combobox", name="Instância").click()
    page.locator("div:nth-child(2) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Meta por Unidade Judiciária").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download6_info:
        page.get_by_test_id("export-btn").click()
    download6 = download6_info.value
    download6.save_as(pasta_antigos / f"{data}_G2.xlsx")

    page.goto("https://app.powerbi.com/groups/me/reports/97121c89-885c-4cac-971e-c3e8a28426d2/6f6168df79608b215c75?experience=power-bi")
    page.wait_for_timeout(2000)
    page.add_style_tag(content="html { zoom: 45% !important; }")
    page.get_by_role("button", name="Limpar todas as segmentações", exact=True).click(timeout=60000)
    page.get_by_role("combobox", name="Instância").click()
    page.locator("div:nth-child(3) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
    page.get_by_test_id("appbar-edit-menu-btn").click()
    page.get_by_role("heading", name="Meta por Unidade Judiciária").click()
    page.get_by_test_id("visual-more-options-btn").click()
    page.get_by_test_id("pbimenu-item.Exportar dados").click()
    page.get_by_test_id("pbi-dropdown").click()
    page.get_by_text(".xlsx (Excel com no máximo").click()
    with page.expect_download() as download7_info:
        page.get_by_test_id("export-btn").click()
    download7 = download7_info.value
    download7.save_as(pasta_antigos / f"{data}_JE.xlsx")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)