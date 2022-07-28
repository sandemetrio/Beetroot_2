# Task_1

class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.name} {self.surname}, I am {self.age} years old!")

# Task_2
class Dog():
    AGE_FACTOR = 7

    def __init__(self, nickname, age):
        self.nick = nickname
        self.age = age

    def human_age(self):
        return print(f'If {self.nick} was a human, it would be {self.age * self.AGE_FACTOR}')

# TAsk_3
class TVControler():
    CHANNELS = ["BBC", "Discovery", "TV1000", "History", "QTV", "M'one"]
    index_chan = 0

    def current_channel(self):
        return f'The current channel is #{self.index_chan + 1} "{self.CHANNELS[self.index_chan]}"'

    def turn_channel(self, N):
        self.index_chan = N - 1
        try:
            return self.current_channel()
        except IndexError:
            return f' Channel {N} not exist!'

    def first_channel(self):
        self.index_chan = 0
        return self.current_channel()

    def last_channel(self):
        self.index_chan = len(self.CHANNELS) - 1
        return self.current_channel()

    def next_channel(self):
        try:
            self.index_chan in range(len(self.CHANNELS))
            self.index_chan += 1
            return self.current_channel()
        except IndexError:
            return self.first_channel()

    def previous_channel(self):
        try:
            self.index_chan in range(1, len(self.CHANNELS))
            self.index_chan -= 1
            return self.current_channel()
        except IndexError:
            return self.last_channel()

    def is_exist(self, chan):
        if type(chan) == int:
            return self.turn_channel(chan)
        else:
            if str(chan) in self.CHANNELS:
                self.index_chan = self.CHANNELS.index(str(chan))
                return self.current_channel()
            return f' Channel {chan} not exist!'

def main():
    # task_1
    cj = Person("Carl", "Johnson", 25)
    cj.talk()

    # task_2
    dog_1 = Dog("Flafy", 6)
    dog_1.human_age()

    # task_3
    controler = TVControler()


    controler.first_channel()
    controler.current_channel()
    controler.first_channel()
    controler.current_channel()
    controler.last_channel()
    controler.turn_channel(6)
    controler.current_channel()
    controler.is_exist("History")
    print(controler.is_exist("History"))


if __name__ == "__main__":
    main()
