#Inferring mRNA from Protein. Soroush

#http://rosalind.info/problems/mrna/

string = "MTTAQCSHSIEWTCEWHMINWGLWQCKDEFLGYTSVVFNPDTGCKMFLVPERWMVQEDDVKVYIHVEQEHETQSPGIWVPWEYRGQMRDFDNGGQMGKSMHTCVQSLCCHKESVRDAGRNAGGSVGGTGQMNEWPQNTYWYWEPYWEQCDDQMFAMWSEGKTCKRHSPHWSQRYFHPYRGWDVLFFLEFPFWGEIMCKCVECDHWCVNSVKFVLPCVQIQTIKTAVDFHSERCPWEGHFSCRGVLLPGFPLFLSRAQWNPTAALPHCWCCPYVEMKQLWVWYFWNQKGFFLWAAATMHLYNYCYNTGWYFSKQVTCLAPICGEDWGETWWVISCNLLDEAVYFWSFVLAEIQPAPQCWPCPICYNIMYYHVNVHMLPLSISDVDYVTWPIPMETTREQCDRWCDTALDLFEYNWQSGMGKDTKMDSTVHEQFEEINLPTETEILSFSWSGRDSGTWQVFNLNFGIWGNNDDIWISKQMFRSTIPKCRAIMSLFCNPRFTFYPQYRPKVCCRKEIMNFVWPKGLCVCTPESPPKYGFDGFILKQLLGDEYYRWWCRVFGWIRVHRKPDPQMITHMYTCEPPTDVLEGKPIEKWVNVPLMWYPVPDEVHAFRLYKFQEHDTLWTFHMYTRMNRIVNVKINVRFMEESCAGPMIQVDTNGMPYTSYSRGWQGADPFHIMVVQWNFCESLMMNKGTMWKFFEPYMKDANQYNYYFNIPIYFLSINCGCPYQWQNIHALHEQFKEQARYEHTFDGIDMMVRKNTGRCIYFCFGEYMQELNEPCFWGCWHNQYMLIAMTGFPVGKCIKRTMGMNNDIFGTNFPYRHAGHEKVWWAQDPDYLMAKPGLGLFANNVGGDVFQTVSLRCCMIVNPEIWSFKWKMYNIPYCMPLAAYWPPYKYFPNPEKQWDKDQIEMFVKDPKIAYYFRCCENMQKPQNCFVHHRHVNYWQHTFFMWTISQMMQQKYQTHYHETKMGRPCKNKGWSAPSPIYVKHWWEFNICEMNYT "

possibilities = 0
if (string != ""):
    possibilities = 1

for x in string:
    if (x == 'F'):
        possibilities = possibilities *2
    elif (x == 'L'):
        possibilities = possibilities *6
    elif (x == 'I'):
        possibilities = possibilities *3
    elif (x == 'M'):
        possibilities = possibilities *1
    elif (x == 'V'):
        possibilities = possibilities *4
    elif (x == 'S'):
        possibilities = possibilities *6
    elif (x == 'P'):
        possibilities = possibilities *4 ###
    elif (x == 'T'):
        possibilities = possibilities *4
    elif (x == 'A'):
        possibilities = possibilities *4
    elif (x == 'Y'):
        possibilities = possibilities *2
    elif (x == ' '):
        possibilities = possibilities *3
    elif (x == 'H'):
        possibilities = possibilities *2
    elif (x == 'Q'):
        possibilities = possibilities *2
    elif (x == 'N'):
        possibilities = possibilities *2
    elif (x == 'K'):
        possibilities = possibilities *2
    elif (x == 'D'):
        possibilities = possibilities *2
    elif (x == 'E'):
        possibilities = possibilities *2
    elif (x == 'C'):
        possibilities = possibilities *2
    elif (x == 'W'):
        possibilities = possibilities *1
    elif (x == 'R'):
        possibilities = possibilities *6
    elif (x == 'G'):
        possibilities = possibilities *4
    possibilities = possibilities % 1000000

print possibilities
