

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
        
        
    print(" ")
    pyttsx3.speak("lets have visualisation of the data")
    plt.scatter(x ='Hours', y = 'Scores', data = data) 
    plt.title('Hours vs Score')  
    plt.xlabel('Hours Studied')  
    plt.ylabel('Score obtained')  
    plt.show()
    pyttsx3.speak("As you seen the plot, you can observe that it has good correlation")

    
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

        
        print("\nTrain-Test-Split : ")
        pyttsx3.speak("Now lets split the data into train set and test set")
        pyttsx3.speak("would you like to specify the test_size or shall we go with the default size")
        print("\nChoose the Default size as of time being, need to resolve issues in specific size")
        user_input = input("would you like to specify the test_size (y/n)?..")
        user_input = user_input.lower()
        if(('y' in user_input) or ('yes' in user_input)):
            testsize = int(input("Specify the test size in range : "))
            testsize /= 10
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = testsize, random_state = 0)
            pyttsx3.speak("The split is made based on the test size you provided")

        elif(('n' in user_input) or ('no' in user_input) or ('default' in user_input)):
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
            pyttsx3.speak("Default test size is used to split")

        else:
            pyttsx3.speak("Oops Invalid choice, as punishment re-run the whole program")
            exit

        print("\nDataset has got split into train and test sets, these are the shapes")
        print("XTrain set  : ", x_train.shape)
        print("XTest set   : ", x_test.shape)
        print("YTrain set  : ", y_train.shape)
        print("YTest set   : ", y_test.shape)
        pyttsx3.speak("Successfully the data got split lets train the algorithm by creating its instance")
        
        print("-"*55, "Training the Algorithm", "-"*54)
        pyttsx3.speak("lets start training the model")
        print(" ")
        regr = LinearRegression()  
        pyttsx3.speak("model instance is created")
        print(" ")
        regr.fit(x_train, y_train) 
        pyttsx3.speak("we fitted the data to the model")
        print(" ")
        line = regr.coef_*x+regr.intercept_
        pyttsx3.speak("lets have look at the data and the regression line")
        print(" ")
        plt.scatter(x, y)
        plt.plot(x, line)
        plt.title('Hours vs Score')  
        plt.xlabel('Hours Studied')  
        plt.ylabel('Score obtained')  
        plt.show()

        pyttsx3.speak("model has been trained successfully")
        print(" ")
        
        print("-"*55, "Testing the Algorithm", "-"*55)
        pyttsx3.speak("lets start testing the Algorithm")
        y_pred = regr.predict(x_test)
        pyttsx3.speak("making predictions")
        print(" ")
        df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
        df
        pyttsx3.speak("successfully predicted the test data, lets look at few eavluation metrics")
        from sklearn import metrics
        print('Mean Absolute Error     :', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error      :', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error :', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        pyttsx3.speak("These are the different errors caluculated")

        print("\nWhat will be predicted score if a student study for 9.25 hrs in a day?")
        pyttsx3.speak(" But still we havent answered the actual question What will be predicted score if a student study for 9.25 hours in a day?")
        y_pred = regr.predict([[9.25]])
        print("The predicted score is:", y_pred)
        pyttsx3.speak("Prediction done on the trained regression model")
        flag = True
        while flag == True:
            pyttsx3.speak("Why dont we try with different hours")
            user_input = int(input("\nLets try with different value of hours:"))
            y_pred = regr.predict([[user_input]])
            print("The predicted score is:", y_pred)
            pyttsx3.speak("Prediction is done, check the value")
            fl = input("Do you want to try it again (y/n)?..")
            if('yes' in fl or 'y' in fl):
                flag = True
            else:
                flag = False
            
        print(" ")
        pyttsx3.speak("Its good to assist you I learned a lot about simple linear regression thank you")


# snippet loads the data and initiates the main()
if __name__=="__main__":
    pyttsx3.speak("Lets first load the data into main function, feed me the dataset name")
    data = input("Feed me the dataset name : ")
    data = pd.read_csv(data)
    main(data)