python train_word2phrase.py \
--text_data_dir data/enwiki-20200901 \
--dataset_name enwiki-20200901 \
--starting_epoch_nr 1 \
--n_epochs 2 \
--max_vocab_size -1 \
--min_word_count 5 \
--threshold 200 \
--threshold_decay 0.5 \
--phrase_sep _ \
--output_dir data