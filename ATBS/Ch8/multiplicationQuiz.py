#!/usr/bin/env python3

import pyinputplus as pyip
import random
import time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = f"{questionNumber}: {num1} x {num2} = "
    try:
        # Right answers are handled by allowregexes
        # wrong answers are handled by blockregexes with custom message
        pyip.inputStr(prompt, allowRegexes=[f'^{(num1 * num2)}$'],
                      blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)  # brief pause to let user see result
print(f"Score: {correctAnswers} / {numberOfQuestions}")
