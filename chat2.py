#讀取及轉換對話

# 讀取檔案
def read(filename):
    lines = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        for line in f:
            lines.append(line.strip())
    return lines

# 轉換對話格式
def convert(lines):
    allen_wc = 0
    allen_image = 0
    allen_stickers = 0
    viki_wc = 0
    viki_image = 0
    viki_stickers = 0
    for line in lines:
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == "Allen":
            if s[2] == "圖片":
                allen_image += 1
            elif s[2] == "貼圖":
                allen_stickers += 1
        else:
            for w in s[2:]:
                allen_wc += len(w)
        if name == "Viki":
            if s[2] == "圖片":
                viki_image += 1
            elif s[2] == "貼圖":
                viki_stickers += 1
            else:
                for w in s[2:]:
                    viki_wc += len(w)
    print("Allen說了: ", allen_wc, "貼圖有:", allen_stickers, "圖片有:", allen_image)
    print("Viki說了: ", viki_wc, "貼圖有:", viki_stickers, "圖片有:", viki_image)

# 寫入檔案
def write_file(file, lines):
    with open(file, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def main():
    lines = read("lineconversation.txt")
    convert(lines)
    # write_file("output.txt", lines)

main()