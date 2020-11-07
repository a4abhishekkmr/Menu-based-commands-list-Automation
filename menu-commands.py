import os
import getpass
print("\t\t\t\t WELCOME TO MY MENU")
os.system("espeak-ng 'Welcome to my menu' ")

passwd = getpass.getpass("Enter your password")

if passwd != "lw" :
	print("password incorrect ....")
	exit()
#while true:
	#os.system("clear")
print("""
\n
press 0 : to show ip address
press 1 : to run date
press 2 : to cal
press 3 : to reboot
press 4 : to configure webserver
press 5 : to check the status of the webserver
press 6 : to exit
press 7 : to activate the slave node
press 8 : to activate the master
press 9 : to check the cluster status
press 10 : to start docker
press 11 : to check status of docker
press 12 : To check the available Image available to launch docker
press 13 : to launch docker container
press 14 : download new docker image
press 15 : to stop docker
press 16 : to Read the RAM
press 17 : ping google.com
press 18 : to download ansible
press 19 : to create a directory of your choice
press 20 : to create a file of your choice
press 21 : to view your file
press 22 : to append your file
press 23 : to remove a directory
press 24 : to remove a file
press 25 : to list the partition of hard disk
press 26 : list the block storage in system
press 27 : to pronounce your name
press 28 : to show all the working ports
press 29 : list all the files in directory
press 30 : ping another ip,__.__.__.__
press 31 : to copy one file to another directory
press 32 : to capture the packet
press 33 : to check the process id of program
press 34 : to kill the program
press 35 : to open python terminal
press 36 : to show me the cpu info
press 37 : to open the task manager
press 38 : to clear cache memory
press 39 : to create user
press 40 : to stop httpd
""")


r = input("enter you choice remote/local: ")

ch = input("Enter ur choice: ")
print(ch)

if r =="local" :
	if int(ch) ==0:
    			os.system("ifconfig")
	elif int(ch) ==2:
			os.system("date")
	elif int(ch) ==2:
			os.system("cal")
	elif int(ch)==3:
			os.sytem("reboot")
	elif int(ch) ==4:
			os.system("systemctl start httpd")
	elif int(ch) ==5:
			os.system("systemctl status httpd")
	elif int(ch) ==51:
			os.system("systemctl stop httpd")
	elif int(ch) ==6:
			exit()
	elif int(ch)==7:
			os.system("hadoop-daemon.sh start datanode")
			os.system("jps")
	elif int(ch)==8:
			print("please choose remote login for configuring master")
	elif int(ch)==9:
			os.system("hadoop dfsadmin -report")
	elif int(ch) ==10:
			os.system("systemctl start docker")
	elif int(ch) ==11:
			os.system("systemctl status docker")
	elif int(ch) ==12:
			os.system("docker images")
	elif int(ch) ==13:
			img=input(("Enter the image you want to launch :"))
			ver=input(("Enter the preffered version :"))
			os.system("docker run -it {}:{} ".format(img,ver))
	elif int(ch) ==14:
			os.system("docker images????????????????????")
	elif int(ch) ==15:
			os.system("systemctl stop docker")
	elif int(ch) ==16:
			os.system("free -m")
	elif int(ch) ==17:
			os.system("ping www.google.com")
	elif int(ch) ==18:
			os.system("pip install ansible")
	elif int(ch) ==19:
			dir=input(("Enter the directory you want to launch :"))
			os.system("mkdir dir")
	elif int(ch) ==20:
			fil=input(("Enter the file you want to launch :"))
			os.system("gedit fil.txt")
	elif int(ch) ==21:
			vie=input(("Enter the file you want to view :"))
			os.system("cat vie.txt")
	elif int(ch) ==22:
			app=input(("Enter the file you want to append :"))
			os.system("cat>app.txt")
	elif int(ch) ==23:
			ared=input(("Enter the directory you want to remove :"))
			os.system("rm -rf ared")
	elif int(ch) ==24:
			aref=input(("Enter the file you want to remove :"))
			os.system("rm -rf aref")
	elif int(ch) ==25:
			os.system("fdisk -l")
	elif int(ch) ==26:
			os.system("lsblk")
	elif int(ch) ==27:
			pron=input(("Enter your name to pronounce:"))
			os.system("espeak-ng pron")
	elif int(ch) ==28:
			os.system("netstat -tnlp")
	elif int(ch) ==29:
			os.system("ls")
	elif int(ch) ==30:
			ip=input(("Enter the ip :"))
			os.system("ping ip")
	elif int(ch) ==31:
			n=input("Enter name of the file you want to copy: ")
			m=input("Enter new name: ")
			os.system("cp {} {}". format(n,m))
	elif int(ch) ==37:
			os.system("top")
	elif int(ch) ==38:
			os.system("free -m")
			os.system("echo 3> /proc/sys/vm/drop-caches")
			os.system("free -m")
	elif int(ch) ==32:
			os.system("tcpdump")
	elif int(ch) ==34:
			kil=input(("Enter the process id you want to kill:"))
			os.system("kill kil")
	elif int(ch) ==36:
			os.system("lscpu")
	elif int(ch) ==35:
			pyth=input(("Enter the name of python file:"))
			os.system("gedit pyth.py")
	elif int(ch) ==39:
			name=input(("Enter the name which you wanna add as a user:"))
			os.system("add-user name")
	elif int(ch) ==33:
			pro=input(("Enter the program for which you want to check the process id:"))
			os.system("pgrep pro")

	else:
			print("not supported")

elif r =="remote":
		ip=input("Enter remote ip:" )
		if int(ch) ==0:
			os.system("ssh {} ifconfig ".format(ip))
		elif int(ch) ==1:
			os.system("ssh {} date ".format(ip))
		elif int(ch) ==2:
			os.system("ssh {} cal ".format(ip))
		elif int(ch)==3:
			os.system("ssh {} reboot".format(ip))
		elif int(ch)==4:
			os.system("ssh {} systemctl start httpd".format(ip))
		elif int(ch)==5:
			os.system("ssh {} systemctl status httpd".format(ip))
		elif int(ch)==51:
			os.system("ssh {} systemctl stop httpd".format(ip))
		elif int(ch) ==6:
			exit()
		elif int(ch) ==7:
			print("this system is configured as datanode, choose local login")
		elif int(ch) ==8:
			os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
			os.system("ssh {} cal ".format(ip))
		elif int(ch) ==9:
			os.system("ssh {} hadoop dfsadmin -report".format(ip))
		elif int(ch)==10:
			os.system("ssh {} systemctl start docker".format(ip))
		elif int(ch)==11:
			os.system("ssh {} systemctl status docker".format(ip))
		elif int(ch)==12:
			os.system("ssh {} docker images".format(ip))
		elif int(ch)==13:
			os.system("ssh {} img=input( Enter the image you want to launch :)".format(ip))
			os.system("ssh {} ver=input(Enter the preffered version :)".format(ip))
			os.system("ssh {} docker run -it {}:{}".format(ip,img,ver))
		elif int(ch)==14:
			os.system("ssh {} systemctl stop docker".format(ip))
		elif int(ch)==15:
			os.system("ssh {} img=input( Enter the image you want to launch :)".format(ip))
			os.system("ssh {} ver=input(Enter the preffered version :)".format(ip))
			os.system("ssh {} docker run -it {}:{}".format(ip,img,ver))
		elif int(ch)==16:
			os.system("ssh {} free -m".format(ip))
		elif int(ch)==40:
            		os.system("ssh {} systemctl disable docker". format (ip))
		elif int(ch)==17:
			os.system("ssh {} ping www.google.com".format(ip))
			os.system("ssh {} docker images". format (ip))
		elif int(ch)==18:
           	 	os.system("ssh {} pip3 install ansible". format (ip))
		elif int(ch)==25:
            		os.system("ssh {} fdisk -l". format (ip))
		elif int(ch)==26:
      			os.system("ssh {} fdisk /dev/xvdf". format (ip))
		elif int(ch)==27:
			text=input("Enter your name to pronounce: ")
			os.system("ssh {} espeak-ng '{}'". format(text). format(ip))
		elif int(ch)==28:
			os.system("ssh {} netstat -tnlp". format(ip))
		elif int(ch)==20:
			name=input("Enter file name with extension: ")
			os.system("ssh {} gedit {}". format(name). format(ip))
		elif int(ch)==19:
			name=input("Enter name of the directory: ")
			os.system("ssh {} mkdir {}". format(name). format(ip))
		elif int(ch)==29:
		#name=input("Enter name of the directory: ")
			os.system("ssh {} ls". format (ip))
		elif int(ch)==21:
			name=input("Enter name of the file: ")
			os.system("ssh {} cat {}". format(name). format(ip))
		elif int(ch)==22:
			name=input("Enter name of the file: ")
			os.system("ssh {} cat>{}". format(name). format(ip))
		elif int(ch)==24:
			name=input("Enter name of the file you want to remove: ")
			os.system("ssh {} rm {}". format(name). format(ip))
		elif int(ch)==23:
			name=input("Enter name of the directory: ")
			os.system("ssh {} rm -rf {}". format(name). format(ip))
		elif int(ch)==30:
			int=input("Enter your destination ip: ")
			os.system("ssh {} espeak-ng '{}'". format(int). format(ip))
		elif int(ch)==31:
			n=input("Enter name of the file you want to copy: ")
			m=input("Enter new name: ")
			os.system("ssh {} cp {} {}". format(n,m). format(ip))
		elif int(ch)==32:
			os.system("ssh {} tcpdump". format(ip))
		elif int(ch)==33:
			n=input("Enter process name: ")
			os.system("ssh {} pgrep {}". format(n). format(ip))
		elif int(ch)==34:
			n=input("Enter process number you want to kill: ")
			os.system("ssh {} kill {}". format(n). format(ip))
		elif int(ch)==35:
			os.system("ssh {} python3". format(ip))
		elif int(ch)==36:
			os.system("ssh {} ls cpu". format(ip))
		elif int(ch)==39:
			n=input("User Name: ")
			os.system("ssh {} add user {}". format(n). format(ip))
		elif int(ch)==0:
			os.system("ssh {} ifconfig enp0s3". format(ip))
		elif int(ch)==37:
			os.system("ssh {} top". format(ip))
		elif int(ch)==38:
			os.system("ssh {} echo 3> /proc/sys/vm/drop-caches". format (ip))
		else:
			print("Invalid Choice")
else:
		print("not supported login")
