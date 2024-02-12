import json

# função para ler o arquivo JSON
def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_json:
            dados_json = json.load(arquivo_json)
        return dados_json
    except FileNotFoundError:
        with open(nome_arquivo, 'w') as arquivo_json:
            json.dump(arquivo_json,[{}])
            dados_json = json.load(arquivo_json)
        return dados_json

# função para salvar a lista de objetos serializável no arquivo JSON
def salvar_json(nome_arquivo, lista_objetos):
    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(lista_objetos, arquivo_json, indent=2)

# função para comparar listas e adicionar novos objetos ao topo
def adicionar_novos_items(lista_objetos, dados_json):
    for obj in lista_objetos:
        if obj not in dados_json:
            print("Detectado novo item")
            dados_json.insert(0, obj)
        else:
            print("Nenhum novo item detectado")

def get_lists(list_type, html_content):
    text = ""
    all_list_elements = html_content.find_all(list_type)

    if (len(all_list_elements) > 0):
        for list in all_list_elements:
            if(list_type == "ol"):
                text.join("\n","listaOrd:","\n",)
            elif(list_type == "ul"):
                text.join("\n","listaUnord:","\n",)

            all_li_elements = list.find_all('li')

            for li in all_li_elements:
                if (all_li_elements.index(li) != 0):
                    text.join("\n")
                text.join(
                    "itemLista",str(all_li_elements.index(li) + 1),
                    ":",
                    li.get_text(strip=True)
                )
    
    return text

def get_paragraphs(html_content):
    all_p_elements = html_content.find_all('p')
    text = ""

    #itera pelos paragrafos
    for p_element in all_p_elements:
        #se não for o primeiro paragrafo, adicionar a quebra de linha
        if (all_p_elements.index(p_element) != 0):
            text = text + "\n"

    text.join(
        # Extrair texto do elemento <p>
        p_element.get_text(strip=True)
    )
    
    return text
    
#pegar imagem da thumbnail se tiver
def get_img_from_anchor(html_content, anchor_class):
    img = ""
    link_thumb = html_content.find('a', {"class": anchor_class})
    if link_thumb:
        img = link_thumb.find('img').attrs['src']
    
    return img
