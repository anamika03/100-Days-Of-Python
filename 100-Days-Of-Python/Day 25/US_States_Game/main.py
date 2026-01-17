import turtle

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=800, height=600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Function to get mouse click coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


import pandas
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [states for states in all_states if states not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state].iloc[0]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


# screen.exitonclick()


