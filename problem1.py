# # print('''Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
# # like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
# # When the blazing sun is set, and the grass with dew is wet. Then you show your little
# # light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
# # are.
# # Then the traveler in the dark thanks you for your tiny spark. How could he see where to
# # go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
# # As your bright and tiny spark lights the traveler in the dark, though I know not what you
# # are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are''')
# import pyttsx3
# engine = pyttsx3.init()
# engine.say(" twinkle twinkle little star how I wonder what you are up above the world so high like a diamond in the sky " 
# "twinkle twinkle little star how I wonder what you are when the blazing sun is set and the grass with dew is wet then you " 
# "show your little light twinkle twinkle all the night twinkle twinkle little star how I wonder what you are then the traveler"
# " in the dark thanks you for your tiny spark how could he see where to go if you did not twinkle so twinkle twinkle little " 
# "star how I wonder what you are as your bright and tiny spark lights the traveler in the dark though I know not what you are" 
# " twinkle twinkle little star twinkle twinkle little star how I wonder what you are")
# engine.runAndWait()
import os

# # Specify the directory path
# directory_path = '/new folder'  # Change this to your desired directory path

# # Check if the directory exists
# if os.path.exists(directory_path) and os.path.isdir(directory_path):
#     print(f"\nContents of '{directory_path}':\n")
    
#     # List directory contents
#     for item in os.listdir(directory_path):
#         print(item)
# else:
#     print("Invalid directory path.")