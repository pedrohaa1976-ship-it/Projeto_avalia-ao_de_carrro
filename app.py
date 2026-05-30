import streamlit as st

st.markdown(
    """
    <style>
    /* Cria as linhas verticais onduladas/entrelaçadas bem finas nas duas laterais */
    .stApp::before, .stApp::after {
        content: "";
        position: fixed;
        top: 0;
        bottom: 0;
        width: 15px;
        z-index: 9999;
        pointer-events: none;
        background-image: 
            linear-gradient(135deg, #dfba6b 25%, transparent 25%, transparent 50%, rgba(254, 254, 244, 0.4) 50%, rgba(254, 254, 244, 0.4) 75%, #dfba6b 75%, #dfba6b 100%),
            linear-gradient(45deg, #dfba6b 25%, transparent 25%, transparent 50%, rgba(254, 254, 244, 0.4) 50%, rgba(254, 254, 244, 0.4) 75%, #dfba6b 75%, #dfba6b 100%);
        background-size: 15px 25px;
    }
    
    .stApp::before { left: 0; border-right: 1px solid #dfba6b; }
    .stApp::after { right: 0; border-left: 1px solid #dfba6b; }

    .block-container {
        padding-left: 35px !important;
        padding-right: 35px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
carros = {
    'Toyota': {
        'nome': 'Toyota Supra',
        'descricao': '**Toyota Supra:** Um ícone dos carros esportivos japoneses. Conhecido por seu motor potente, alta capacidade de customização e visual agressivo nas pistas.',
        'preco': 1200.00,
        'categoria': 'Premium',
        'url': 'https://s2-autoesporte.glbimg.com/ldDohn4WnycpnoV011hJFIr4ZH8=/0x0:620x413/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_cf9d035bf26b4646b105bd958f32089d/internal_photos/bs/2020/4/4/x2zcTXRAiIq4xq8UykBg/2019-05-07-toyota-supra-2020-1280-09.jpg'
    },
    'Volkswagen': {
        'nome': 'Volkswagen Fusca',
        'descricao': '**Volkswagen Fusca:** O clássico mais amado do mundo. Marcou gerações com sua mecânica simples, alta durabilidade e design atemporal e simpático.',
        'preco': 350.00,
        'categoria': 'Carros Clássicos',
        'url': 'https://upload.wikimedia.org/wikipedia/commons/e/e3/Volkswagen_Gol_Highline_2023_%2853708009248%29_%28cropped%29.jpg'
    },
    'Hyundai': {
        'nome': 'Hyundai HB20',
        'descricao': '**Hyundai HB20:** Um dos carros mais vendidos do Brasil. Destaca-se pelo design moderno, ótimo pacote de tecnologia e excelente custo-benefício para o dia a dia.',
        'preco': 1400.00,
        'categoria': 'Econômico',
        'url': 'https://t.ctcdn.com.br/9Rr1aLgTPy7HwcMN2Em_x7sYjWQ=/1024x576/smart/i634844.jpeg'
    },
    'General': {
        'nome': 'Chevrolet Impala 1967 (GM)',
        'descricao': '**Chevrolet Impala 1967 (GM):** Um dos muscle cars mais icônicos do mundo. Famoso por sua carroceria fastback, design agressivo e grande presença cultural.',
        'preco': 1500.00,
        'categoria': 'Coleção / Eventos',
        'url': 'https://vintageclassicos.com.br/wp-content/uploads/2023/10/Chevy-Impala-1967-2-1024x768.jpg'
    }
}

st.title('O carro ideal 🚗')
col_busca1, col_busca2 = st.columns(2)

with col_busca1:
    pesquisa = st.text_input('Digite o nome ou modelo do carro:', '')

with col_busca2:
    preco_maximo = st.slider('Preço máximo da diária (R$):', min_value=100, max_value=2000, value=2000, step=50)

marcas_filtradas = []
for marca, dados in carros.items():
    termo = pesquisa.lower()
    nome_valido = termo in dados['nome'].lower() or termo in marca.lower()
    preco_valido = dados['preco'] <= preco_maximo
    
    if nome_valido and preco_valido:
        marcas_filtradas.append(marca)

if not marcas_filtradas:
    st.warning('Nenhum veículo encontrado com os filtros aplicados.')
else:
    col1, col2 = st.columns(2)

    with col1:
        veiculo = st.selectbox('Selecione a marca automotiva desejada:', marcas_filtradas)
        
        info = carros[veiculo]
        st.write(info['descricao'])
        
        col_dados1, col_dados2 = st.columns(2)
        
        with col_dados1:
            st.metric(label=f"Valor da diária ({info['categoria']})", value=f"R$ {info['preco']:.2f}".replace('.', ','))
            dias = st.number_input('Quantidade de diárias:', min_value=1, max_value=30, value=1, step=1)
            
        with col_dados2:
            preco_total = info['preco'] * dias
            st.metric(label="Valor Total Estimado", value=f"R$ {preco_total:.2f}".replace('.', ','))
        
    with col2:
        st.image(info['url'], caption=f'Modelo da {veiculo}', use_container_width=True)