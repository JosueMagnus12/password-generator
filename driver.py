import merge_sort
import binary_search
import password_generator
import time

my_password = password_generator.generate_password(15)
passwords = [0] * 1_000_000

start = time.time()
for i in range(1_000_000):
    passwords[i] = password_generator.generate_password(15)
end = time.time()

start2 = time.time()
merge_sort.merge_sort(passwords,0,999_999)
end2 = time.time()

start3 = time.time()
result = binary_search.binary_search(passwords,0,999_999,my_password)
end3 = time.time()

print(passwords)
print("Your password is: " + my_password)

if result:
    print("Insecure generator")
else:
    print("Secure generator")

print("Filling time: {}".format(end - start))
print("Sorting time: {}".format(end2 - start2))
print("Searching time: {}".format(end3 - start3))