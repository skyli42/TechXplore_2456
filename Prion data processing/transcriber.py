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
        if counter == 0:
            name = get_name(line)
        elif counter == 8:
            sequence = get_sequence(line)
        elif counter == 9:
            classification = get_classification(line)
            #TODO: Save in a csv file
            with open('data.csv', 'a') as csvfile:
                line = '%s,%s,%s' % (name, sequence, classification)
                csvfile.write(line)
                csvfile.write('\n')
                csvfile.close()
            print(name, sequence, classification)

        counter += 1

        if line[0] == '_':
            counter = -1


