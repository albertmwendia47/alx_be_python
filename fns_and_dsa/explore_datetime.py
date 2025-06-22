from datetime import datetime, timedelta
def display_current_datetime ():
    current_date = datetime.now()
    print(current_date);

display_current_datetime()

def calculate_future_date():
    days = int(input("Enter number of days to add: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


display_current_datetime()
calculate_future_date()    


    

    