import argparse
import sys
from datetime import datetime
from os import makedirs
from os.path import join

import joblib
import numpy as np
from eval_utils import evaluate_model_word_analogies
from word2vec import load_model_training_output

sys.path.append("..")
from utils import get_model_checkpoint_filepaths


def parse_args() -> argparse.Namespace:
    """
    Parses arguments sent to the python script.

    Returns
    -------
    parsed_args : argparse.Namespace
        Parsed arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_dir",
        type=str,
        default="",
        help="Directory of the model to evaluate",
    )
    parser.add_argument(
        "--model_name", type=str, default="word2vec", help="Name of the trained model"
    )
    parser.add_argument(
        "--dataset_name",
        type=str,
        default="enwiki",
        help="Name of the dataset the model is trained on",
    )
    parser.add_argument(
        "--sswr_dataset_filepath",
        type=str,
        default="",
        help="Filepath of the SSWR test dataset",
    )
    parser.add_argument(
        "--msr_dataset_filepath",
        type=str,
        default="",
        help="Filepath of the MSR test dataset",
    )
    parser.add_argument(
        "--vocab_size",
        type=int,
        default=30000,
        help="Vocabulary size to use when evaluating on the test datasets",
    )
    parser.add_argument(
        "--top_n_prediction",
        type=int,
        default=1,
        help="Which top-N prediction we would like to do",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="output",
        help="Output directory to save evaluation results",
    )
    return parser.parse_args()


def save_analogies_accuracies_to_file(
    analogies_dataset_name: str, output_dir: str, analogies_accuracies: dict
) -> None:
    """
    Saves analogy accuracies to file.

    Parameters
    ----------
    analogies_dataset_name : str
        Name of the analogies dataset
    output_dir : str
        Output directory
    analogies_accuracies : dict
        Dictionary containing accuracies
    """
    analogies_output_filepath = join(output_dir, f"{analogies_dataset_name}.joblib")
    joblib.dump(analogies_accuracies, analogies_output_filepath)


def evaluate_word2vec(
    model_dir: str,
    model_name: str,
    dataset_name: str,
    sswr_dataset_filepath: str,
    msr_dataset_filepath: str,
    vocab_size: int,
    top_n_prediction: int,
    output_dir: str,
) -> None:
    """
    Evaluates a word2vec model on the SSWR and MSR test analogy datasets.

    Parameters
    ----------
    model_dir : str
        Directory of the model to evaluate.
    model_name : str
        Name of the trained model.
    dataset_name : str
        Name of the dataset the model is trained on.
    sswr_dataset_filepath : str
        Filepath of the SSWR test dataset.
    msr_dataset_filepath : str
        Filepath of the MSR test dataset.
    vocab_size : int
        Vocabulary size to use when evaluating on the test datasets.
    top_n_prediction : int
        Which top-N prediction we would like to do.
    output_dir : str
        Output directory to save evaluation results.
    """
    # Load output from training word2vec
    w2v_training_output = load_model_training_output(
        model_training_output_dir=model_dir,
        model_name=model_name,
        dataset_name=dataset_name,
    )
    last_embedding_weights = w2v_training_output["last_embedding_weights"]
    words = w2v_training_output["words"]
    word_to_int = w2v_training_output["word_to_int"]

    # Append date/time to output directory.
    output_dir = join(output_dir, datetime.now().strftime("%d-%b-%Y_%H-%M-%S"))
    makedirs(output_dir, exist_ok=True)

    # SSWR
    print("--- Evaluating SSWR ---")
    sswr_accuracies = evaluate_model_word_analogies(
        analogies_filepath=sswr_dataset_filepath,
        word_embeddings=last_embedding_weights,
        word_to_int=word_to_int,
        words=words,
        vocab_size=vocab_size,
        top_n=top_n_prediction,
    )
    save_analogies_accuracies_to_file("sswr", output_dir, sswr_accuracies)
    print(sswr_accuracies)

    # MSR
    print("--- Evaluating MSR ---")
    msr_accuracies = evaluate_model_word_analogies(
        analogies_filepath=msr_dataset_filepath,
        word_embeddings=last_embedding_weights,
        word_to_int=word_to_int,
        words=words,
        vocab_size=vocab_size,
        top_n=top_n_prediction,
    )
    save_analogies_accuracies_to_file("msr", output_dir, msr_accuracies)
    print(msr_accuracies)


if __name__ == "__main__":
    args = parse_args()

    # Perform evaluation
    evaluate_word2vec(
        model_dir=args.model_dir,
        model_name=args.model_name,
        dataset_name=args.dataset_name,
        sswr_dataset_filepath=args.sswr_dataset_filepath,
        msr_dataset_filepath=args.msr_dataset_filepath,
        vocab_size=args.vocab_size,
        top_n_prediction=args.top_n_prediction,
        output_dir=args.output_dir,
    )
