'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

from_member = input()
to_member = input()

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

def relationship_status(from_member, to_member, social_graph):
    if from_member not in social_graph or "following" not in social_graph[from_member]:
        return "invalid from_member"
    if to_member not in social_graph or "following" not in social_graph[to_member]:
        return "invalid to_member"

    status = ""
    if from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
        status = "friends"
    elif from_member in social_graph[to_member]["following"]:
        status = "followed by"
    elif to_member in social_graph[from_member]["following"]:
        status = "follower"
    else:
        status = "no relationship"
    return status

print(relationship_status(from_member, to_member, social_graph))

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

board = [
['O','X','O'],
['','O','X'],
['X','O','X'],
]

def tic_tac_toe(board):
    size = len(board)
    found = False
    winner = ""
    loop = 1
    
    while loop == 1:
        # check diagonal from top left to bottom right
        winner = board[0][0]
        for i in range(size):
            if board[0][0] != board[i][i]:
                break
            elif board[0][0] == board[i][i]:
                if i == size-1:
                    if winner != "":
                        found = True
        if found:
            break
            
        # check diagonal from top right to bottom left
        winner = board[0][size-1]
        for i in range(size):
            if board[0][size-1] != board[i][size-1-i]:
                break
            elif board[0][size-1] == board[i][size-1-i]:
                if i == size-1:
                    if winner != "":
                        found = True
        if found:
            break
            
        # check rows
        for row in range(size):
            winner = board[row][0]
            for column in range(size):
                if board[row][0] != board[row][column]:
                    break
                elif board[row][0] == board[row][column]:
                    if column == size-1:
                        if winner != "":
                            found = True
                            break
            if found:
                break 
        
        if found:
            break
            
        # check columns
        for column in range(size):
            winner = board[0][column]
            for row in range(size):
                if board[0][column] != board[row][column]:
                    break
                elif board[0][column] == board[row][column]:
                    if row == size-1:
                        if winner != "":
                            found = True
                            break
            if found:
                break 
        
        if found:
            break
        
        loop += 1
            
    if found:
        return winner
    else:
        return "NO WINNER"

        
tic_tac_toe(board)

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

first_stop = input()
second_stop = input()

route_map = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

def eta(first_stop, second_stop, route_map):
    if (first_stop, second_stop) in route_map:
        return route_map[(first_stop, second_stop)]['travel_time_mins']
    
    stop_times = {stop: float('inf') for stop in route_map}
    stop_times[first_stop] = 0
    visited = set()
    current_stop = first_stop
    
    while current_stop != second_stop:
        visited.add(current_stop)
        for stop, route in route_map.items():
            if current_stop in stop and stop_times[stop[1]] > stop_times[current_stop] + route['travel_time_mins']:
                stop_times[stop[1]] = stop_times[current_stop] + route['travel_time_mins']
        current_stop = min(stop_times, key=stop_times.get)
        if stop_times[current_stop] == float('inf'):
            return -1
    
    return stop_times[second_stop]

        
print(eta(first_stop, second_stop, route_map))