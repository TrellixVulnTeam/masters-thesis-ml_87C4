#!/bin/bash
screen -dmS word2phrase_dawiki -L -Logfile word2phrase_dawiki.logs python train_word2phrase.py \
--text_data_dir data/dawiki-20210101 \
--dataset_name dawiki-20210101 \
--starting_epoch_nr 1 \
--n_epochs 2 \
--max_vocab_size -1 \
--min_word_count 5 \
--threshold 200 \
--threshold_decay 0.5 \
--phrase_sep _ \
--output_dir data
