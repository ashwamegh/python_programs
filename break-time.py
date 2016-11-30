import webbrowser
import time

total_breaks=3
break_count=0

print("This program was started on"+time.ctime())
while break_count<total_breaks:
     time.sleep(10)
     webbrowser.open("https://www.youtube.com/watch?v=ZFQM5yV0aHchttps://www.youtube.com/watch?v=ZFQM5yV0aHc")
     break_count=break_count+1
