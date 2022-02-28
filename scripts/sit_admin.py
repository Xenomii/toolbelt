def main():
    f = open("../text_files/sit_admin_num.txt", "w")
    for i in range(1800000, 2299999):
        f.write(str(i) + "\n")

if __name__ == "__main__":
    main()