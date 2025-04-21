import math


def main():

    # Ask user for input
    num_as_string = input("Enter a positive number :")
    print("")

    # Initialize counter to 0
    counter_loop = 0

    # try catch and calculations
    try:
        num_as_int = int(num_as_string)
        if num_as_int > 0:
            while True:
                counter_loop = counter_loop + 1
                squared = counter_loop**2
                print("{}^2 = {}".format(counter_loop, squared))
                if counter_loop >= num_as_int:
                    break
        else:
            print("input is invalid please try again!")
    except Exception:
        print("input is invalid please try again!")


if __name__ == "__main__":
    main()
