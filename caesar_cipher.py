alphabet_eng="abcdefghijklmnopqrstuvwxyz"
alphabet_rus="фбвгдеёжзиклмнопрстуфхцчшщъыьэюя"

alphabets=[alphabet_eng,alphabet_rus]

def caesar_convert(str: str = "None", rot: int = 0) -> str:
    """caesar_convert(str: str = "None", rot: int = 0) -> str:"""
    ans=""
    for i in str:
        for alphabet in alphabets:
            if i.lower() in alphabet:
                letter=alphabet[(alphabet.index(i.lower())+rot)%(len(alphabet))]
                i=(letter,letter.upper())[i.isupper()]
                break
        ans+=i
    return(ans)

if __name__ == '__main__':
    while True:
        rot=int(input("Enter shift (key): "))
        text=input("Enter text: ")
        print(f"Encrypted > {caesar_convert(text,rot)}\nDecrypted > {caesar_convert(text,-rot)}"
