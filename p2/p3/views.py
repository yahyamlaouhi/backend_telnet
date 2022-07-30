from django.template.defaulttags import register
from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from dataclasses import field
from os import linesep
from itertools import groupby
import csv
from rest_framework.response import Response
import jwt
import pandas as pd
from numpy import AxisError, append, nan
from bs4 import BeautifulSoup
import textwrap
from . models import csvfile, myuploadfile,tablecsv,Table,tablecsvs
from p3.models import NUser
from p2 import settings
from .serializers import NUserSerialiser,RegisterSerializer,MyTokenObtainPairSerializer,AdminSerializer, csvfileSerialiser, uploadcsvSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view


from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)






@api_view(['GET'])
def verify_token(request):
    jwtToken = request.GET.get('token', False)
    decodedData = jwt.decode(jwtToken, "", algorithms=['HS256'], verify=True)
    return Response(decodedData)



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer




class NUserViewSet(viewsets.ModelViewSet):
    serializer_class = NUserSerialiser
    queryset = NUser.objects.all()



class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =AdminSerializer



class csvfileViewSet(viewsets.ModelViewSet):
    queryset = csvfile.objects.all()
    serializer_class =csvfileSerialiser


@csrf_exempt
def Home2(request):
    return render(request, "p33/index2.html")

@csrf_exempt
def Home(request):
    return render(request, "p33/index.html")





# @csrf_exempt
# def User(request):
#     if request.method=='POST':
#         serializer = NUserSerialiser(data=request.data)
#         NomPrenom=serializer.data['NomPrenom']
#         Email=request.POST['email']
#         Pwd1=request.POST['pass1']
#         Pwd2=request.POST['pass2']
#         Department=request.POST['dep']
#         Role=request.POST['role']

#         if Pwd1 != Pwd2:
#             messages.success(request, "Les mots de passe ne correspondent pas!!")
#             return redirect('reg')

#         if NUser.objects.filter(Email=Email).exists():
#             messages.success(request, "E-mail déjà enregistré!!")
#             return redirect('reg')

#         if len(NomPrenom)>20:
#             messages.success(request, "Le nom d'utilisateur doit comporter moins de 20 caractères!!")
#             return redirect('reg')

#         # Welcome Email
#         subject = "Bienvenue sur Telnet Reporting!!"
#         message = "Bienvenue " + request.POST['un'] + " \n" + "Bienvenue sur Telnet!! \nMerci d'avoir visité notre site Web\n.\nVotre adresse email pour connecter est: " +request.POST['email']+"\n.\nVotre Mot de passe pour connecter est:" +request.POST['pass1']+"\nMerci"        
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [Email]
#         send_mail(subject, message, from_email, recipient_list, fail_silently=True)


#         NUser(NomPrenom=NomPrenom,Email=Email,Pwd1=Pwd1,Department=Department,Role=Role).save()
#         # messages.success(request,"le nouveau utilisateur\n"+request.POST['un']+ "\nest ajouté avec succés")
#         return render (request, "p33/register.html")
#     else:
#         return render (request, "p33/register.html")




@csrf_exempt
def Cpage(request):
    if request.method=="POST":
        try:
            Userdetails=NUser.objects.get(Email=request.POST['Email'],Pwd1=request.POST['pass1'])
            request.session['Email']=Userdetails.Email
            return render(request, "p33/index2.html")
        except NUser.DoesNotExist as e:
            messages.success(request,'Email / Mot de passe Invalide..!')
    return render(request, "p33/login.html")


@csrf_exempt
def Dec(request):
    try:
        del request.session['Email']
    except:
        return render(request, "p33/index.html")
    return render(request, "p33/index.html")

@csrf_exempt
@register.filter
def get_newElement(dictionary, key):
    return dictionary.get(key)

def indexf(request):

    context = {
        'data':myuploadfile.objects.all(),

            }
    return render(request,"p33/dash.html",context)


@api_view(['GET',"POST"])
def upload(request):
    if request.method == 'POST':
        serializer = uploadcsvSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = pd.read_csv(serializer.data, delimiter=',')
            print(data)
            return Response(1)

    return Response(0)

            
    



@csrf_exempt
def send_files(request):
    
        
        if request.method == 'POST':

            myfiles = request.FILES.getlist('uploadfiles')
            context = {}
            newElement={}
            
        for f in myfiles:
            myuploadfile(myfile=f).save()
            data = pd.read_csv('p3/csvs/'+ request.FILES['uploadfiles'].name, delimiter=',')
            data_dict = data.to_dict()
            

            for i in  range(0, len(data_dict["Date and time[ms]"])):
                newElement[i]=(str(data_dict["Message Id"][i]))+"+"+(str(data_dict["Data"][i]))

            context['data'] = data_dict
            context['newElement']=newElement

           
        csv_fp = open(f'p3/csvs/' + request.FILES['uploadfiles'].name, 'r')
        file_data = csv_fp.read()
        lines = file_data.split('\n')
        for line in range(0, len(lines)):

            for line in lines:
                    fields = line.split(',')
                    data_dict = {}
                    data_dict['Date'] = fields[0]
                    data_dict['Stamp'] = fields[1]
                    data_dict['Direction'] = fields[2]
                    data_dict['Source'] = fields[3]
                    data_dict['Destination'] = fields[4]
                    data_dict['MessageId'] = fields[5]
                    data_dict['Length'] = fields[6]
                    data_dict['StatusTx'] = fields[7]
                    data_dict['Data'] = fields[8]
                    Table(Date=data_dict['Date'],Stamp=data_dict['Stamp'],Direction=data_dict['Direction'],Source=data_dict['Source'],Destination=data_dict['Destination'],MessageId=data_dict['MessageId'],Length=data_dict['Length'],StatusTx=data_dict['StatusTx'],Data=data_dict['Data']).save()  

        return render(request, "p33/index2.html",context)


# def datatable(request):
#     context = {}
#     return render(request, "p33/index2.html",context)

@csrf_exempt
def mantissa(str):
    num = 0
    for idx in range(len(str)):
        num += int(str[idx])*2**(-(idx+1))
    return num

@csrf_exempt
def switch(test, bin, counter):
    if len(test) == 1:
        counter+=1
    else: 
        counter
    if counter !=0:
        bin=bin.append(test)
    else:
        bin = test
    return bin , counter

@csrf_exempt
def check_value_exist(test_dict, value):
    do_exist = False
    for key, val in test_dict.items():
        if key == value:
            do_exist = True
    return do_exist

@csrf_exempt
def search(request):
    context4 = {}
    context = {}
    data=""
    msg_id=""
    data2=""
    # dle=[],
    # lend=[],
    # fldna=[],
    # usa=[],
    # fldt=[],
    # i=[],
    # j=[],

    # if check_value_exist(request.POST, 'data') :
    #     context4 = {}
    # if request.method == 'POST':
        
    # if check_value_exist(request.POST, 'data') :
    if request.method == 'POST':
        # if check_value_exist(request.POST, 'data') :
            data=""
            msg_id=""
            data2=""
            context = {}
            liste1=[]
            liste2=[]
            liste3=[]
            liste4=[]
            liste5=[]
            liste6=[]
            liste7=[]

            data2 = request.POST
            data3 = data2.get('data')
            list_data = str(data3).split("+")
            print(list_data)
            # print('list_data des valeurs',list_data)
            # msg_id , data = [ list_data[i] for i in (0, -1) ]
            # print(list_datae)
            msg_id=list_data[0]
            data=list_data[1]
                # msg_id = str('118')
                # data = str('1142')
            # print('Message ID :',msg_id)
            # print('Data :',data)
            # context4 ['msg_id']=msg_id
            # context4 ['data']=data
            # print(context4)

            count = int(msg_id, 16)
            print("Valeur décimal = ", count)


            lis =['p3/xml/CubeSat_carrier_msgid.xml','p3/xml/CubeSat_carrier_msgid.xml','p3/xml/OBCU_msgid.xml','p3/xml/PS_msgid.xml','p3/xml/UHF_msgid.xml','p3/xml/VMS_msgid_en.xml','p3/xml/Wheel_msgid.xml']
            for k in lis:
                fd = open(k, 'r')

                xml_file = fd.read()

                lend = 0
                lengthpos = 0
                num_of_bits=0
                soup = BeautifulSoup(xml_file, 'lxml')
                for tag in soup.findAll("packet"):
                    len1 = lend
                    if int(tag.find("pacid").text) == count:
                        print("id", int(tag.find("pacid").text))
                        if int(tag.find("datalen").text):
                            dlen = int(tag.find("datalen").text)
                            num_of_bits= dlen * 8
                            print(dlen)
                            
                        scale = 16

                        msg_id = bin(int(data, scale))[2:].zfill(num_of_bits)

                        for fld in tag.findAll("field"):
                            usa1 = fld.find("fldlen")
                            lend = int(usa1.text)
                            fld1 = fld.find("flddesc")
                            usa = (fld1.text)
                            fldt1 = fld.find("fldtype")
                            fldt = (fldt1.text)
                            fldna1 = fld.find("fldname")
                            fldna =(fldna1.text)

                            print("\n")
                            print("Longeur du champ =", lend)
                            print("Nom du champ :", fldna)
                            print("Déscription du champ :", usa)
                            print("Type du champ :", fldt)

                            len1+=lend
                            j=len1
                            i=lengthpos
                            lengthpos += lend

                            stri = msg_id [int(i):int(j)]

                            if (lend >= 16):
                                split = textwrap.wrap(stri, 8)
                                list = []
                                if len(split) % 2 == 0:
                                    for n in range(0, len(split), 2):
                                        if len(split[n+1]) >= 8:
                                            list.append(split[n + 1])
                                            list.append(split[n])
                                        else:
                                            list.append(split[n])
                                            list.append(split[n + 1])
                                else:
                                    for n in range(0, len(split), 2):
                                        if n == len(split)-1:
                                            list.append(split[n])
                                        else:
                                            list.append(split[n + 1])
                                            list.append(split[n])
                                list = ''.join(list)
                            else:
                                list = stri

                            if fldt == 'int':
                                if list[0] == '1':
                                    sign = -1
                                else:
                                    sign = 1
                                dle = sign*int(list[1:], 2)
                            elif fldt == 'float':
                                sign_bit = int(list[0])
                                exp_bias = int(list[1:9], 2)
                                decimal = mantissa(list[9:])
                                exp_unbias = exp_bias-127
                                dle = pow(-1, sign_bit)*(1+decimal)*pow(2, exp_unbias)
                            elif list =="":
                                dle=list
                            else:
                                dle = int(list, 2)

                            print("Position du Data de ce champ:")
                            print("De :",i)
                            print("Jusqu'à :",j)
                            print(dle)
                            # liste1 =lend,fldna,usa,fldt,i,j,dle
                            # liste2.append(liste1)
 
                            # l1=(liste2)
                            # context4['l1']=l1

                            liste1.append(lend)
                            liste2.append(fldna)
                            liste3.append(usa)
                            liste4.append(fldt)
                            liste5.append(i)
                            liste6.append(j)
                            liste7.append(dle)
                        l1=(liste1)
                        l2=(liste2)
                        l3=(liste3)
                        l4=(liste4)
                        l5=(liste5)
                        l6=(liste6)
                        l7=(liste7)
                        context['l1']=l1,l2,l3,l4,l5,l6,l7
                       
            fd.close()
        # return render(request, "p33/rapport.html",{'context4':context4})
    return render(request, "p33/rapport.html", {'context':context})
    # return redirect("http://127.0.0.1:8000/rapport")
    # else:
    #     return HttpResponse('error')
