def main():
    f = open("../text_files/4_digit_numbers.txt", "w")
    for i in range(10000):
        f.write("{:04d}".format(i) + "\n")
    f.close()

if __name__ == "__main__":
    main()