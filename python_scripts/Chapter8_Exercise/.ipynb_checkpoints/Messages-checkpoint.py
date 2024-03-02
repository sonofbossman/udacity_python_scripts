"""
Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
"""

messages = [
    "Hi, How're you doing?",
    "Howdy Partner, have you completed the task?",
    "I just got home.",
    "Knock! Knock!! You got a package!"
]

# def show_messages(messageList):
#     for message in messageList:
#         print(message)

# show_messages(messages)

"""
Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
"""

sent_messages = []
def send_messages(messageList):
    while messageList:
        message = messageList.pop()
        sent_messages.append(message)
        print(message)

# send_messages(messages)
# print("\nTesting...\n")
# print(f"{messages}\n")
# print(sent_messages)

"""
Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.
"""

send_messages(messages[:])
print("\nTesting...\n")
print(f"{messages}\n")
print(sent_messages)