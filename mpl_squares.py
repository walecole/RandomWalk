import matplotlib.pyplot as plt

input_values = list(range(1,6))
squares = [x**2 for x in input_values]
plt.scatter(input_values, squares, c= squares, cmap=plt.cm.Blues, edgecolor= 'none', s=40)

#set chart labels
plt.title("Sqaure Numbers", fontsize= 24)
plt.xlabel("Value", fontsize= 14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.show()