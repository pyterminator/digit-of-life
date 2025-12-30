# https://youtube.com/@PyTerminator

while True:
    print("------------------------------")
    print("Gün.Ay.İl şəklində daxil edin.")
    print("Məs : 25.03.2002")
    print("Oyunu dayandırmaq üçün exit yazın.")
    i = input("Doğum tarixiniz : ")
    if i == "exit": break
    
    try:
        nums = i.split(".")
        check_up = all(num.isdigit() for num in nums)
        if check_up:
            bd = "".join(nums)
            bd = int(bd)
            while bd >= 10:
                total = 0
                for n in str(bd):
                    total += int(n)
                bd = total
            print(f"Sizin həyat rəqəminiz : {bd}")
        else:
            raise Exception("Yanlış format!!!")

    except Exception as e: print(e)
