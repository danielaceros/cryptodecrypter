<html>
<div align="center">
<img src="https://blog.cloudflare.com/content/images/2021/02/Hybrid-WAF-keys.png" alt="alt text" width="600" height="300"></img>
</div>
<h1 align="center">@danielaceros
<div align="center">
<a href=https://github.com/danielaceros><img src="https://img.shields.io/static/v1?label=&labelColor=505050&message=@danielaceros&color=%230076D6&style=flat&logo=google-chrome&logoColor=%230076D6" alt="website"/></a>
<img src="https://img.shields.io/github/followers/danielaceros?style=social" alt="Star Badge"/>
<a><img src="https://img.shields.io/github/last-commit/danielaceros/instaloaderbot" alt="Join Community Badge"/></a>
<a><img src="https://img.shields.io/github/repo-size/danielaceros/instaloaderbot" />
</div>
</html>

# cryptodecrypter
A simple script that allows you to ENCRYPT and DECRYPT files using a KEY.
## Getting Started
Download the repo, and install the necessary modules if you don't have it
```bash
pip/pip3 install cryptography
pip/pip3 install time
pip/pip3 install tqdm
```
## Usage
Use the 'crypt.py' to encrypt any file, you only have to put the file path once the script request it, it will be generated a file 'key.key', don't delete it.
Use the 'decrypt.py' on the same path that the file and the 'key.key', and introduce your path, so the file will be decrypted.
## Running Code
```bash
python crypt.py #to crypt
python decrypt.py # to decrypt
python3 crypt.py # to crypt
python3 decrypt.py # to decrypt
```
## License
[GPL](https://choosealicense.com/licenses/gpl-3.0/)
