import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd

##st.title('TIGRES FUTEBOL AMERICANO')



##st.sidebar.header('User Input Features')
##selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))

# Web scraping of NBA player stats
##@st.cache

def load_data():
    html = requests.get('https://docs.google.com/spreadsheets/d/1ZcN10BO983D_6sRr3VoSb3ZOn38oV-a1f5EIGSlXrWs/edit#gid=664418087').text
    soup = BeautifulSoup(html, "lxml")
    tables = soup.find_all("table")
    index = 0
    for table in tables:
        with open(str(index) + ".csv", "w") as f:
            wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])
        index = index + 1
        
    dados = pd.read_csv("teste.csv", sep=',')

    indexNames = dados[ dados['Status'] == 'out' ].index

    dados = dados.dropna(axis=0, how='all') 
    dados = dados.dropna(axis=1, how='all')
    dados = dados.drop(['CPF','E-mail', 'RG', 'Endereço'], axis=1)
    
    return dados

playerstats = load_data()
print(playerstats)

##st.dataframe(playerstats)