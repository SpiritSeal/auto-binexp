# Automatic binexp CTF solver PoC

> This repo contains a selection of code from this last week highlighting the current approach I am iterating and its' limitations

## Solution Progress

| Challenge       | Solve Status |
| -------- | ------- |
| Lab 1 0x00  | Consistely Solves    |
| Lab 1 0x01 | Consistently Solves     |
| Lab 1 0x02    | Consistently Solves    |
| Lab 1 0x03  | Infinitely Loops (repeatedly attempts to run the same Shift Cipher decryption code without changing it)    |
| Lab 2 Challenge 1 | Usually hangs self while running ./target binary with generated shellcode payload     |

## Preparation
```sh
# Copy over the arifacts you would like to run on from ./samples to ./artifacts. Optionally include a README describing the challenge.
# Inititalize a langchain_openai Chat variable named model in ./src/_config.py, including any relevant API keys
```


## Run locally (warning: arbitrary code exection):
```sh
pip install -r requirements.txt
python src/main.py
```

## Run in a docker container
```sh
./br.sh
```