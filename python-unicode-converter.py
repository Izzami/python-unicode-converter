def main():
    frases = input("Input: ")
    frasec = list(frases)

    with open("table.txt") as tabella:
        for i in range(len(frases)):
            current = 0
            for linea in tabella:
                if current == ord(frasec[i]):
                    print(linea[:6], end=" ")
                    break
                current += 1
            tabella.seek(0)

    print()

if __name__ == "__main__":
    main()
