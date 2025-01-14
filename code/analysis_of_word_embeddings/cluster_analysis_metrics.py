import numpy as np
from sklearn.metrics import (
    calinski_harabasz_score,
    davies_bouldin_score,
    silhouette_score,
)


def silhouette_score_metric(
    word_embeddings: np.ndarray, cluster_labels: np.ndarray, clusterer, **kwargs: dict
) -> tuple:
    """
    Wrapper function for silhouette score used in `cluster_analysis` function.

    Parameters
    ----------
    word_embeddings : np.ndarray
        Word embeddings/pairwise distances to evaluate on
    cluster_labels : np.ndarray
        Predicted cluster labels
    clusterer : clustering instance
        Clustering instance (fitted on data)
    **kwargs : dict
        Keyword arguments passed to `silhouette_score`

    Returns
    -------
    result : tuple
        Result as a triple, consisting of metric title, metric score and whether or not
        the metrics objective function is to maximize the metric score.
    """
    # Compute metric scores
    if cluster_labels is None:
        cluster_labels = clusterer.labels_
    num_unique_labels = len(np.unique(cluster_labels))
    num_samples = len(word_embeddings)
    if 2 <= num_unique_labels <= num_samples - 1:
        metric_score = silhouette_score(
            X=word_embeddings, labels=cluster_labels, **kwargs
        )
    else:
        metric_score = np.nan

    # Return tuple with result
    return "Silhouette Coefficient", metric_score, True


def davies_bouldin_score_metric(
    word_embeddings: np.ndarray, cluster_labels: np.ndarray, clusterer, **_: dict
) -> tuple:
    """
    Wrapper function for Davies–Bouldin index used in `cluster_analysis` function.

    Parameters
    ----------
    word_embeddings : np.ndarray
        Word embeddings to evaluate on
    cluster_labels : np.ndarray
        Predicted cluster labels
    clusterer : clustering instance
        Clustering instance (fitted on data)
    **_ : dict
        Keyword arguments sent into the void (not used)

    Returns
    -------
    result : tuple
        Result as a triple, consisting of metric title, metric score and whether or not
        the metrics objective function is to maximize the metric score.
    """
    # Compute metric scores
    if cluster_labels is None:
        cluster_labels = clusterer.labels_
    metric_score = davies_bouldin_score(X=word_embeddings, labels=cluster_labels)

    # Return tuple with result
    return "Davies–Bouldin index", metric_score, False


def calinski_harabasz_score_metric(
    word_embeddings: np.ndarray, cluster_labels: np.ndarray, clusterer, **_: dict
) -> tuple:
    """
    Wrapper function for Calinski-Harabasz Index used in `cluster_analysis` function.

    Parameters
    ----------
    word_embeddings : np.ndarray
        Word embeddings to evaluate on
    cluster_labels : np.ndarray
        Predicted cluster labels
    clusterer : clustering instance
        Clustering instance (fitted on data)
    **_ : dict
        Keyword arguments sent into the void (not used)

    Returns
    -------
    result : tuple
        Result as a triple, consisting of metric title, metric score and whether or not
        the metrics objective function is to maximize the metric score.
    """
    # Compute metric scores
    if cluster_labels is None:
        cluster_labels = clusterer.labels_
    metric_score = calinski_harabasz_score(X=word_embeddings, labels=cluster_labels)

    # Return tuple with result
    return "Calinski-Harabasz Index", metric_score, True
