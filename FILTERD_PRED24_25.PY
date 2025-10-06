import json
from datetime import datetime

# Input JSON containing predictions up to 2026
input_json_path = r"D:\OMS\brfood\samples_ph\FINALPREDICTIONS\predicted_prices_cleaned_skus.json"

# Output JSON filtered to 2024-2025
output_json_path = r"D:\OMS\brfood\samples_ph\FINALPREDICTIONS\predicted_prices_2025_2026.json"

# Load existing predictions
with open(input_json_path, 'r') as f:
    all_skus = json.load(f)

# Filter predictions to only include dates in 2024-2025
filtered_skus = []

for sku_entry in all_skus:
    filtered_prices = [
        p for p in sku_entry.get('price_updates', [])
        if 2025 <= datetime.fromisoformat(p['predicted_pricechangedate']).year <= 2026
    ]
    if filtered_prices:  # Only keep SKUs that have predictions in this window
        filtered_skus.append({
            'sku': sku_entry['sku'],
            'price_updates': filtered_prices
        })

# Save the filtered JSON
with open(output_json_path, 'w') as f:
    json.dump(filtered_skus, f, indent=4)

print(f"Filtered predictions for 2024-2025 saved to: {output_json_path}")
