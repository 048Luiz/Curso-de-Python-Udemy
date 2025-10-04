"""
CONSTANTE = 'Variáveis' que não vão mudar
muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 80 # velocidade atual do carro
local_carro = 90 # local que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 10 #A distância onde o radar pega

velocidade_carro_radar = velocidade > RADAR_1
carro_passou_radar = (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado = carro_passou_radar and velocidade_carro_radar

if velocidade_carro_radar:
    print('O carro excedeu a velocidade permitida!')
else: 
    print('O carro passou dentro da velocidade permitida!')

if carro_multado:
    print('O carro foi multado!')
