import streamlit as st
import pandas as pd
import requests as rqt
dadosMulheres = rqt.get('https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome')

dadosMulheres.headers['Content-Type']
dados_M_json = dadosMulheres.json()


dados_M_json.keys()
dfmulheres = pd.DataFrame(dados_M_json['dados'])

dfmulheres['sexo'] = 'feminino'

dadosHomens = rqt.get('https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome')

dados_H_json = dadosHomens.json()
dfhomens = pd.DataFrame(dados_H_json['dados'])

dfhomens['sexo'] = 'masculino'
df_concat = pd.concat([dfmulheres, dfhomens], axis = 'index')

#Crie um dashboard no streamlit com essas informações e insira um selectbox que realize filtragem por gênero.
st.title ('Análise da quantidade de deputados por sexo')
sexo_selecionado = st.selectbox('Selecione o sexo', df_concat['sexo'].unique())

#Crie um gráfico de barras com o número de homens e mulheres deputados por estado, a depender do sexo selecionado.
# Se necessário, peça ajuda ao chat GPT sobre como calcular a quantidade de deputados por estado.
st.header('Quantidade de deputados por estado', sexo_selecionado)
dadosFiltrados = df_concat[df_concat['sexo'] == sexo_selecionado]
st.title('Deputados do sexo ' + sexo_selecionado)
ocorrencias = dadosFiltrados['siglaUf'].value_counts()
dfEstados = pd.DataFrame({
      'siglaUf':ocorrencias.index,
      'quantidade':ocorrencias.values}
)
st.bar_chart(dfEstados,
             x = 'siglaUf',
             y = 'quantidade', 
             x_label = "estado",
             y_label = 'Quantidade de deputados')
st.dataframe(dadosFiltrados)

#Acrescente informações sobre o total de deputados, além do total de homens e mulheres.
totalHomens = dfhomens['id'].count()
st.metric('O total de homens é ', totalHomens)

totalMulheres = dfmulheres['id'].count()
st.metric('O total de mulheres é ', totalMulheres)
