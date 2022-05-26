# PGP-Passbreak-Attempt
A Reddit user sent me a private message, through Reddit, asking for some help related to PGP, he proposed a problem, gave me some constraints for the password and I attempted to help him as best I could, my curiosity was peaked with this sudden challenge...two hours later this script was the result.

## Password constraints
1. Alphabetic upper and lowercase
2. Shifted 10 (A > K)
3. English word

If the PGP Message and password constraints are correct, it *should* be able to decipher the message eventually according to the Reddit user.

## Compressed files
I had to compress two text files that were larger than 25 mb,to upload it to GitHub, unzip them to use them with the python script.

## Python
I used python 3.9 to create this.
Libraries os and pgpy used.

## Credit
Thank you dwyl and your english wordlist for making my job easier.
- https://github.com/dwyl/english-words
- https://github.com/SecurityInnovation/PGPy
