import string
import re
import http.client
import sys

def create_maping_table(keyword : string):
    keyword = keyword.upper()
    alphabet = string.ascii_uppercase
    plainlst = list(alphabet)
    encryptlst = list(alphabet)                                       
    usedalph = set()
    #remove keyword characters from encrplist
    #print(list(keyword),encryptlst)
    keywpart = []
    for ch in list(keyword):
        try:
            encryptlst.remove(ch)
            keywpart.append(ch)
        except ValueError as ve:
            #skip duplicities
            pass
    encryptlst = keywpart + encryptlst
    #print('enchars list', encryptlst, len(encryptlst))
    decrmap = {}
    i = 0
    for ch in encryptlst:
        decrmap[ch] = alphabet[i]
        i += 1
    return decrmap

def decrypt_with(encrypted,keywordmap):
    res = []
    enc = encrypted.upper()
    for ch in enc:
        res.append(keywordmap[ch])
    return ''.join(res)

def keywordcipher_decrypt(enciphered:string, keyword:string):
    return decrypt_with(enciphered,create_maping_table(keyword))

def find_in_wordsunscrambler_results(data):
    tofind = b"""class="wordWrapper">"""
    fidx = data.find(tofind)
    sidx = fidx + len(tofind)
    es = data[sidx:].find(b"<")
    es2 = data[sidx:].find(b"\n")
    if es==-1 or es2==-1:
        raise Exception("unexpected html content")
    es = min(es,es2)
    result = data[sidx:sidx+es]
    #print(result)
    return result.decode().upper()

class NumberPart:
    def __init__(self,pair="A0"):
        self.ciphletter = pair[0]
        self.number = pair[1]
        self.plainletter = "."
    def __repr__(self):
        return "{}->{}:{}".format(self.ciphletter,self.plainletter,self.number)

def processInput(pairsinput):
    pairs = pairsinput.split(',')
    res = []
    for pair in pairs:
        res.append( NumberPart(pair) )
    return res

def getciphertext(numberparts):
    ciphert = ""
    for item in numberparts:
        ciphert += item.ciphletter
    return ciphert

def updateCodePairs(codepairs,plainletters):
    i = 0
    for item in codepairs:
        item.plainletter = plainletters[i]
        i += 1
    return codepairs

def map_code_pairs(codepairs,resultingword):
    mp = {}
    for item in codepairs:
        mp[item.plainletter] = item.number
    code = ''
    for letter in resultingword:
        code += mp[letter]
    return code

def reprResults(code,unencryptedword):
    output = "launch code [{}], plain word [{}]".format(code,unencryptedword)
    #output = "launch code [{}], plain word [{}]".format(code,"")
    return output

#keyword = "UNWORKABLES"
#ciphertext = "BKLMNQRW"

def do_the_deciphering(keyword="",pairs=""):
    codepairs = processInput(pairs)
    ciphertext = getciphertext(codepairs)
    print(ciphertext)
    plainletters = keywordcipher_decrypt(ciphertext,keyword)
    print('plain:',plainletters)
    updateCodePairs(codepairs,plainletters)
    #now do request to:
    #https://wordunscrambler.me/unscramble/mortgeab
    try:    
        conn = http.client.HTTPSConnection("wordunscrambler.me")
        #conn.request("GET", "/")
        conn.request("GET", "/unscramble/" + plainletters)
        #conn.request("HEAD","/index.html")
        r = conn.getresponse()
        #print(r.status, r.reason)
        if r.status != 200:
            raise Exception("url error")
        data2 = r.read()
        if False:
            #write for deb. purposes
            with open('index.html','wb') as f:
                f.write(data2)
        #search for resulting word in website result
        res = find_in_wordsunscrambler_results(data2)
        #map code pairs
        result = map_code_pairs(codepairs,res)
        #presentation
        print(reprResults(result,res))
        #print(res)#only decryption
        pass
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    if len(sys.argv)>2:
        print(sys.argv)
        keyw, pairs = sys.argv[0], sys.argv[1]
        print(keyw,pairs)
        do_the_deciphering(keyw,pairs)
    else:
        keyword = "SUBNORMALITY"
        pairs = "C4,E6,H1,K9,M1,O4,S2,U9"
        #do_the_deciphering(keyword,pairs)
        #keyword = "OVERMANS"
        #pairs = "B1,D2,G1,H8,L3,N2,O6,P8"
        #do_the_deciphering(keyword,pairs)
        #do_the_deciphering("DRUMBEATINGS","b3,l6,m1,o5,h2,p0,q7,u8")
        #do_the_deciphering("CONSUMPTIVELY","A8,C0,G0,K3,O3,J6,S9,U9")
        #do_the_deciphering("FISHERWOMAN","W3,F3,G7,H2,O9,Q1,S4,V2")
        #do_the_deciphering("QUESTIONABLY","F8,I7,K2,M7,Q9,U8,V7,Y9")
        #do_the_deciphering("STICKHANDLER","D5,F5,K1,O0,P3,S0,U0,Z9")
        #do_the_deciphering("HYDROPLANES","A7,B6,F8,K3,L4,M0,N0,T0")
        do_the_deciphering("MULTIBRANCHED","D8,F7,G1,L0,M6,O8,R2,N7")
