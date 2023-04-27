from time import sleep
from celery import shared_task
import datetime
import time # import the time module
from .models import Location

@shared_task()
def ad_run(cities, start_date, end_date, visitors_per_day):
    print('------------------------> TASK START!')
    # define the maximum allowed visitors for each location
    total_max_visitors = 0
    for city_id in cities:
        location = Location.objects.get(id=city_id)
        total_max_visitors += location.max_daily_visitors

    # get the start date, end date, and total number of visitors per day from the user
    start_date_str = start_date
    end_date_str = end_date
    visitors_per_day = int(visitors_per_day)

    # convert the start date and end date strings to datetime objects
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()

    # calculate the number of days between the start and end dates
    num_days = (end_date - start_date).days + 1

    # calculate the number of visitors allowed per location per day
    max_visitors_per_location = {}
    for city_id in cities:
        location = Location.objects.get(id=city_id)
        max_visitors_per_location[location.name] = location.max_daily_visitors

    current_day_visitors = 0  # initialize the number of visitors for the current day
    for i in range(num_days):
        # print the current date for reference
        current_date = start_date + datetime.timedelta(days=i)
        print(f"Checking visitor count for {current_date.strftime('%Y-%m-%d')}...")
        # loop through each location and check the visitor count
        for city_id in cities:
            location = Location.objects.get(id=city_id)
            location_name = location.name
            location_limit = max_visitors_per_location[location_name]
            if current_day_visitors >= visitors_per_day:
                print(f"Ad is blocked for {location_name} for {current_date.strftime('%Y-%m-%d')}.")
            else:
                if location_limit <= 0:
                    print(f"No visitors allowed for {location_name}.")
                else:
                    # calculate the remaining visitors for the current location
                    remaining_visitors = location_limit - current_day_visitors
                    # calculate the visitors to be added for the current location
                    visitors_to_add = min(remaining_visitors, visitors_per_day - current_day_visitors)
                    if visitors_to_add <= 0:
                        print(f"Ad is blocked for {location_name} for {current_date.strftime('%Y-%m-%d')}.")
                    else:
                        # update the current day's visitors count
                        current_day_visitors += visitors_to_add
                        # update the location's remaining visitors count
                        max_visitors_per_location[location_name] -= visitors_to_add
                        print(f"Ad is active for {location_name} with {visitors_to_add} visitors.")
        # reset the current day's visitors count for the next day
        current_day_visitors = 0
        # add a 3 second sleep before moving to the next day
        time.sleep(3)
    print('---> Ad campaign Completed!!!')
