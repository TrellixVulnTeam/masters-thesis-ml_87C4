#!/bin/bash
screen -dmS postprocess_word2vec_semeval_2010_task_14 -L -Logfile postprocess_word2vec_semeval_2010_task_14.logs python postprocess_word2vec_embeddings.py \
--model_training_output_dir ../output/word2vec_training/word2vec_semeval_2010_task_14 \
--model_name word2vec \
--dataset_name semeval_2010_task_14 \
--vocab_size -1 \
--annoy_index_n_trees 500 \
--scann_num_leaves_scaling 5
screen -r postprocess_word2vec_semeval_2010_task_14
