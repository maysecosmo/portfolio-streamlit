import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title='Meu Portfólio | Mayse', layout='wide')

# Menu lateral
st.sidebar.title('Navegação')
aba = st.sidebar.radio('Ir para:', ['Sobre Mim', 'Serviços e Prazos', 'Orçamento Inteligente'])

if aba == 'Sobre Mim':
    st.title('Olá, eu sou Mayse ✨')
    st.subheader('Freelancer de Edição & Estudante de ADS')
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info('📍 Recife, PE')
    with col2:
        st.write('''
        Sou revisora, editora e agora futura desenvolvedora. Este espaço une minha 
        experiência com palavras e minha transição para o mundo Full-Stack.
        ''')
    
    st.divider()
    st.write('### Minha Jornada')
    st.markdown('''
    - 📚 Experiência com Saber Editorial.
    - 💻 Cursando Análise e Desenvolvimento de Sistemas (Wyden).
    - 🐍 Foco em Python, Lógica e Desenvolvimento Full-Stack.
    ''')

elif aba == 'Serviços e Prazos':
    st.title('Serviços Editoriais 📖')
    
    dados = {
        'Serviço': ['Revisão Simples', 'Edição Crítica', 'Formatação ABNT'],
        'Prazo Médio': ['3-5 dias', '7-10 dias', '2-4 dias'],
        'Complexidade': ['Baixa', 'Média', 'Média']
    }
    df = pd.DataFrame(dados)
    st.table(df)

elif aba == 'Orçamento Inteligente':
    st.title('Simulador de Orçamento 💻')
    st.write('Selecione os detalhes do seu projeto para uma estimativa baseada em lógica de programação.')
    
    tipo_servico = st.selectbox('Tipo de serviço:', ['Revisão', 'Edição', 'Consultoria'])
    paginas = st.number_input('Quantidade de páginas:', min_value=1, value=10)
    
    if st.button('Calcular Estimativa'):
        # Lógica de cálculo
        preco_base = 10 if tipo_servico == 'Revisão' else 20
        total = paginas * preco_base
        st.success(f'O valor estimado para seu projeto de {tipo_servico} é: R$ {total},00')
        st.caption('Nota: Este cálculo foi gerado por uma função Python integrada ao Streamlit.')

    # Sessão de Contato
    st.divider()
    st.subheader('Vamos tirar seu projeto do papel? ✨')
    
    col_mail, col_link = st.columns(2)
    with col_mail:
        st.write('**📧 E-mail:**')
        st.code('maysecosmo@gmail.com')
    
    with col_link:
        st.write('**🔗 LinkedIn:**')
        st.markdown('[Acesse meu perfil profissional](https://www.linkedin.com/in/seu-usuario-aqui/)')
    
    st.info('Dica: Mencione que você veio pelo portfólio para prioridade no atendimento!')