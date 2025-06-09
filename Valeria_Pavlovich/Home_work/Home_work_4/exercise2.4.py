import time
import winsound
seconds_input = int(input('Enter time in seconds: '))
start_time = time.time()
for i in range(seconds_input, 0, -1):
    minutes = i // 60
    seconds = i % 60
    print(f'Time: {minutes:02d}:{seconds:02d}')
    winsound.Beep (1000, 300)
    time.sleep(0.7)
print('Start!')
winsound.Beep (1000, 1000)
