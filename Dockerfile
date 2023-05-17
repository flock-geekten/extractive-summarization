FROM ubuntu:18.04


# aptとpipの更新
RUN apt update
RUN apt -y upgrade
RUN apt install -y python3 python3-pip


# mecabとmecab-ipadic-NEologdの導入
RUN apt install -y mecab
RUN apt install -y libmecab-dev
RUN apt install -y mecab-ipadic-utf8
RUN apt install -y git
RUN apt install -y make
RUN apt install -y curl
RUN apt install -y xz-utils
RUN apt install -y file
RUN apt install -y sudo
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
RUN cd /mecab-ipadic-neologd && ./bin/install-mecab-ipadic-neologd -n -y

# pythonのライブラリ
WORKDIR /home
COPY requirements.txt ${PWD}
RUN pip3 install -r requirements.txt


# 以下はjupyterlabの拡張機能を使うための前処理(最新版のnode.jpのインストール)
RUN apt install -y nodejs npm curl
RUN npm cache clean
RUN npm install n -g
RUN n stable
RUN ln -sf /usr/local/bin/node /usr/bin/node
RUN apt purge -y nodejs npm


## JupyterLabの拡張機能
# 自動整形
RUN jupyter labextension install @ryantam626/jupyterlab_code_formatter
RUN jupyter serverextension enable --py jupyterlab_code_formatter
# jupyterlabの"Table of Contents"
RUN jupyter labextension install @jupyterlab/toc


# 作業ディレクトリ
WORKDIR /home/workspace