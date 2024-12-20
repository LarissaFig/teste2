import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

df.drop(columns=['Unnamed: 0'], inplace=True)
list = ['Lat_d', 'Long_d']
# convertendo para numeros
df[list] = df[list].apply(pd.to_numeric, errors='coerce')
estados = df['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     estados)
dadosFiltrados = df[df['NM_UF'] == estadoFiltro]
if st.checkbox('Mostrar tabela'):
  st.write(dadosFiltrados)
st.map(dadosFiltrados, latitude="Lat_d", longitude="Long_d")

qtdmunicipios = len(df['NM_MUNIC'].unique())
st.write('A quantidade de municípios é', qtdmunicipios)
st.write('A quantidade de municípios é ' + str(qtdmunicipios))

qtdcomunidades = len(df['NM_AGLOM'].unique())
st.write('A quantidade de comunidades é ' + str(qtdcomunidades))

st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())

st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])

numero = st.slider('Escolha o número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))
