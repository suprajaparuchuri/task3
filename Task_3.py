import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("D:\Data Analytics\Techno_Hacks\Task_3.csv")

# Create a histogram
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Species', bins=20, kde=True)  # Replace 'Numeric_Column' with your numerical column
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Numeric Data Distribution')
plt.grid(True)

# Create a bar chart
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Species')  # Replace 'Species' with your categorical column
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Bar Chart of Categorical Data Distribution')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility if needed

# Show the bar chart
plt.tight_layout()
# Show the histogram
plt.show()
