import random

import time

class Control():


    def __init__(self, tv_status = "off", tv_sound = 0, channel_list = ["AzTv"], channel = "AzTv"):

        self.tv_status = tv_status
        self.tv_sound = tv_sound
        self.channel_list = channel_list
        self.channel = channel

    def tv_open(self):

        if (self.tv_status == "Open"):
            print("TV is already on..")
        else: 
            print("TV opening...")
            self.tv_status = "Open"

    def tv_closed(self):

        if (self.tv_status == "Closed"):
            print("TV is already closed...")
        else:
            print("TV closing...")
            self.tv_status = "Closed"

    def sound_settings(self):

        while True:
            answer = input("Decrease valume: '<'\n Increase valume: '>'\n Exit: exit")

            if (answer == "<"):
                if (self.tv_sound != 0):

                    self.tv_sound -= 1
                    print("Sound:", self.tv_sound)
            elif (answer == ">"):
                if (self.tv_sound != 101):

                    self.tv_sound += 1

                    print("Sound:", self.tv_sound)
            else: 
                print("Sound updated:", self.tv_sound)
                break
    def add_channel(self,channel_name):

        print("Adding chanel.....")
        time.sleep(1)

        self.channel_list.append(channel_name)

        print("Chanel added....")

    def random_channel(self):

        random_index = random.randint(0, len(self.channel_list)-1)

        self.channel = self.channel_list[random_index]

        print("Current cahnnel:", self.channel)

    def __len__(self):

        return len(self.channel_list)

    def __str__(self):

        return "TV status: {}\nTV sound: {}\nChannel list: {}\nCurrent chanel: {}\n".format(self.tv_status, self.tv_sound, self.channel_list, self.channel)

control = Control()
print("""

TV Aplication

1. Turn On TV

2. Turn Off TV

3. Sound Settings

4. Add Channel

5. Get Number of Channels

6. Switch to Random Channel

7. TV Information

Press 'q' to exit.

""")

while True:

    operation = input("Select operation:")

    if (operation == "q"):
        print("Closing aplication....")
        break
    elif (operation == "1"):
        control.tv_open()

    elif (operation == "2"):
        control.tv_closed()

    elif (operation == "3"):
        control.sound_settings()

    elif (operation == "4"):
        channel_name = input("Enter channel names separated by ',':")

        channel_list = channel_name.split(",")

        for ch in channel_list:
            control.add_channel(ch)

    elif (operation == "5"):

        print("Number of channels: ", len(control))

    elif (operation == "6"):
        control.random_channel()
    elif (operation == "7"):
        print(control)

    else:
        print("Invaklid operation...")



