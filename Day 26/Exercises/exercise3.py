with open("file1.txt") as file1:
    file1_numbers = file1.readlines()
with open("file2.txt") as file2:
    file2_numbers = file2.readlines()

file1_numbers = [x.replace("\n", "") for x in file1_numbers]
file2_numbers = [x.replace("\n", "") for x in file2_numbers]
result = [int(x) for x in file1_numbers if x in file2_numbers]
print(result)