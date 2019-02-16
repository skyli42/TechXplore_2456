import csv

def get_sequence(text: str) -> str:
    t = text[8:]
    return t.strip()

def get_name(text: str) -> str:
    t = text[12:]
    return t.strip()
def get_classification(text: str) -> str:
    t = text[37:]
    return t.strip()

with open('Big.txt', 'r') as file:
    text = file.readlines()
    name = ''
    sequence = ''
    classification = ''
    counter = 0


    for line in text:
        if counter == 1:
            name = get_name(line)
        elif counter == 8:
            sequence = get_sequence(line)
        elif counter == 9:
            classification = get_classification(line)
            #TODO: Save in a csv file
            with open('data.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([name, sequence, classification])
            print(name, sequence, classification)

        counter += 1

        if line[0] == '_':
            counter = -1


