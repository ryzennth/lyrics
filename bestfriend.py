import sys
import time

def jalanin_lirik():
    lirik = [
        "I say that I'm happy",
        "I say that I'm happy",
        "But no, no, no, no",
        "No, no, no",
        "Oh, I still wanna be your favorite boy",
        "I wanna be the one that makes your day",
        "The one you think about as you lie awake",
        "And I can't wait to be your number, your number one",
        "I'll be your biggest fan and you'll be mine",
        "But I still wanna break your heart and make you cry",
    ]

    print("\n==Best Friend - Rex Orange County==")
    time.sleep(2)
    for baris in lirik:
        for karakter in baris:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(0.3)
        print('')
    print("//code by zan")

jalanin_lirik()
