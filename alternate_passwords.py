def main():
    f1 = open("text_files/passwords.txt", "r")
    f2 = open("text_files/alternate_passwords.txt", "w")

    for i in range(200):
        if i % 2 == 0:
            f2.write("peter\n")
        else:
            f2.write(f1.readline())

if __name__ == "__main__":
    main()