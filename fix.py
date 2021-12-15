#yehezkiel erickson
#12219017
#UAS Pemrograman  Komputer /IF 2112
#Aplikasi GUI berbasi streamlit

#import modul yang dibutuhkan
import streamlit as st
import pandas as pd
import plotly.express as px

#merge data produksi minyak mentah dengan data detail negara
data = pd.read_csv ("produksi_minyak_mentah.csv")
dataNegara = pd.read_json ('kode_negara_lengkap.json')
dataNegara=dataNegara.rename(columns={"alpha-3":"kode_negara"})
data=pd.merge(dataNegara,data,on='kode_negara')

#membuat selektor display
selectorNegara = data['name'].drop_duplicates()
selectorTahun = data['tahun'].drop_duplicates()
selectorBesar = [1,2,3,5,10,20,50,100]

#Judul
st.title('Produksi Minyak Mentah Dunia')

##Produksi Minyak Mentah Tiap Negara Per Tahun
st.markdown('Produksi Minyak Mentah Tiap Negara Per Tahun')
selectNegara = st.selectbox('Pilih Negara',selectorNegara)
dataA = data[data['name'] == selectNegara]
dataA_graph=px.bar(
  dataA,
  x="tahun",
  y="produksi",
  title=str("Produksi Minyak Mentah "+selectNegara)
)
st.plotly_chart(dataA_graph)

##Produksi Minyak Mentah Terbesar pada Tahun x
st.markdown('Produksi Minyak Mentah Terbesar pada Tahun ')
selectTahun = st.selectbox('Pilih Tahun', selectorTahun)
selectBanyakNegara = st.selectbox('Pilih Banyak Negara', selectorBesar)
dataB = data[data['tahun'] == selectTahun]
dataB=dataB.sort_values(["produksi"],ascending=[0])
dataB=dataB[:selectBanyakNegara]
dataB_graph=px.bar(
  dataB,
  x="name",
  y="produksi"
)
st.plotly_chart(dataB_graph)

##Produksi Minyak Mentah Kumulatif Terbesar
st.markdown('Produksi Minyak Mentah Kumulatif Terbesar')
selectBanyakNegara2 = st.selectbox('Pilih Banyak Negara ', selectorBesar)
dataC = data.groupby(["name"])["produksi"].sum().reset_index()
dataC=dataC.sort_values(["produksi"],ascending=[0])
dataC=dataC[:selectBanyakNegara2]
dataC_graph=px.bar(
  dataC,
  x="name",
  y="produksi"
)
st.plotly_chart(dataC_graph)

