#pylint : disable=E0602
import sys
import requests
baseUrl='https://www.chessmail.de/api/users/'

def fetchUser(userUrl):
    try:
        r=requests.get(userUrl)
        if r.status_code!=200:
            return
        user=r.json()
        return user
    except Exception as e:
        print(e)
        return None


def fetchUsers(users):
    for userUrl in users:
        user=fetchUser(userUrl)
        if not user is None:
            # print(user)
            name=user.get('username')
            rating=user.get('rating')
            if (not name is None) & (not rating is None):
                # print(f" <!--* {name}|| {rating} *-->")
                print(f"{{{{CLUBLIGA/Spieler|{name}}}}} <!--* {name}|| {rating} *-->||{{{{CLUBLIGA/Spieler|{name}}}}}")
    return

def main(args):
    lst=[]
    for a in args:
        items=a.split(None)
        for item in items:
                url=baseUrl+item
                lst.append(url)
    
    # print(lst)
    fetchUsers(lst)
        
    return

if __name__ == "__main__":
    lst=[]
    if (len(sys.argv)<2):
        lst=["name1 name2 name3 ..."]
    else:
        lst=sys.argv[1:]
    main(lst)

