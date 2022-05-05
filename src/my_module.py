from numpy import Infinity


def get_cheapest_hotel(number):   #DO NOT change the function's name
    
    #Models used in the code
    workdays = ['mon', 'tues', 'wed', 'thur', 'fri']
    weekend = ['sat', 'sun']
    client_types = ['Regular', 'Rewards']
    hotels  = ['Lakewood', 'Bridgewood', 'Ridgewood']
    hotel_prices = {'Lakewood': {'workdays': {'Regular': 110, 'Rewards': 80}, 'weekend': {'Regular': 90, 'Rewards': 80}}, 'Bridgewood': {'workdays': {'Regular': 160, 'Rewards': 110}, 'weekend': {'Regular': 60, 'Rewards': 50}}, 'Ridgewood': {'workdays': {'Regular': 220, 'Rewards': 100}, 'weekend': {'Regular': 150, 'Rewards': 40}}}
    hotel_ratings = {'Lakewood': 3, 'Bridgewood': 4, 'Ridgewood': 5}

    if (isinstance(number, str)):
        str_input = number
    else: 
        return "Inappropriate input. Please, insert a string. Format expected: <client_type>: <date1>, <date2>, <date3>, ..."
    
    #Getting client type from input
    client_type = str_input.split(': ')[0]
    if(client_type not in client_types):
        return "Inappropriate client type inserted. Please, insert 'Regular' or 'Rewards'. Format expected: <client_type>: <date1>, <date2>, <date3>, ..."
    
    #Getting whole dates from input
    staying_dates = str_input.split(': ')[1]
    staying_dates_list = staying_dates.split(', ')

    #Getting weekdays from input (without parentheses)
    staying_weekdays = []
    for date in staying_dates_list:
        staying_weekdays.append(date.split('(')[1][0:-1])

    #Logic
    
    cheapest_hotel = ''
    cheapest_value = Infinity
    for hotel in hotels:
        value = 0
        for staying_weekday in staying_weekdays:
            if(staying_weekday in workdays):
                value = value + hotel_prices[hotel]['workdays'][client_type]
            elif(staying_weekday in weekend):
                value = value + hotel_prices[hotel]['weekend'][client_type]
            else:
                return "Inappropriate weekday inserted. Please insert one of the following: 'mon', 'tues', 'wed', 'thur', 'fri', 'sat', 'sun'. Format expected: <client_type>: <date1>, <date2>, <date3>, ..."
        if(value < cheapest_value):
            cheapest_value = value
            cheapest_hotel = hotel
        elif(value == cheapest_value and hotel_ratings[hotel] > hotel_ratings[cheapest_hotel]):
            cheapest_hotel = hotel

    return cheapest_hotel
