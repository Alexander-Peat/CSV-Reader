#example file:
#C:\Users\ajpea\Things I've Written Or Created\New Python Programs\example.txt

file_to_open = r""
file_to_open = str(input(r"Enter the name of the file to open (include full path and '.csv' extension): "))

with open(file_to_open) as csv_file:
    line_array = csv_file.read().splitlines()

#print(line_array)

no_columns = int(line_array[0].count('"') / 2)
no_rows = len(line_array) - 1

def read_header(line_array_f, no_columns_f):
    raw_header = line_array_f.pop(0)

    headers = []

    for loop in range(no_columns_f):
        raw_header = raw_header[1:]

        header = ""
        
        while raw_header[0] != '"':
            header = header + raw_header[0]
            raw_header = raw_header[1:]

        raw_header = raw_header[1:]

        if len(raw_header) > 0 and raw_header[0] == ",":
            raw_header = raw_header[1:]

        headers.append(header)

    return line_array_f, headers

line_array, headers = read_header(line_array, no_columns)

#print(line_array)
#print(headers)

def process_row(unprocessed_row, no_columns_f):
    processed_row_f = [""] * no_columns_f

    for loop in range(no_columns_f):
        cell = ""

        while len(unprocessed_row) > 0 and unprocessed_row[0] != ",":
            cell = cell + unprocessed_row[0]
            unprocessed_row = unprocessed_row[1:]

        processed_row_f[loop] = cell

        if len(unprocessed_row) > 0 and unprocessed_row[0] == ",":
            unprocessed_row = unprocessed_row[1:]

    return processed_row_f

processed_rows = [""] * no_rows

for loop in range(no_rows):
    processed_rows[loop] = process_row(line_array[loop], no_columns)

#print(headers)
#print(processed_rows)

max_lengths = [0] * no_columns

for column_index in range(no_columns):
    max_length = 0

    for row_index in range(no_rows):
        if len(processed_rows[row_index][column_index]) > max_length:
            max_length = len(processed_rows[row_index][column_index])

    if len(headers[column_index]) > max_length:
        max_length = len(headers[column_index])

    max_lengths[column_index] = max_length

#print(max_lengths)

max_number_column_width = len(str(no_rows))

header_string = ""

for loop in range(max_number_column_width):
    header_string = header_string + "/"

header_string = header_string + "|"

for loop in range(len(headers)):
    no_spaces = 0
    
    if len(headers[loop]) < max_lengths[loop]:
        no_spaces = max_lengths[loop] - len(headers[loop])

    if no_spaces < 0:
        no_spaces = 0

    header_string = header_string + headers[loop]

    for loop in range(no_spaces):
        header_string = header_string + " "
    
    header_string = header_string + "|"

seperating_line = ""

for loop in range(len(header_string)):
    seperating_line = seperating_line + "="

print(seperating_line)
print(header_string)
print(seperating_line)

content_lines = [""] * no_rows

for loop1 in range(no_rows):
    #content_lines[loop1] = content_lines[loop1] + str(loop1 + 1) + "|"

    for loop3 in range(max_number_column_width - len(str(loop1 + 1))):
        content_lines[loop1] = content_lines[loop1] + "0"

    content_lines[loop1] = content_lines[loop1] + str(loop1 + 1)
    content_lines[loop1] = content_lines[loop1] + "|"

    for loop2 in range(no_columns):
        no_zeros = 0
        content_lines[loop1] = content_lines[loop1] + processed_rows[loop1][loop2]

        if len(processed_rows[loop1][loop2]) < max_lengths[loop2]:
            no_zeros = max_lengths[loop2] - len(processed_rows[loop1][loop2])

        if no_zeros < 0:
            no_zeros = 0

        for loop in range(no_zeros):
            content_lines[loop1] = content_lines[loop1] + " "

        content_lines[loop1] = content_lines[loop1] + "|"

for loop in range(len(content_lines)):
    print(content_lines[loop])

print(seperating_line)
