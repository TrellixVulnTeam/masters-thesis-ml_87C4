import numpy as np
from cdbw import CDbw
from dsi import dsi
from dunn_index import dunn
from hdbscan import HDBSCAN
from hdbscan.validity import validity_index as dbcv
from s_dbw import SD, S_Dbw
from sklearn.metrics import davies_bouldin_score, silhouette_score


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


def dsi_score_metric(
    word_embeddings: np.ndarray, cluster_labels: np.ndarray, clusterer, **kwargs: dict
) -> tuple:
    """
    Wrapper function for Distance-based Separability Index (DSI) used in `cluster_analysis` function.

    Parameters
    ----------
    word_embeddings : np.ndarray
        Word embeddings/pairwise distances to evaluate on
    cluster_labels : np.ndarray
        Predicted cluster labels
    clusterer : clustering instance
        Clustering instance (fitted on data)
    **kwargs : dict
        Keyword arguments passed to `dsi`

    Returns
    -------
    result : tuple
        Result as a triple, consisting of metric title, metric score and whether or not
        the metrics objective function is to maximize the metric score.
    """
    # Compute metric scores
    if cluster_labels is None:
        cluster_labels = clusterer.labels_

    metric_score = dsi(X=word_embeddings, labels=cluster_labels, **kwargs)

    # Return tuple with result
    return "Distance-based Separability Index", metric_score, True


def dbcv_score_metric(
    word_embeddings: np.ndarray, cluster_labels: np.ndarray, clusterer, **kwargs: dict
) -> tuple:
    """
    Wrapper function for Density Based Clustering Validation index (DBCV) used in `cluster_analysis` function.

    Parameters
    ----------
    word_embeddings : np.ndarray
        Word embeddings/pairwise distances to evaluate on
    cluster_labels : np.ndarray
        Predicted cluster labels
    clusterer : clustering instance
        Clustering instance (fitted on data)
    **kwargs : dict
        Keyword arguments passed to `dbcv`

    Returns
    -------
    result : tuple
        Result as a triple, consisting of metric title, metric score and whether or not
        the metrics objective function is to maximize the metric score.
    """
    # Compute metric scores
    if cluster_labels is None:
        cluster_labels = clusterer.labels_

    metric_score = dbcv(
        X=word_embeddings, labels=cluster_labels, per_cluster_scores=False, **kwargs
    )

    # Return tuple with result
    return "Density Based Clustering Validation index", metric_score, True


def davies_bouldin_score_metric(
    word_embeddings: np.ndarray, cluster_labels: np.ndarray, clusterer, **_: dict
) -> tuple:
    """
    Wrapper function for Davies–Bouldin index used in `cluster_analysis` function.

    Parameters
    ----------
    word_embeddings : np.ndarray
        Word embeddings/pairwise distances to evaluate on
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


def dunn_score_metric(
    cluster_labels: np.ndarray, word_embeddings: np.ndarray, **_: dict
) -> tuple:
    """
    Wrapper function for Dunn score used in `cluster_analysis` function.

    Parameters
    ----------
    cluster_labels : np.ndarray
        Predicted cluster labels
    word_embeddings : np.ndarray
        Pairwise word distances
    **_ : dict
        Keyword arguments sent into the void (not used)

    Returns
    -------
    result : tuple
        Result as a triple, consisting of metric title, metric score and whether or not
        the metrics objective function is to maximize the metric score.
    """
    # Compute metric scores
    metric_score = dunn(labels=cluster_labels, distances=word_embeddings)

    # Return tuple with result
    return "Dunn index", metric_score, True


def s_dbw_score_metric(
    word_embeddings: np.ndarray, cluster_labels: np.ndarray, clusterer, **kwargs: dict
) -> tuple:
    """
    Wrapper function for S_Dbw score used in `cluster_analysis` function.

    Parameters
    ----------
    word_embeddings : np.ndarray
        Word embeddings/pairwise distances to evaluate on
    cluster_labels : np.ndarray
        Predicted cluster labels
    clusterer : clustering instance
        Clustering instance (fitted on data)
    **kwargs : dict
        Keyword arguments passed to `S_Dbw`

    Returns
    -------
    result : tuple
        Result as a triple, consisting of metric title, metric score and whether or not
        the metrics objective function is to maximize the metric score.
    """
    # Compute metric scores
    if cluster_labels is None:
        cluster_labels = clusterer.labels_
    metric_score = S_Dbw(
        X=word_embeddings, labels=cluster_labels, metric="cosine", **kwargs
    )

    # Return tuple with result
    return "S_Dbw validity index", metric_score, False


def sd_score_metric(
    word_embeddings: np.ndarray, cluster_labels: np.ndarray, clusterer, **kwargs: dict
) -> tuple:
    """
    Wrapper function for SD score used in `cluster_analysis` function.

    Parameters
    ----------
    word_embeddings : np.ndarray
        Word embeddings/pairwise distances to evaluate on
    cluster_labels : np.ndarray
        Predicted cluster labels
    clusterer : clustering instance
        Clustering instance (fitted on data)
    **kwargs : dict
        Keyword arguments passed to `SD`

    Returns
    -------
    result : tuple
        Result as a triple, consisting of metric title, metric score and whether or not
        the metrics objective function is to maximize the metric score.
    """
    # Compute metric scores
    if cluster_labels is None:
        cluster_labels = clusterer.labels_
    metric_score = SD(
        X=word_embeddings, labels=cluster_labels, metric="cosine", **kwargs
    )

    # Return tuple with result
    return "SD validity index", metric_score, False


def cdbw_score_metric(
    word_embeddings: np.ndarray, cluster_labels: np.ndarray, clusterer, **kwargs: dict
) -> tuple:
    """
    Wrapper function for CDbw score used in `cluster_analysis` function.

    Parameters
    ----------
    word_embeddings : np.ndarray
        Word embeddings/pairwise distances to evaluate on
    cluster_labels : np.ndarray
        Predicted cluster labels
    clusterer : clustering instance
        Clustering instance (fitted on data)
    **kwargs : dict
        Keyword arguments passed to `CDbw`

    Returns
    -------
    result : tuple
        Result as a triple, consisting of metric title, metric score and whether or not
        the metrics objective function is to maximize the metric score.
    """
    # Compute metric scores
    if cluster_labels is None:
        cluster_labels = clusterer.labels_
    metric_score = CDbw(
        X=word_embeddings, labels=cluster_labels, metric="cosine", s=3, **kwargs
    )

    # Return tuple with result
    return "CDbw validity index", metric_score, True


def relative_dbcv_score_metric(clusterer: HDBSCAN, **_: dict) -> tuple:
    """
    Wrapper function for (relative) DBCV score used in `cluster_analysis` function.

    Parameters
    ----------
    clusterer : HDBSCAN instance
        HDBSCAN instance (fitted on data)
    **_ : dict
        Keyword arguments sent into the void (not used)

    Returns
    -------
    result : tuple
        Result as a triple, consisting of metric title, metric score and whether or not
        the metrics objective function is to maximize the metric score.
    """
    # Get DBCV score directly from fitted HDBSCAN instance
    metric_score = clusterer.relative_validity_

    # Return tuple with result
    return "Density-Based Clustering Validation (relative)", metric_score, True
