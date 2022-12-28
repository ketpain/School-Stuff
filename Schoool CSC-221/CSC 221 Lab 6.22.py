highway_number = int(input())
evenTest = 0
highwayString = str(highway_number)

if(highway_number == 0 or highway_number == 200 or highway_number == 300 or highway_number == 400 or highway_number == 500 or highway_number == 600 or highway_number == 700 or highway_number == 800 or highway_number == 900 or highway_number >= 1000):
    print(highwayString + " is not a valid interstate highway number.")

elif(highway_number >= 1 and highway_number <= 99):
    evenTest = highway_number % 2
    if(evenTest == 0):
        print("I-" + highwayString + " is primary, going east/west.")
    elif(evenTest == 1):
        print("I-" + highwayString + " is primary, going north/south.")

elif(highway_number >= 100 and highway_number <= 999):
    evenTest = highway_number % 2

    #highwaytest = str(highway_number)[-2:]
    #if(highwaytest == 0):

    if(evenTest == 0):
        print("I-" + highwayString + " is auxiliary, serving I-" + str(highway_number)[-1:] + ", going east/west.")
    elif(evenTest == 1):
        print("I-" + highwayString + " is auxiliary, serving I-" + str(highway_number)[-1:] + ", going north/south.")