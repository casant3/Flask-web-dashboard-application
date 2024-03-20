import matplotlib.pyplot as plt
import pandas as pd

menu_items = ['Hot Chocolate', 'Mocha', 'Latte', 'Americano', 'Cappuccino', 'Tea', 'Toast', 'Muffin', 'Stroopwafel']
data = [18, 11, 15, 11, 16, 15, 1, 4, 1]


df = pd.DataFrame({'Menu Items': menu_items, 'Count': data})

sorted_df = df.sort_values(by='Count', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(sorted_df['Menu Items'], sorted_df['Count'], color='skyblue')

plt.xlabel('Menu Items')
plt.ylabel('Count')
plt.title('Sunday\nCount of Menu Items', fontweight='bold')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()