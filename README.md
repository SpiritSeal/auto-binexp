# Automatic binexp CTF solver PoC

> This repo contains a selection of code from this last week highlighting the current approach I am iterating and its' limitations

## Solution Progress

| Challenge       | Solve Status |
| -------- | ------- |
| Lab 1 0x00  | Consistely Solves    |
| Lab 1 0x01 | Consistently Solves     |
| Lab 1 0x02    | Consistently Solves    |
| Lab 1 0x03  | Infinitely Loops (repeatedly attempts to run the same Shift Cipher decryption code without changing it)    |
| Lab 2 Challenge 1 | Usually Crashes while running generated      |

## Preparation
```sh
# Copy over the arifacts you would like to run on from ./samples to ./artifacts. Optionally include a README describing the challenge.
```

> Copy to .env
```
LLM_API_KEY="sk-..."
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