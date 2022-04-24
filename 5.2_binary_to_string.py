


def fraction_to_binary(num, arr: list):
    if len(arr) >= 32:
        # raise Exception('Error')
        return

    num *= 2

    if num > 1:
        arr.append(1)
        num = num - 1
    elif num < 1:
        arr.append(0)
    else:
        arr.append(1)
        return

    fraction_to_binary(num, arr)



def main():
    arr = []
    fraction_to_binary(0.72, arr)
    print(arr)



if __name__ == '__main__':
    main()