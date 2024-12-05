import streamlit as st
from equacao import Equacao
import pandas as pd

class EquacaoUI:
    def main():
        st.header("Equação do 2º grau")
        a = st.text_input("Informe o valor de a")
        b = st.text_input("Informe o valor de b")
        c = st.text_input("Informe o valor de c")
        n = st.text_input("Informe o número de pontos do gráfico", "5")
        if st.button("Calcular"):
            eq = Equacao(float(a), float(b), float(c))
            st.write(f"Delta = {eq.delta()}")
            st.write(f"X1 = {eq.x1()}")
            st.write(f"X2 = {eq.x2()}")     

            px = [] # coordenada x de vários pontos
            py = [] # coordenada y de vários pontos
            x1 = eq.x1() # menor raiz
            x2 = eq.x2() # maior raiz

            if eq.delta() > 0:
                d = x2 - x1
                xmin = x1 - d/2 # limite inferior do gráfico
                xmax = x2 + d/2 # limite superior
            if eq.delta() == 0:
                xmin = 0.5 * x1 # limite inferior do gráfico
                xmax = 1.5 * x1 # limite superior
            if eq.delta() < 0:
                xmin = 0.5*eq.xplano()
                xmax = 1.5*eq.xplano()
            if xmin == 0 and xmax == 0:
                xmin = -5
                xmax = 5

            npontos = int(n)
            d = (xmax-xmin)/npontos
            x = xmin
            while x < xmax:
                px.append(x)
                py.append(eq.y(x))
                x += d
            px.append(xmax)
            py.append(eq.y(xmax))
            #st.write(px)
            #st.write(py)
            dic = { "x" : px, "y" : py }
            chart_data = pd.DataFrame(dic)
            st.line_chart(chart_data, x = "x", y = "y")

