import streamlit as st

st.title("Calculadora de Juros e Multa de Boleto")

input_valor_principal = st.number_input(
    "Valor Principal (R$)", min_value=0.0, format="%.2f"
)
input_taxa_juros = st.number_input("Taxa de Juros (%)", min_value=0.0, format="%.2f")
input_tipo_calculo = st.selectbox("", ["ao mês (a.m.)", "ao dia (a.d.)"])
input_multa = st.number_input("Multa (%)", min_value=0.0, format="%.2f")
input_dias_corridos = st.number_input("Dias Corridos (desde o vencimento)", min_value=0)

if input_tipo_calculo == "ao mês (a.m.)":
    taxa_juros_calculo = input_taxa_juros / 100
    dias_corridos_calculo = input_dias_corridos / 30
else:
    taxa_juros_calculo = input_taxa_juros / 100
    dias_corridos_calculo = input_dias_corridos

juros = round(input_valor_principal * taxa_juros_calculo * dias_corridos_calculo, 2)
multa = round(input_valor_principal * (input_multa / 100), 2)
resultado_final = round(input_valor_principal + juros + multa, 2)

st.write(
    f"**Juros**: {input_valor_principal:.2f} * {taxa_juros_calculo:.4f} * {dias_corridos_calculo:.4f} = `R$ {juros:.2f}`"
)

st.write(
    f"**Multa**: {input_valor_principal:.2f} * ({input_multa:.4f} / {dias_corridos_calculo:.4f}) = `R$ {multa:.2f}`"
)

st.write(
    f"**Valor Final**: {input_valor_principal:.2f} + {juros:.2f} + {multa:.2f} = `R$ {resultado_final:.2f}`"
)

st.markdown(
    """<div style="height:83px;"></div>""",
    unsafe_allow_html=True,
)

st.write(
    """
 **Fórmulas**
- Juros: `Valor Principal * Taxa de Juros * Dias Corridos`
- Multa: `Valor Principal * (Multa / 100)`
- Valor Final: `Valor Principal + Juros + Multa`
"""
)
