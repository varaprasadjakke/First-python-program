# Calculate gold price by ornament or pure rate (wastage,gst and hall mark charges)

print("Enter pure rate or ornament rate or by total.")
print("1.By Pure Rate (24kt)\n2.By Ornament Rate (22kt)\n3.By Total\n4.Exit")


hm=100 #hm = hall mark
for i in range(50):
    choice=input("\nEnter Choice(1/2/3/4): ")
    if choice=="1":
        weight=float(input("\nEnter weight     : "))
        purerate=int(input("Enter Pure Rate (24kt)  : "))
        p=int(input("Enter Percentage : "))
        print("\nTotal: ",round(((weight*(92+p)/100)*purerate)+hm))
    elif choice=="2":
        weight=float(input("\nEnter Weight            : "))
        orn=int(input("Enter Ornament Rate (22kt)     : "))
        p=int(input("Enter Wastage Percentage: "))
        gst=3
        gold_rate=weight*orn
        wastage=(gold_rate*p)/100
        va=(wastage*hm)/gold_rate
        gold_rate1=gold_rate+wastage
        tax=(gold_rate1*3)/100
        total=gold_rate+wastage+tax+hm
        print(" ")
        print("Gold Rate      :",round(gold_rate))
        print("Wastage        :",(round(wastage)),", v/a :",(round(va)),"%")
        print("Gold and Making:",round(gold_rate1))
        print("GST            :",round(tax))
        print("Hall Mark      :",hm)
        print("\nTotal Cost     :",round(total))
    elif choice=="3":
        total=int(input("\nTotal Amount: "))
        weight=float(input("Enter Weight : "))
        ornament=int(input("Enter Ornament Rate: "))
        gold_rate=weight*ornament
        hm=100
        gst=(total*3)/100
        va=total-gold_rate-hm-gst
        wastage=(va*hm)/gold_rate
        print("\nGold Amount :",(round(gold_rate)))
        print("Wastage     :",(round(va)),", v/a :",(round(wastage)),"%")
        print("GST         :",(round(gst)))
        print("HallMark    :",(round(hm)))
        print("Total       :",(total))
    elif choice=="4":
        print("\nSee you again")
        break
    else:
        print("\nError")
