# This program will allow the user to calculate the dot product or the cross product for 
# vectors that they provide

import os

def dot(u1,u2):
	dotprod = u1[0]*u2[0]+u1[1]*u2[1]+u1[2]*u2[2]

	print("Your vectors: V1 = < " + str(u1[0]) + ", " + str(u1[1]) + ", " + str(u1[2]) + " > and V2 = < " + str(u2[0]) + ", " + str(u2[1]) + ", " + str(u2[2]) + " > \n")

	print("V1 * V2 = " + str(dotprod))


def cross(u1,u2):
	v_i=u1[1]*u2[2]-u1[2]*u2[1]
	v_j=-1*(u1[0]*u2[2]-u1[2]*u2[0])
	v_k=u1[0]*u2[1]-u1[1]*u2[0] 

	print("Your vectors: V1 = < " + str(u1[0]) + ", " + str(u1[1]) + ", " + str(u1[2]) + " > and V2 = < " + str(u2[0]) + ", " + str(u2[1]) + ", " + str(u2[2]) + " > \n")

	crossprod="< " + str(v_i) + ", " + str(v_j) + ", " + str(v_k) + " > = " + str(v_i) + "i + " + str(v_j) + "j + " + str(v_k) + "k"
	print("V1 X V2 = " + crossprod)


def dot_and_cross(u1,u2):
	dotprod = u1[0]*u2[0]+u1[1]*u2[1]+u1[2]*u2[2]

	v_i=u1[1]*u2[2]-u1[2]*u2[1]
	v_j=-1*(u1[0]*u2[2]-u1[2]*u2[0])
	v_k=u1[0]*u2[1]-u1[1]*u2[0] 

	print("Your vectors: V1 = < " + str(u1[0]) + ", " + str(u1[1]) + ", " + str(u1[2]) + " > and V2 = < " + str(u2[0]) + ", " + str(u2[1]) + ", " + str(u2[2]) + " > \n")

	crossprod="< " + str(v_i) + ", " + str(v_j) + ", " + str(v_k) + " > = " + str(v_i) + "i + " + str(v_j) + "j + " + str(v_k) + "k"

	print("V1 * V2 = " + str(dotprod))
	print("V1 X V2 = " + crossprod)

########################################################

run_flag = 1

while run_flag == 1:

	os.system('cls' if os.name == 'nt' else "printf '\033c'")

	print("Please enter in the components of vector 1:")

	while 1==1:
		try:
			v1_comp1=float((input("1st: ")))
			break
		except KeyboardInterrupt:
			exit()
		except:
			continue

	while 1==1:
		try:
			v1_comp2=float((input("2nd: ")))
			break
		except KeyboardInterrupt:
			exit()
		except:
			continue

	while 1==1:
		try:
			v1_comp3=float((input("3rd: ")))
			break
		except KeyboardInterrupt:
			exit()
		except:
			continue

	print("")

################################

	print("Please enter in the components of vector 2:")

	while 1==1:
		try:
			v2_comp1=float((input("1st: ")))
			break
		except KeyboardInterrupt:
			exit()
		except:
			continue

	while 1==1:
		try:
			v2_comp2=float((input("2nd: ")))
			break
		except KeyboardInterrupt:
			exit()
		except:
			continue

	while 1==1:
		try:
			v2_comp3=float((input("3rd: ")))
			break
		except KeyboardInterrupt:
			exit()
		except:
			continue
	
	v1=[v1_comp1, v1_comp2, v1_comp3]
	v2=[v2_comp1, v2_comp2, v2_comp3]

##################################################

	while 1==1:
		os.system('cls' if os.name == 'nt' else "printf '\033c'")
		print("Your vectors: V1 = < " + str(v1[0]) + ", " + str(v1[1]) + ", " + str(v1[2]) + " > and V2 = < " + str(v2[0]) + ", " + str(v2[1]) + ", " + str(v2[2]) + " > \n")

		opper = (input("Dot product, cross product or both? (1, 2, or 3) \n"))

		if opper == '1':
			break
		elif opper == '2':
			break
		elif opper == '3':
			break
		else:
			continue

	if opper == '1':
		os.system('cls' if os.name == 'nt' else "printf '\033c'")
		dot(v1,v2)
	if opper == '2':
		os.system('cls' if os.name == 'nt' else "printf '\033c'")
		cross(v1,v2)
	if opper == '3':
		os.system('cls' if os.name == 'nt' else "printf '\033c'")
		dot_and_cross(v1,v2)

	print("")

	while 1==1:
		exityn=(input("Run again for different vectors? (y/n) \n")) 
		if exityn == 'y':
			os.system('cls' if os.name == 'nt' else "printf '\033c'")
			break
		elif exityn == 'n':
			exit()
		else:
			continue