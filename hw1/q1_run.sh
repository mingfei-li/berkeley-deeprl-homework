#!/bin/zsh

for n_steps ({1000..30000..1000}) {
        echo "n_steps = $n_steps" >> log
        python cs285/scripts/run_hw1.py \
                --expert_policy_file cs285/policies/experts/$1.pkl \
                --env_name $1-v4 --exp_name bc_${1:l} --n_iter 1 \
                --eval_batch_size 5000 \
                --expert_data cs285/expert_data/expert_data_$1-v4.pkl \
                --video_log_freq -1 \
                --train_batch_size 1000 \
                --num_agent_train_steps_per_iter $n_steps >> log
}