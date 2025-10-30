---
layout: post
title: "Don't Anger IT"
date: 2025-10-10
---


# Don't Anger IT
**CTF:** MST Miner 2025
**Challenge Description:**

```md
We would love to give you this flag, but our former IT Admin has left on not the greatest of terms and has encrypted the file.
Thankfully, he was never the most secure individual, and we believe the password for the file is an old local account password.
We have several of our users and their exposed password hashes from a data breach. If you can figure out what his password was 
and decrypt the file, the flag is yours
```

## Finding the password

Running hashcat, a popular hash cracker, on the breached hashes with rockyou.txt we get the output:

```bash
┌──(kali㉿kali)-[~/Desktop]
└─$ hashcat -m 0 extractedhashes /usr/share/wordlists/rockyou.txt

e1964798cfe86e914af895f8d0291812:spongebob                
6c84cbd30cf9350a990bad2bcc1bec5f:patrick                  
5912d7bfd10f631f1715bf85bbb72d97:genius                   
5b14843741dfb491e8e57589667ad88a:invincible               
926811886f475151c52dd365c90a7efc:traitor                  
86802be68d8e6475a5b4a6e35385b277:scammer  
```

All that is left is unzipping the zip with the password `spongebob`, we are left with flag.txt a file containing only the flag `flag{Strong-passwords?Never-heard-of-her}`.

## Potential Alternatives

Although I did not try, one could probably have ran zip2john and used John the Ripper to bruteforce the password.