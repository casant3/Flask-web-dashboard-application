import matplotlib.pyplot as plt
import pandas as pd

p_method = ['Debit', 'Credit', 'Voucher', 'Cash']
data = [22, 10, 8, 6]

plt.title("Monday\nPercentage Of Total Count By Payment Method", fontweight='bold')


plt.pie(
    data, 
    labels = p_method, 
    autopct = "%.2f%%", 
    explode = [0.05, 0, 0, 0]
    )

plt.legend(title="Categories", loc="upper right", bbox_to_anchor=(1.2, 0.25))


plt.show()