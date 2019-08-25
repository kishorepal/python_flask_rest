FROM python:3.6

ARG project_dir=/src/

ADD src/lib_list.txt $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txtS