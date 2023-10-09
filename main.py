
file_paths = ['viesis.txt', 'admin.txt']

with open('output-file.txt', 'w', encoding='utf-8') as output_file:
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            for line in input_file:
                output_file.write(line)



file = open('viesis.txt', 'w')

cilvēki = ['Elizabete', 'Deniss', 'Marija', 'Nikolajs']
vecums = [32, 34, 25, 24]

for i in range(0, 4):
    entry = cilvēki[i] + "-" + str(vecums[i])+'\n'
    file.write(entry)



file = open('admin.txt', 'w')

cilvēki = ['Zoja', 'Markuss', 'Mareks', 'Samanta']
vecums = [20, 35, 29, 37]

for i in range(0, 4):
    entry = cilvēki[i] + "-" + str(vecums[i])+'\n'
    file.write(entry)

numbers = [32, 34, 25, 24, 20, 35, 29, 37]
sumOfNums = 0
count = 0
for number in numbers:
    sumOfNums += number
    count += 1
average = sumOfNums / count
print("Vecumi: ", numbers)
print("Vidējais vecums:", average)



with open("output-file.txt", "a") as f:
  print(" ", file=f)
  print("Vecumi: 32, 34, 25, 24, 20, 35, 29, 37", file=f)
  print("Vid. vecums: 29.5", file=f)



def oldest_student(students):
	return max(students, key=students.get)

print(oldest_student({"Elizabete-32": 32, "Deniss-34": 34,
                      "Marija-25": 25, "Nikolajs-24": 24,
                      "Zoja-20": 20, "Markuss-35": 35,
                      "Mareks-29": 29, "Samanta-37": 37,}))

def youngest_student(students):
	return min(students, key=students.get)

print(youngest_student({"Elizabete-32": 32, "Deniss-34": 34,
                      "Marija-25": 25, "Nikolajs-24": 24,
                      "Zoja-20": 20, "Markuss-35": 35,
                      "Mareks-29": 29, "Samanta-37": 37,}))

with open("output-file.txt", "a") as f:
  print("Max. vecums: Samanta-37", file=f)
  print("Min. vecums: Zoja-20", file=f)






