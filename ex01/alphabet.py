import random
import datetime
st = datetime.datetime.now()
tai_moji = 10 # 対象文字数
ke_moji = 2  # 欠損文字数
chance = 2 # 試行回数

def shutudai(alh):
    moji = random.sample(alh, tai_moji)
    print("対象文字", end = " ")
    for i in moji:
      print(i, end = " ")
    print()
    
    nai_moji = random.sample(moji, ke_moji)
    print("表示文字", end = " ")
    for i in moji:
        if i not in nai_moji:
            print(i, end = " ")         
    print()
    print("デバック用欠損文字", nai_moji)
    return nai_moji

def kaito(ans):
    num = int(input("欠損文字はいくつあるでしょうか？："))
    if num != ke_moji:
        print("不正解です")
    for i in range(num):
        a = input(f"{i + 1}文字目を入力してください：")
        if a not in ans:
            print("不正解です。残念です")
            return False
        else:
            ans.remove(a)
    else:
        print("完全クリアです！！！！")
        return True
    return False
if __name__ == "__main__":
    alh = [chr(i + 65) for i in range(26)]
    nai_moji = shutudai(alh)
    for i in range(chance):
        hantei = kaito(nai_moji)
        if hantei:
            break
        else:
            print("-" * 20)
    ed = datetime.datetime.now()
    print(f"所要時間 :{(ed-st).seconds} s")