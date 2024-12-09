import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados do arquivo CSV (inserir path/caminho aqui)
arquivo_csv = "C:\Exsto\XT403-Software\Ensaios\Irradiação\TX=tipo L,RX=plano terra ambas verticais.csv"
dados = pd.read_csv(arquivo_csv, skiprows=4, sep=',', encoding='latin-1')  # Pula as 4 primeiras linhas

# Renomear as colunas para facilitar o uso
dados.columns = ["Angulo", "GVert_dB", "GHoriz_dB"]

# Converter ângulos para radianos (necessário para gráficos polares)
dados["Angulo_rad"] = np.radians(dados["Angulo"])

# Criar figura para os gráficos
fig, axs = plt.subplots(1, 2, subplot_kw={'projection': 'polar'}, figsize=(12, 6))

# Gráfico polar para o ganho vertical
axs[1].plot(dados["Angulo_rad"], dados["GVert_dB"], color="blue", label="Ganho Vertical (dB)")
axs[1].set_title("Diagrama de Irradiação Vertical", va='bottom')
axs[1].grid(True)
axs[1].legend()

# Gráfico polar para o ganho horizontal
axs[0].plot(dados["Angulo_rad"], dados["GHoriz_dB"], color="red", label="Ganho Horizontal (dB)")
axs[0].set_title("Diagrama de Irradiação Horizontal", va='bottom')
axs[0].grid(True)
axs[0].legend()

# Ajustar layout
plt.tight_layout()

# Exibir os gráficos
plt.show()