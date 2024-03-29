"""
Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
"""

def make_album(artist,album_title,total_songs=None):
    music_album = {}
    music_album[artist] = album_title
    if total_songs:
        music_album['total_songs'] = total_songs
    return music_album

# print(make_album("Spyro","Holy Ghost",10))
# print(make_album("Mohbad","Feel Good"))
# print(make_album("DotMan","Enu Gbe",7))

"""
Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""

def user_input():
    while True:
        # total_songs=None
        print("A program to input an album’s artist and title")
        print("Enter 'q' to quit.\n")
        artist = input("Name of Artist: ")
        if artist.lower() == 'q':
            break
        album_title = input("Album Title: ")
        if album_title.lower() == 'q':
            break
        print_out = make_album(artist,album_title)
        # else:
        #     print_out = make_album(artist,album_title)
        print(f"{print_out}\n")

user_input()