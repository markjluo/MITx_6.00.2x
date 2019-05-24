cows = {'Horns': 50, 'Louis': 45, 'MooMoo': 85, 'Polaris': 20, 'Clover': 5, 'Muscles': 65, 'Miss Bella': 15, 'Milkshake': 75, 'Lotus': 10, 'Patches': 60}
limit=100

def greedy_cow_transport_internet(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:
    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows
    Does not mutate the given dictionary of cows.
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    total = []
    copy = dict.copy(cows)
    sorted_list = sorted(cows.values(), reverse=True)
    totalcost = 0

    while (len(sorted_list) != 0):
        totalcost = 0
        result = []
        for i in range(len(sorted_list)):
            if ((totalcost + sorted_list[i]) <= limit):
                totalcost += sorted_list[i]
                for key in copy:
                    if (cows[key] == sorted_list[i]):
                        entry = key
                result.append(entry)
                del copy[entry]

        total.append(result)
        for i in result:
            if cows[i] in sorted_list:
                sorted_list.remove(cows[i])
    return total





class COW(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight


def cowsobjects(names, weight):
    a = []
    for i in range(len(names)):
        a.append(COW(names[i], weight[i]))
    return a


names = []
weight = []
for i in cows:
    names.append(i)
    weight.append(cows[i])

l = cowsobjects(names, weight)
l = sorted(l, key=COW.getWeight, reverse=True)

cownames = []
for i in l:
    cownames.append(i.getName())

transport = []
trip = []
while len(cownames) != 0:
    total = 0
    for name in cownames:
        if total + cows[name] <= limit:
            trip.append(name)
            total += cows[name]

    for i in trip:
        del(cownames[cownames.index(i)])

    transport.append(trip)
    trip = []



print(transport)

