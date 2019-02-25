import threading
import os
import time

def tester(input):
    video_720p = "ffmpeg -i " + input + " -b:v 2M -r 30 -s hd720 720v.mp4"
    video_480p = "ffmpeg -i " + input + " -b:v 1M -r 30 -s hd480 480v.mp4"

    start1 = time.time()
    os.system(video_720p)
    end1 = time.time()
    start2 = time.time()
    os.system(video_480p)
    end2 = time.time()
    print("it took")
    print(end1 - start1)
    print("seconds for the 720 video to be created")
    print(end2 - start2)
    print("seconds for the 480 video to be created")

tester("ec500test.mp4")
