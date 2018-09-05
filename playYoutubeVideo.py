import webbrowser
import time
total_breaks=0
print("this program started on "+time.ctime())
while(total_breaks<3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=zggQw2wb60M")
    total_breaks=total_breaks+1
