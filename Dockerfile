FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c rdkit rdkit=2020.09
RUN conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cpuonly -c pytorch
RUN conda install scipy=1.5.2
RUN conda install seaborn=0.11.0=py_0
RUN pip install tqdm
RUN pip install pyyml
RUN pip install scikit-learn==0.23.2

WORKDIR /repo
COPY ./repo
