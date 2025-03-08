#!/bin/zsh

python cs285/scripts/run_hw1.py \
    --expert_policy_file cs285/policies/experts/$1.pkl \
    --env_name $1-v4 --exp_name dagger_${1:l} --n_iter 10 \
    --do_dagger --expert_data cs285/expert_data/expert_data_$1-v4.pkl