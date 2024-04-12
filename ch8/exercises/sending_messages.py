def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        message = unsent_messages.pop()
        print(f"\nSending message:\n {message}")
        sent_messages.append(message)
    

def show_messages(messages):
    if messages:
        for message in messages:
           print(message)
    else:
        print("\nMessage queue is empty\n")

my_msgs = ['Hey, are you free today??', 'ttyl', 'Did you get milk at the store?']
sent_msgs = []

print("Message queue:")
show_messages(my_msgs)
send_messages(my_msgs,sent_msgs)

print("Message queue:")
show_messages(my_msgs)

print("Sent Messages:")
show_messages(sent_msgs)