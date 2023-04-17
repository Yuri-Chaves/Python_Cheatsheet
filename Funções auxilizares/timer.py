import time
start = time.time()
end = time.time()
print('{: ^11} timer {:02}:{:02} {: ^11}'.format('', int((end-start)/60), int((end-start)-((int((end-start) / 60))*60)), ''))
for i in range(118):
    time.sleep(.45)
    end = time.time()
    print('{: ^11} timer {:02}:{:02} {: ^11}'.format('', int((end-start)/60), int((end-start)-((int((end-start) / 60))*60)), ''))