weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
# temp_f = (temp_c * 9/5) + 32

weather_f = {x:(y * 9/5) + 32 for x,y in weather_c.items()}


print(weather_f)
