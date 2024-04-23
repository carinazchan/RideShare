#Menu.py

#imports
from datetime import datetime
from helper import helper
from db_operations import db_operations

#global variables
db_ops = db_operations()


#functions

#prints a welcome to the user for RideShare app
def startScreen():
    print("Welcome to RideShare!")

#prints out options for RideShare app depending on if user is a new user, rider, or driver
def options():
    print(
        """Are you a new user, a rider, or a driver?
    1. New User
    2. Rider
    3. Driver
    4. Exit"""
    )

#ensures choices are error-checked (will not let you choose any other options than 1-4)
    return helper.get_choice([1, 2, 3, 4])

#function that dictates options if you are a new user to the app, can either identify as a rider or driver
def newUserOptions():
    print(
        """Would you like to be a rider or a driver?
    1. Rider
    2. Driver"""
    )
#error-checking on option choices
    newAccount = helper.get_choice([1, 2])

#inserts a new rider if rider option is selected, otherwise inserts new driver if driver option selected
    if newAccount == 1:
        riderInsert()
    if newAccount == 2:
        driverInsert()

#function that inserts a new rider into the database
def riderInsert():
    #asks for ID until correct output given
    riderID = input("ID Number: ")
    if not riderID:
        print("You must enter a valid ID.")
    while not riderID:
        riderID = input("ID Number: ")

    #asks for name until correct output is given
    name = input("Name: ")
    if not name:
        print("You must enter a name for the song.")
    while not name:
        name = input("Name: ")

    #builds query based on new updated values we got from the user and modifies Rider db with resulting query
    query = "INSERT INTO Rider VALUES (%s, %s)"
    dictionary = (riderID, name)
    db_ops.modify_query_params(query, dictionary)

#function that inserts a new driver into the database
def driverInsert():
    #asks for ID until correct output given
    driverID = input("ID Number: ")
    if not driverID:
        print("You must enter a valid ID.")
    while not driverID:
        driverID = input("ID Number: ")

    #asks for name until correct output is given
    name = input("Name: ")
    if not name:
        print("You must enter a name for the song.")
    while not name:
        name = input("Name: ")

    #asks for a driver mode input (either true or false) until correct output given
    mode = input("Driver Mode Verification: ").lower()
    if mode not in ["true", "false"]:
        print("Mode verification value should be True or False.")
    while mode not in ["true", "false"]:
        mode = input("Driver Mode Verification: ").lower()

    #builds query based on new updated values we got from the user to update Driver db with new Driver
    query = "INSERT INTO Driver VALUES (%s, %s, %s)"
    dictionary = (driverID, name, mode)
    db_ops.modify_query_params(query, dictionary)

#function that displays all functions if you are a Rider (need to log in to see)
def riderMenu():
    #asks for ID number to log in
    print("What is your ID number?")
    riderID = input("ID Number: ")

    #check to see if ID number is valid and log in...
    IDvalidity = db_ops.check_riderID(riderID)

    #depending on if ID is valid or not, either exits to main menu or repeats Rider functions until Rider exits the app
    if not (IDvalidity):
        while True:
            print(
                """
            Would you like to:
                1. View rides
                2. Find a driver
                3. Rate my driver
                4. Exit
            """
            )
            #ensures error-checking for options
            riderChoice = helper.get_choice([1, 2, 3, 4])

            #ensures functionality for each of the Rider options (viewing rides, finding driver, rating driver, or exiting)
            if riderChoice == 1:
                riderViewRides(riderID)
            if riderChoice == 2:
                findADriver(riderID)
            if riderChoice == 3:
                rateDriver(riderID)
            if riderChoice == 4:
                break
    #exits to main menu if unable to provide proper Rider ID number and log in
    if IDvalidity:
        print("Not a valid ID number. Try logging in with a valid one.")

#function to view each of the rides the logged in Rider has
def riderViewRides(ID):
    #query statement to get all rides that the rider has taken
    queryOfRides = """
    SELECT *
    FROM Ride
    WHERE riderID = '{}';
    """.format(ID)

    #queries the database and pretty(ish) prints the rides for the rider
    print("Here is your list of rides:")
    print(
        "(Ride ID, Rider ID, Driver ID, Date, Pickup Location, Dropoff Location, Rating)"
    )
    rides = db_ops.select_query(queryOfRides)
    for i in range(len(rides)):
        print("Ride " + str(i) + ": ", rides[i])

#function that finds a random driver for the logged in Rider
def findADriver(ID):
    #query that finds random driver with driver mode verified
    query = """
    SELECT name
    FROM Driver
    WHERE driverMode = 'true'
    ORDER BY RAND()
    LIMIT 1
    """

    #returns random driver and prints confirmation of matched driver to user
    driver = db_ops.single_record(query)
    print("You have been matched with " + driver + "!")

    #gathers information to store in a new Ride entry
    print("Please provide the following: ")
    pickup = input("Pick up Location: ")
    dropoff = input("Drop-off Location: ")

    #generates rideID seeing next unused number
    count = """
    SELECT COUNT(*)
    FROM Ride
    """
    rideID = db_ops.single_record(count) + 1

    #gets driverID from driver name
    name = """
    SELECT driverID
    FROM Driver
    WHERE name = '{}'
    """.format(
        driver
    )
    driverID = db_ops.single_record(name)

    #sets current date to date
    currdate = datetime.now()
    date = currdate.strftime("%Y-%m-%d %H:%M:%S")

    #initially sets rating to 0/Null until updated
    rating = 0

    #with all info for Ride gathered, inserts new record for Ride into the Ride database
    newRide = """
    INSERT INTO Ride VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    dictionary = (rideID, ID, driverID, date, pickup, dropoff, rating)
    db_ops.modify_query_params(newRide, dictionary)

    #informs user of successful Ride entry and shares the Ride ID with them
    print("Successfully created Ride " + str(rideID))

#function to rate the driver of logged in Rider's most recent ride
def rateDriver(riderID):
    #query statement to get all rides that the rider has taken
    queryOfRides = """
    SELECT *
    FROM Ride
    WHERE riderID = '{}'
    ORDER BY date ASC;
    """.format(
        riderID
    )

    #list of all of the rides that the rider has taken in order of most recent to least recent
    allOfRidersRides = db_ops.select_query(queryOfRides)

    #first ride result from the sorted list (most recent ride)
    recentRide = allOfRidersRides[0]

    #rideID from the most recent ride
    correctRideID = recentRide[0]

    #pretty(ish) prints the most recent ride to the rider
    print("Here is your most recent ride:")
    print(
        "(Ride ID, Rider ID, Driver ID, Date, Pickup Location, Dropoff Location, Rating)"
    )
    print()
    helper.pretty_print([recentRide])

    #prompts rider if the displayed ride is correct
    correctRideUserInput = input("Is this correct? (Type 'Yes' or 'No'): ")
    print()

    #if the ride displayed is NOT the intended ride the rider wishes to see
    while correctRideUserInput.lower() == "no":

        #prompts rider for the correct rideID of the ride the rider wishes to see
        correctRideID = input(
            "Please input the correct Ride ID of the ride you'd like to rate: "
        )

        #query statement for getting the correct ride
        queryOfCorrectRide = """
        SELECT *
        FROM Ride
        WHERE rideID = '{}';
        """.format(
            correctRideID
        )

        #correct ride attributes
        correctRecentRide = db_ops.select_query(queryOfCorrectRide)[0]

        #pretty(ish) prints the correct ride the rider wishes to see
        print("Here is your most recent ride:")
        print("(Ride ID, Rider ID, Driver ID, Date, Pickup Location, Dropoff Location, Rating)")
        print()
        helper.pretty_print([correctRecentRide])

        #reprompts user if the displayed ride is correct
        correctRideUserInput = input("Is this correct? (Type 'Yes' or 'No'): ")
        print()

    #if the ride is the correct ride the rider wishes to see
    if correctRideUserInput.lower() == "yes":

        #prompt rider for ride rating
        inputRating = input("Please input a rating from 1 to 5: ")
        print()

        #query statement to chaneg ride rating
        updateRatingQuery = """
        UPDATE Ride
        SET rating = '{}'
        WHERE rideID = '{}';
        """.format(
            inputRating, correctRideID
        )

        #queries the database to change the ride rating
        db_ops.modify_query(updateRatingQuery)
        print("You have successfully rated your ride!")

    return

#function that displays Driver menu and log-in to Driver account
def driverLogin():
    #asks for driver ID to properly log in
    print("What is your ID number?")
    driverID = input("ID Number: ")

    #check to see if ID number is valid and log in...
    IDvalidity = db_ops.check_driverID(driverID)

    #depending on successful login, either prints options on repeat or exits to main menu
    if not (IDvalidity):
        while True:
            print(
                """
            Would you like to:
                1. View Rating
                2. View Rides
                3. Activiate/Deactivate Driver Mode
                4. Exit
            """
            )
            driverChoice = helper.get_choice([1, 2, 3, 4])

            if driverChoice == 1:
                viewRating(driverID)
            if driverChoice == 2:
                driverViewRides(driverID)
            if driverChoice == 3:
                toggleMode(driverID)
            if driverChoice == 4:
                break
    #exits to main menu if an invalid ID given (login unsuccessful)
    if IDvalidity:
        print("Not a valid ID - try a valid ID next time.")

    return

#function that allows logged in Driver to view their current average rating
def viewRating(ID):
    #query that returns average rating with given ID
    query = """
    SELECT AVG(rating)
    FROM Ride
    WHERE driverID = {}
    """.format(
        ID
    )

    #prints current rating to user
    rating = db_ops.single_record(query)
    print("Your Current Rating: ")
    print(rating)

#function that allows logged in Driver to view all rides they've driven
def driverViewRides(ID):
    #query statement to get all rides that driver has driven
    queryOfRides = """
    SELECT *
    FROM Ride
    WHERE driverID = '{}'
    """.format(
        ID
    )

    #queries the database and pretty prints the drives for the driver
    print("Here is your list of rides:")
    print(
        "(Ride ID, Rider ID, Driver ID, Date, Pickup Location, Dropoff Location, Rating)"
    )
    rides = db_ops.select_query(queryOfRides)
    for i in range(len(rides)):
        print("Ride " + str(i) + ": ", rides[i])

#function that toggles Driver Mode Verification for logged in Driver
def toggleMode(ID):
    #query that returns the current mode of the driver
    query = """
    SELECT driverMode
    FROM Driver
    WHERE driverID = {}
    """.format(
        ID
    )
    mode = db_ops.single_record(query)

    #if mode is true, then toggle it to false
    if mode.lower() in ["true"]:
        newQuery = """
        UPDATE Driver
        SET driverMode = 'false'
        WHERE driverID = {}
        """.format(
            ID
        )

        db_ops.modify_query(newQuery)
        #prints successful deactivation to driver
        print("Your driver mode has been successfully deactivated.")
    #if mode is currently false, toggle it to true
    if mode.lower() in ["false"]:
        newQuery = """
        UPDATE Driver
        SET driverMode = 'true'
        WHERE driverID = {}
        """.format(
            ID
        )
        db_ops.modify_query(newQuery)
        #prints successful activation to driver
        print("Your driver mode has been successfully activated!")

#start screen - beginning of main menu
startScreen()

#while loop that loops through main menu until user chooses to exit
while True:
    user_choice = options()
    if user_choice == 1:
        newUserOptions()
    if user_choice == 2:
        riderMenu()
    if user_choice == 3:
        driverLogin()
    if user_choice == 4:
        print("Exiting RideShare App, ByeBye!!")
        break

db_ops.destructor()
