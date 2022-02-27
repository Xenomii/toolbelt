def main():
    f = open("text_files/alternate_users.txt", "w")
    for i in range(200):
        if i % 2 == 0:
            f.write("wiener\n")
        else:
            f.write("carlos\n")
    f.close()

if __name__ == "__main__":
    main()