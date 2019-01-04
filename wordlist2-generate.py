#!/usr/bin/env python3

import sys
import time

start = time.clock()
def wordlisGenerate():
	if len(sys.argv) < 2:
		print("[+] Wrong usage!!\n[+] example : python3 %s <filewordlist.txt>" %(sys.argv[0]))
		sys.exit(0)
	else:
		print("\n\t[+] Wordlist Generate-beta.0.01 (LOL :v) [+]\n")
		input_kata = input ("* Input your word to generate : ")
		get_hasil = open("output-generate2.txt","w")
		with open(sys.argv[1],'r') as my_wordList:
			for x in my_wordList:
				get_hasil.write(input_kata+"{}\n".format(x.strip()))
				get_hasil.write(x.strip()+"{}\n".format(input_kata))
				# print(input_kata+"{}".format(x.strip()))
		get_hasil.close()

if __name__ == '__main__':
	try:
		wordlisGenerate()
		print("\n[+] Done Generate . . .\n[+] Time Generate : {} sec . .\n[+] Output Name   : output-generate2.txt".format(time.clock() - start))
	except Exception as e:
		print("ada kesalahan :", e)