from bs4 import BeautifulSoup
import os
import csv
import requests
import pandas as pd
import streamlit as st


st.title('Estatísticas - Tigres FA')

st.markdown("""
Estatísticas gerais, por setor e individuais de 2023
""")

st.sidebar.header('Sidebar')


# Web scraping of NFL player stats
# https://www.pro-football-reference.com/years/2019/rushing.htm
@st.cache_data

def load_players_data():
    arquivo = "dados/Dados Atletas - Tigres.csv"
    dados = pd.read_csv(arquivo, sep=',')
    dados_tratados = dados.drop(['ID', 'CPF','Endereço','Data de Nascimento','RG', 'E-mail'], axis=1)
    return dados_tratados

def load_game_data():
    arquivo = "dados/Jogos/2023/2023 CBFA - Oilers vs Tigres.xlsx"
    #dados = []
    dados=pd.read_excel(arquivo, sheet_name="Indy")
    #dados.append(pd.read_excel(arquivo, sheet_name="Geral"))
    #dados.append(pd.read_excel(arquivo, sheet_name="Sobre"))
    print(dados)
    return dados




playerstats = load_players_data()
gamestats = load_game_data()



###### Cadastro Geral de Atletas
st.header('Cadastro Geral de Atletas')

# Filtering data
unique_pos = ['RB','QB','WR','OL','DL','LB','DB']
selected_pos = st.multiselect('Position', unique_pos, unique_pos)
df_selected = playerstats[(playerstats.Pos.isin(selected_pos))]

st.write('Número total de atletas: ' + str(df_selected.shape[0]))
st.dataframe(df_selected, hide_index=True)

###### Estatisticas Gerais (temporada e por partida)
st.header('Estatísticas Gerais')
st.write('Dados gerais do time ataque/defesa')
#st.dataframe(gamestats[1])
#Filtro de dados 

option = st.selectbox('How would you like to be contacted?',(range(100)))
st.write('You selected:', option)
st.dataframe(gamestats.iloc[int(option)])

###### Estatisticas Individuais (temporada e por partida)
st.header('Estatísticas Individuais')
st.write('Dados individuais do time ataque/defesa')

numeros = list(range(100))
selected_number = st.multiselect('Numero', numeros, numeros)
df_indy = gamestats[(gamestats.Numero.isin(selected_number))]
st.dataframe(df_indy, hide_index=True)

