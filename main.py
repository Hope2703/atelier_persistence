document = open("document.txt");
print(document.read());
document.close();
# r : lecture
# a : ajout
# w : écriture
# x : création


with open("file.txt", "x") as file:
    file.write("Hello, World!")

with open("file.txt", "w") as file:
    file.write("How are you?")

with open("file.txt", "a") as file:
    file.write("\nI am fine.")