from essential_generators import DocumentGenerator
import time
import keyboard
accuracy = 0
wrong = 0
sped = 0
words  = 1
x = DocumentGenerator().sentence()
print(x)
event = keyboard.read_event()
y = ""
event  = keyboard.read_event()

for i in range(len(x)):
    
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == "backspace":
            y = y[:-1]

        # space
        elif event.name == "space":
            y += " "
        elif len(event.name) == 1:
            y += event.name
        print(y,end="")


for i in range(len(x)):
    if x[i] == y[i]:
        accuracy += 1
        if x[i] == " ":
            words += 1
    else:
        wrong += 1
print(accuracy)
print(words)
print(wrong)
print(len(x))