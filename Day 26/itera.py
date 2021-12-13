import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

studen_data_frame = pd.DataFrame(student_dict)
# print(studen_data_frame)

#Loop thorugh data frame

# for (key,value) in studen_data_frame.items():
#     print(value)

# Loop through rows a data frame

for(index, row) in studen_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)