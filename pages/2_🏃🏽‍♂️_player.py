import streamlit as st

import requests


import requests
from PIL import Image
from io import BytesIO



st.set_page_config(
    page_title= 'Players',
    page_icon= '🏃🏼',
    layout='wide'
)

df_data = st.session_state['data']

clubes = df_data['Club'].unique()
club = st.sidebar.selectbox('Clube',clubes)

df_players = df_data[(df_data['Club'] == club)]
players = df_players['Name'].unique()
player = st.sidebar.selectbox('Jogador', players)

player_stats = df_data[df_data['Name'] == player].iloc[0]

photo_url = player_stats["Photo"].strip()
if photo_url.startswith("http"):
    try:
        response = requests.get(photo_url)
        img = Image.open(BytesIO(response.content))
        st.image(img, width=100)
    except Exception as e:
        st.error(f"Erro ao carregar a imagem: {e}")

# st.image(player_stats['Photo'].strip())
st.title(player_stats['Name'])

st.markdown(f'**Clube:** {player_stats['Club']}')
st.markdown(f'**Posição:** {player_stats['Position']}')

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f'**Idade:** {player_stats['Age']}')
col2.markdown(f'**Altura:** {player_stats['Height(cm.)']/100}')
col3.markdown(f'**Peso:** {player_stats['Weight(lbs.)']*.453:.2f}')
st.divider()

st.subheader(f'Overall {player_stats['Overall']}')
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")


# import requests
# from PIL import Image
# from io import BytesIO


# photo_url = player_stats["Photo"].strip()
# # st.write(f"URL da imagem: {photo_url}")  # só para verificar

# if photo_url.startswith("http"):
#     try:
#         response = requests.get(photo_url)
#         img = Image.open(BytesIO(response.content))
#         st.image(img, width=200)
#     except Exception as e:
#         st.error(f"Erro ao carregar a imagem: {e}")
# else:
#     st.warning("URL da imagem inválida.")


