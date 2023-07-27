######################
# Question 1: Artist #
######################

'''
class Artist:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    
    # Accesors
    
    def get_name(self):
        return self.name
    
    def get_dob(self):
        return self.dob
    
jt = Artist("Justin Timberlake", (1981, 1, 31))
'''

# print(jt.get_name())
# print(jt.get_dob())

##########################
# Question 2: Artist Age #
##########################

class Artist:
    def __init__(self, name, dob):
        self._name = name
        self._dob = dob
        
    def get_name(self):
        return self._name
    
    def get_dob(self):
        return self._dob
        
    def age(self):
        # your code here
        
        if self._dob[1] > get_date_today()[1]:
            return get_date_today()[0] - self._dob[0] - 1
        else:
            return get_date_today()[0] - self._dob[0]
        
        
def get_date_today():
    return (2013, 10, 30)

jt = Artist("Justin Timberlake", (1981, 1, 31))

# print(Artist('Hayley Williams', (1988, 12, 27)).age())

# print(jt.age())

########################
# Question 3: Duration #
########################

class Duration:
    def __init__(self, minutes, seconds):
        self._total_seconds = minutes * 60 + seconds
    
    def get_minutes(self):
        return self._total_seconds // 60
    
    def get_seconds(self):
        return self._total_seconds % 60
    
##############################################
# Question 4: Duration String Representation #
##############################################

    def __str__(self):
        return f"{self.get_minutes():02d}:{self.get_seconds():02d}"
        
# print(str(Duration(3, 20)))
# print(str(Duration(0,0)))
# print(str(Duration(103,20)))

##################################
# Question 5: Duration Operators #
##################################

    def __add__(self, newDuration):
        return Duration(self.get_minutes() + newDuration.get_minutes(), self.get_seconds() + newDuration.get_seconds())
    
####################
# Question 6: Song #
####################

class Song:
    def __init__(self, artist, title, duration):
        self._artist = artist
        self._title = title
        self._duration = duration
        
    # Accessors
    
    def get_artist(self):
        # Fill in your code here
        return self._artist
    
    def get_title(self):
        # Fill in your code here
        return self._title
        
    def get_duration(self):
        # Fill in your code here
        return self._duration

#####################
# Question 7: Album #
#####################

class Album:
    def __init__(self, artist, title):
        self._artist = artist
        self._title = title
        self._songs = []
    
    def add_song(self, song):
        self._songs.append(song)
        
    def total_runtime(self):
        total_duration = Duration(0, 0)
        for song in self._songs:
            total_duration += song._duration
        return total_duration