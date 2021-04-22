import requests
import os
from unidecode import unidecode

def buscar_dados_governo():
    print("=" * 60) 
    print("Informe os parâmetros para pesquisa e geração do arquivo CSV")
    id_cnae = input("Favor informar CNAE:")
    uf = input("Favor informar UF:")
    print("=" * 60) 
    
    retorno = requests.get(f"http://compras.dados.gov.br/fornecedores/v1/fornecedores.csv?id_cnae={id_cnae}&uf={uf}")
    retorno.encoding = 'ISO-8859-1'
    retorno = "sep=,\n" + unidecode(retorno.text)
    with open(f"dados_cnae_{id_cnae}_uf_{uf}.csv", "w") as arquivo_csv: 
        arquivo_csv.write(retorno) 
        print("Gerado arquivo: " + arquivo_csv.name)
        print("=" * 60)
        arquivo_csv.close()
        
buscar_dados_governo()