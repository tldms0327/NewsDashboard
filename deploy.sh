#!/bin/bash

 $( aws ecr get-login --no-include-email --region ap-northeast-2 --profile ybigta-conference)
export VER=$1

docker build --tag 532214462726.dkr.ecr.ap-northeast-2.amazonaws.com/crawler:$VER -f Dockerfile .

docker push 532214462726.dkr.ecr.ap-northeast-2.amazonaws.com/crawler:$VER
docker tag 532214462726.dkr.ecr.ap-northeast-2.amazonaws.com/crawler:$VER 532214462726.dkr.ecr.ap-northeast-2.amazonaws.com/crawler:dev
docker push 532214462726.dkr.ecr.ap-northeast-2.amazonaws.com/crawler:dev
