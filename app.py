import streamlit as st

st.title("Calculadora de Juros e Multa de Boleto")

input_valor_principal = st.number_input(
    "Valor Principal (R$)", min_value=0.0, format="%.2f"
)
input_taxa_juros = st.number_input("Taxa de Juros (%)", min_value=0.0, format="%.2f")
input_tipo_calculo = st.selectbox("Tipo de Cálculo", ["ao mês (a.m.)", "ao dia (a.d.)"])
input_multa = st.number_input("Multa (%)", min_value=0.0, format="%.2f")
input_dias_corridos = st.number_input("Dias Corridos", min_value=0)

if input_tipo_calculo == "ao mês (a.m.)":
    taxa_juros_calculo = input_taxa_juros / 100
    dias_corridos_calculo = input_dias_corridos / 30
else:
    taxa_juros_calculo = input_taxa_juros / 100
    dias_corridos_calculo = input_dias_corridos

juros = round(input_valor_principal * taxa_juros_calculo * dias_corridos_calculo, 2)
multa = round(input_valor_principal * (input_multa / 100), 2)
resultado_final = round(input_valor_principal + juros + multa, 2)

st.write("---")
st.write("**Resultados**")
st.write(
    f"{input_valor_principal:.2f} + {juros:.2f} + {multa:.2f} = {resultado_final:.2f}"
)

st.write("**Juros:**")
st.write(f"R$ {juros:.2f}")
st.write("**Multa**")
st.write(f"R$ {multa:.2f}")

st.write("**Valor Final**")
st.write(f"R$ {resultado_final:.2f}")
