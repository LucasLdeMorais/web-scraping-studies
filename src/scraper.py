import requests
import re
from bs4 import BeautifulSoup
from classes import Noticia
from utils import get_img_from_anchor, get_lists, get_paragraphs

BASE_URL = "http://sindpdrj.org.br/portal/v2/category/destaques/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def scrape():
    response = requests.get(BASE_URL, headers=HEADERS)
    html = response.content.decode()
    soup = BeautifulSoup(html, 'html.parser')

    #pega postagens da lista de destaques com base no padrão de id
    post_id_pattern = re.compile("^post-\d{5}$")
    posts = soup.find_all(id=post_id_pattern)
    posts_obj_arr = []

    #itera por cada post
    for post in posts:
        post_resumido = post.find('div', {"class": "post_entry"})

        #pegar imagem da thumbnail se tiver
        post_img = get_img_from_anchor(post_resumido, "thumb")

        #pega link do post inteiro
        url = post.find('a').get('href')
        post_html = requests.get(url, headers=HEADERS).content.decode()
        post_soup = BeautifulSoup(post_html, 'html.parser')

        #cata o titulo do post
        post_titulo = post_soup.find('h1', {"class":"titulo"}).contents[0]

        #cata div do conteúdo do post
        post_content_div = post_soup.find('div', {"class": "post_entry"})
        
        post_text = ""

        #pega todos os paragrafos do conteúdo
        post_text.join([get_paragraphs(post_content_div)])

        #pega todos as listas do conteúdo
        post_text.join([
            get_lists('ol', post_content_div), 
            get_lists('ul', post_content_div)
        ])

        #adiciona no array de posts formatados
        posts_obj_arr.append(Noticia(post_titulo,post_img,post_text))

    dados_serializaveis = [
        {
        'titulo': obj.titulo, 
        'imagem': obj.imagem, 
        'texto': obj.texto
        } for obj in posts_obj_arr
    ]
    
    return dados_serializaveis