import matplotlib.pyplot as plt
import numpy as np

# Years from 2025 to 2033
years = np.arange(2025, 2034)

# Initial market value in 2025 ($17 billion)
initial_value = 17  
growth_rate = 0.067  # Compound annual growth rate (CAGR) 6.7%

# Calculate market values using compound growth
market_values = initial_value * (1 + growth_rate) ** (years - 2025)


plt.figure(figsize=(10, 6))
bars = plt.bar(years, market_values, color=plt.cm.Blues(np.linspace(0, 1, len(years))))

plt.title(f'Logistics Software Market (2025-2033) - CAGR {growth_rate*100:.1f}%', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Market Value (Billion USD)', fontsize=12)


for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.1f}', ha='center', va='bottom', fontsize=10)

plt.xticks(years, [str(year) for year in years])

plt.show()
