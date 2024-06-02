velocidade = 62
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_acima = velocidade > RADAR_1
carro_range_do_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <= (LOCAL_1 + RADAR_RANGE)

if carro_range_do_radar and \
velocidade_acima:
    print('Carro multado.')