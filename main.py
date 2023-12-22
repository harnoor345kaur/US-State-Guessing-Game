import turtle
from turtle import Screen
import pandas

screen = Screen()
screen.title("US State Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
df = pandas.DataFrame(data)
list_states = df["state"].tolist()
guessed_state = []

i = 0
while len(guessed_state) < 50:
    answer_state_i = screen.textinput(title = f"Score: {i}/50   Guess the state: ", prompt = "What is the guess ? ")
    answer_state_i2 = []
    for j in range(1,len(answer_state_i)):
        word = answer_state_i[j].lower()
        answer_state_i2.append(word)
    answer_state = answer_state_i[0].upper() + ("".join(answer_state_i2))

    if answer_state in list_states and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        x_cor = int(data[data.state == answer_state].x)
        y_cor = int(data[data.state == answer_state].y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.setpos((x_cor, y_cor))
        t.write(f"{answer_state}", font = ("Courier", 18, "normal"))
        i += 1

    if answer_state == "Exit":
        missing_states = []
        for x in list_states:
            if x not in guessed_state:
                missing_states.append(x)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

screen.exitonclick()




    







# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
