FROM python:3.12-bullseye

#  Install tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-11-jdk wget unzip curl \
    && rm -rf /var/lib/apt/lists/*

# Install Allure CLI
RUN wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz \
    && tar -zxvf allure-2.27.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure \
    && rm allure-2.27.0.tgz

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# set the working directory
WORKDIR /app

# copy the project into the container
COPY . .

# set the default command
CMD ["tail", "-f", "/dev/null"]
