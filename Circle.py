def CircleArea(CirclePara):
    Answer = 3.14159 * CirclePara * CirclePara
    print(round(Answer,1))
UserInput = int(input("Circle Radius here"))

CircleArea(UserInput)