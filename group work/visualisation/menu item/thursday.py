import matplotlib.pyplot as plt
import pandas as pd

menu_items = ['Hot Chocolate', 'Mocha', 'Latte', 'Americano', 'Cappuccino', 'Tea', 'Panini', 'Toast', 'Croissant', 'Buttered Roll', 'Muffin', 'Stroopwafel']
data = [20, 17, 22, 21, 22, 18, 4, 2, 4, 3, 1, 6]

df = pd.DataFrame({'Menu Items': menu_items, 'Count': data})

sorted_df = df.sort_values(by='Count', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(sorted_df['Menu Items'], sorted_df['Count'], color='skyblue')

plt.xlabel('Menu Items')
plt.ylabel('Count')
plt.title('Thursday\nCount of Menu Items', fontweight='bold')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()