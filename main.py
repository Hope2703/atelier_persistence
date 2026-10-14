document = open("document.txt");
print(document.read());
document.close();
# r : lecture
# a : ajout
# w : écriture
# x : création


with open("file.txt", "x") as file:
    file.write("Hello, World!")
    