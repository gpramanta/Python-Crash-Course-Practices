# Personal Message:
first_name = "komang"
middle_name = "pramanta"
last_name = "gerinata"
full_name = first_name.title() + " " + middle_name.title() + " " + last_name.title()
print("\tHello" + " " + full_name + "!\n" + "\tWould you like to learn some Python today?\n")

# Name Cases:
first_name = "komang"
middle_name = "pramanta"
last_name = "gerinata"
full_name = first_name + " " + middle_name + " " + last_name
print(full_name.title())
print(full_name.lower())
print(full_name.upper() + "\n")

# Famous Quote:
name = "Lord Krishna"
quote = "\"Whatever action a great man performs common men follow in his footstep. \n\tWhatever standard he sets by exemplary act all the world pursues.\""
print("\t" + name + " " + "once said in the Bhagavad-gita:\n" + "\t" + quote + "\n")

# Famous Quote 2:
famous_person = "Sri Srimad A.C. Bhaktivedanta Swami Prabhupada"
message = "Chant Hare Krishna and be Happy!"
print("\t" + famous_person + " once said:\n" + "\t" + message + "\n")

# Stripping Names:
name = " \tkomang pramanta gerinata\n "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())