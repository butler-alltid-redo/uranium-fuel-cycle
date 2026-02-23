import matplotlib.pyplot as plt
import numpy as np

# Parameters
tails_assay = np.linspace(0.1, 0.5, 100)  # Tails assay in percentage
enrichment_cost = 1 / tails_assay  # Hypothetical inversely proportional relationship
uranium_needed = 1 / (1 - tails_assay)  # Hypothetical inverse relationship with tails assay

# Create the figure
plt.figure(figsize=(12, 8))

# SWU vs. Tails Assay
plt.subplot(2, 1, 1)
plt.plot(tails_assay, enrichment_cost, label='SWU vs. Tails Assay')
plt.xlabel('Tails Assay (%)')
plt.ylabel('Separative Work Units (SWU)')
plt.title('SWU and Uranium Needs in Tails Assay Relationship')
plt.legend()
plt.grid()

# Uranium Needed vs. Tails Assay
plt.subplot(2, 1, 2)
plt.plot(tails_assay, uranium_needed, label='Uranium Needed vs. Tails Assay', color='orange')
plt.xlabel('Tails Assay (%)')
plt.ylabel('Uranium Needed')
plt.legend()
plt.grid()

# Save the figure
plt.tight_layout()
plt.savefig('balance_visualization.png')
plt.show()

# Uranium Needed vs. SWU
plt.figure(figsize=(10, 6))
plt.plot(enrichment_cost, uranium_needed, label='Uranium Needed vs. SWU', color='green')
plt.xlabel('Separative Work Units (SWU)')
plt.ylabel('Uranium Needed')
plt.title('Uranium Needed as a Function of SWU')
plt.legend()
plt.grid()

# Save the figure
plt.savefig('uranium_vs_swu.png')
plt.show()