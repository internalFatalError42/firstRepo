def shrink(input_string: str):
    input_string += " "
    start = True
    index = 0
    count = 1
    final_string = ""

    for i in input_string:
        if start:
            start = False
            continue
        last_char = input_string[index]
        if i == last_char:
            count += 1
        else:
            if count > 3:
                final_string += "$" + str(count) + last_char
            else:
                final_string += last_char * count
            count = 1
        index += 1
    print(final_string)


def main():
    shrink("aaaaabbbccc")


if __name__ == '__main__':
    main()
