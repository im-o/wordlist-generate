#!/usr/bin/env python3

import sys
import time

start = time.clock()
tampung_kata = []
tampung_wordlist = []
def wordlisGenerate():
	if len(sys.argv) < 3:
		print("[+] Wrong usage!!\n[+] example : python3 %s <kataYgDigenerate.txt> <filewordlist.txt>" %(sys.argv[0]))
		sys.exit(0)
	else:
		print("\n\t[+] Wordlist Generate-beta.0.01 (LOL :v) [+]\n")
		with open(sys.argv[1],'r') as word_generate:
			for x in word_generate:
				tampung_kata.append(x.strip())
		with open(sys.argv[2],'r') as my_wordList:
			for x in my_wordList:
				tampung_wordlist.append(x.strip())

if __name__ == '__main__':
	try:		
		wordlisGenerate()
		get_hasil = open("output-generate.txt","w")
		for x in tampung_kata:
			for y in tampung_wordlist:
				get_hasil.write("{0}{1}\n".format(x,y))
				get_hasil.write("{0}{1}\n".format(y,x))
		print("\n[+] Done Generate . . .\n[+] Time Generate : {} sec . .\n[+] Output Name   : output-generate.txt".format(time.clock() - start))

	except Exception as e:
		print("ada kesalahan :", e)
