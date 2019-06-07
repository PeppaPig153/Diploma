import sys
import os
import scanner

def main():
    filename = ""

    if(len(sys.argv) > 1): # введение имени файла
        try: # провера на существоване файла
            file = open(str(sys.argv[1]))
        except IOError:
            print(u'Не удалось открыть файл!')
            return
        else:
            filename = str(sys.argv[1])

    scanner.scanner(filename) # сканируем картинку

if __name__ == "__main__":
    main()