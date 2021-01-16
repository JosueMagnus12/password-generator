import merge_sort
import binary_search
import password_generator
import time

def main():
    #prompt
    n_char = int(input("How many characters in the passwords? (a strong password contains at least 10 characters): "))
    n_pass = int(input("How many passwords for the test? (big numbers are recommended): "))

    #creating the first password and the list
    my_password = password_generator.generate_password(n_char)
    passwords = [0] * n_pass

    #filling the list up
    start = time.time()
    for i in range(n_pass):
        passwords[i] = password_generator.generate_password(n_char)
    end = time.time()

    #sorting the list
    start2 = time.time()
    merge_sort.merge_sort(passwords,0,n_pass - 1)
    end2 = time.time()

    #searching the password
    start3 = time.time()
    result = binary_search.binary_search(passwords,0,n_pass - 1,my_password)
    end3 = time.time()

    #results
    print(passwords)
    print("Your password is: " + my_password)

    if result:
        print("Insecure generator")
    else:
        print("Secure generator")

    total_time_filling = round(end - start,5)
    total_time_sorting = round(end2 - start2,5)
    total_time_searching = round(end3 - start3,5)

    print("Filling time: {}s".format(total_time_filling))
    print("Sorting time: {}s".format(total_time_sorting))
    print("Searching time: {}s".format(total_time_searching))

if __name__ == "__main__":
    main()