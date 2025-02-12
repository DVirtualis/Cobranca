import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações de tema e estilo (mantenha igual às suas páginas originais)
# ... [Cole aqui todo o código CSS e de temas das suas páginas originais] ...

# Configuração das taxas de juros das máquinas (mantido do seu código original)
TAXAS = {
    "Point": {2: 0.0442, 3: 0.0532, 4: 0.0622, 5: 0.0712, 6: 0.0802, 7: 0.0892, 8: 0.0982, 9: 0.1072, 10: 0.1162, 11: 0.1252, 12: 0.1342},
    "Link de Pagamento": {"Débito": 0.015, "Crédito a Vista": 0.0310, "Pix":0.0049, 2: 0.0439, 3: 0.0514, 4: 0.0589, 5: 0.0664, 6: 0.0739, 7: 0.0818, 8: 0.0893, 9: 0.0968, 10: 0.1043, 11: 0.1118, 12: 0.1193},
    "Visa": {"Crédito a Vista": 0.0235, "Débito a Vista": 0.0142, "QRCode pelo App": 0.0075, 2: 0.0269, 3: 0.0269, 4: 0.0269, 5: 0.0269, 6: 0.0269, 7: 0.0300, 8: 0.0300, 9: 0.0300, 10: 0.0300, 11: 0.0300, 12: 0.0300, 13: 0.0270, 14: 0.0270, 15: 0.0270, 16: 0.0270, 17: 0.0270, 18: 0.0270},
    "Visa Crédito com Juros": {2: 0.0205, 3: 0.0205, 4: 0.0205, 5: 0.0205, 6: 0.0205, 7: 0.0205, 8: 0.0205, 9: 0.0205, 10: 0.0205, 11: 0.0205, 12: 0.0205}
}

# Funções de cálculo de amortização (adaptadas para usar as taxas das máquinas)
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

# Interface unificada
def main():
    st.title("Calculadora Financeira Integrada")
    
    # Seção de seleção de taxa
    with st.expander("Configurações da Taxa", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            tipo_parcelamento = st.selectbox("Operadora", options=list(TAXAS.keys()))
        with col2:
            num_parcelas = st.selectbox(
                "Forma de Pagamento",
                options=list(TAXAS[tipo_parcelamento].keys()),
                format_func=lambda x: f"{x}X" if isinstance(x, int) else x
            )
    
    # Seção de parâmetros do financiamento
    with st.expander("Parâmetros do Financiamento", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            valor = st.number_input("Valor Financiado (R$)", min_value=0.01, value=10000.0, step=100.0)
        with col2:
            metodo = st.selectbox("Método de Amortização", ["Price", "SAC", "SACRE", "MEJS"])
        with col3:
            meses = st.slider("Parcelas", min_value=1, max_value=18, value=12)
    
    # Obtenção da taxa
    if isinstance(num_parcelas, int):
        taxa = TAXAS[tipo_parcelamento][num_parcelas]
    else:
        taxa = TAXAS[tipo_parcelamento][num_parcelas]
    
    # Cálculo e exibição
    if st.button("Calcular"):
        try:
            if metodo == "Price":
                parcela = calcular_price(valor, taxa, meses)
            elif metodo == "SAC":
                parcelas = calcular_sac(valor, taxa, meses)
                parcela = parcelas[0]
            elif metodo == "SACRE":
                parcelas = calcular_sacre(valor, taxa, meses)
                parcela = parcelas[0]
            elif metodo == "MEJS":
                parcela = calcular_mejs(valor, taxa, meses)
            
            st.success(f"Valor da Parcela ({metodo}): R$ {parcela:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            
            # Tabela de amortização
            if metodo in ["Price", "SAC", "SACRE"]:
                df = pd.DataFrame({
                    "Mês": range(1, meses+1),
                    "Parcela": parcelas if metodo != "Price" else [parcela]*meses
                })
                fig = px.line(df, x="Mês", y="Parcela", title="Evolução das Parcelas")
                st.plotly_chart(fig)
                
        except Exception as e:
            st.error(f"Erro no cálculo: {str(e)}")

if __name__ == "__main__":
    main()