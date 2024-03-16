"""
CONSTANTE = "variáveis" que não vão mudar e são escritas em MAIUSCULO
muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61     # Velocidade atual do carro
local_carro = 100   # Local em que o carro está na estrada

RADAR_1 = 60    # Velocidade máxima do radar 1
LOCAL_1 = 100   # Local onde o radar 1 esta
RADAR_RANGE = 1 # A distância one o radar pega

# Código depois
vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_no_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_no_radar_1 and vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print('A velocidade do carro passou do radar 1')

if carro_passou_no_radar_1:
    print('Carro passou no radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')

'''
# Código antes
if velocidade > RADAR_1:
    print('Velocidaede do carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('Carro multado em radar 1')
'''
