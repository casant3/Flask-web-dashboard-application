import matplotlib.pyplot as plt
import pandas as pd

menu_items = ['Hot Chocolate', 'Mocha', 'Latte', 'Americano', 'Cappuccino', 'Tea', 'Panini', 'Croissant', 'Buttered Roll', 'Muffin', 'Stroopwafel']
data = [32, 27, 24, 23, 33, 38, 1, 3, 3, 3, 1]

df = pd.DataFrame({'Menu Items': menu_items, 'Count': data})

sorted_df = df.sort_values(by='Count', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(sorted_df['Menu Items'], sorted_df['Count'], color='skyblue')

plt.xlabel('Menu Items')
plt.ylabel('Count')
plt.title('Wednesday\nCount of Menu Items', fontweight='bold')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()