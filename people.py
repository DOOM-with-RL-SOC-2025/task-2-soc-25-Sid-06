"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : int
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:
        # Change the city 
        # Return true if city change, successful, return false if city same as old city
        if self.city == new_city:
            return False
        self.city = new_city
        return True

    def migrate_branch(self, new_code:int) -> bool:
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.
        if len(self.branches) != 1:
            return False
        old_branch = self.branches[0]
        if branchmap[old_branch]["city"] == branchmap[new_code]["city"]:
            self.branches[0] = new_code
            return True
        return False

    def increment(self, increment_amt: int) -> None:
        # Increment salary by amount specified.
        self.salary += increment_amt

class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 
        valid_positions = ["Junior", "Senior", "Team Lead", "Director"]
        if position in valid_positions:
            self.position = position
        else:
            self.position = "Junior"

    def increment(self, amt:int) -> None:
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        bonus = int(amt * 0.1)
        self.salary += amt + bonus
        
    def promote(self, position:str) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        valid_positions = ["Junior", "Senior", "Team Lead", "Director"]
        try:
            current_index = valid_positions.index(self.position)
            new_index = valid_positions.index(position)
        except ValueError:
            return False
        if new_index <= current_index:
            return False
        self.position = position
        self.increment(int(self.salary * 0.3))
        return True

class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to

    def __init__(self, name, age, ID, city, branchcodes, position="Rep", salary=None, superior=None):
        super().__init__(name, age, ID, city, branchcodes, salary)
        valid_positions = ["Rep", "Manager", "Head"]
        if position in valid_positions:
            self.position = position
        else:
            self.position = "Rep"
        self.superior = superior

    def increment(self, amt:int) -> None:
        # increment with 5% bonus
        bonus = int(amt * 0.05)
        self.salary += amt + bonus

    def promote(self, position:str) -> bool:
        valid_positions = ["Rep", "Manager", "Head"]
        try:
            current_index = valid_positions.index(self.position)
            new_index = valid_positions.index(position)
        except ValueError:
            return False
        if new_index <= current_index:
            return False
        self.position = position
        self.increment(int(self.salary * 0.3))
        # If promoted to Head, superior should be None
        if self.position == "Head":
            self.superior = None
        return True

    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        if self.superior is None:
            return (None, None)
        for s in sales_roster:
            if s.ID == self.superior:
                return (s.ID, s.name)
        return (None, None)

    def add_superior(self) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        valid_positions = ["Rep", "Manager", "Head"]
        current_index = valid_positions.index(self.position)
        if current_index == len(valid_positions) - 1:
            # Already Head, no superior
            return False
        next_position = valid_positions[current_index + 1]
        for s in sales_roster:
            if s.position == next_position:
                self.superior = s.ID
                return True
        return False

    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        if new_code not in self.branches:
            self.branches.append(new_code)
        return True








