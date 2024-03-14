import sys
myfile1= r"D:\1Tide2024\2_Feb\Time.txt"
S1=""
S2=''
S3=''
a= "0"
b= "00"
time=""
h1= ""
m1= ""

#TestCalc_CBTide2.py
print("TestCalc_CBTide2.py")
print("")

with open(myfile1,"r")as f1:
	next (f1)
	next (f1)

	for line in f1:
		ss1= line
		S1= ss1.strip()
		#print(S1)
		S2= S1.replace(":",'')
		S3= S2.replace("\n",'')
		#print(S3)
		if len(S3)== 3:
			S4= a + S3
			#print("lenth S3= ",len(S3))
			#print(S4)
			time= S4[ :5]
			h1= time[:2]
			m1= time[2:4]
			#print("h1=",h1)
			#print("m1=", m1)
			#print("time=",time)
			#sys.exit()

		elif len(S3)== 2:
			S4 == b + S3
			time = S4[:5]
			h1S = time[:2]
			m1S = time[2:4]
			while h1S != "":
				  h1= int(h1S)

			while m1S != "":
				  m1= int(m1S)

			'''Calc Claybank Tide'''

		def cbtime(str):
			cbmin1S = cbTimeS[2:4]
			print(cbmin1S)
			cbmin1 = int(cbmin1S)
			cbmin2 = cbmin1 + 46
			if cbmin2 > 60:
				cbh1 = cbh1 + 1
				cbmin3 = cbmin2 - 60
				cbTimeS = str(cbh1) + str(cbmin3)

			else:
				cbh1 = cbh1
				cbmin2 = cbmin2
				cbTimeS = str(cbh1) + str(cbmin2)

			sys.exit()
#x= cbtime("1624")
#print(x)
print("")
print("Don")
