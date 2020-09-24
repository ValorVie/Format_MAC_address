import re
import win32clipboard
import win32con
#str='18-31-BF-D0-67-98'
#print(len(str))

def format_mac(mac:str) -> str:
    if len(mac) == 17:
        mac = re.sub('[-:.]', '', mac).lower() # remove delimiters and convert to lower case
        mac = ''.join(mac.split()) # remove whitespaces
        # assert len(mac) == 12 # length should be now exactly 12 (eg. 008041aefd7e)
        # assert mac.isalnum() # should only contain letters and numbers
    elif len(mac) == 12:
        # convert mac in canonical form (eg. 00:80:41:ae:fd:7e)
        mac = ":".join(["%s" % (mac[i:i + 2]) for i in range(0, 12, 2)])
    return mac
#test
print('請輸入MAC address:')
lst = []
while True:
    temp = input()
    if temp == '':
        break
    elif len(temp) == 12 or len(temp) == 17:
        b = format_mac(temp)
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, b)
        win32clipboard.CloseClipboard()
        lst.append(temp)
        print('格式化完畢:')
        print(b)
    else:
        print('MAC格式不符合')
string = '\n'.join(lst)
print('Bye!')

# while True:
#     a = input("請輸入資料:")
#     b=format_mac(a)
#     win32clipboard.OpenClipboard()
#     win32clipboard.EmptyClipboard()
#     win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, b)
#     win32clipboard.CloseClipboard()
#     if a == "exit":
#         exit()
#     print(b)