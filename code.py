# JAI BAJARANG BALI

# manitianajay45



from time import sleep
from turtle import update
from pip import main
import requests


# https://codeforces.com/api/user.info?handles=manitianajay45;

contest= "https://codeforces.com/api/contest.standings?contestId=1699&from=1&showUnofficial=false"



def string_matching(a,b):
    if(b in a):
        return True
    return False

def get_data(api):
    response = requests.get(f"{api}")
    if response.status_code == 200:
        return response.json()
    else:
        return None



def contest_data(url):
    return get_data(url)



print("Enter Contest Id")
contest_id=input()


print("Enter No of organizations name you want to give as an input")

no=int(input())


inp=[]

print("Enter Organizations names")


for i in range(no):
    org=input()
    inp.append(org)    



for i in range(len(inp)):
    inp[i]=inp[i].lower().replace(" ","")

    
    # print(cont_data['result'][0])



def upadated_standings(contestid):
    contest_url="https://codeforces.com/api/contest.standings?contestId="
    contest_url+=(str(contestid))
    contest_url+="&from=1&count=9000&showUnofficial=false"
    contest_standings=contest_data(contest_url)

    if(contest_standings==None):
        return None

    contestant=contest_standings['result']['rows']

    no_of_contestant=len(contestant)
    print(no_of_contestant)
    st=1
    cont_lis=[]
    while(st<=no_of_contestant):
        handle_url="https://codeforces.com/api/user.info?handles="
        for i in range(st,min(st+700,no_of_contestant)):
            handle=contestant[i]['party']['members'][0]['handle']
            hndl=str(handle)+";"
            handle_url+=hndl
        cont_data=get_data(handle_url)

        if(cont_data==None):
            break
        # print(len(cont_data['result']))

        sz=len(cont_data['result'])

        for i in range(0,sz):
            cont_org=cont_data['result'][i]
            # print(type(cont_data))
            if(cont_org.get('organization')==None):
                continue

            cont_org1=cont_org['organization']
            cont_org1=cont_org1.lower().replace(" ","")
            for j in range(len(inp)):
                if(string_matching(cont_org1,inp[j])):
                    cont_lis.append(contestant[i+st])
                    break
            
            
            # print(handle_url)
        st+=700

    contest_standings['result']['rows']=cont_lis


    file=open('results.csv','w')
    file.write("Rank,overall Rank,user_id\n")

    for i in range(0,len(cont_lis)):
        file.write(str(i+1))
        file.write(",")
        file.write(str(cont_lis[i]['rank']))
        file.write(",")
        file.write(str(cont_lis[i]['party']['members'][0]['handle']))
        file.write("\n")
    
    file.close()
    
upadated_standings(contest_id)




