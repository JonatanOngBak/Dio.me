def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados ...
    print(f"Carro incerido com sucesso! {marca}/{modelo}/{ano}/{placa}")


#salvar_carro("Fiat", "Palio", 1999, "ABC-1234")  # esta forma é a menos indicada

#salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ACB1234")  # esta forma é a segunda menos indicada

salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})