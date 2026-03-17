with open("tmp/add_to_the_same_file", "a") as file:
    file.write("There gonna be a lot of copies of this line\n")


with open("tmp/every_time_clean_file", "w") as file:
    file.write("This line is the only one line in the file\n")


with open("tmp/this_will_write_just_once", "x") as file:
    file.write("This line will not be replaced!\n")