import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('gasolina.csv')

# Gerar o gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')
plt.title('Preço da Gasolina nos Primeiros 10 Dias de Julho de 2021')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.legend(['Preço da Gasolina'], loc='upper right')
plt.grid(True)
plt.savefig('gasolina.png')
plt.show()
