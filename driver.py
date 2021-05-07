import merge_sort
import binary_search
import password_generator
import time

def main():
    #creating the first password
    my_password = password_generator.generate_password(18)

    #filling the list up
    start = time.time()
    passwords = [password_generator.generate_password(18) for i in range(1_000_000)]
    end = time.time()

    #sorting the list
    start2 = time.time()
    merge_sort.merge_sort(passwords)
    end2 = time.time()

    #searching the password
    start3 = time.time()
    result = binary_search.binary_search(passwords,0,999_999,my_password)
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
