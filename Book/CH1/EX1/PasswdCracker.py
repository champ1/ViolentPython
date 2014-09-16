#!/usr/bin/python
# -*- coding: utf-8 -*-
import crypt

def testPass(hashAlg, salt, cryptPass):
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, '$' + hashAlg + '$' + salt)
        print "This is original:  " + cryptPass
        print "This is tested one:" + cryptWord
        if cryptWord == cryptPass:
            print '[+] Found Password: ' + word + '\n'
            return
    print '[-] Password Not Found.\n'
    return


def main():
    passFile = open('passwd.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            if '$' in line:
                hashAlg = cryptPass.split('$')[1]
                salt = cryptPass.split('$')[2]
                #cryptPass = cryptPass.split('$')[3]
                print '[*] Cracking Password For: ' + user
                testPass(hashAlg, salt, cryptPass)


if __name__ == '__main__':
    main()
