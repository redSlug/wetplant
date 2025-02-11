import pywhatkit

receiver_phone_number = "+0016509991124"
message_to_send = "Hello World!"

print('about to send message');
pywhatkit.sendwhatmsg_instantly(receiver_phone_number, message_to_send)
print('sent message')