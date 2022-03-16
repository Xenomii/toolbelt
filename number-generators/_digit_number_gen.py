def main():
    f = open("../text_files/3_digit_numbers.txt", "w")
    for i in range(1000):
        f.write("{:03d}".format(i) + "\n")
    f.close()

if __name__ == "__main__":
    main()