# 🔬 Electrostatic Analysis of Fabrics

This project presents a complete data analysis on the electrostatic behavior of different fabrics after friction, using descriptive statistics, data visualization, and hypothesis testing. It was developed as part of the course **Base Experimental das Ciências Naturais (BECN)** at UFABC.

---

## 📌 1. Research Question

**What is the relative ability of different fabrics (Cotton, Wool, Polyester, and Polyurethane) to accumulate electrostatic charge through friction?**

---

## 💡 2. Hypothesis

Based on the **triboelectric series**, our hypothesis is:

- **Polyurethane** will accumulate the highest negative electrostatic charge.
- **Polyester** will be second.
- **Cotton**, being neutral, will accumulate the least (serves as a control).

---

## 🧪 3. Methodology

- **Instrument**: Leaf electroscope.
- **Measurement**: Deflection angle (°) of the aluminum leaves.
- **Interpretation**: The greater the angle, the greater the charge accumulation.

We simulated **10 experiments per fabric**, with variation to reflect realistic experimental errors.

---

## 📊 4. Data Visualization

![Deflection Angle by Fabric Type](grafico_deflexao_tecidos.png)

- Bars represent the **average deflection**.
- Error lines indicate the **standard deviation** for each material.

---

## 📈 5. Descriptive Statistics

| Fabric       | Mean (°) | Standard Deviation (°) |
|--------------|----------|-------------------------|
| Cotton       | 6.0      | 1.25                    |
| Wool         | 12.7     | 1.34                    |
| Polyester    | 32.4     | 2.22                    |
| Polyurethane | 47.3     | 2.98                    |

---

## 🧠 6. Statistical Analysis

### 🔎 ANOVA Test (Analysis of Variance)

- **Null Hypothesis (H₀)**: All groups have the same mean.
- **Result**: p < 0.0001 → **We reject H₀** → There are significant differences.

### 🧪 Tukey HSD Test (Post-Hoc)

| Comparison              | Mean Difference (°) | Significance   |
|-------------------------|---------------------|----------------|
| Cotton vs Wool          | -6.7                | Significant    |
| Cotton vs Polyester     | -26.4               | Significant    |
| Cotton vs Polyurethane  | -41.3               | Significant    |
| Wool vs Polyester       | -19.7               | Significant    |
| Wool vs Polyurethane    | -34.6               | Significant    |
| Polyester vs Polyurethane | -14.9             | Significant    |

---

## ✅ 7. Conclusion

The analysis confirms the initial hypothesis:

**Order of fabric electrification (lowest → highest):**

1. Cotton  
2. Wool  
3. Polyester  
4. Polyurethane

---

## 🛠️ 8. Practical Applications

- **Industrial issue**: Polyurethane accumulates a high charge → risk of electrostatic shock during handling.
- **Suggested solution**: Use gloves made of **cotton** or conductive fabrics like carbon to dissipate the charge.

---

## 🔗 9. Access the Project

- 📂 Repository: [github.com/luanviccs/analise-eletrostatica-tecidos](https://github.com/luanviccs/analise-eletrostatica-tecidos)
- 🌐 Online presentation: [luanviccs.github.io/analise-eletrostatica-tecidos](https://luanviccs.github.io/analise-eletrostatica-tecidos)

---
