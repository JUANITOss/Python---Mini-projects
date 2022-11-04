def add_time(start, duration, date = ""):

    dates = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  
    time,tod = start.split()
    hour,mins = time.split(":")
    plush,plusm = duration.split(":")
    tod = tod.upper()
    hour, mins, plush, plusm = int(hour), int(mins), int(plush), int(plusm)
    days = 0
    
    #Validating if the date is correct or not
    
    if hour > 12 or hour < 1:
        print("The hour is not in the valid range of 1-12.")
        return
    
    if 0 > mins or mins > 59:
        print("The minutes should not be lower than 0 or higher than 59.")
        return
    
    # Obtaining the minutes, the hours, the amount of days and the cycle
    
    totmins = mins + plusm
    
    if totmins >= 60:
        totmins -= 60
        tothours = hour + plush + 1
    else:
        tothours = hour + plush
    
    while True:
        
        if tothours < 12:
            break
        if tod == "PM":
            tod = "AM"
            days += 1
        else:
            tod = "PM"
        
        tothours -= 12
    
    # In case the total hours are equal to zero
    print(f"{tothours:02}:{totmins:02} {tod}")
    if tothours == 0:
        tothours = 12

        if tod == "PM":
            days -= 1
            tod = "AM"
        
    # Preparing the print for the date
    
    if date != "":
         
        date = date.title()
    
        if date not in dates:
            date = ""

        else:
            
            i = dates.index(date)
            i += days
            
            while i > len(dates):
                
                i -= 7
            
            date = dates[i]
            date = ", " + date
    
    # Preparing the print for the days
    
    if days == 1:
        days = " (next day)"
    elif days > 1:
        days = " (" + str(days) + " days later)"
    else:
        days = ""

    
    new_time = f"{tothours:02}:{totmins:02} {tod}{date}{days}"
    
    return new_time

print(add_time("11:59 pm", "00:01", "FrIday"))