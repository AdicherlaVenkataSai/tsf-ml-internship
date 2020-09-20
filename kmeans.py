

"""
Code is developed on Visual Studio Code (Ubuntu OS)
Created by: VenkataSai Adicherla 
Time: 11:00 pm 8 September
Task Provider: The Sparks Foundation (Machine Leaning Intern - Task 2)

Feel free to download the code and check it
Any errors or questions can contact me(details in readme)
Note:  Check the requirements.txt file before executing the code
"""

from os import system
system("clear")
# snippet to check whether the modules are avilable or not
import pyttsx3 
from _cffi_backend import string
# snippet to modify the audio pace and range 
voiceEngine = pyttsx3.init()
rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
newVoiceRate,newVolume =  160, 0.4
voiceEngine.setProperty('rate', newVoiceRate)
voiceEngine.setProperty('volume', newVolume)
pyttsx3.speak("Hello I am Sai's personal assistant")
# print(" ")
pyttsx3.speak("Am here to assist you through out the execution.")
pyttsx3.speak(" ")

try:
    pyttsx3.speak(" importing the modules ")
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pyttsx3 
    print("-"*49, "Successfully imported the modules", "-"*49)
    pyttsx3.speak("Successfully imported the modules")
except:
    print("Oops!, few modules are missing\nInstall the modules by executing `pip install -r requirements.txt`")
    pyttsx3.speak("Oops!, few modules are missing kindly install the modules")


# snippet to main() funtion the whole magic happens here
def main(data):
    print(" ")
    print("-"*59, "Main function", "-"*59)
    pyttsx3.speak("Welcome to main function, the whole magic happens here")
    # print(" ")
    pyttsx3.speak("Before applying the algorithm its good practise to have a look at the data")
    print(" ")
    pyttsx3.speak("would you like to see dataset information")
    user_input = input("would you like to see dataset information (y/n)?..")
    user_input = user_input.lower()

    if(('y' in user_input) or ('yes' in user_input)):
        print("-"*56, "DataSet Information", "-"*56) 
        print('\nThe shape of the data is: ',data.shape)
        print(" ")
        print('\nDataset: \n',data.head())
        print(" ")
        print("\nChecking for null values: \n",data.isnull().sum())
        print(" ")
        print("\nChecking the dataypes: \n",data.dtypes)
        print(" ")
        print("\nDescription about the data:  \n",data.describe())
        print(" ")
        data.info()
        pyttsx3.speak(" As I have manually checked, no null values are present in the data, more information about the dataset is available on scree, go thorugh it")


        print("Clustering Problem")
        pyttsx3.speak("As were dealing with clustering problem kmeans, we need to find the k value But how do we do?, yes we can use eblow curve method to find the optimal value of k")
        x = data.iloc[:, [0, 1, 2, 3]].values

        from sklearn.cluster import KMeans
        ls = []

        for i in range(1, 11):
            kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
            kmeans.fit(x)
            ls.append(kmeans.inertia_)
    
        print("Plotting the Elbow curve")
        pyttsx3.speak("Lets plot the eblow curve")
        plt.plot(range(1, 11), ls)
        plt.title('The elbow method')
        plt.xlabel('Number of clusters')
        plt.ylabel('')
        plt.show()       
    
    print("-"*57, "Choose the module", "-"*57)
    pyttsx3.speak("which model would you like to use sci kit learn module or scratch module")
    print(" ")
    print("Choose the sklearn moudle as of time being, till i update the scratch module")
    user_input = input("Enter your choice a. sklearn module b. scratch module :")


    if('a' in user_input):

        pyttsx3.speak("sci kitlearn module is used for the implementation of regression model")
        try:
            from sklearn.model_selection import train_test_split
            from sklearn.linear_model import LinearRegression
            from sklearn import metrics
            pyttsx3.speak("Imported the required sci kit learn module")
        except:
            print("\nOops!, few modules are missing\nInstall the modules by executing `pip install -r requirements.txt`")
            pyttsx3.speak("Oops!, few modules are missing kindly install the modules")
        
        print("\nDividing the dataset into attributes and labels :")
        pyttsx3.speak("Dividing the dataset into attributes and labels")
        x = data.iloc[:, :-1].values  
        y = data.iloc[:, 1].values
        print("\nAttributes:\n",x)
        print("\nLables :",y)

        
        
        print("Applying kmeans instance on the dataset")
        pyttsx3.speak("Applying kmeans instance on the dataset")
        kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
        pyttsx3.speak("Predictions are made")
        y_kmeans = kmeans.fit_predict(x)

        pyttsx3.speak("Now lets visualise the Clusters foremd")
        plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Iris-setosa')
        plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Iris-versicolour')
        plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Iris-virginica')
        pyttsx3.speak("Plotting the centroids of the cluster")
        plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'yellow', label = 'Centroids')
        plt.legend()

        print(" ")
        pyttsx3.speak("Its good to assist you I learned a lot about simple Clustering techniques thank you")



# snippet loads the data and initiates the main()
if __name__=="__main__":
    pyttsx3.speak("Lets first load the data into main function, feed me the dataset name")
    data = input("Feed me the dataset name : ")
    data = pd.read_csv(data)
    main(data)