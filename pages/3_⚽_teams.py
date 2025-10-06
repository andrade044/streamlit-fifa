
import streamlit as st

st.set_page_config(
    page_title='Players',
    page_icon='🏃🏼',
    layout='wide'
)

df_data = st.session_state['data']

clubes = df_data['Club'].unique()
club = st.sidebar.selectbox('Clube', clubes)

df_filtered = df_data[df_data['Club'] == club].set_index('Name')

# Substitui valores inválidos na coluna 'Photo' por None
df_filtered['Photo'] = df_filtered['Photo'].apply(lambda x: x if str(x).startswith("http") else None)

st.image(df_filtered.iloc[0]['Club Logo'])
st.markdown(f'## {club}')

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(
    df_filtered[columns], 
    column_config={
        'Photo': st.column_config.ImageColumn(),
        'Flag': st.column_config.ImageColumn('Country'),            
    }
)
