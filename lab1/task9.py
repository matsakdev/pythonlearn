def find_min_elements_in_matrix(matrix):
    # for each row
    for row in matrix:
        # we assume that first element is min
        min_element = row[0]
        # for each column
        for element in row:
            if element < min_element:
                # change min element to current
                min_element = element
        print(min_element)