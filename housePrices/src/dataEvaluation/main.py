from houseData import data
import matplotlib.pyplot as plt # pip3 install matplotlib
import seaborn as sns # pip3 install seaborn

plt.figure(figsize=(10, 6))
plt.bar(data['bedroom_count'], data['age']) # x , y 
plt.title('Line plot of Bedrooms vs. Age')
plt.xlabel('Bedroom Count')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()
