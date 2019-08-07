FROM amazonlinux

# time docker build . -f Dockerfile -t dsheffner/yaml:latest
# docker run -it dsheffner/yaml:latest

# test to see if the c library is working
# from yaml import CLoader as Loader

RUN \
    yum update -y && \
    yum upgrade -y && \
    yum install -y \
        bzip2-devel \
        fail2ban \
        file \
        gcc \
        glibc-devel \
        gzip \
        java-1.8.0-openjdk.x86_64 \
        libffi-devel \
        libyaml-devel.x86_64 \
        make \
        ncurses-devel \
        openssl-devel \
        readline-devel \
        sqlite-devel \
        tar.x86_64 \
        tk-devel \
        tmux \
        uuid-devel \
        wget \
        xz-devel \
        zlib-devel

# install python
RUN wget -q https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz && \
    tar -xf Python-3.7.4.tgz && \
    cd Python-3.7.4/ && \
    ./configure --prefix=/opt/python37 --enable-shared --enable-optimizations && \
     make -j4 && \
     make altinstall

# upgrade pip
RUN \
    export LD_LIBRARY_PATH=/opt/python37/lib && /opt/python37/bin/pip3.7 install --upgrade pip

COPY ./bashrc /root/.bashrc

# yaml c library
RUN \
     wget -q https://pyyaml.org/download/libyaml/yaml-0.2.2.tar.gz && \
     tar -xf yaml-0.2.2.tar.gz && \
     cd yaml-0.2.2 && \
     ./configure && \
     make -j4 && \
     make install

# pyyaml
 RUN \
    wget -q https://pyyaml.org/download/pyyaml/PyYAML-5.1.2.tar.gz && \
    tar -xf PyYAML-5.1.2.tar.gz && \
    cd PyYAML-5.1.2 && \
    export LD_LIBRARY_PATH=/opt/python37/lib && /opt/python37/bin/python3.7 setup.py --with-libyaml install

COPY ./stuff.yaml /root/stuff.yaml
COPY ./Yamlexample.py /root/Yamlexample.py

CMD ["/bin/bash"]
