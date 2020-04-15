
def calculated_start_col(seating_2d_array) :
    seating_col_start = []
    initialize_col = 0
    for seats_idx, seats_array in enumerate(seating_2d_array):
        number_of_columns = seats_array[0]
        seating_col_start.append(initialize_col)
        initialize_col = initialize_col + number_of_columns
    return seating_col_start


def allocate_seat_obj(seating_2d_array):
    max_seat_row = 0
    max_seat_col = 0
    window_seat_obj = {}
    aisle_seat_obj = {}
    middle_seat_obj = {}
    windows_count = 0
    aisle_count = 0
    middle_count = 0
    len_seating_2d_array = len(seating_2d_array)
    for seats_idx, seats_array in enumerate(seating_2d_array):
        number_of_columns = seats_array[0]
        number_of_rows = seats_array[1]
        max_seat_col = max_seat_col + number_of_columns


        windows_array = []
        aisle_array = []
        middle_array = []
        if seats_idx == 0:  # left window
            windows_array.append({'seats_index': seats_idx, 'col' : 0, 'passenger_id': None})

            remaining_number_of_cols = number_of_columns - 1

            if remaining_number_of_cols == 0:
                pass
            elif remaining_number_of_cols == 1:
                aisle_array.append({'seats_index': seats_idx, 'col' : 1, 'passenger_id': None})
            else:
                col_index = 1
                col_count = 0
                while col_count < remaining_number_of_cols - 1:
                    middle_array.append({'seats_index': seats_idx, 'col' : col_index, 'passenger_id': None})
                    col_index = col_index + 1
                    col_count = col_count + 1
                aisle_array.append({'seats_index': seats_idx, 'col' : col_index, 'passenger_id': None})

        elif seats_idx == len_seating_2d_array - 1:  # right window

            windows_array.append({'seats_index': seats_idx, 'col' : number_of_columns-1, 'passenger_id': None})

            remaining_number_of_cols = number_of_columns - 1
            if remaining_number_of_cols == 0:
                pass
            elif remaining_number_of_cols == 1:
                aisle_array.append({'seats_index': seats_idx, 'col' : 0, 'passenger_id': None})
            else:
                aisle_array.append({'seats_index': seats_idx, 'col' : 0, 'passenger_id': None})
                col_index = 1
                col_count = 0
                while col_count < remaining_number_of_cols - 1:
                    middle_array.append({'seats_index': seats_idx, 'col' : col_index, 'passenger_id': None})
                    col_index = col_index + 1
                    col_count = col_count + 1
        else:  # other seats array
            if number_of_columns == 1:
                aisle_array.append({'seats_index': seats_idx, 'col' : 0, 'passenger_id': None})
            elif number_of_columns == 2:
                aisle_array.append({'seats_index': seats_idx, 'col' : 0, 'passenger_id': None})
                aisle_array.append({'seats_index': seats_idx, 'col' : 1, 'passenger_id': None})
            else:
                aisle_array.append({'seats_index': seats_idx, 'col' : 0, 'passenger_id': None})
                aisle_array.append({'seats_index': seats_idx, 'col' : number_of_columns-1, 'passenger_id': None})
                col_index = 1
                col_count = 0
                remaining_number_of_cols = number_of_columns - 2
                while col_count < remaining_number_of_cols:
                    middle_array.append({'seats_index': seats_idx, 'col' : col_index, 'passenger_id': None})
                    col_index = col_index + 1
                    col_count = col_count + 1

        for row in range(number_of_rows):
            if max_seat_row < (row+1) :
                max_seat_row = (row+1)


            if row in window_seat_obj.keys():
                window_seat_obj[row] = window_seat_obj[row] + windows_array

            else:
                window_seat_obj[row] = windows_array

            windows_count = windows_count + len(windows_array)

            if row in aisle_seat_obj.keys():
                aisle_seat_obj[row] = aisle_seat_obj[row] + aisle_array
            else:
                aisle_seat_obj[row] = aisle_array

            aisle_count = aisle_count + len(aisle_array)
            if row in middle_seat_obj.keys():
                middle_seat_obj[row] = middle_seat_obj[row] + middle_array
            else:
                middle_seat_obj[row] = middle_array

            middle_count = middle_count + len(middle_array)

    return {"window_obj": {"seat_obj": window_seat_obj, "seat_count": windows_count},
            "middle_obj": {"seat_obj": middle_seat_obj, "seat_count": middle_count},
            "aisle_obj": {"seat_obj": aisle_seat_obj, "seat_count": aisle_count}} , max_seat_row, max_seat_col

def flattern_seat_obj (seat_obj, type) :
    seat_arr = []
    for row in seat_obj.keys() :
        for seat_info in seat_obj[row] :
            new_seat_info = dict({'row': row, 'type': type}, **seat_info)
            seat_arr.append(new_seat_info)
    return seat_arr

def passenger_seat_in(passenger_number, windows,middle, aisle):
    seat_array = []

    seat_array = seat_array + flattern_seat_obj(aisle, 'a') + flattern_seat_obj(windows, 'w') + \
                 flattern_seat_obj(middle, 'm')

    passenger_id = 1
    while passenger_id <= passenger_number:
        seat_array[passenger_id - 1]['passenger_id'] = passenger_id
        passenger_id = passenger_id + 1

    return seat_array

def print_grid (seating_grid, plan, max_row, max_col) :
    # grid = [['XX'] * max_col] * max_row
    grid = [['XX'for i in range(max_col)] for j in range(max_row)]
    col_start_array = calculated_start_col(seating_grid)
    for seat_information in plan :
        row = seat_information['row']
        type_of_seat = seat_information['type']
        seats_index = seat_information['seats_index']
        passengerr_id = seat_information['passenger_id']
        if passengerr_id is None :
            passengerr_id = "X"
        col = seat_information['col']
        calculated_col = col_start_array[seats_index]
        # print(passengerr_id, row, calculated_col+col, col)
        # print(f'{type_of_seat.upper()}{passengerr_id}')
        # print(grid[row][calculated_col+col])
        grid[int(row)][int(calculated_col+col)] = f'{type_of_seat.upper()}{passengerr_id}'

    print('\n'.join([''.join(['{:4}'.format(item) for item in row_in_grid])
                     for row_in_grid in grid]))

    f = open("result.txt", "w")
    f.write('\n'.join([''.join(['{:4}'.format(item) for item in row_in_grid])
                     for row_in_grid in grid]))
    f.close()
    return grid

def run_main(passenger_number, seating_grid) :
    # allocate seat types to each seat position
    seating_obj, max_row, max_col = allocate_seat_obj(seating_grid)

    window_seat_obj = seating_obj["window_obj"]["seat_obj"]
    middle_seat_obj = seating_obj["middle_obj"]["seat_obj"]
    aisle_seat_obj = seating_obj["aisle_obj"]["seat_obj"]

    # allow passenger seat in
    seatings_plan = passenger_seat_in(passenger_number, window_seat_obj, middle_seat_obj, aisle_seat_obj)

    # print out passa
    gd = print_grid(seating_grid,seatings_plan, max_row, max_col)

    return gd

if __name__ == "__main__" :

    input_seating_grid = [[3, 2], [4, 3], [2, 3], [3, 4]]
    input_passenger_num = 30

    output_grid = run_main(input_passenger_num, input_seating_grid)
