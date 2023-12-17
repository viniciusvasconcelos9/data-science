#from bs4 import BeautifulSoup
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
option_sidebar = st.sidebar.selectbox('Menu',['Cadastro Geral', 'Indy', 'Team'])
st.sidebar.write('You selected:', option_sidebar)



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

if option_sidebar == 'Cadastro Geral':
    st.header('Cadastro Geral de Atletas')
    unique_pos = ['RB','QB','WR','OL','DL','LB','DB']
    selected_pos = st.multiselect('Position', unique_pos, unique_pos)
    df_selected = playerstats[(playerstats.Pos.isin(selected_pos))]

    st.write('Número total de atletas: ' + str(df_selected.shape[0]))
    st.dataframe(df_selected, hide_index=True)
elif option_sidebar == 'Indy':
    st.header('Estatísticas Individuais')
    st.write('Dados individuais do time ataque/defesa')
elif option_sidebar == 'Team':
    st.header('Estatísticas Coletivas   ')
    st.write('Dados individuais do time ataque/defesa')
    
    

