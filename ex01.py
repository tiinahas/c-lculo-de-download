# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps)
# Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# tamanho_arquivo: armazena o tamanho do arquivo para download em MB informado pelo usuário.

# velocidade_internet: armazena a velocidade da internet em Mbps informada pelo usuário.

# tamanho_em_bits: armazena o tamanho do arquivo para download em bits, calculado a partir do tamanho do arquivo em MB. A constante 8 é usada para converter bytes em bits e as constantes 1024 * 1024 são usadas para converter megabytes em bytes.

# tempo_em_segundos: armazena o tempo aproximado de download em segundos, calculado a partir da divisão do tamanho do arquivo em bits pela velocidade da internet em Mbps. As constantes 1024 * 1024 são usadas para converter Mbps em bits por segundo.

# tempo_em_minutos: armazena o tempo aproximado de download em minutos, calculado a partir da divisão do tempo de download em segundos por 60 (número de segundos em um minuto).

tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_internet = float(input("Digite a velocidade da sua internet em Mbps: "))

tamanho_em_bits = tamanho_arquivo * 8 * 1024 * 1024
tempo_em_segundos = tamanho_em_bits / (velocidade_internet * 1024 * 1024)
tempo_em_minutos = tempo_em_segundos / 60

print(f"O tempo aproximado de download é de {tempo_em_minutos:.2f} minutos.")
