# 2. Generate graphs based on data for visualization of data (any number of graphs)
# MANIS SAHA

import random
import matplotlib.pyplot as plt

# Simulate the data
blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
simulated_data = [random.choice(blood_types) for _ in range(100)]

# Count occurrences of each blood type
blood_type_counts = {blood_type: simulated_data.count(blood_type) for blood_type in blood_types}

# Generate bar graph
plt.figure(figsize=(10, 6))
plt.bar(blood_type_counts.keys(), blood_type_counts.values(), color='skyblue')
plt.xlabel('Blood Type')
plt.ylabel('Count')
plt.title('Distribution of Blood Types')
plt.show()

# Generate pie chart
plt.figure(figsize=(8, 8))
plt.pie(blood_type_counts.values(), labels=blood_type_counts.keys(), autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Blood Type Distribution')
plt.show()
