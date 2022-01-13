from typing import ValuesView
from django.http.request import validate_host
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Destination
def datab(request):
    
    datas = Destination.objects.all()
    
    return render(request,'database.html',{'datas':datas})
# def datae(request):
#     datae = Destination.objects.all()
    
#     return render(request,'data.html',{'datae':datae})

# def data(request):
    # conn=sql
    # print(conn)
    # values = []
    
    # values.append(request.POST["Name"])
    # values.append(request.POST["Principal_Amount"])
    # values.append(request.POST["Interest_Rate"])
    # values.append(request.POST["Given_Intrest"])
    # values.append(request.POST["Given_Principle"])
    # values.append(request.POST["Pending_Intrest"])
    # values.append(request.POST["Balance_Principle_Amount"])
     
    
    # # values=(Id_no,Name,Principal_Amount,Interest_Rate,Given_Intrest,Given_Principle,Pending_Intrest,Balance_Principle_Amount)
    # query="insert into finance values( %s, %s, %s, %s, %s, %s, %s)"
    # cur=conn.cursor()
    # a=cur.execute(query, values)
    # conn.commit()
    # if a==1:
    #     print("Success")
    # else:
        # print("Error")
    return render(request,'data.html',{})
    # lis = []
    # lis.append(request.POST["Id_no"])
    # lis.append(request.POST["Name"])
    # lis.append(request.POST["Principal_Amount"])
    # lis.append(request.POST["Interest_Rate"])
    # lis.append(request.POST["Given_Intrest"])
    # lis.append(request.POST["Given_Principle"])
    # lis.append(request.POST["Pending_Intrest"])
    # lis.append(request.POST["Balance_Principle_Amount"])
     
    # post = lis
    # return render(request,"b.html",{"post":post})


# # Create your views here.
# Id_no=int(input("Enter the id:"))
#     Name=str(input("Enter the name:"))
#     Principal_Amount=str(input("Enter the principal amount :"))
#     Interest_Rate=int(input("Enter the intrest rate"))
#     Given_Intrest=int(input("Enter the given intrest"))
#     Given_Principle=int(input("Enter the given principal"))
#     Pending_Intrest=int(input("Enter the pending interest"))
#     Balance_Principle_Amount=int(input("Enter the balance principal amount"))