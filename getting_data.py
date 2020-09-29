def get_data():
    '''
    Gets pick-up and drop-off coordinates from the user, as well as the
    number of passengers in the car and the current date and time.
    '''
    import googlemaps
    from datetime import datetime
    import pytz 
    from hidden import API_KEY

    gmaps = googlemaps.Client(key=API_KEY) 

    # Geocoding pick-up ddress 
    pickup_address = input('Enter pick-up address: ')
    pickup_geocode = gmaps.geocode(pickup_address)

    # Geocoding drop-off address
    dropoff_address = input('Enter drop-off address: ')
    dropoff_geocode = gmaps.geocode(dropoff_address)

    # Getting the current date and time 
    now = datetime.now()

    # Converting local time to Eastern Daylight time 
    # to match data in the data frame used to train/test/validate the neural network
    local_timezone = pytz.timezone('Europe/Warsaw')
    now = local_timezone.localize(now)
    
    target_timezone = pytz.timezone('US/Eastern')
    now = target_timezone.normalize(now)

    # Getting pick-up and drop-off coordinates from the user
    pickup_latitude = pickup_geocode[0]['geometry']['location']['lat']
    pickup_longitude = pickup_geocode[0]['geometry']['location']['lng']

    dropoff_latitude = dropoff_geocode[0]['geometry']['location']['lat']
    dropoff_longitude = dropoff_geocode[0]['geometry']['location']['lng']

    # Getting the number of passengers
    num_passengers = input('How many passengers were in the taxi: ')

    # Storing everything in a dictionary to easily access the data when testing
    data = {
        'pickup_latitude': pickup_latitude,
        'pickup_longitude': pickup_longitude,
        'dropoff_latitude': dropoff_latitude,
        'dropoff_longitude': dropoff_longitude,
        'passenger_count': num_passengers,
        'EDTdate': str(now)[:19]
    }

    return data 