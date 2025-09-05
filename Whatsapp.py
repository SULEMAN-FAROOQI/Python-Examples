# Whatsapp message sender:

# Sending an instant message:

'''

import pywhatkit

phone_number = "+1234567890"  # Include country code
message = "Hello from PyWhatKit!"
pywhatkit.sendwhatmsg_instantly(phone_number, message)

'''

# Scheduling a message to be sent at a specific time:

'''

import pywhatkit

phone_number = "+1234567890"
message = "This message will be sent later."
hour = 17  # 5 PM in 24-hour format
minute = 30
pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

'''

# Sending an image to a group:

'''

import pywhatkit

group_name = "My WhatsApp Group"
image_path = "path/to/your/image.png"
caption = "Check out this image!"
pywhatkit.sendwhats_image(group_name, image_path, caption)

'''

# Playing YouTube Videos:

# Playing a specific video by its title:

'''

import pywhatkit

video_title = "Python tutorial for beginners"
pywhatkit.playonyt(video_title)

'''

# Performing Google Searches:

# Searching for a keyword:

'''

import pywhatkit

keyword = "PyWhatKit library"
pywhatkit.search(keyword)

'''

# Getting Information from Wikipedia:

#Retrieving information on a topic:

'''
import pywhatkit

topic = "Artificial Intelligence"
lines_to_print = 5  # Limit the output to 5 lines
pywhatkit.info(topic, lines=lines_to_print)

'''