import streamlit as st
import requests


def fazear_pergunta_llm(pergunta, chave_api):
    url = 'http://localhost/api/v1/workspace/documentos/chat'
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
        # Inspecionar conteúdo da resposta
        conteudo_resposta_bruto = response.content
        st.write(f"Resposta bruta: {conteudo_resposta_bruto}")

        try:
            # Tentar decodificar como UTF-8
            conteudo_resposta = conteudo_resposta_bruto.decode('utf-8')
        except UnicodeDecodeError as e:
            st.write(f"Erro de decodificação UTF-8: {e}")
            # Decodificar usando latin-1 como fallback
            conteudo_resposta = conteudo_resposta_bruto.decode('latin-1')

        conteudo_json = response.json()
        return conteudo_json.get('textResponse', 'Resposta não encontrada')
    else:
        return f"Erro ao fazer a pergunta {response.status_code}"

st.title('Unimed Assistent!')
chave_api = "B2VDWKK-C6VMS23-P6WYGCK-XPEQE7Q"

pergunta_usuario = st.text_input('Faça sua pergunta:')

if st.button('Enviar'):
    resposta = fazear_pergunta_llm(pergunta_usuario, chave_api)
    st.write(resposta)
