# data_dict = {
#     "states": ["Edirne", "Kırklareli", "Tekirdağ", "İstanbul", "Kocaeli", "Yalova", "Bursa", "Balıkesir", "Çanakkale",
#                "Manisa", "İzmir", "Aydın", "Muğla", "Kütahya", "Uşak", "Denizli", "Burdur", "Antalya", "Isparta",
#                "Afyon", "Eskişehir", "Bilecik", "Sakarya", "Düzce", "Bolu", "Ankara", "Konya", "Karaman", "Mersin",
#                "Niğde", "Aksaray", "Nevşehir", "Kırşehir", "Kırıkkale", "Çankırı", "Karabük", "Zonguldak", "Bartın",
#                "Kastamonu", "Sinop", "Çorum", "Yozgat", "Kayseri", "Adana", "Amasya", "Samsun", "Ordu", "Tokat",
#                "Sivas", "Kahramanmaraş", "Osmaniye", "Hatay", "Kilis", "Gaziantep", "Adıyaman", "Malatya", "Giresun",
#                "Gümüşhane", "Trabzon", "Bayburt", "Erzincan", "Tunceli", "Elazığ", "Diyarbakır", "Şanlıurfa", "Mardin",
#                "Batman", "Bingöl", "Erzurum", "Rize", "Artvin", "Ardahan", "Kars", "Iğdır", "Ağrı", "Muş", "Bitlis", "Siirt", "Şırnak", "Hakkari", "Van"],
#     "coordinate_x": [-629, -564, -593, -495, -406, -451, -485, -580, -655, -567, -617, -592, -569, -465, -473, -480,
#                      -426, -397, -356, -390, -359, -403, -367, -318, -301, -218, -246, -174, -138, -69, -134, -60, -104,
#                      -138, -162, -215, -271, -218, -142, -51, -71, -29, 8, -14, 7, 17, 129, 62, 111, 88, 54, 57, 118,
#                      139, 182, 172, 206, 270, 290, 330, 259, 274, 266, 348, 262, 387, 428, 370, 418, 372, 435, 506,
#                      528, 595, 543, 456, 476, 483, 508, 616, 591],
#     "coordinate_y": [274, 319, 263, 270, 232, 209, 160, 126, 162, 44, 1, -51, -101, 81, 16, -47, -85, -128, -56, 25,
#                      115, 159, 215, 229, 194, 148, -16, -112, -162, -42, -11, 28, 83, 130, 210, 252, 263, 296, 293, 300,
#                      197, 117, 21, -104, 213, 261, 233, 180, 117, -38, -107, -189, -145, -120, -52, 22, 213, 192, 239,
#                      189, 131, 80, 25, -17, -108, -85, -33, 73, 168, 249, 281, 279, 220, 174, 137, 75, 24, -24, -64, -46, 22]
# }
#
# df = pd.DataFrame(data_dict)
# df.to_csv("81_states.csv")

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Turkey States Game")
screen.setup(width=1500, height=700)

image = "turkey_states.gif"
screen.addshape(image)
turtle.shape(image)
guessed = []

while len(guessed) < 81:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="What's another state's name?").title()
    data = pd.read_csv("81_states.csv")
    states = data.states.to_list()

    if answer_state == "Exit":
        missing = []
        for x in states:
            if x not in guessed:
                missing.append(x)
        new_data = pd.DataFrame(missing)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(int(state_data.coordinate_x), int(state_data.coordinate_y))
        t.write(answer_state)
