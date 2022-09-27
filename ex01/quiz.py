import random
def shutudai(toi_lst):
    toi = random.choice(toi_lst)
    print("問題:" + toi["q"])
    return toi["a"]
    
def kaito(seikai):
    ans = input("答え:")
    if ans in seikai:
        return "正解"
    else:
        return "不正解"
    
if __name__ == "__main__":
    toi_lst = [{"q":"サザエの旦那の名前は?", "a":["ますお", "マスオ", "MASUO"]},
     {"q": "カツオの妹の名前は?", "a":["わかめ", "ワカメ", "WAKAME"]},
     {"q": "タラオはカツオから見てどんな関係?", "a":["おい", "オイ", "甥", "甥っ子", "おいっこ", "nephew"]}
     ]
    seikai = shutudai(toi_lst)
    print(kaito(seikai))
    
    