def grade_calculaor(row):


    row = row[:-1]

    list = row.split(",")

    name = list[0]

    grade1 = int(list[1])

    grade2 = int(list[2])

    grade3 = int(list[3])

    final_grade = grade1 * (3/10) + grade2 * (3/10) + grade3 * (4/10)

    if (final_grade >= 90):

        letter = "AA"
    elif (final_grade >= 85):
        letter = "BA"
    elif (final_grade >= 80):
        letter = "BB"
    elif (final_grade >= 75):
        letter = "CB"
    elif (final_grade >= 70):
        letter = "CC"
    elif (final_grade >= 65):
        letter = "DC"
    elif (final_grade >= 60):
        letter = "DD"
    elif (final_grade >= 55):
        letter = "FD"
    else:
        letter = "FF"

    return name + "------------------> " + letter + "\n"







with open("file.txt","r",encoding= "utf-8") as file:

    items_to_add = []

    for i in file:

        items_to_add.append(grade_calculaor(i))

    with open("gradaes.txt","w",encoding="utf-8") as file2:

        for i in items_to_add:
            file2.write(i)



