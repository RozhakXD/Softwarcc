import requests, json, time, sys
from rich.console import Console
from rich import print

def Login(username: str, password: str):
    with requests.Session() as session:
        session.headers.update(
            {
                'Content-Type': 'application/json',
                'Host': 'mplus-softwarcc.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
            }
        )
        data = json.dumps(
            {
                'identity': f'{username}',
                'password': f'{password}'
            }
        )
        response1 = session.post('https://mplus-softwarcc.com/api/collections/guest/auth-with-password', data=data, allow_redirects=True, verify=True)
        if '"token":' in str(response1.text):
            json_response1 = json.loads(response1.text)
            userid = json_response1['record']['id']
            token = json_response1['token']

            print(f"[bold white]Token:[bold green] {token}\n")
            return (userid, token)
        else:
            print(f'[bold red]Invalid username or password!')
            sys.exit(0)

def Kerjakan_Misi(authorization: str, userid: str, i: int):
    with requests.Session() as session:
        session.headers.update(
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
                'Host': 'mplus-softwarcc.com',
                'Authorization': '{}'.format(authorization)
            }
        )
        response1 = session.get('https://mplus-softwarcc.com/api/collections/guest/{}/state'.format(userid), verify=True)
        response2 = session.get('https://mplus-softwarcc.com/api/collections/guest_task/{}/plan'.format(userid), verify=True)
        if 'task is complete' in str(response2.text):
            print(f'[bold red]Task is complete!')

            return ('null')
        elif 'no related products price' in str(response2.text):
            print(f'[bold red]No related products price!')

            return ('null')
        else:
            json_response2 = json.loads(response2.text)
            id_ = json_response2['Data']['id']

            response3 = session.get('https://mplus-softwarcc.com/api/collections/guest_plan/{}/{}/action'.format(userid, id_), verify=True)
            if 'You clicked too quickly' in str(response3.text):
                print(f"[bold green]{i}[bold white].[bold yellow] You clicked too quickly!\n")
                time.sleep(5)
            elif 'Congratulations!' in str(response3.text):
                Message =  json.loads(response3.text)['Message']
                print(f"[bold green]{i}[bold white].[bold green] {Message}\n")
                time.sleep(2)
            else:
                print(f"[bold green]{i}[bold white].[bold red] {response3.text}\n")
                time.sleep(5)
        return ('null')

if __name__=='__main__':
    print("""[bold blue]  ______         ___                               
[bold blue] / _____)       / __)  _                           
[bold blue]( (____   ___ _| |__ _| |_ _ _ _ _____  ____ _____ 
[bold blue] \____ \ / _ (_   __|_   _) | | (____ |/ ___) ___ |
[bold blue] _____) ) |_| || |    | |_| | | / ___ | |   | ____|
[bold blue](______/ \___/ |_|     \__)\___/\_____|_|   |_____)
""")

    username = Console().input('[bold white]Username: ')
    password = Console().input('[bold white]Password: ')
    userid, token = Login(username=username, password=password)
    for i in range(40):
        Kerjakan_Misi(authorization=token, userid=userid, i=i)
        for i in range(10, 0, -1):
            print(f"[bold white]Tunggu[bold green] {i}[bold white] detik!     ", end='\r')
            time.sleep(1)
        continue
    sys.exit(1)