Explicação do fluxo. 


Abre o navegador com o login salvo
↓
G1: abre o relatório → limpa filtros → seleciona G1
    → entra em edição → exporta → salva Excel
↓
G2: abre o relatório → limpa filtros → seleciona G2
    → entra em edição → exporta → salva Excel
↓
JE: abre o relatório → limpa filtros → seleciona JE
    → entra em edição → exporta → salva Excel
↓
TR: abre o relatório → limpa filtros → seleciona TR
    → entra em edição → exporta → salva Excel
↓
Fecha o navegador
 


get_by_role("button", name="Limpar todas as segmentações")    #Entrou no site - limpar filtros
get_by_role("combobox", name="grau").locator("i") #selecionar grau 
locator("div:nth-child(2) > .slicerItemContainer > .slicerCheckbox > .glyphicon") #G1
locator("div:nth-child(3) > .slicerItemContainer > .slicerCheckbox > .glyphicon") #G2
locator("div:nth-child(4) > .slicerItemContainer > .slicerCheckbox > .glyphicon") #JE 
locator("div:nth-child(5) > .slicerItemContainer > .slicerCheckbox > .glyphicon") #TR
get_by_test_id("appbar-edit-menu-btn")  #EDITAR
locator(".visual.customPadding.allow-deferred-rendering.visual-clusteredBarChart > .cartesianChart > .clearCatcher")  #selecionei o gráfico desejado
get_by_test_id("visual-more-options-btn")  #Tres pontos 
locator("#cdk-overlay-11").get_by_test_id("pbimenu-item.Exportar dados") # Exportar dados 
locator("#pbi-radio-button-1 > .pbi-radio-button-internal > section > .pbi-radio-button-circle > .pbi-radio-button-checkmark")   #Selecionar dados resumidos 
get_by_test_id("pbi-dropdown")     #Tabela suspensa 
get_by_text (".xlsx (Excel com no máximo"))      #xlsx (Excel com no maximo 150.000 linhas)
get_by_test_id("export-btn")      #Baixar arquivo
