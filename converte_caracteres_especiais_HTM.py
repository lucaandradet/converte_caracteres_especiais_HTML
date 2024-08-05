import os

# Dicionário de substituição de caracteres
substituicoes = {
    'Á': '&Aacute;', 'á': '&aacute;', 'Â': '&Acirc;', 'â': '&acirc;',
    'À': '&Agrave;', 'à': '&agrave;', 'Å': '&Aring;', 'å': '&aring;',
    'Ã': '&Atilde;', 'ã': '&atilde;', 'Ä': '&Auml;', 'ä': '&auml;',
    'Æ': '&AElig;', 'æ': '&aelig;', 'É': '&Eacute;', 'é': '&eacute;',
    'Ê': '&Ecirc;', 'ê': '&ecirc;', 'È': '&Egrave;', 'è': '&egrave;',
    'Ë': '&Euml;', 'ë': '&euml;', 'Ð': '&ETH;', 'ð': '&eth;',
    'Í': '&Iacute;', 'í': '&iacute;', 'Î': '&Icirc;', 'î': '&icirc;',
    'Ì': '&Igrave;', 'ì': '&igrave;', 'Ï': '&Iuml;', 'ï': '&iuml;',
    'Ó': '&Oacute;', 'ó': '&oacute;', 'Ô': '&Ocirc;', 'ô': '&ocirc;',
    'Ò': '&Ograve;', 'ò': '&ograve;', 'Ø': '&Oslash;', 'ø': '&oslash;',
    'Õ': '&Otilde;', 'õ': '&otilde;', 'Ö': '&Ouml;', 'ö': '&ouml;',
    'Ú': '&Uacute;', 'ú': '&uacute;', 'Û': '&Ucirc;', 'û': '&ucirc;',
    'Ù': '&Ugrave;', 'ù': '&ugrave;', 'Ü': '&Uuml;', 'ü': '&uuml;',
    'Ç': '&Ccedil;', 'ç': '&ccedil;', 'Ñ': '&Ntilde;', 'ñ': '&ntilde;',
    'Ý': '&Yacute;', 'ý': '&yacute;'
}

# Função para substituir caracteres especiais no texto
def substituir_caracteres(texto, substituicoes):
    for char, subst in substituicoes.items():
        texto = texto.replace(char, subst)
    return texto

# Caminho completo para o arquivo HTML
caminho_arquivo = 'd:/Projetos/Python/converte_caracteres_especiais_HTM/notas_taxa_cobertura.htm'

# Verificação se o arquivo existe
if not os.path.exists(caminho_arquivo):
    print(f"Arquivo não encontrado: {caminho_arquivo}")
else:
    # Leitura do arquivo HTML usando a codificação 'latin-1'
    with open(caminho_arquivo, 'r', encoding='latin-1') as file:
        conteudo = file.read()

    # Substituição dos caracteres especiais
    conteudo_substituido = substituir_caracteres(conteudo, substituicoes)

    # Salvando o conteúdo modificado em um novo arquivo
    caminho_arquivo_modificado = 'd:/Projetos/Python/converte_caracteres_especiais_HTM/notas_taxa_cobertura_modificado.htm'
    with open(caminho_arquivo_modificado, 'w', encoding='utf-8') as file:
        file.write(conteudo_substituido)

    print(f"Substituição concluída e arquivo salvo como '{caminho_arquivo_modificado}'")