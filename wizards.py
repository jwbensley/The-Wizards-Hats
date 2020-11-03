#! /usr/bin/env python3

import random

def play():

    hats = [
        random.randint(1,10) for i in range(0, 10)
    ]
    print(f"Hats: {hats}")

    predictions = []

    for i in range(0,10):
        total = sum(hats[:i])
        total += sum(hats[i+1:])
        
        total_str = f"Wizard {i+1} sees a total value of {total} ("
        for hat in hats[:i]:
            total_str += f"{hat} + "
        for hat in hats[i+1:]:
            total_str += f"{hat} + "
        total_str = total_str[:-3] + ")"
        print(total_str)

        # Get the last digit of the total value
        unit = total % 10

        if unit > i:
            prediction = (i + 10) - unit
        elif unit < i:
            prediction = i - unit
        else:
            prediction = 0

        #print(f"prediction is {prediction}")
        predictions.append(prediction)

    correct = False
    for i in range(0,10):
        if (predictions[i] + 1) == hats[i]:
            print(f"Wizard {i+1} predicted {predictions[i] + 1} correctly")
            correct = True

    print("")
    return correct


results = {"won": 0, "lost": 0}
for i in range(1,1001):
    result = play()
    if result:
        results["won"] += 1
    else:
        results["lost"] += 1

print(f"{results}")