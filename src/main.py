from scraper import scrape
from utils import ler_json, adicionar_novos_items, salvar_json

DATA_FILE = "../data/posts.json"

def main():
    posts = scrape()
    json_data = ler_json(DATA_FILE)

    #adicionar novos objetos ao topo do arquivo, se houver
    adicionar_novos_items(posts, json_data)

    #salvar a lista de objetos atualizada no arquivo JSON
    salvar_json(DATA_FILE, json_data)

if __name__ == "__main__":
    main()