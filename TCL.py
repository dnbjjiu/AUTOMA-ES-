from datetime import date
from pathlib import Path
from time import sleep
from playwright.sync_api import sync_playwright

URL = "https://app.powerbi.com/groups/me/reports/c5cdb4d4-131e-4eeb-a52a-d6de5efd39d4/ReportSectionc51293895131cec6dfe1?language=pt-BR&experience=power-bi"
SESSAO = Path(r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Playwright dados\sessao.json")
PASTA = Path(r"C:\Users\artur.dantas\Desktop\PowerBI Automacao\Downloads\Taxa de congestionamento Liquida")
DIA = date.today().isoformat()

with sync_playwright() as pw:
    navegador = pw.chromium.launch(channel="chrome", headless=False)
    try:
        contexto = navegador.new_context(accept_downloads=True, storage_state=str(SESSAO) if SESSAO.exists() else None)
        pagina = contexto.new_page()
        pagina.set_default_timeout(60_000)
        PASTA.mkdir(parents=True, exist_ok=True)
        SESSAO.parent.mkdir(parents=True, exist_ok=True)
        for grau, posicao in (("G1", 2), ("G2", 3), ("JE", 4), ("TR", 5)):
            print(f"Iniciando: {grau}", flush=True)
            pagina.goto(URL)
            limpar = pagina.get_by_role("button", name="Limpar todas as segmentações")
            limpar.wait_for(state="visible", timeout=300_000)
            contexto.storage_state(path=str(SESSAO), indexed_db=True)
            limpar.click()
            sleep(1)
            pagina.get_by_text("Todos").first.click()
            pagina.locator(f"div:nth-child({posicao}) > .slicerItemContainer > .slicerCheckbox > .glyphicon").click()
            pagina.keyboard.press("Escape")
            pagina.get_by_test_id("appbar-edit-menu-btn").click()
            pagina.get_by_role("heading", name="TCL por Unidade Judiciária", exact=True).click()
            pagina.get_by_test_id("visual-more-options-btn").click()
            pagina.get_by_test_id("pbimenu-item.Exportar dados").click()
            pagina.locator("#pbi-radio-button-1 > .pbi-radio-button-internal > section > .pbi-radio-button-circle > .pbi-radio-button-checkmark").click()
            pagina.get_by_test_id("pbi-dropdown").click()
            pagina.get_by_text(".xlsx (Excel com no máximo").click()
            with pagina.expect_download(timeout=180_000) as download:
                pagina.get_by_test_id("export-btn").click()
            print(f"Download iniciado: {grau}", flush=True)
            destino = PASTA / f"{DIA}_{grau}.xlsx"
            download.value.save_as(destino)
            print(f"Salvo: {destino.name}", flush=True)
    finally:
        navegador.close()