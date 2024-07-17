import pandas as pd
# data={
# 'Age':[25,10,30,12,44,10],
# 'Salary':[5000,400,3000,800,8000,800]
# }
# df=pd.DataFrame(data)

# mean_age=df['Age'].mean()
# mean_salary=df['Salary'].mean()
# print("Mean of Age:",mean_age)
# print("Mean of Salary:",mean_salary)


# #median
# median_age=df['Age'].median
# median_salary=df['Salary'].median
# print("Median of Age:",median_age)
# print("median salary: ",mean_salary)






# #mode ->most frequent values
# #mode can be more than one , multimodel
# mode_age=df['Age'].mode()[0]
# mode_salary=df['Salary'].mode()[0]
# print("Mode of Age:",mode_age)
# print("Mode of Salary:",mode_salary)

# #Standard deviation
# std_age=df['Age'].std()
# std_salary=df['Salary'].std()
# print(std_age)
# print(std_salary)

# print("variance..")
# #variance
# var_age=df['Age'].var()
# var_salary=df['Salary'].var()
# print(var_age)
# print(var_salary)


#Normal
# Distribution
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# # Set parameters for the normal distribution
# mu = 0
# sigma = 0.1

# # Generate 1000 samples from a normal distribution
# s = np.random.normal(mu, sigma, 1000)

# # Create histogram of the samples
# count, bins, ignored = plt.hist(s, 30, density=True, alpha=0.6, color='g')

# # Plot the normal distribution PDF
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
# plt.title('Normal Distribution')
# plt.xlabel('Value')
# plt.ylabel('Probability Density')
# plt.show()




#Binomial Distribution

# n,p=10,0.5
# binomial= np.random.binomial(n,p,1000)

# plt.hist(binomial,bins=10,density=True,alpha=0.6,color='y')
# plt.show()


#iqr
import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Q1 = np.percentile(data, 25)
Q2 = np.median(data)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

print("Q1: " + str(Q1))
print("Q2 [median]: " + str(Q2))
print("Q3: " + str(Q3))
print("IQR: " + str(IQR))
