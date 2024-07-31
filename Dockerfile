# Use an official Python runtime as a parent image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /usr/src/app

RUN yes | unminimize


# RUN apt-get update && apt-get install -y coreutils build-essential libssl-dev libffi-dev python3-dev curl
RUN dpkg --add-architecture i386
RUN apt-get update -y
# RUN apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386
RUN apt-get install -y libc6-i386
RUN apt-get install -y coreutils build-essential libssl-dev libffi-dev python3-dev curl file python-is-python3 python3-pip radare2
RUN apt-get install -y gdb

COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN  --mount=type=cache,target=/root/.cache \
    pip3 install -r requirements.txt --break-system-packages

# Copy the current directory contents into the container at /usr/src/app
COPY . .
COPY flag.txt /proc/flag


# Make port 80 available to the world outside this container
EXPOSE 80

# Run main.py when the container launches
CMD ["python3", "-u", "src/main.py"]
