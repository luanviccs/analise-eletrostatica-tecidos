## Apêndice: Código Python para Análise

Abaixo está o código em Python (usando as bibliotecas `pandas`, `matplotlib` e `scipy`) que foi usado para realizar esta análise.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 1. Dados do Experimento
data = {
    'Algodão': [6, 5, 7, 4, 6, 5, 8, 6, 5, 7],
    'Lã': [12, 14, 11, 13, 15, 12, 11, 14, 13, 12],
    'Poliéster': [31, 33, 29, 35, 32, 30, 34, 36, 31, 33],
    'Poliuretano': [45, 49, 42, 51, 47, 46, 44, 52, 48, 49]
}
df = pd.DataFrame(data)

# 2. Análise Descritiva
desc_stats = df.describe().loc[['mean', 'std']].T
print("--- Estatísticas Descritivas ---")
print(desc_stats)

# 3. Visualização de Dados
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

means = df.mean()
errors = df.std()

means.plot(kind='bar', yerr=errors, ax=ax, capsize=5, color=sns.color_palette("viridis", 4))

ax.set_title('Deflexão Média por Tipo de Tecido', fontsize=16, fontweight='bold')
ax.set_ylabel('Ângulo de Deflexão (°)', fontsize=12)
ax.set_xlabel('Tipo de Tecido', fontsize=12)
ax.set_xticklabels(df.columns, rotation=0)
plt.tight_layout()
# plt.savefig('deflexao_media_tecidos.png') # Salva a figura
plt.show()

# 4. Análise Estatística (ANOVA)
f_statistic, p_value = f_oneway(df['Algodão'], df['Lã'], df['Poliéster'], df['Poliuretano'])
print("\n--- Resultado do Teste ANOVA ---")
print(f"Estatística F: {f_statistic:.2f}")
print(f"Valor-p: {p_value}")

if p_value < 0.05:
    print("Conclusão: Rejeitamos a hipótese nula. As diferenças são significativas.")
else:
    print("Conclusão: Não podemos rejeitar a hipótese nula.")

# 5. Teste Post-Hoc de Tukey
df_melt = df.melt(var_name='grupo', value_name='valor')
tukey_results = pairwise_tukeyhsd(endog=df_melt['valor'], groups=df_melt['grupo'], alpha=0.05)

print("\n--- Resultado do Teste de Tukey HSD ---")
print(tukey_results)
