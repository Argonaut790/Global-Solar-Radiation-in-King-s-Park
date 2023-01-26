import mysql.connector
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def main() -> None:
    #retrieve data from mysql
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Tung266314",
        database="gsr"
    )
    mycursor = mydb.cursor()
    
    mycursor.execute(
        "SELECT sun FROM temperature.join_result\
        ORDER BY Year, Month, Day;"
    )

    x = mycursor.fetchall()
    #print(x)

    mycursor.execute(
        "SELECT avgTemp FROM temperature.join_result\
        ORDER BY Year, Month, Day;"
    )

    y = mycursor.fetchall()
    #print(y)
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    lr = LinearRegression()
    lr.fit(x_train, y_train)
    c = lr.intercept_
    m = lr.coef_
    #print(m)

    y_pred_train = lr.predict(x_train) #lr model is done now reuse the x training data to predict it y value which is using 70% of the data
    #print(y_pred_train)

    # Sun-AvgTemp
    plot.subplot(1,3,1)
    plot.scatter(x_train, y_train, label="Training Data", color="red", s=8, alpha=0.7)
    plot.scatter(x_test, y_test, label="Testing Data", color="green", s=8, alpha=0.7)
    plot.plot(x_train, y_pred_train, label="Linear Regression", color='blue')
    plot.legend()
    plot.title("Bright Sun Time - Average Temperature Relationship", y=1.04)
    plot.title(f"r^2 = {r2_score(y_train, y_pred_train):.2f}", loc='right', size=7)
    print("Sun - AvgTemp")
    print(f"r^2 = {r2_score(y_train, y_pred_train):.2f}")
    print(f"score = {lr.score(x_train, y_train)}")
    plot.xlabel("Bright Sun Time")
    plot.ylabel("Average Temperature")
    
    mycursor.execute(
        "SELECT rh FROM temperature.join_result\
        ORDER BY Year, Month, Day;"
    )

    x = mycursor.fetchall()
    #print(x)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    lr_hr = LinearRegression()
    lr_hr.fit(x_train, y_train)
    c_hr = lr_hr.intercept_
    m_hr = lr_hr.coef_
    #print(m_hr)

    y_pred_train = lr_hr.predict(x_train) #lr model is done now reuse the x training data to predict it y value which is using 70% of the data
    #print(y_pred_train)

    # RH-AvgTemp
    plot.subplot(1,3,2)
    plot.scatter(x_train, y_train, label="Training Data", color="red", s=8, alpha=0.7)
    plot.scatter(x_test, y_test, label="Testing Data", color="green", s=8, alpha=0.7)
    plot.plot(x_train, y_pred_train, label="Linear Regression", color='blue')
    plot.legend()
    plot.title("Relative Humidity - Average Temperature Relationship", y=1.04)
    plot.title(f"r^2 = {r2_score(y_train, y_pred_train):.2f}", loc='right', size=7)
    print("RH - AvgTemp")
    print(f"r^2 = {r2_score(y_train, y_pred_train):.2f}")
    print(f"score = {lr_hr.score(x_train, y_train)}")
    plot.xlabel("Relative Humidity")
    plot.ylabel("Average Temperature")
    
    mycursor.execute(
        "SELECT gsr FROM temperature.join_result\
        ORDER BY Year, Month, Day;"
    )

    x = mycursor.fetchall()
    #print(x)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    lr_gsr = LinearRegression()
    lr_gsr.fit(x_train, y_train)
    c_gsr = lr_gsr.intercept_
    m_gsr = lr_gsr.coef_
    #print(m_gsr)

    y_pred_train = lr_gsr.predict(x_train) #lr model is done now reuse the x training data to predict it y value which is using 70% of the data
    #print(y_pred_train)

    # GSR-AvgTemp
    plot.subplot(1,3,3)
    plot.scatter(x_train, y_train, label="Training Data", color="red", s=8, alpha=0.7)
    plot.scatter(x_test, y_test, label="Testing Data", color="green", s=8, alpha=0.7)
    plot.plot(x_train, y_pred_train, label="Linear Regression", color='blue')
    plot.legend()
    plot.title("Global Solar Radiation - Average Temperature Relationship", y=1.04)
    plot.title(f"r^2 = {r2_score(y_train, y_pred_train):.2f}", loc='right', size=7)
    print("RH - AvgTemp")
    print(f"r^2 = {r2_score(y_train, y_pred_train):.2f}")
    print(f"score = {lr_gsr.score(x_train, y_train)}")
    plot.xlabel("Global Solar Radiation")
    plot.ylabel("Average Temperature")

    plot.show()

if __name__ == "__main__":
    main()