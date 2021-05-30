#-*-coding:utf8;-*-

import os, shutil as sh,random

G='\033[032m'
os.chdir ('/storage/emulated/0')
global fld_nm
def CrtDr ():
    global fld_nm
    os.chdir ('/storage/emulated/0/.cracked')
    fldr=str (random.randint (0,999999))
    fld_nm="/storage/emulated/0/.cracked/Fldr_"+fldr
    os.mkdir (fld_nm)
    
try:
    os.mkdir (".cracked")
    CrtDr()
except FileExistsError:
    CrtDr ()
    pass

os.chdir ('/storage/emulated/0')
for (rt,fd,fl) in os.walk ('.'):
    for fn in fl:
        if fn.endswith ('.bin'):
            fnl = '%s/%s'%(rt,fn)
            i = 0
            print("\nOpening: ", fnl)
            fa = open(fnl, "rb")
            bet = fa.read(3)
            a = bet.hex()
            b = 'ffd8ff'
            try:
                res = int(a, 16) ^ int(b, 16)
                res = hex(res)
                res = res[:4]
                print("xor byte is:", res)
                print("\n")
                res = int(res, 16)
                new = open(fnl+".jpg", "wb")
                barr = []
                #print("decrypting file......")
                with open(fnl, "rb") as f:
                    byte = f.read(1)
                    while byte:
                        if i < 128:
                            bytem = int(byte.hex(), 16) ^ res
                            barr.append(bytem)
                        else:
                            barr.append(int(byte.hex(), 16))
                        i = i+1
                        byte = f.read(1)
                barrb = bytes(barr)
                new.write(barrb)
                new.close()
                fa.close()
                bin_jpg=fnl+'.jpg'
                try:
                    jpg='IMG_'+str (random.randint (0,999999999))+'.jpg'
                    os.renames (bin_jpg, jpg)
                    sh.move (jpg, fld_nm)
                    print("_ * _"*6)
                    print(G+"\nFile decryption & movement: SUCCESS!\n\033[0m")
                    print("_ * _"*6)
                except IOError or OSError as error:
                    print("_ * _"*6)
                    print(G+"\nFile movement: FAILED!\n\033[0m")
                    print (G+"Error code: \033[03m\033[031m"+str (error)+"\033[0m")
                    print("_ * _"*6)
                    pass
                    
            except ValueError or FileNotFoundError as error:
                print (G+"Error code: \033[03m\033[031m"+str (error)+"\033[0m")
                pass