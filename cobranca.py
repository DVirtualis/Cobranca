import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações de tema e estilo (mantenha igual às suas páginas originais)

def page_cobranca():
    # Paleta de cores atualizada
    COLORS = ['##0095fb', '#7C3AED', '#3B82F6', '#10B981', '#EF4444', '#F59E0B']
    COLORS_DARK = ['#1b4f72', '#d35400', '#145a32', '#7b241c', '#5b2c6f']

    # Configuração do tema no session_state
    ms = st.session_state
    if "themes" not in ms:
        ms.themes = {
            "current_theme": "light",
            "light": {
                "theme.base": "light",
                "theme.backgroundColor": "#F3F4F6",  # Cor de fundo
                "theme.primaryColor": "#383bf8",     # Cor primária (botões, links)
                "theme.secondaryBackgroundColor": "#F3F4F6",  # Cor de fundo secundária
                "theme.textColor": "#111827",        # Cor do texto
                "button_face": "Modo Escuro 🌙",     # Texto do botão
                "colors": COLORS,                    # Paleta de cores
            },
            "dark": {
                "theme.base": "dark",
                "theme.backgroundColor": "#1F2937",  # Cor de fundo
                "theme.primaryColor": "#70c4fc",     # Cor primária (botões, links)
                "theme.secondaryBackgroundColor": "#1f2937",  # Cor de fundo secundária
                "theme.textColor": "#efefef",        # Cor do texto
                "button_face": "Modo Claro 🌞",      # Texto do botão
                "colors": COLORS_DARK,               # Paleta de cores
            }
        }

    # Função para alternar o tema
    def change_theme():
        current_theme = ms.themes["current_theme"]
        ms.themes["current_theme"] = "dark" if current_theme == "light" else "light"
        ms.themes["refreshed"] = True  # Atualiza o estado

    # Configuração do tema atual
    current_theme = ms.themes["current_theme"]
    theme_config = ms.themes[current_theme]

    # Botão de alternar tema
    if st.button(theme_config["button_face"], on_click=change_theme):
        pass


    # Aplicar as cores do tema atual
    colors = theme_config["colors"]

    # Injetar CSS personalizado com base no tema atual
    st.markdown(
        f"""
        <style>
        /* ===== [CONFIGURAÇÃO GLOBAL] ===== */
        html, body, .stApp {{
            background-color: {theme_config["theme.backgroundColor"]};
            color: {theme_config["theme.textColor"]};
        }}

        /* ===== [COMPONENTES DO STREAMLIT] ===== */
        /* Ajuste para Selectbox */
        .stSelectbox > div > div {{
            background-color: {theme_config["theme.secondaryBackgroundColor"]} !important;
            color: {theme_config["theme.textColor"]} !important;
            border-radius:5px;
            border: 2px solid {theme_config["theme.primaryColor"]} !important; /* Cor oposta do tema */
        }}

        .stSelectbox > div > div:hover {{
            background-color: {theme_config["theme.primaryColor"]} !important;
            color: #FFFFFF !important;
                border: 2px solid {theme_config["theme.textColor"]} !important; /* Cor oposta do tema */
        border-radius: 5px; /* Bordas arredondadas */
        transition: border-color 0.3s ease-in-out; /* Suaviza a transição */



        }}

        /* Placeholder ajustado */
        .stSelectbox > div > div::placeholder {{
            color: {theme_config["theme.textColor"]} !important;
            opacity: 0.7;
        }}

        
        /* ===== [CABEÇALHOS E TÍTULOS] ===== */
        h1, h2, h3, h4, h5, h6,
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
        .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {{
            color: {theme_config["theme.textColor"]} !important;
        }}

    /* ===== [COMPONENTES PRINCIPAIS] ===== */
        .stDataFrame, .stMetric, .stJson, .stAlert,
        .stExpander .stMarkdown, .stTooltip{{
            color: {theme_config["theme.textColor"]} !important;
        }}
        
        
        /* ===== [SIDEBAR] ===== */
        .stSidebar {{
            background-color: {theme_config["theme.secondaryBackgroundColor"]} !important;
            border-radius: 15px;
            padding: 10px;
        }}

        .nav-link.active {{
        background-color: {theme_config["theme.primaryColor"]} !important;
        color: #FFFFFF !important; /* Texto branco para contraste */
        font-weight: bold !important; /* Texto em negrito para destaque */
        border-radius: 8px; /* Bordas arredondadas */
        padding: 10px; /* Espaçamento interno */
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra para destaque */
    }}

    /* Ícones dentro do item ativo */
    .nav-link.active .icon {{
        color: #FFFFFF !important; /* Altera a cor do ícone no item ativo */
    }}

    /* Estilo para itens inativos */
    .nav-link {{
        color: {theme_config["theme.textColor"]} !important; /* Cor do texto do tema */
        transition: background-color 0.3s, color 0.3s; /* Transição suave ao passar o mouse */
    }}

    .nav-link:hover {{
        background-color: {theme_config["theme.primaryColor"]}33; /* Cor primária translúcida */
        color: {theme_config["theme.primaryColor"]} !important; /* Texto na cor primária */
    }}
        /* Ajusta texto e fundo nos botões */
        .stButton>button {{
            background-color: {theme_config["theme.primaryColor"]} !important;
            color: #FFFFFF !important;
        }}

        /* ===== [GENÉRICO] ===== */
        /* Ajusta elementos dinâmicos */
        .st-emotion-cache-1cj4yv0,
        .st-emotion-cache-efbu8t {{
            background-color: {theme_config["theme.secondaryBackgroundColor"]} !important;
        
        }}
        
        /* ===== [COMPONENTES ESPECÍFICOS] ===== */
        .stMultiSelect span[data-baseweb="tag"] {{
            background-color: {theme_config["theme.primaryColor"]} !important;
            color: white !important;
        }}

        .stButton>button p {{
            color: white !important;
        }}

        .stElementToolbarButton  {{
                color: white !important;
            }}
        
        
        div[data-testid="stMetricValue"] {{
            color: {theme_config["theme.textColor"]} !important;
        }}

        #[class*="stMetric"]
        {{
            color: {theme_config["theme.textColor"]} !important;
        }}
        
        [class*="st-emotion-cache"] {{
            color: {theme_config["theme.primaryColor"]} !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )
 # Função de formatação monetária
    def formatar_moeda(valor):
        """Formata valores monetários no padrão brasileiro"""
        return f"R$ {valor: ,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    # Configuração das taxas de juros das máquinas (mantido do seu código original)
    TAXAS = {
        "Point": {2: 0.0442, 3: 0.0532, 4: 0.0622, 5: 0.0712, 6: 0.0802, 7: 0.0892, 8: 0.0982, 9: 0.1072, 10: 0.1162, 11: 0.1252, 12: 0.1342},
        "Link de Pagamento": {"Débito": 0.015, "Crédito a Vista": 0.0310, "Pix":0.0049, 2: 0.0439, 3: 0.0514, 4: 0.0589, 5: 0.0664, 6: 0.0739, 7: 0.0818, 8: 0.0893, 9: 0.0968, 10: 0.1043, 11: 0.1118, 12: 0.1193},
        "Stone - Visa": {"Crédito a Vista": 0.0235, "Débito a Vista": 0.0142, "QRCode pelo App": 0.0075, 2: 0.0269, 3: 0.0269, 4: 0.0269, 5: 0.0269, 6: 0.0269, 7: 0.0300, 8: 0.0300, 9: 0.0300, 10: 0.0300, 11: 0.0300, 12: 0.0300, 13: 0.0270, 14: 0.0270, 15: 0.0270, 16: 0.0270, 17: 0.0270, 18: 0.0270},
        "Stone - Visa Crédito com Juros": {2: 0.0205, 3: 0.0205, 4: 0.0205, 5: 0.0205, 6: 0.0205, 7: 0.0205, 8: 0.0205, 9: 0.0205, 10: 0.0205, 11: 0.0205, 12: 0.0205}
    }

     # Funções de cálculo
    def calcular_price(pv, taxa_mensal, meses):
        if taxa_mensal == 0: return pv / meses
        return (pv * taxa_mensal) / (1 - (1 + taxa_mensal)**-meses)

    def calcular_sac(pv, taxa_mensal, meses):
        amortizacao = pv / meses
        return [amortizacao + (pv - amortizacao * i) * taxa_mensal for i in range(meses)]

    def calcular_sacre(pv, taxa_mensal, meses):
        saldo = pv
        amort_base = pv / meses
        return [amort_base * (1 + taxa_mensal)**(i+1) + (saldo - amort_base * i) * taxa_mensal for i in range(meses)]

    def calcular_mejs(pv, taxa_mensal, meses):
        total_juros = pv * taxa_mensal * meses
        return (pv + total_juros) / meses

    # Interface
    st.title("📈 Calculadora Financeira Integrada")
    st.markdown("---")
    
    modo_calculo = st.radio(
        "**Selecione o Tipo de Cálculo:**", 
        ["🏦 Financiamento", "💳 Parcelamento Simples"],
        horizontal=True,
        key="modo_calculo_radio"
    )
    
    with st.expander("⚙️ Configurações da Taxa", expanded=True):
        col1, col2 = st.columns([2, 3])
        with col1:
            tipo_parcelamento = st.selectbox(
                "**Operadora**", 
                options=list(TAXAS.keys()),
                key="operadora_select"
            )
        with col2:
            num_parcelas = st.selectbox(
                "**Forma de Pagamento**",
                options=list(TAXAS[tipo_parcelamento].keys()),
                format_func=lambda x: f"{x}X" if isinstance(x, int) else x,
                key="forma_pagamento"
            )
            # Mostra a taxa selecionada em formato de card
            taxa_selecionada = TAXAS[tipo_parcelamento][num_parcelas]
            if tipo_parcelamento in ["Point", "Link de Pagamento"] and isinstance(num_parcelas, int):
                taxa_selecionada = taxa_selecionada / num_parcelas  # Taxa total → mensal
                

            st.markdown(
                f"""
                <div style="
                    background-color: {theme_config['theme.secondaryBackgroundColor']};
                    padding: 0.75rem;
                    border-radius: 10px;
                    border: 1px solid {theme_config['theme.primaryColor']};
                    margin-top: 1rem;
                    text-align: center;
                ">
                    <p style="margin: 0; font-size: 1.1rem; color: {theme_config['theme.textColor']}">
                        <strong>Taxa Mensal Aplicada:</strong> {taxa_selecionada:.2%}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
    
    # Inicialização segura das variáveis
    valor = 0.0
    desconto = 0.0
    meses = 1
    
    if modo_calculo == "🏦 Financiamento":
        with st.expander("📊 Parâmetros do Financiamento", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                valor = st.number_input("**Valor Bruto (R$)**", 
                                      min_value=0.01, 
                                      value=10000.0, 
                                      step=100.0,
                                      key="valor_bruto")
                desconto = st.number_input("**Desconto (R$)**", 
                                         min_value=0.0, 
                                         max_value=valor if valor > 0 else 0.0, 
                                         value=0.0, 
                                         step=100.0,
                                         key="desconto")
            with col2:
                percentual = (desconto / valor * 100) if valor > 0 else 0.0
                st.metric("**Percentual de Desconto**", f"{percentual:.2f}%")
                st.metric("**Valor Líquido**", formatar_moeda(valor - desconto))
            
            metodo = st.selectbox("**Método de Amortização**",
                                ["Price", "SAC", "SACRE", "MEJS"],
                                key="metodo_amortizacao")
            meses = num_parcelas if isinstance(num_parcelas, int) else 1
    else:
        with st.expander("💸 Parâmetros do Parcelamento", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                valor = st.number_input("**Valor Total (R$)**", 
                                      min_value=0.01, 
                                      value=10000.0, 
                                      step=100.0,
                                      key="valor_total")
            with col2:
                meses = num_parcelas if isinstance(num_parcelas, int) else 1
                st.metric("**Parcelas**", meses if isinstance(num_parcelas, int) else "À Vista")

    st.markdown("---")
    calcular_btn = st.button("🔄 Calcular", type="primary")

    if calcular_btn:
        try:
            tabela = []
            taxa = TAXAS[tipo_parcelamento][num_parcelas]
            if tipo_parcelamento in ["Point", "Link de Pagamento"] and isinstance(num_parcelas, int):
                taxa = taxa / num_parcelas  
                
            valor_base = valor - desconto 
            if modo_calculo == "🏦 Financiamento":
                if metodo == "Price":
                    parcela = calcular_price(valor_base, taxa, meses)
                    saldo = valor_base
                    for i in range(1, meses+1):
                        juros = saldo * taxa
                        amort = parcela - juros
                        saldo -= amort
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Taxa Mensal": taxa_selecionada,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0)
                        })
                
                elif metodo == "SAC":
                    parcelas = calcular_sac(valor_base, taxa, meses)
                    saldo = valor_base
                    amort = valor_base / meses
                    for i, parcela in enumerate(parcelas, 1):
                        juros = saldo * taxa
                        saldo -= amort
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Taxa Mensal": taxa_selecionada,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0)
                        })
                
                elif metodo == "SACRE":
                    parcelas = calcular_sacre(valor_base, taxa, meses)
                    saldo = valor_base
                    amort_base = valor_base / meses
                    fator = 1 + taxa
                    for i, parcela in enumerate(parcelas, 1):
                        juros = saldo * taxa
                        amort = amort_base * (fator**i)
                        saldo -= amort
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Taxa Mensal": taxa_selecionada,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0)
                        })
                
                elif metodo == "MEJS":
                    parcela = calcular_mejs(valor_base, taxa, meses)
                    saldo = valor_base
                    amort = valor_base / meses
                    for i in range(1, meses+1):
                        juros = valor_base * taxa
                        saldo -= amort
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Taxa Mensal": taxa_selecionada,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0)
                            
                        })

                
                # Adicionar total pago
                total_pago = 0
                for item in tabela:
                    total_pago += item["Parcela"]
                    item["Total Pago"] = total_pago
                
                # Detalhes do cálculo
                with st.expander("🧮 Detalhes do Cálculo", expanded=False):
                    if metodo == "Price":
                        st.markdown(f"""
                        **Fórmula Price:**  
                        `P = (PV * i) / (1 - (1 + i)^-n)`  
                        
                        **Valores Aplicados:**  
                        - PV (Valor Presente) = {formatar_moeda(valor_base).replace('$', '\\$')}  
                        - i (Taxa Mensal) = {taxa:.4%}  
                        - n (Períodos) = {meses}  
                        
                        **Cálculo:**  
                        ```python
                        P = ({formatar_moeda(valor_base).replace('$', '\\$')} * {taxa:.4%}) 
                        / (1 - (1 + {taxa:.4%})^-{meses})
                        = {formatar_moeda(parcela).replace('$', '\\$')}
                        ```
                        """)
                    
                    elif metodo == "SAC":
                        st.markdown(f"""
                        **Fórmula SAC:**  
                        `Amortização = PV / n`  
                        `Juros = Saldo Devedor * i`  
                        `Parcela = Amortização + Juros`  
                        
                        **Parâmetros:**  
                        - Amortização Constante = {formatar_moeda(valor_base/meses).replace('$', '\\$')}  
             
                        """)
                    
                    elif metodo == "SACRE":
                        st.markdown(f"""
                        **Fórmula SACRE:**  
                        `Fator de Correção = 1 + i`  
                        `Amortização = (PV/n) * (1 + i)^período`  
                        
                        **Componentes:**  
                        - Fator Mensal = {1 + taxa:.5f}  
                        - Amortização Base = {formatar_moeda(valor_base/meses).replace('$', '\\$')} 
                       
                        """)
                    
                    elif metodo == "MEJS":
                        total_juros = valor_base * taxa * meses
                        st.markdown(f"""
                        **Fórmula MEJS:**  
                        `Total Juros = PV * i * n`  
                        `Parcela = (PV + Total Juros) / n`  
                        
                        **Cálculo Direto:**  
                        - Juros Totais = {formatar_moeda(total_juros).replace('$', '\\$')}  
                        - Parcela = ({formatar_moeda(valor_base).replace('$', '\\$')} + {formatar_moeda(total_juros).replace('$', '\\$')}) / {meses}  
                                          
                        """)

            else:  # Parcelamento Simples
                if isinstance(num_parcelas, int):
                    total_juros = valor * taxa * meses
                    valor_parcela = (valor + total_juros) / meses
                else:
                    total_juros = valor * taxa
                    valor_parcela = valor + total_juros
                
                for i in range(1, meses + 1):
                    tabela.append({
                        "Mês": i,
                        "Parcela": valor_parcela,
                        "Juros": total_juros / meses if isinstance(num_parcelas, int) else total_juros,
                        "Taxa Mensal": taxa_selecionada,
                        "Total Pago": valor_parcela * i
                    })
                
                
                # Detalhes do cálculo
                with st.expander("🧮 Detalhes do Cálculo", expanded=False):
                    if isinstance(num_parcelas, int):
                        st.markdown(f"""
                        **Fórmula Parcelado:**  
                        `Total Juros = Valor * Taxa * Parcelas`  
                        `Valor Parcela = (Valor + Total Juros) / Parcelas`  
                        
                        **Aplicação:**  
                        1. Total Juros = {formatar_moeda(valor).replace('$', '\\$')} * {taxa:.4%} * {meses} = {formatar_moeda(total_juros).replace('$', '\\$')}  
                        2. Valor Parcela = ({formatar_moeda(valor).replace('$', '\\$')} + {formatar_moeda(total_juros).replace('$', '\\$')}) / {meses}  
                        """)
                    else:
                        st.markdown(f"""
                        **Fórmula à Vista:**  
                        `Valor Total = Valor * (1 + Taxa)`  
                        
                        **Cálculo:**  
                        {formatar_moeda(valor).replace('$', '\\$')} * (1 + {taxa:.4%}) = {formatar_moeda(valor_parcela).replace('$', '\\$')}  
                        """)

            # Exibição dos resultados
            if tabela:
                df = pd.DataFrame(tabela)
                df['Mês'] = df['Mês'].astype(int)

                if 'Total Pago' not in df.columns:
                    df['Total Pago'] = df['Parcela'].cumsum()

                # Configurar colunas
                cols = ["Mês", "Parcela", "Juros", "Taxa Mensal","Total Pago"]
                if modo_calculo == "🏦 Financiamento":
                    cols.insert(3, "Amortização")
                    cols.insert(4, "Saldo Devedor")
                    

                st.markdown("### 📑 Detalhamento do Parcelamento")
                st.dataframe(
                df[cols].style.format({
                    # Formatação específica para cada coluna
                    'Taxa Mensal': lambda x: f"{x:.2%}",  # Percentual (ex: 5.00%)
                    **{  # Formata as demais colunas como moeda (exceto Taxa Mensal)
                        col: lambda x: formatar_moeda(x) 
                        for col in cols[1:] 
                        if col != 'Taxa Mensal'
                    }
                })
                .applymap(lambda x: 'color: #2ecc71;', subset=['Parcela'])
                .applymap(lambda x: 'color: #e74c3c;', subset=['Juros'])
                .applymap(lambda x:  f"{x:.2%}" 'color: #366666;', subset=['Taxa Mensal'])
                .applymap(lambda x: 'color: #3498db;', subset=['Total Pago']),
                use_container_width=True,hide_index=True,
                height=400
            )

                # Gráfico
                fig = px.line(
                    df, 
                    x="Mês", 
                    y="Parcela",
                    title="📈 Evolução das Parcelas",
                    markers=True,
                    color_discrete_sequence=["#2ecc71"]
                )
                fig.update_layout(
                    xaxis_title="Mês",
                    yaxis_title="Valor da Parcela",
                    xaxis=dict(tickmode='linear', dtick=1)
                )
                st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"## ❌ Erro no cálculo: {str(e)}")