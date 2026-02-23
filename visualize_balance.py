import matplotlib.pyplot as plt
import numpy as np

# Parameters
tails_assay = np.linspace(0.1, 0.5, 100)  # Tails assay in percentage
enrichment_cost = 1 / tails_assay  # Hypothetical inversely proportional relationship

# Plot
plt.figure(figsize=(10, 6))
plt.plot(tails_assay, enrichment_cost, label='SWU vs. Tails Assay')
plt.xlabel('Tails Assay (%)')
plt.ylabel('Separative Work Units (SWU)')
plt.title('Balance Between Tails Assay and SWU in Uranium Fuel Cycle')
plt.legend()
plt.grid()

# Save figure
plt.savefig('balance_visualization.png')
plt.show()