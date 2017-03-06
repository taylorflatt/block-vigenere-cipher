# Vigenere Cipher
Encrypts text using an iterative block version of the Vigenere Cipher. That is, instead of simply shifting by a certain amount, each new pass through the cipher takes a different key based on the previous iteration.

I assume a 30-character wheel that includes the alphabet and the following symbols: `, . - _`

## Usage
Make sure python 3.6 is installed. Then run,

`python main.py`

You will be asked to input some text you would like to encrypt. Finally, you will be asked to input a key which will serve as the value that is iteratively passed through the encryption.

## Example

###Input
Text: ThisIs_A_Test

Key: MyKey

### Output
Plaintext: ThisIs_A_Test

Key: MyKeyBBSWCTAS

Ciphertext: BBSWCTASVVXSH

### Explanation
The first k-characters are run through the encryption using the given text (0, k) and key (0,k) where k is the length of the key. For each subsequent iteration, the output of the previous cipher is used as input for the key. You will notice how _BBSWC_ is used instead of _MyKey_ for the second iteration.

1. First Iteration

   Text = ThisI  
   Key = MyKey  
   Output = BBSWC  
   
2. Second Iteration

   Text = s_a_t  
   Key = BBSWC  
   Output = TASVV 
   
3. Third Iteration

   Text = est  
   Key = TASVV  
   Output = XSH 
