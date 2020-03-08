import hashlib

class principale():
    def __init__(self, login, psd_hash, liste):
        self.login = login 
        self.psd_hash = psd_hash
        self.liste = liste

    def psd_list(self):
        file_list = open(self.liste, "r")
        noun_list = file_list.readlines()
        for i in noun_list:
            i1 = i.rstrip('\n')
            h = hashlib.md5(bytes(i1, 'utf-8')).hexdigest()
            if h == self.psd_hash: return i
        file_list.close()

    def psd_login_Nbr(self):
        first=self.login[0:1]
        for i in range(0, 10000):
            a = str(i)+self.login
            b = str(i)+first.upper()+self.login[1:]
            c = self.login+str(i)
            d = first.upper()+self.login[1:]+str(i)
            a1 = hashlib.md5(bytes(a, 'utf-8')).hexdigest()
            b1 = hashlib.md5(bytes(b, 'utf-8')).hexdigest()
            c1 = hashlib.md5(bytes(c, 'utf-8')).hexdigest()
            d1 = hashlib.md5(bytes(d, 'utf-8')).hexdigest()

            #print (a,b,c,d)

            if a1 == self.psd_hash:
                return a
            elif b1 == self.psd_hash:
                return b
            elif c1 == self.psd_hash:
                return c
            elif d1 == self.psd_hash:
                return d

        for f in range(0, 1000):
            a2 = "0"+str(f)+self.login
            b2 = "0"+str(f)+first.upper()+self.login[1:]
            c2 = self.login+"0"+str(f)
            d2 = first.upper()+self.login[1:]+"0"+str(f)
            e2 = "00"+str(f)+self.login
            f2 = "00"+str(f)+first.upper()+self.login[1:]
            g2 = self.login+"00"+str(f)
            h2 = first.upper()+self.login[1:]+"00"+str(f)

            #print (a2,b2,c2,d2,e2,f2,g2,h2)

            a3 = hashlib.md5(bytes(a2, 'utf-8')).hexdigest()
            b3 = hashlib.md5(bytes(b2, 'utf-8')).hexdigest()
            c3 = hashlib.md5(bytes(c2, 'utf-8')).hexdigest()
            d3 = hashlib.md5(bytes(d2, 'utf-8')).hexdigest()
            e3 = hashlib.md5(bytes(e2, 'utf-8')).hexdigest()
            f3 = hashlib.md5(bytes(f2, 'utf-8')).hexdigest()
            g3 = hashlib.md5(bytes(g2, 'utf-8')).hexdigest()
            h3 = hashlib.md5(bytes(h2, 'utf-8')).hexdigest()

            if a3 == self.psd_hash:
                return a2
            elif b3 == self.psd_hash:
                return b2
            elif c3 == self.psd_hash:
                return c2
            elif d3 == self.psd_hash:
                return d2
            elif e3 == self.psd_hash:
                return e2
            elif f3 == self.psd_hash:
                return f2
            elif g3 == self.psd_hash:
                return g2
            elif h3 == self.psd_hash:
                return h2

        for g in range(0, 10):

            a4 = "00"+str(g)+self.login
            b4 = "00"+str(g)+first.upper()+self.login[1:]
            c4 = self.login+"00"+str(g)
            d4 = first.upper()+self.login[1:]+"00"+str(g)
            e4 = "000"+str(g)+self.login
            f4 = "000"+str(g)+first.upper()+self.login[1:]
            g4 = self.login+"000"+str(g)
            h4 = first.upper()+self.login[1:]+"000"+str(g)

            #print( a4,b4,c4,d4,e4,f4,g4,h4)

            a5 = hashlib.md5(bytes(a4, 'utf-8')).hexdigest()
            b5 = hashlib.md5(bytes(b4, 'utf-8')).hexdigest()
            c5 = hashlib.md5(bytes(c4, 'utf-8')).hexdigest()
            d5 = hashlib.md5(bytes(d4, 'utf-8')).hexdigest()
            e5 = hashlib.md5(bytes(e4, 'utf-8')).hexdigest()
            f5 = hashlib.md5(bytes(f4, 'utf-8')).hexdigest()
            g5 = hashlib.md5(bytes(g4, 'utf-8')).hexdigest()
            h5 = hashlib.md5(bytes(h4, 'utf-8')).hexdigest()

            if a5 == self.psd_hash:
                return a4
            elif b5 == self.psd_hash:
                return b4
            elif c5 == self.psd_hash:
                return c4
            elif d5 == self.psd_hash:
                return d4
            elif e5 == self.psd_hash:
                return e4
            elif f5 == self.psd_hash:
                return f4
            elif g5 == self.psd_hash:
                return g4
            elif h5 == self.psd_hash:
                return h4

    def psd_Alogin_born(self):
        alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","U","V","W","X","Y","Z"]
        for i in alphabet:
            a=i+self.login
            for b in range(1900,2021):
                b=a+str(b)
                c=hashlib.md5(bytes(b,'utf-8')).hexdigest()
                if c==self.psd_hash: return b

    def psd_liste_Nbr(self):
        file_list = open(self.liste, "r")
        noun_list = file_list.readlines()
        for i in noun_list:
            i1 = i.rstrip('\n')
            first = i1[0]
            first_maj = first.upper()

            for i in range(0,):
                a = str(i)+i1
                b = str(i)+first_maj+i1[1:]
                c = i1+str(i)
                d = first_maj+i1[1:]+str(i)
                a1 = hashlib.md5(bytes(a, 'utf-8')).hexdigest()
                b1 = hashlib.md5(bytes(b, 'utf-8')).hexdigest()
                c1 = hashlib.md5(bytes(c, 'utf-8')).hexdigest()
                d1 = hashlib.md5(bytes(d, 'utf-8')).hexdigest()

                if a1 == self.psd_hash: return a                   
                elif b1 == self.psd_hash: return b          
                elif c1 == self.psd_hash: return c
                elif d1 == self.psd_hash: return d
    
    def psd_login_voyelle(self):

        maj_login=self.login.upper()

        login_wowel=maj_login.translate({ord('A'): 'a', ord('E'): 'e',ord('I'): 'i', ord('O'): 'o'})

        hash_psd=hashlib.md5(bytes(login_wowel,'utf-8')).hexdigest()

        if hash_psd==self.psd_hash: return login_wowel
                    
    def psd_2xliste(self):
        file_list = open(self.liste, "r")
        noun_list = file_list.readlines()
        for i in noun_list:
            i1 = i.rstrip('\n')
            for e in noun_list:
                i2 = e.rstrip('\n')
                b = i1+i2
                h = hashlib.md5(bytes(b, 'utf-8')).hexdigest()
                if h == self.psd_hash: return b
        file_list.close()

    def psd_liste_reversex2(self):
        file_list = open(self.liste, "r")
        noun_list = file_list.readlines()
        for i in noun_list:
            i1 = i.rstrip('\n')
            i2 = i1[::-1]
            i3 = i2+i2
            h = hashlib.md5(bytes(i3, 'utf-8')).hexdigest()
            if h == self.psd_hash:
                return i3
        file_list.close()