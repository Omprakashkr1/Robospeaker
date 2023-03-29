import pyttsx3
if __name__ == '__main__':
    print(".............welcome to Robospeaker..........")
    while True:
        st = input("enter what you want me to pronounce : ")
        engine = pyttsx3.init()
        engine.say(st)
        engine.runAndWait()
        opt=input("do you want to repeat(y/n):")
        if opt == 'n':
            break

