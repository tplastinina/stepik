with open("C:/Users/tanze/Documents/Python/datten/dataset_24465_4.txt") as f, open("C:/Users/tanze/Documents/Python/datten/test_copy.txt", "w") as w:
    f_lines = f.read().splitlines() #прочитали и разделили на линии

    for line in f_lines[::-1]: #перевернули(начали с последнего)
        w.write('%s\n' % line) #записываем в новый файл, убирая перевод строки

