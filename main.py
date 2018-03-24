import multiplications_of_first_x_odd_numbers, get_common_elements, delete_even_elements

def main():
    try:
        delete_even_elements.delete_even_elements_lower_than_x([1,2,2,2,3,4,4,4,5], 3)
        multiplications_of_first_x_odd_numbers.multiplications_of_first_x_odd_numbers(5,0)
        get_common_elements.get_common_elements([1,9,7,10,8,4,5], [], 6)
    except ValueError:
        print("List is empty!")


if __name__ == '__main__':
    main()