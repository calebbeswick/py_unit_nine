import dog

# 1. Create another instance of a dog. Yours should be named dog2 and given a name.
dog1 = dog.Dog("Fifi")
dog2 = dog.Dog("John")

# 2. Print the name of each dog
print(dog1.get_name())
print(dog2.get_name())

# 3. Calling the print_trick_list() method for each dog. The example below should print out:
# Fifi has not performed any tricks yet
# dog1.print_trick_list()
dog1.print_trick_list()

# 4. Call each of the three trick methods for each of the dogs. There should be six lines in total (3 tricks
# for each do). Make sure to do a different order of tricks for each dog.

dog1.sit()
dog1.jump()
dog1.roll_over()
dog2.roll_over()
dog2.sit()
dog2.jump()




# 5. Call the print_trick_list() again for each dog.
dog1.print_trick_list()