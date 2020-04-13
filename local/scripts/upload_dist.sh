set -ex

user=$1
host=$2
root=$3
project=$4
port=$5

remote=$user@$host
path=$root/$project
front_dist=frontend-dist.tar.gz
backend_dist=backend-dist.tar.gz

ssh $remote mkdir -p $path/.doy/local
rsync -av .doy/local/$front_dist $remote:$path/.doy/local/$front_dist
rsync -av .doy/local/$backend_dist $remote:$path/.doy/local/$backend_dist
rsync -av Dockerfile $remote:$path/Dockerfile
ssh $remote $root/doy/local/scripts/local_deploy.sh $root $project $port
