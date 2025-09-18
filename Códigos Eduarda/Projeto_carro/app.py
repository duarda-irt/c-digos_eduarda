import streamlit as st 




st.sidebar.title("aluguel de carros")
st.sidebar.image("logo.png")
st.sidebar.write("escolha um carro ideal para voce ")
carros = ["gol", "BMW","toro", "jeep"]
opcao = st.sidebar.selectbox("escolha o modelo do carro :", carros)

st.title("RENTaCAR- aluguel de carro")
st.image(f"{opcao}.png")
st.markdown(f"voce alugou o modelo: {opcao}, aproveite o tempo de uso e volte sempre!")
st.markdown("---")

dias = st.text_input(f"por quantos dias o {opcao} foi alugado?")
km = st.text_input(f"quantos km voce rodou com o {opcao}?")

if opcao == "BMW" :
    diaria = 1500

elif opcao == "gol" :
    diaria = 350

elif opcao == "toro":
    diaria= 850

elif opcao == "jeep":
    diaria= 950

if st.button("calcular"):
    dias = int(dias)
    km = float(km)
    
    total_dias = dias * diaria 
    total_km = km * 0.15
    aluguel_total = total_dias + total_km
st.warning(f'voce alugou o {opcao} por {dias} dias e rodou {km} km. O valor total a pagar é R${aluguel_total:.2f}')