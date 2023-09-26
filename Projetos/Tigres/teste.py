from bs4 import BeautifulSoup
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

def load_data():
    dados = pd.read_csv("dados.csv", sep=',')

    dados_tratados = dados.drop(['ID','Email','Nascimento','Entrada'], axis=1)
    print(dados)
    return dados_tratados

playerstats = load_data()
print(type(playerstats))


###### Cadastro Geral de Atletas
st.header('Cadastro Geral de Atletas')

# Filtering data
unique_pos = ['RB','QB','WR','OL','DL','LB','DB']
selected_pos = st.multiselect('Position', unique_pos, unique_pos)
df_selected = playerstats[(playerstats.Pos.isin(selected_pos))]

st.write('Número total de atletas: ' + str(df_selected.shape[0]))
st.dataframe(df_selected)

###### Estatisticas Gerais (temporada e por partida)

###### Estatisticas Individuais (temporada e por partida)