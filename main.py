import fileinput
import random
import math

def Load(txt):
	for line in fileinput.input(files="input.txt"):
		txt=line
		return str
		#todo concat other lines



def ParseInput(txt):
	i=0
	while i < 20:
		print(txt[i])
		i=i+1

playergui='¶ '

def o_surf(i):
	if i==0:
		return '. '#'⁛'
	if i==1:	
		return '≋≋'
	return 0

def o(i):	
	if i==0:
		return '. '#'⁛'
	if i==1:
		return 'X '
	if i==2:   
		return playergui
	if i==3:
		return 'Ý '#'Y'
	if i==4:	
		return '≋≋'
	if i==5:
		return 't '
	if i==6:
		return '░░'#'▓▒'#▓'
	if i==7:
		return 'i '#'⚘ '
	if i==8:
		return '~ '
	if i==9:
		return '& '
	if i==10:
		return 'Ω '
	if i==11:
		return '  '
	if i==12:
		return 'o '
	if i==13:
		return 'Qo'
	if i==14:
		return 'r '
	if i==15:
		return 'ß '
	if i==16:
		return '▓▒'
	if i==17:
		return 'T '
	if i==18:
		return 'Г '
	if i==19:
		return 'µ'
	return 0

def name(i):	
	if i==0:
		return 'ground'
	if i==1:
		return 'x'
	if i==2:
		return 'player'
	if i==3:
		return 'tree'
	if i==4:	
		return 'water'
	if i==5:
		return 'bush'
	if i==6:
		return 'fence'#'wooden fence'#▓▓'
	if i==7:
		return 'flower'#'⚘ '
	if i==8:
		return 'branch'
	if i==9:
		return 'fire'
	if i==10:
		return 'cave'
	if i==11:
		return 'none'
	if i==12:
		return 'stone'
	if i==13:
		return 'rocks'
	if i==14:
		return 'rabbit'
	if i==15:
		return 'bear'
	if i==16:
		return 'rock wall'
	if i==17:
		return 'pickaxe'
	if i==18:
		return 'axe'
	if i==19:
		return 'boat'
	return 0



def ent_attack(i):	
	if i==0:
		return 0
	if i==1:
		return 0
	if i==2:
		return 0
	if i==3:
		return 0
	if i==4:	
		return 0
	if i==5:
		return 0
	if i==6:
		return 0
	if i==7:
		return 0
	if i==8:
		return 1
	if i==9:
		return 0
	if i==10:
		return 0
	if i==11:
		return 0
	if i==12:
		return 2
	if i==13:
		return 0
	if i==14:
		return 0
	if i==15:
		return 0
	if i==16:
		return 0
	if i==17:
		return 0
	if i==18:
		return 0
	if i==19:
		return 0
	return 0


def craftreceipt(i):	#[num_outputs,input0,input1,input2,input3,input4,input5,input6,input7]
	if i==0:
		return 0
	if i==1:
		return 0
	if i==2:
		return 0
	if i==3:
		return 0
	if i==4:	
		return 0
	if i==5:
		return 0
	if i==6:
		return [1,8,8,8,0,0,0,0,0]
	if i==7:
		return 0
	if i==8:
		return 0
	if i==9:
		return [1,8,8,0,0,0,0,0,0]
	if i==10:
		return 0
	if i==11:
		return 0
	if i==12:
		return 0
	if i==13:
		return [1,12,12,12,12,0,0,0,0]
	if i==14:
		return 0
	if i==15:
		return 0
	if i==16:
		return [1,13,0,0,0,0,0,0,0]
	if i==17:
		return 0
	if i==18:
		return 0
	if i==19:
		return 0

	return 0


def pickable(i):	
	if i==0:
		return 0
	if i==1:
		return 0
	if i==2:
		return 0
	if i==3:
		return 0
	if i==4:	
		return 0
	if i==5:
		return 0
	if i==6:
		return 0
	if i==7:
		return 1
	if i==8:
		return 1
	if i==9:
		return 0
	if i==10:
		return 0
	if i==11:
		return 0
	if i==12:
		return 1
	if i==13:
		return 0
	if i==14:
		return 1
	if i==15:
		return 0
	if i==16:
		return 0
	if i==17:
		return 0
	if i==18:
		return 0
	if i==19:
		return 0

	return 0

def name2(i):
	return str(o(i))+str(name(i))

def shadow(i):	


	if i==3:
		return 1
	if i==6:
		return 1
	if i==13:
		return 1
	if i==16:
		return 1
	if i==19:
		return 0


	return 0

def InvSubIfPossible(type,subtract):
	amount = 0
	for i in range(InvSize):
		if Inv[i]==type:
			amount+=1
	if amount >= subtract:
		InvSub(type,subtract)
		return True
	else:
		return False

#def InvSort()
#	for i in range(InvSize):
#		if Inv[i]

def InvSub(type,subtract):
	for i in range(InvSize):
		if subtract>0 and Inv[i]==type:
			subtract-=1
			Inv[i]=0

def InvAdd(type):
	for i in range(InvSize):
		if Inv[i]==0:
			Inv[i]=type
			return True
	return False

def InvCheck(type):
	amount=0
	for i in range(InvSize):
		if Inv[i]==type:
			amount+=1
	return amount












def PrintMinimap():
	_side = 16
	_sector = round(side/_side)
	groundgandicap = 0.28		
	rockgandicap = 1.75		
	forestgandicap = 4.0	
	lakegandicap = 1
		
	
	
	for _ybig in range(_side):
		line = ''
		for _xbig in range(_side):
		
			if (int(ply_x*_side/side) == _xbig) and (int(ply_y*_side/side) == _ybig):	
				line = line+o(2)#'@ '
			else:
				#print(ply_x*_side/side)
				#print(ply_y*_side/side)
				table=[0,0]
				for i in range(ent_num):
					table.append(0)
			
				for _x in range(_sector):
					for _y in range(_sector):
						table[arr[_x+_xbig*_side+(_y+_ybig*_side)*side]]+=1
						
				maxindex=0
				max=0
				
								
				for i in range(ent_num):
					if i==0 and ply_z == 0:
						table[i]*=groundgandicap
					elif i==4 and ply_z == 0:
						table[i]*=lakegandicap
					elif i==3 and ply_z == 0:
						table[i]*=forestgandicap
					elif i==16 and ply_z == -1:
						table[i]*=rockgandicap
						
					if table[i]>max:
						max=table[i]
						maxindex=i
							
				line = line+o(maxindex)
				#print(table)
		print(line)















def Main():
	seed = 0
	random.seed(seed)

	max_enemies = 16
	
	enemies_x = [0,0]
	enemies_y = [0,0]
	#enemies_y = [0,0]

	for i in range(max_enemies-2):
		enemies_x.append(0)
		enemies_y.append(0)

	global side, size
	side = 256
	size = side*side
	sizet = (side+32)*(side+32)*2

	wside = 32
	wsideh = int(wside/2)
	wsize = wside*wside

	aiside = 40
	aisideh = int(aiside/2)
	aisize = aiside*aiside

	lastactivity=""
	global arr, arrd, arr2, arrh
	global ent_num
	ent_num = 18
	
	arr=[0,0]
	arrd=[0,0]
	arr2=[0,0]
	
	for i in range(sizet):
		arr.append(0)
		arrd.append(0)
		arr2.append(0)
	
	wvis=[0,0]
	for i in range(wsize):
		wvis.append(0)
	
	desc=[""]
	for i in range(wside):
		desc.append("")
	
	global ply_x,ply_y,ply_z, playergui
	
	ply_x=127
	ply_y=127
	ply_z=0
	ply_ded=False
	hp=100

	global Inv
	Inv=[0,0]
	global InvSize
	InvSize = 18

	for i in range(InvSize-2):
		Inv.append(0)
	
	for i in range(size):
		arrd[i]=16

	for i in range(size):
		_x=0
		_y=0
		x=i%side
		y=int(i/side)
		if random.random() <= 0.006:
			if arr[i*2] == 0:
				arr[i] = 3
		if random.random() <= 0.006:
			if arr[i] == 0:
				arr[i] = 8
		if random.random() <= 0.0015:
			forest_size = random.randint(2,14)
			ellipse=1#random.randint(1,4)/2.0
			sz=random.randint(1,30)
			for _x in range(-forest_size,forest_size):
				for _y in range(-forest_size,forest_size):
					dist = math.sqrt(pow(_x,2)+pow(_y,2))
					go = False
					if dist <= forest_size-0.25:
						if random.randint(1,30)>24:
							go = True
						if random.random() <= 0.015:
							go = False
							for _i in range(-6,6):
								if random.random() <= 0.5:
									if arrd[x+_x+((y+_y-1)*side)+_i]==16:
										arrd[x+_x+((y+_y-1)*side)+_i] = 0
									if arrd[x+_x+((y+_y)*side)+_i]==16:
										arrd[x+_x+((y+_y)*side)+_i] = 0
									if arrd[x+_x+((y+_y+1)*side)+_i]==16:
										arrd[x+_x+((y+_y+1)*side)+_i] = 0
								else:
									if arrd[x+_x-1+((y+_y+_i)*side)]==16:
										arrd[x+_x-1+((y+_y+_i)*side)] = 0
									if arrd[x+_x+((y+_y+_i)*side)]==16:
										arrd[x+_x+((y+_y+_i)*side)] = 0
									if arrd[x+_x+1+((y+_y+_i)*side)]==16:
										arrd[x+_x+1+((y+_y+_i)*side)] = 0
							if random.random() <= 0.25:
								arr[x+_x+((y+_y)*side)] = 10
								arrd[x+_x+((y+_y)*side)] = 10
									
					if dist > forest_size-2 and random.randint(1,40)>4:
						go = False	
					if go == True:
						arr[x+_x+((y+_y)*side)] = 3
					#if random.randint(1,30)>29
					#arr[(x+(random.randint(-2,2))*side+random.randint(-2,2))] = 4
				
		if random.random() <= 0.005:
			for _i in range(-16,16):
				if random.random() <= 0.5:
					if arrd[x+_x+((y+_y-1)*side)+_i]==16:
						arrd[x+_x+((y+_y-1)*side)+_i] = 0
					if arrd[x+_x+((y+_y)*side)+_i]==16:
						arrd[x+_x+((y+_y)*side)+_i] = 0
					if arrd[x+_x+((y+_y+1)*side)+_i]==16:
						arrd[x+_x+((y+_y+1)*side)+_i] = 0
				else:
					if arrd[x+_x-1+((y+_y+_i)*side)]==16:
						arrd[x+_x-1+((y+_y+_i)*side)] = 0
					if arrd[x+_x+((y+_y+_i)*side)]==16:
						arrd[x+_x+((y+_y+_i)*side)] = 0
					if arrd[x+_x+1+((y+_y+_i)*side)]==16:
						arrd[x+_x+1+((y+_y+_i)*side)] = 0	
		
		if random.random() <= 0.0006:
			lake_size = random.randint(1,14)
			ellipse=1#random.randint(1,4)/2.0
			sz=random.randint(1,30)
			for _x in range(-lake_size,lake_size):
				for _y in range(-lake_size,lake_size):
					dist = math.sqrt(pow(_x,2)+pow(_y,2))
					go = False
					if dist <= lake_size-0.25:
						go = True
					if dist > lake_size-1 and random.randint(1,40)>20:
						go = False
					if go == True:
						arr[x+_x+((y+_y)*side)] = 4

		if random.random() <= 0.0015:
			if arr[x+(y+1)*side] == 0 and arr[x+(y-1)*side] == 0 and arr[x+1+(y)*side] == 0 and arr[x-1+(y)*side] == 0:
				arr[(x)+(y)*side] = 14
		if random.random() <= 0.0005:
			if arr[x+(y+1)*side] == 0 and arr[x+(y-1)*side] == 0 and arr[x+1+(y)*side] == 0 and arr[x-1+(y)*side] == 0:
				arr[(x)+(y)*side] = 15
		if (random.random() <= 0.002):
			if arr[i] == 0:
				arr[i] = 7
		if (random.random() <= 0.002):
			if arr[i] == 0:
				arr[i] = 12
		if (True and random.random() <= 0.001):
			if arr[i] == 0:
				arr[i] = 13










	for i in range(side):
		arr[i]=16
		arr[size-i]=16
		arr[side*i]=16
		arr[side*(side-i)]=16
		arrd[i]=16
		arrd[size-i]=16
		arrd[side*i]=16
		arrd[side*(side-i)]=16

	arr[ply_y*side+ply_x]=2
		
	step = -1
	tool=0
	hp_s = ''
	ply_xy_s = ''
	freeze = 0	

	Inv[2]=17
	Inv[3]=18	

	while True:
		
		craft=''
		craftables=[False,False]
		
		for i in range(ent_num):
			craftables.append(False)
		
		for i in range(ent_num) :
			receipt = craftreceipt(i)
			if receipt:
				fail = False
				for k in range(8):
					if receipt[k+1]:
						num = 0
						for j in range(8-k):
							if receipt[k+j+1]==receipt[k+1]:
								num += 1#receipt[j+1]
							
						if InvCheck(receipt[k+1])<num:
							fail = True
							#print("i:"+str(i)+",k:"+str(k))
							break
				if fail==False:
					craftables[i]=True
					craft = craft+'['+o(i)+name(i)+']'
			
		res_wood=InvCheck(8)
		#print()
		step+=1
		#if res_wood>=2:
		#	craft = '['+o()+']'
		#if res_wood>=3:
		#	craft = craft + '[wall]'
		
		_time = step*10
		_timeH = int(_time / 60)
		_time%=60
		_timeH%=24
		k=_time/60.0
		s_time = str(_time)
		s_timeH = str(_timeH)

		if s_time == '0':
			s_time = '00'
		if s_timeH == '0':
			s_timeH = '00'

		time = s_timeH+':'+s_time
		addtime = ' '
		
		temp_keypoints = [5,4,3,4,5,6,7,8,12,15,18,19,20,21,20,19,17,15,13,11,9,7,6,5]
		temp = round(temp_keypoints[_timeH]*k+temp_keypoints[(_timeH+1)%24]*(1-k))
		addtemp = '°C '

		desc[2]=('step:'+ str(step)+' seed:'+str(seed))
		desc[3]=("x:"+str(ply_x)+ " y:"+str(ply_y))		
		
		if freeze>0:
			ply_xy_s = 'player frozen for ' + str(freeze) +' step'
		else: ply_xy_s = ''
		if ply_xy_s:
			desc[3]+=' | '+(ply_xy_s)

		desc[4]=("HP "+str(hp))
		if hp_s:
			desc[4]+=' | '+(hp_s)

		if craft=='':
			craft = 'x'
		#desc[15]="       craft"
		desc[15]="craft: "+craft

		
		desc[21]=lastactivity
		#lastactivity = ""
		desc[5]=("time "+str(time)+ addtime)
		#desc[6]=("temp "+str(temp)+ addtemp)
		
		desc[0]=" = = RGLK = ="
		
		

		desc[10]="┌      items       ┐"

		for i in range(3):
			desc[i+11]="| " + str(o(Inv[i*6]))+" "+str(o(Inv[i*6+1]))+" "+str(o(Inv[i*6+2]))+" "+str(o(Inv[i*6+3]))+" "+str(o(Inv[i*6+4]))+" "+str(o(Inv[i*6+5]))+"|"


	
		#desc[wside-2]="West:"+o(arr[(ply_y+0)*side+ply_x-1])+"East:"+o(arr[(ply_y+0)*side+ply_x+1])+"North:"+o(arr[(ply_y-1)*side+ply_x])+"South:"+o(arr[(ply_y+1)*side+ply_x])
		desc[wside-1]="controls: w/a/s/d"# (up: left: down: right:)"
		#desc[17]=""
		#desc[18]=""
		#desc[19]=""
		#desc[20]=""

		ln = 0
		
		while ln<ent_num/4:
			desc[ln+24]=str(name2(ln*4))+", "+str(name2(ln*4+1))+", "+str(name2(ln*4+2))+", "+str(name2(ln*4+3))
			ln+=1


	#for i in range(wside-7):
		#desc[i]="| "+(desc[i])

		if False:
			ltrs='ctorioloutam'
			for i in range(400):
				l=random.randint(5,8)
				word="fau"
				used=[1,0,0,0,0,0,0,0,0,0,0,0]
				for a in range(l):
					letter=0
					while(True):
						letter=random.randint(0,10)
						if used[letter]==False:
							used[letter]=True
							break
					word+=ltrs[letter]
				print(word)

		#a = input()
		#print(a)	
		for x in range(size):
			arr2[x] = arr[x]
		for x in range(1,side-1):
			for y in range(1,side-1):
				mmm=1#arr2[x*side+y]=0
	
		#print(random.randint(5,9))


		for i in range(wside):
			k=(i+ply_y-wsideh)*side
			_s=''
			for l in range(wside) :
				visible = True
				dist = math.sqrt(pow(l-wsideh,2)+pow(i-wsideh,2))
				
				if dist >= wsideh-0.6:
					visible = False
				else:
					visible=True
					if int(dist)>0:
						d_x=(l-wsideh)/dist
						d_y=(i-wsideh)/dist
						if True:
							for j in range(int(dist)):
								if shadow(arr[round(round(ply_y+j*d_y)*side+ply_x+j*d_x)]):
									visible=False
				if visible:
					wvis[i*wside+l] = True
				else:
					wvis[i*wside+l] = False
				
		
		for i in range(wside):
			k=(i+ply_y-wsideh)*side
			_s=''
			for l in range(wside) :
				if wvis[i*wside+l] == True:
					_s = _s + o(arr[l+k+ply_x-wsideh])# + ' '
				else:
					_s = _s + ' ' + ' '
				
			_s=_s+"| "+desc[i]
			
			print(_s)
		#print(' ',flush=True)





		# BOTS AI
		for i in range(-aisideh,aisideh):
			k=(i+ply_y)*side
			_s=''
			for j in range(-aisideh,aisideh):
				if arr[k+ply_x+j] == 14:
					_x=random.randint(-1,1)
					_y=random.randint(-1,1)
					
					if abs(j)<8 and abs(i)<8:
						#if random.randint(0,4)==0:
						if (j>0):
							_x=+1 
						elif j<0:
							_x=-1
						if (i>0):
							_y=+1 
						elif i<0:
							_y=-1

					if arr2[(i+ply_y+_y)*side+ply_x+j+_x]==0:
						arr2[k+ply_x+j]=0
						arr2[(i+ply_y+_y)*side+ply_x+j+_x]=14
					else:
						if random.randint(0,1)==0:
							_x=-_x
						if random.randint(0,1)==0:
							_y=-_y
						if arr2[(i+ply_y+_y)*side+ply_x+j+_x]==0:
							arr2[k+ply_x+j]=0
							arr2[(i+ply_y+_y)*side+ply_x+j+_x]=14
						else:
							if random.randint(0,1)==0:
								_x=-_x
							if random.randint(0,1)==0:
								_y=-_y
							if arr2[(i+ply_y+_y)*side+ply_x+j+_x]==0:
								arr2[k+ply_x+j]=0
								arr2[(i+ply_y+_y)*side+ply_x+j+_x]=14


				if arr[k+ply_x+j] == 15:
					_x=random.randint(-1,1)
					_y=random.randint(-1,1)
					if (abs(j)==1 and i==0) or (abs(i)==1 and j==0):
						#print("bear hurt")
						hp-=random.randint(5,15)
						hp_s = 'bear hurt player'
						if random.randint(0,1)==0:
							freeze=1
						
					else:
						if abs(j)<8 and abs(i)<8:
							#if random.randint(0,4)==0:
							if (j<0):
								_x=+1 
							elif j>0:
								_x=-1
							if (i<0):
								_y=+1 
							elif i>0:
								_y=-1
		
						if arr2[(i+ply_y+_y)*side+ply_x+j+_x]==0:
							arr2[k+ply_x+j]=0
							arr2[(i+ply_y+_y)*side+ply_x+j+_x]=15
						else:
							if random.randint(0,1)==0:
								_x=-_x
							if random.randint(0,1)==0:
								_y=-_y
							if arr2[(i+ply_y+_y)*side+ply_x+j+_x]==0:
								arr2[k+ply_x+j]=0
								arr2[(i+ply_y+_y)*side+ply_x+j+_x]=15
							else:
								if random.randint(0,1)==0:
									_x=-_x
								if random.randint(0,1)==0:
									_y=-_y
								if arr2[(i+ply_y+_y)*side+ply_x+j+_x]==0:
									arr2[k+ply_x+j]=0
									arr2[(i+ply_y+_y)*side+ply_x+j+_x]=15
		
		

		

		update=False
		
		while update==False:
			if hp <=0:
				ply_ded=True
				playergui="X "
			if ply_ded:
				inpt=input('r to restart: ')
				update = True
			else:

				res_wood=InvCheck(8)
				#print('ur turn:')
				inpt=input('move: ')
				result = -1
				_x=0
				_y=0
				
				
				
				if freeze<=0:	
					for i in range(0,InvSize):
						if Inv[i]>0:
							if inpt==name(Inv[i]) and tool!=inpt :
								result = 2	
								print('changed tool to',inpt)
								tool = Inv[i]
									
								break
		
				if tool==0:
					s_tool = 'x '
				else:
					s_tool = name(tool) + "(attack+"+str(ent_attack(tool))+") "
		
				for i in range(1,ent_num): 
					if InvCheck(i)>0 and tool!=i:
						s_tool+="["+o(i)+name(i)+"]"
				
	
				#attack = 
				desc[16]="tool: "+s_tool
								
				if tool :
					playergui='¶'+o(tool)[0]
				else:
					playergui='¶ '
					
							
	
				if freeze<=0:
					
					
					if inpt=='minimap' or inpt=='map':
						PrintMinimap()
						#result=2
		
					#if inpt[0]=='give' and :
					
					lastactivity_candidate=""	

					if inpt=='dump':
						
						for i in range(InvSize):
							Inv[i]=0
						result = 2

					if inpt=='pass':
						result = 2	
					if inpt=='left' or inpt=='a':
						_x-=1
						lastactivity_candidate = 'moved west'
					if inpt=='right' or inpt=='d':
						_x+=1 
						lastactivity_candidate = 'moved east'
					if inpt=='up' or inpt=='w':
						_y-=1
						lastactivity_candidate = 'moved north'
					if inpt=='down' or inpt=='s':
						_y+=1
						lastactivity_candidate = 'moved south'
					if inpt=='rabbit' or inpt=='r':
						arr2[(ply_y)*side+ply_x+8] = 14
						result=2
					if inpt=='fire':
						print('tryin fire')
						if InvSubIfPossible(8,2):
							print('fire successful')
							arr2[(ply_y+1)*side+ply_x] = 9
							result = 2		
						else:
							result = 0
					if inpt=='wall':
						#if res_wood>=3:
						if InvSubIfPossible(8,3):
							arr2[(ply_y+1)*side+ply_x] = 6
							result=2		
						else:
							result = 0
					if inpt=='rock':
						if InvSubIfPossible(13,4):
							arr2[(ply_y+1)*side+ply_x] = 16
							result=2		
						else:
							result = 0
					
					if result==-1:			
						#result = PlyGo(arr2[(ply_y+_y)*side+ply_x+_x]
						candidate = arr2[(ply_y+_y)*side+ply_x+_x]
			
						result = 0
						#print(candidate)			
			
						if candidate == 0:
							result = 1
						if candidate == 4:
							#arr2[(ply_y+_y)*side+ply_x+_x]=0
							print("drank water")
							result = 2
						if pickable(candidate) == True:
							
							if InvAdd(candidate):						
								arr2[(ply_y+_y)*side+ply_x+_x]=0
								result = 2
							else:
								print("no free space")
								
						if candidate == 16:
							if tool == 17:
								arr2[(ply_y+_y)*side+ply_x+_x]=13
							result = 2
						if candidate == 13:
							if tool == 17:
								if InvAdd(candidate):						
									arr2[(ply_y+_y)*side+ply_x+_x]=0
									result = 2
								else:
									print("no free space")
							result = 2

						if candidate == 3:
							if tool == 18:
								arr2[(ply_y+_y)*side+ply_x+_x]=8
							result = 2


						if candidate == 10:
							if ply_z ==0:
		
								if arrd[(ply_y)*side+ply_x]==0:
			
									lastactivity="entered dungeon"
									#print()
									result = 2
									ply_z = -1
									arr[(ply_y)*side+ply_x]=0
									for x in range(size):
										arr2[x] = arrd[x]
									for x in range(size):
										arrd[x] = arr[x]
									for x in range(size):
										arr[x] = arr2[x]
									arr2[(ply_y)*side+ply_x]=2
								else:
									print("entrance is blocked")	
							elif ply_z == -1:
		
								if arrd[(ply_y)*side+ply_x]==0:
			
									lastactivity="left dungeon"
									result = 2
									ply_z = 0
									arr[(ply_y)*side+ply_x]=0
									for x in range(size):
										arr2[x] = arrd[x]
									for x in range(size):
										arrd[x] = arr[x]
									for x in range(size):
										arr[x] = arr2[x]
									arr2[(ply_y)*side+ply_x]=2
								else:
									print("entrance is blocked")
				else:
					result = 2
					freeze-=1
	
				#if result == 0:
					#print('err')
				if result == 1:	 
					arr2[ply_y*side+ply_x]=0
					ply_y=ply_y+_y
					ply_x=ply_x+_x
					arr2[(ply_y)*side+ply_x]=2
					update=True
					#print('ply moved')
					lastactivity='you '+lastactivity_candidate
				if result == 2:	 
					update=True
	


			


		for x in range(size):
			arr[x] = arr2[x]
	
Main()
