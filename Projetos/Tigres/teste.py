from bs4 import BeautifulSoup
import os
import csv
import requests
import pandas as pd
import streamlit as st




st.title('Estatísticas - Tigres FA')

st.sidebar.image('tigres.png')
sidebar_option = st.sidebar.selectbox('Menu',['Dados Gerais','Team', 'Indy'])
@st.cache_data

def load_players_data():
    arquivo = "dados/Dados Atletas - Tigres.xlsx"
    dados = pd.read_excel(arquivo)
    dados_tratados = dados.drop(['ID', 'CPF','Endereço','Data de Nascimento','RG', 'E-mail', 'Status'], axis=1)
    return dados_tratados

def load_game_data():
    arquivo = "dados/Jogos/2023/2023 CBFA - Oilers vs Tigres.xlsx"
    #dados = []
    dados=pd.read_excel(arquivo, sheet_name="Indy")
    #dados.append(pd.read_excel(arquivo, sheet_name="Geral"))
    #dados.append(pd.read_excel(arquivo, sheet_name="Sobre"))
    return dados

gamestats = load_game_data()
playerstats = load_players_data()
playerstats = playerstats.fillna(0)

if sidebar_option == 'Dados Gerais':
    
    st.header('Cadastro Geral de Atletas')

    
    unique_pos = ['RB','QB','WR','OL','DL','LB','DB']
    selected_pos = st.multiselect('Position', unique_pos, unique_pos)
    df_selected = playerstats[(playerstats.Pos.isin(selected_pos))]

    st.write('Número total de atletas: ' + str(df_selected.shape[0]))
    st.dataframe(df_selected, hide_index=True)

if sidebar_option == "Indy":
    st.header('Estatísticas Individuais')


    #st.write(playerstats['Numero'])
    option = st.selectbox('Número do jogador',(playerstats['Numero']))
    resultado = playerstats[playerstats['Numero'] == option]
    
    st.subheader(resultado['Nome'].to_string(index=False))
    col2, col3 = st.columns(2)

    col2.write('Posição: ' + resultado['Pos'].to_string(index=False))
    col2.write('Altura: ' + resultado['Altura'].to_string(index=False))
    col2.write('Peso: ' + resultado['Peso'].to_string(index=False))
    col2.write('Idade: ')
    col2.write('Experiência: ')

    col3.write('Supino: ' + resultado['Supino'].to_string(index=False))
    col3.write('Agachamento: ' + resultado['Agachamento'].to_string(index=False))
    col3.write('Desenvolvimento: ' + resultado['Desenvolvimento'].to_string(index=False))
    col3.write('Salto horizontal: ' + resultado['Salto horizontal'].to_string(index=False))
    col3.write('40 yds: ' + resultado['40 yds'].to_string(index=False))
    
    st.subheader('Estatísticas')
    
    st.write('FILTRO DE TEMPORADA')
    st.write('FILTRO DE COMPETIÇAO')
    st.write('FILTRO DE JOGOS')

    if resultado['Pos'].to_string(index=False) == 'QB':
        st.write('Passes lançados: ')
        st.write('Passes completos: ')
        st.write('TD: ')
        st.write('TD corrido: ')
        st.write('Jardas lançadas: ')
        st.write('Jardas corridas: ')
        st.write('Rating: ')
    elif resultado['Pos'].to_string(index=False) == "OL":
        st.subheader('OL')
    elif resultado['Pos'].to_string(index=False) == "LB" or "DL" or "DB":
        st.write('Tackle: ')
        st.write('Tackle for loss: ')
        st.write('Sack: ')
        st.write('Interceptações: ')
        st.write('TD: ')
        st.write('Fumble forçado: ')
        st.write('Fumble recuperado: ')
    elif resultado['Pos'].to_string(index=False) == "RB" or "WR":
        st.write('Alvo: ')
        st.write('Jardas corridas: ')
        st.write('Passes recebidos: ')
        st.write('Jardas recebidas: ')
        st.write('TD: ')
        st.write('Fumble: ')

print('teste')