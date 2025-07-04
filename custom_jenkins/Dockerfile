FROM python:3.9-slim

USER root

RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    python3-venv \
    docker.io && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# RUN ln -sf /usr/local/bin/python /usr/local/bin/python3

RUN groupadd -g 1000 jenkins && \
    useradd -d /home/jenkins -u 1000 -g jenkins -m jenkins

WORKDIR /home/jenkins

USER jenkins

ENV PATH="/usr/bin:${PATH}"





