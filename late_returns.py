from datetime import datetime, timedelta

def total_number_late_returns(inputTimes):  
    late_returns = 0
    borrowed_batteries = 0

    ## We need to loop through the input times and convert the time into hours to be able to check if the difference exceeds 5 hours.
    ## The time in this format "H:M" needs the datetime function to be converted into seconds then into hours by dividing by 3600
    ## The function below returns the number of return times for only 1 rider, not multiple

    for borrow_time_input, return_time_input in inputTimes:
        # convert time string to datetime
        borrow_time = datetime.strptime(borrow_time_input, '%H:%M')
        return_time = datetime.strptime(return_time_input, '%H:%M')
        print("Borrow time:", borrow_time)
        print("Return time:", return_time)

        # Find the difference, convert to hours, and check if the difference is greater than 5
        diff = return_time - borrow_time
        diff_in_seconds = diff.total_seconds()
        print('Difference in seconds:', diff_in_seconds)
        
        if diff_in_seconds / 3600 > 5:
            # if the difference is greater than 5, increase the number of late returns
            late_returns += 1
            borrowed_batteries += 1

    return late_returns

# Sample input
inputTimes = [
    ['04:00', '11:00'],
    ['13:00', '16:00'],
    ['06:00', '10:00'],
    ['12:30', '13:30'],
    ['02:00', '11:00']
]

total_late_returns = total_number_late_returns(inputTimes)
print("Number of late returns:", total_late_returns)
