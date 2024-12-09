import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados do arquivo CSV (inserir path/caminho aqui)
arquivo_csv = r"C:\Exsto\XT403-Software\Ensaios\Irradiação\TR=helicoidal,RX=circular.csv"
dados = pd.read_csv(arquivo_csv, skiprows=4, sep=',', encoding='latin-1')  # Pula as 4 primeiras linhas

# Renomear as colunas para facilitar o uso
dados.columns = ["Angulo", "GVert_dB", "GHoriz_dB"]

# Converter ângulos para radianos (necessário para gráficos polares)
dados["Angulo_rad"] = np.radians(dados["Angulo"])

# Converter valores de dB para escala linear
dados["GVert_linear"] = 10**(dados["GVert_dB"] / 10)
dados["GHoriz_linear"] = 10**(dados["GHoriz_dB"] / 10)

# Criar figura para os gráficos
fig, axs = plt.subplots(2, 2, subplot_kw={'projection': 'polar'}, figsize=(12, 12))

# Gráfico polar para o ganho vertical em dB
axs[0, 0].plot(dados["Angulo_rad"], dados["GVert_dB"], color="blue", label="Ganho Vertical (dB)")
axs[0, 0].set_title("Diagrama de Irradiação Vertical (dB)", va='bottom')
axs[0, 0].grid(True)
axs[0, 0].legend()

# Gráfico polar para o ganho horizontal em dB
axs[0, 1].plot(dados["Angulo_rad"], dados["GHoriz_dB"], color="red", label="Ganho Horizontal (dB)")
axs[0, 1].set_title("Diagrama de Irradiação Horizontal (dB)", va='bottom')
axs[0, 1].grid(True)
axs[0, 1].legend()

# Gráfico polar para o ganho vertical em escala linear
axs[1, 0].plot(dados["Angulo_rad"], dados["GVert_linear"], color="blue", label="Ganho Vertical (Linear)")
axs[1, 0].set_title("Diagrama de Irradiação Vertical (Linear)", va='bottom')
axs[1, 0].grid(True)
axs[1, 0].legend()

# Gráfico polar para o ganho horizontal em escala linear
axs[1, 1].plot(dados["Angulo_rad"], dados["GHoriz_linear"], color="red", label="Ganho Horizontal (Linear)")
axs[1, 1].set_title("Diagrama de Irradiação Horizontal (Linear)", va='bottom')
axs[1, 1].grid(True)
axs[1, 1].legend()

# Ajustar layout
plt.tight_layout()

# Exibir os gráficos
plt.show()
