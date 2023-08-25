

class person:
    
    def __init__(self, age = None, gender = None, verbose = 1):
        if age is None:
            if verbose: print('Default constructor called')
        else:
            self.age = age
            if verbose: print('Parameterized constructor called with age ', self.age)
        if gender is None:
            if verbose: print('Default constructor called')
        else:
            self.gender = gender
            if verbose: print('Parameterized constructor called with gender ', self.gender)



    def getGender(self):
        if hasattr(self, 'gender'):
            return self.gender
        else:
            print('This person has not gender yet')

    def setGender(self, Gender: str):
        if type(Gender) != str: raise Exception('Gender must be a str object')
        if ((str(Gender) != 'male') and (str(Gender) != 'female') and (str(Gender) != 'other')): raise Exception('Gender must either male, female or other')
        self.gender = Gender
    
    def setAge(self, Age):
        self.age = Age
    
    def getAge(self):
        if hasattr(self, 'age'):
            return self.age
        else:
            print('This person has not age yet')

    def HoldHand(self):
        if hasattr(self, 'age'):
            if (self.age >= 18):
                print('You are holding hands with ' + self.name)
            else:
                print(self.name + ' is too young to hold handswith him/her')
        else:
            print('This person has not age defined, set the age with person.setAge()')


class waifu(person):

    def __init__(self, name=None):
        if type(name) != str: raise Exception('Gender must be a str object')

        if name is None:
            print('Default constructor called')
        else:
            self.name = name
            print('Parameterized constructor called with name', self.name)
    
    def method(self):
        if hasattr(self, 'name'):
            print('Method called with name', self.name)
        else:
            print('Method called without a name')

    def setName(self, name):
        if hasattr(self, 'name'):
            print('You cannot change the name of your waifu')
        else:
            if type(name) != str: raise Exception('Gender must be a str object')
            self.name = name
            print('The name of your waifu is now', self.name) 
            
    def getName(self):
        if hasattr(self, 'name'):
            return self.name
        else:
            print('This person has no name yet')

    
class husbando(person):
    gender = 'male'
    def __init__(self, name=None):
        if name is None:
            print('Default constructor called')
        else:
            self.name = name
            print('Parameterized constructor called with name', self.name)
    
    def method(self):
        if hasattr(self, 'name'):
            print('Method called with name', self.name)
        else:
            print('Method called without a name')

    def setName(self, name):
        if hasattr(self, 'name'):
            print('You cannot change the name of your waifu')
        else:
            self.name = name
            print('The name of your waifu is now', self.name) 
    def getName(self):
        return self.name