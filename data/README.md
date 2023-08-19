# Datasets

To add a dataset add a subsection to this file called `Dataset: <dataset name>` and include a code block with the commands to download the dataset to the folder `<dataset name>`. Then use the helper script to download a dataset at the command line:
``` sh
./get-dataset.sh <dataset name> | sh
```

## Dataset: pm-transcripts

``` sh
git clone https://github.com/wragge/pm-transcripts pm-transcripts
cd pm-transcripts
git checkout -b thaum-data-main 97683f1
```

## Dataset: hansard-xml

You can use sed at the command line to change this script on the fly.
`./get-dataset.sh hansard-xml | sed 's/YEAR=2020/YEAR=2019/g' | sh`
We have remote urls for 1998 - 2020.

``` sh
DATA_DIR=$(pwd)
REMOTE_URLS="$(pwd)/remotes/hansard-urls"
YEAR=2020
THREADS=20
mkdir -p hansard-xml/senate/${YEAR} hansard-xml/hofreps/${YEAR}
cd ${DATA_DIR}/hansard-xml/senate/${YEAR}
cat ${REMOTE_URLS}/${YEAR}-au-hansard-senate.csv | xargs -n 1 -P ${THREADS} wget -q
cd ${DATA_DIR}/hansard-xml/hofreps/${YEAR}
cat ${REMOTE_URLS}/${YEAR}-au-hansard-hofreps.csv | xargs -n 1 -P ${THREADS} wget -q
```