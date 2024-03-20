import matplotlib.pyplot as plt
import pandas as pd

menu_items = ['Hot Chocolate', 'Mocha', 'Latte', 'Americano', 'Cappuccino', 'Tea', 'Panini', 'Toast', 'Croissant', 'Buttered Roll', 'Muffin']
data = [37, 33, 32, 31, 28, 23, 6, 4, 3, 2, 1]

df = pd.DataFrame({'Menu Items': menu_items, 'Count': data})

sorted_df = df.sort_values(by='Count', ascending=False)

plt.figure(figsize=(10, 6))
bars = plt.bar(sorted_df['Menu Items'], sorted_df['Count'], color='skyblue')

plt.xlabel('Menu Items')
plt.ylabel('Count')
plt.title('Monday\nCount of Menu Items', fontweight='bold')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()