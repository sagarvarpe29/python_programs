#Create movies dictionary object
current_movies = {'DDLJ':'10:00 AM',
                  'Kuch Kuch Hota Hai': '12:30 PM',
                  'Maine Pyar Kiya': '2:45 PM',
                  'ZNMD': '5:30PM'}

#Print the movies that are playing
print("We are showing the following movies")
for key in current_movies:
    print(key)

movie = input("Which movie would you like the showtime for?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, 'is playing at', showtime)