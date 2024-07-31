import os
import subprocess

CHALLENGE_DIR = "../../../LLM_CTF_Challenges"

# find . -type f -name README.md
challenges = subprocess.check_output(f"find {CHALLENGE_DIR} -type f -name README.md", shell=True).decode().split("\n")
challenges = [c for c in challenges if c]
# print(challenges, len(challenges))

# docker run -v $challenge_dir:/usr/src/app/artifacts binexpsolver
for challenge in challenges:
    challenge_dir = os.path.dirname(challenge)
    # realpath
    challenge_dir = os.path.realpath(challenge_dir)
    print(challenge_dir)
    input()
    os.system(f"docker run -v {challenge_dir}:/usr/src/app/artifacts binexpsolver")
    print("Done with challenge", challenge_dir)