from sklearn.linear_model import LinearRegression as lr
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import r2_score

def lin_reg(df2):
    store=1
    df_x=df2[df2.Store==store][['Fuel_Price','CPI','Unemployment']]
    df_y=df2[df2.Store==store][['Weekly_Sales']]
    reg=lr()
    x_train,x_test,y_train,y_test=tts(df_x,df_y,test_size=0.3)
    reg.fit(x_train,y_train)
    print(reg.coef_)
    y_pred=reg.predict(x_test)
    return round(r2_score(y_test,y_pred),5)

def get_day_from_date(walmart_data):
    walmart_data['Day'] = pd.to_datetime(walmart_data['Date']).dt.day_name()
    return walmart_data

def date_to_number(walmart_data):
    x_features_object = walmart_data[walmart_data['Store'] ==1][['Store','Date']]
    date_obj = walmart_data[walmart_data['Store'] ==1][['Date']]
    date_obj.index +=1
    x_features_object.Date = date_obj.index
    return (x_features_object)

def log_reg(walmart_data):
    response_set_cpi = walmart_data[walmart_data['Store'] ==1]['CPI'].astype('int64')
    response_set_unemployment = walmart_data[walmart_data['Store'] ==1]['Unemployment'].astype('int64')
    x_train_cpi,x_test_cpi,y_train_cpi,y_test_cpi = train_test_split(feature_dataset,response_set_cpi,random_state=1)
    x_train_unemp, x_test_unemp, y_train_unemp, y_test_unemp = train_test_split(feature_dataset,response_set_unemployment,random_state=1)
    logreg = LogisticRegression(max_iter=10000)
    logreg.fit(x_train_cpi,y_train_cpi)
    y_pred = logreg.predict(x_test_cpi)
    logreg.fit(x_train_unemp,y_train_unemp)
    y_pred_unemp = logreg.predict(x_test_unemp)
    #print(metrics.accuracy_score(y_test_cpi,y_pred))
    #print(metrics.accuracy_score(y_test_unemp,y_pred_unemp))
    print('cpi actual :', y_test_cpi.values[0:10])
    print('cpi Predicted :', y_pred[0:10])
    print('actual Unemployment :', y_test_unemp.values[0:30])
    print('Predicted Unemployment :', y_pred_unemp[0:30])