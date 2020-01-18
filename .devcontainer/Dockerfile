#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------
FROM python:3.8

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Or your actual UID, GID on Linux if not the default 1000
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Configure apt and install packages
RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils 2>&1 \
    # Verify git, process tools, lsb-release (common in install instructions for CLIs) installed
    && apt-get -y install git iproute2 procps lsb-release wget
# install DVC
RUN wget https://dvc.org/deb/dvc.list -O /etc/apt/sources.list.d/dvc.list \ 
    && apt-get update \
    && apt-get install dvc
## install dvc compelitation
RUN apt install --reinstall bash-completion \
    && wget -O /etc/bash_completion.d/dvc https://raw.githubusercontent.com/iterative/dvc/master/scripts/completion/dvc.bash \
    && echo ". /etc/bash_completion" >> ~/.bashrc
## install git compelitation 
RUN wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -O ~/.git-completion.bash \
    && chmod a+x ~/.git-completion.bash \
    && echo "source ~/.git-completion.bash" >> ~/.bashrc
# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* 
# install mlflow
RUN pip install mlflow
# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog