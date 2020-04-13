set -ex

root=$1
project=$2
port=$3

cd $root/$project

# extract frontend
mkdir -p frontend
cd frontend
tar xzf ../.doy/local/frontend-dist.tar.gz
cd ..

# extract backend
tar xzf .doy/local/backend-dist.tar.gz

# OPTIONAL setup HTTPS cert

# OPTIONAL setup nginx site

# OPTIONAL setup docker

# build docker image
# TODO: exclude frontend files
docker build -t $project .

# stop previous docker container
docker stop $project || true

# start docker container
docker run \
    -itd \
    --rm \
    --name $project \
    -p $port:8000 \
    -v $PWD/frontend/dist:/frontend/dist \
    $project

# inspect docker output
docker logs --tail 35 $project
