import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
%matplotlib inline

sizes = [1.5, 4.0, 2.0, 2.5]
labels = 'History', 'Math', 'English', 'Psychology'


plt.pie(sizes,
       labels = labels)


plt.title('The courses in school')
plt.axis('equal')


plt.show()
