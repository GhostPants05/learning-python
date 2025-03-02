import random
import time
x=1
while x <= 10:
    value = random.randint(0,4)
    value1 = random.randint(0,5)
    name = ['Paul', 'Richard', 'Frank', 'Anne', 'Sarah']
    random_name = name[value]
    emotion = ['happy', 'sad', 'mad', 'triggered', 'cute', 'emotional']
    random_emotion = emotion[value1]
    print(random_name, 'why are you so', random_emotion, '?')
    x += 1
    time.sleep(1)