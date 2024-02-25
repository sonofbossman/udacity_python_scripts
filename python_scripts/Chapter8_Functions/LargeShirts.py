Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.


def make_shirt(size, text):
    print(f'The shirt is {size} in size with "{text}" printed on it.')

make_shirt("Medium", "SonofBossman")
make_shirt(text="Hakingbacrown", size="Large")