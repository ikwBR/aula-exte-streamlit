import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configuração da página
st.set_page_config(page_title="Plotador de Função Quadrática", layout="centered")

# Título e Descrição
st.title('Gráfico de uma Função de Segundo Grau')
st.markdown(r"""
Esta aplicação plota o gráfico da função:
$$
y = ax^2 + bx + c
$$
Altere os valores na barra lateral para ver o gráfico mudar em tempo real.
""")

# --- Entrada de Dados (Sidebar) ---
st.sidebar.header('Parâmetros')

# Substituindo os inputs manuais por widgets do Streamlit
# 'value' define o valor inicial e 'step' define o incremento das setinhas
a = st.sidebar.number_input("Digite o valor de a:", value=1.0, step=0.5, format="%.2f")
b = st.sidebar.number_input("Digite o valor de b:", value=0.0, step=0.5, format="%.2f")
c = st.sidebar.number_input("Digite o valor de c:", value=0.0, step=0.5, format="%.2f")

# Aviso interativo se 'a' for zero
if a == 0:
    st.sidebar.warning("Com a = 0, a função se torna linear (1º grau).")

# --- Lógica de Cálculo ---
# Gera valores de x
x = np.linspace(-10, 10, 400) 

# Calcula os valores de y
y = a * x**2 + b * x + c

# --- Criação do Gráfico ---
# Usamos 'fig, ax' (Interface Orientada a Objetos) pois é mais estável no Streamlit
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x, y, label=f'y = {a}x² + {b}x + {c}', color='blue')

# Configurações do gráfico
ax.set_title('Visualização do Gráfico')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Eixos centrais
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Ajuste de limites (opcional, para manter o zoom estável)
# ax.set_ylim(-20, 20) 

# --- Exibição ---
st.pyplot(fig)

# Exibe as raízes (bônus)
delta = b**2 - 4*a*c
if a != 0:
    st.divider()
    st.subheader("Informações Adicionais")
    st.write(f"**Delta ($\Delta$):** {delta:.2f}")
