def day1_part1():
    """Main function for day 1 part 1."""
    current_number = 50
    num_of_zeroes = 0
    with open('input.txt', 'r') as file:
        for line in file:
            # .strip() removes the newline character ('\n') and extra spaces
            rotation_string = line.strip()
            rotation_number = rotation_string[1:]
            rotation_number = int(rotation_number)
            if rotation_string[0] == 'L':
                transition_num = current_number - rotation_number
                current_number = transition_num % 100
            elif rotation_string[0] == 'R':
                transition_num = current_number + rotation_number
                current_number = transition_num % 100
            
            if current_number == 0:
                num_of_zeroes += 1
    print(num_of_zeroes)

def day1_part2():
    """Main function for day 1 part 2."""
    current_number = 50
    num_of_zeroes = 0
    with open('input.txt', 'r') as file:
        for line in file:
            # .strip() removes the newline character ('\n') and extra spaces
            rotation_string = line.strip()
            rotation_number = rotation_string[1:]
            rotation_number = int(rotation_number)
            transition_zeroes = 0
            if rotation_string[0] == 'L':
                transition_num = current_number - rotation_number
                if transition_num < 0:
                    if current_number != 0:
                        transition_zeroes = ((transition_num - 1) // 100) * -1
                        num_of_zeroes += transition_zeroes
                    else:
                        if rotation_number >= 100:
                            transition_zeroes = ((transition_num - 1) // 100) * -1
                            num_of_zeroes += transition_zeroes - 1 
                elif transition_num % 100 == 0:
                    num_of_zeroes += 1
                current_number = transition_num % 100
            elif rotation_string[0] == 'R':
                transition_num = current_number + rotation_number
                transition_zeroes = (transition_num // 100)
                num_of_zeroes += transition_zeroes
                current_number = transition_num % 100
    print(num_of_zeroes)

if __name__ == "__main__":
    day1_part2()
# if __name__ == "__main__":
#     day1_part2()

