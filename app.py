import streamlit as st
import requests
###
# Função para aplicar estilos CSS personalizados
def adicionar_estilos_css():
    st.markdown(
        """
        <style>
        .reportview-container .main .block-container{
            font-family: 'Verdana';
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def fazear_pergunta_llm(pergunta, chave_api):
    url = 'http://192.168.0.88:3001/api/v1/workspace/documentos/chat'
    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': f'Bearer {chave_api}'
    }
    data = {
        "message": pergunta,
        "mode": "chat"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        conteudo_json = response.json()
        return conteudo_json.get('textResponse', 'Resposta não encontrada')
    else:
        return f"Erro ao fazer a pergunta {response.status_code}"
        
st.image("logo_unimed_bot.png", width=100)
st.title('UnimedBR Assistent!')
chave_api = "B2VDWKK-C6VMS23-P6WYGCK-XPEQE7Q"
adicionar_estilos_css()
pergunta_usuario = st.text_input('Faça sua pergunta:')

if st.button('Enviar'):
    resposta = fazear_pergunta_llm(pergunta_usuario, chave_api)
    st.write(resposta)
