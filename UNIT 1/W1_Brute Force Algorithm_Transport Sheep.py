def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]




# def brute_force_cow_transport_internet(cows, limit=10):
#
#     list = []
#     for partition in get_partitions(cows.keys()):
#         list.append(partition)
#
#     z = []
#
#     for i in range(len(list)):
#         a = []
#         for j in range(len(list[i])):
#             b = []
#             for k in list[i][j]:
#                 b.append(cows[k])
#             if sum(b) > limit:
#                 break
#             a.append(list[i][j])
#
#         if len(a) == len(list[i]):
#             z.append(a)
#
#     numTrips = []
#     for tlist in z:
#         numTrips.append(len(tlist))
#
#     for tripsList in z:
#         if len(tripsList) == min(numTrips):
#             return tripsList


def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    cownames = []
    for cow in cows:
        cownames.append(cow)

    result = []
    for partition in get_partitions(cownames):
        val = True
        for trip in partition:
            weight = 0
            for cow in trip:
                weight += cows[cow]
            if weight > limit:
                val = False
        if val == True:
            result.append(partition)

    numtrips = []
    for transport in result:
        numtrips.append(len(transport))

    for transport in result:
        if len(transport) == min(numtrips):
            return transport






print(brute_force_cow_transport({'Horns': 25, 'MooMoo': 50, 'Miss Bella': 25, 'Boo': 20, 'Lotus': 40, 'Milkshake': 40}, 100))

