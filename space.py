import ISS_Info

print('[+]Space tool[+]')

print("****     **                 ")            
print("/**/**   /**           ******")           
print("/**//**  /**  ******  /**///**")    
print("/** //** /** //////** /**  /**")  
print("/**  //**/**  ******* /******")     
print("/**   //**** **////** /**///")      
print("/**    //***//********/**")       
print("//      ///  //////// //")        
print("instagram: 3h6h ")
print("snap: tv-of ")
print("<>---<>---<>")
print('[Enter number 1 to run]')

user = input("1)The number of astronauts and the name of each astronaut\n")
print('____________________________________')

if user == '1':
	nap = ISS_Info.iss_people_in_space()
	print("Currently there {} astronauts in space:"
	.format(nap['number']))
for n in nap['people']:
	print("Name: {} ('Craft: {}'))"
	.format(n['name'],n['craft']))
	nap = ISS_Info.iss_current_loc()

print(':)_________is over __________(:')

print('-------------/\---------------')

print('\\Performance is under development...')

