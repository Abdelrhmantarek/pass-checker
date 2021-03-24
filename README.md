# pass-checker
Tool that you can use to check if your password is secure, using the https://haveibeenpwned.com/ API. Input a password and check if it has been hacked.


![pass_checker_abdelrhman](https://user-images.githubusercontent.com/41340967/112235775-fff8e380-8c47-11eb-82aa-526371f8fb5d.png)



we are going to use 2 types of methods to check :
- Using Console  
- Using Text File


1.Using Console

   ->> In first type we are going to enter the inputs through console.
 
   ->> Here inputs means passwords.
 
   ->> We can give any number of inputs by giving spaces.

2. Using Text File

->> In second type we are going to save our passwords in simple text file that is .txt .

->> We then open our text file and read our passwords line by line.

->> Here also we can save any number of passwords.


---

## Some info you should know about..

DATA BREACH:

- Our passwords gets leaked all the time.
- Ever heard of Data breaches? A data breach is the intentional or unintentional release of secure or private/confidentional information to an untrusted environment. example:- facebook, linkedin, Equifax, yahoo etc, has been hacked with data breaches.
- All these companies sometimes leaks their databases therefore, our usernames and passwords gets leaked to the public.
- Hackers compile these lists of usernames and passwords and try to login to different services.


OUR API:

- As explained above, there are databases or we can think them as massive excel files of all emails and passwords that have ever been leaked throughout the history.
- Using these databases there is a website called https://haveibeenpwned.com/ created by Troy Hunt where we can check whether our emails or passwords have ever been pwned or not.
- But remember even though this website is trustworthy which also uses https a secured way of transferring data, yet we should not trust because the best security is to trust no one.
- Because what happens here is, whenever we enter our passwords or emails it will be transferred to the servers somewhere around the world throught the internet.
- And that is why we build our own tool in our own PC to securely check our passwords.
- And this above mentioned website gives us an API called Password API which we will be using to build our tool.


HASH Functions :

- One needs to always Hash or Encrypt their passwords before storing it.
- A Hash function is simply a function that generates a value of fixed length for each given input.
- There are many Algorithms of Hash functions such as SHA1, MD5, SHA-256 etc.
- https://passwordsgenerator.net/sha1-hash-generator/ --->Using this website we can hash our passwords.
- As mentioned before, the Password API uses SHA1 Algorithm for hashing the passwords.
- For example, let passy123 be a password, the hashed form is going to be '239FADF8AF0166CCD8528CC41564635F1580F306'. And no matter how many times I give passy123 the hashed form is going to be the same, This technique is called Idempotent.


**MODULES**

- sys module : The sys module is built in module which comes along with python interpreter.

- requests module : The requests module is not a built in module, This module needs to be downloaded. This module is used to make requests to the browser during runtime.

`pip install requests`

- hashlib module : The hashlib module is not a built in module, this module needs to be downloaded. This module is used to hash our password during runtime.

`pip install hashlib`

Password API:

```
import requests
url = 'https://api.pwnedpasswords.com/range/' + [hashedpassword]
res = requests.get(url)
```

- The first step is to import a requests module.

- The requests module is going to allow us to make a request to haveibeenpwned website through browser.

- Its kinda like having browser without a actual browser.

- The second step is to assign a Password API url to a variable named 'url'.

- Here hashedpassword is the hashed form of your password.

- As the example mentioned above, the hashed password for 'passy123' is '239FADF8AF0166CCD8528CC41564635F1580F306'.

- But in the url we just pass the 5 prefix of your hashed password.

- So the code will basically look like 👇

```
import requests
url = 'https://api.pwnedpasswords.com/range/' + '239FA'
res = requests.get(url)
```

- Third step is to request API through request.get(url) method and assigning it to a variable called 'res'.



K-ANONYMITY :

- This is a modern technique that big companies like FAANG use to protect the privacy of their customers.
- K-Anonymity allows somebody to receive information about us but yet still not know who we are.
- The way this works is that we only give the first 5 characters of our hashed passwords.
- The Password API has the list of all the passwords that have been leaked, However all these passwords are hashed with SHA1 Algorithm.
- So its going to look in its databases of all these passwords and pick all the hashed passwords that has these first 5 characters.
- Hence in response we will get all the hashed passwords which has these first 5 characters and then we can compare our entire hashed password with the list of response hashed passwords in our own PC.
- This way the Passowrd API is never going to know our full hash and never ever be able to guess our password.

