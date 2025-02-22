"""Higher Order Geometric Laplacian EigenMaps (HOGLEE) class."""
from typing import Literal, Union

import networkx as nx
import numpy as np
from karateclub import GLEE
from toponetx.classes import Complex

from topoembedx.neighborhood import neighborhood_from_complex


class HOGLEE(GLEE):
    """Class for Higher Order Geometric Laplacian EigenMaps (HOGLEE).

    Parameters
    ----------
    dimensions : int, optional
        Dimensionality of embedding. Defaults to 3.
    seed : int, optional
        Random seed value. Defaults to 42.
    """

    A: np.ndarray
    ind: list

    def fit(
        self,
        complex: Complex,
        neighborhood_type: Literal["adj", "coadj"] = "adj",
        neighborhood_dim={"rank": 0, "via_rank": -1},
    ) -> None:
        """Fit a Higher Order Geometric Laplacian EigenMaps model.

        Parameters
        ----------
        complex : toponetx.classes.Complex
            A complex object. The complex object can be one of the following:
            - CellComplex
            - CombinatorialComplex
            - PathComplex
            - SimplicialComplex
            - ColoredHyperGraph
        neighborhood_type : {"adj", "coadj"}, default="adj"
            The type of neighborhood to compute. "adj" for adjacency matrix, "coadj" for coadjacency matrix.
        neighborhood_dim : dict
            The integer parmaters needed to specify the neighborhood of the cells to generate the embedding.
            In TopoNetX  (co)adjacency neighborhood matrices are specified via one or two parameters.
            - For Cell/Simplicial/Path complexes (co)adjacency matrix is specified by a single parameter, this is precisely
            neighborhood_dim["rank"].
            - For Combinatorial/ColoredHyperGraph the (co)adjacency matrix is specified by a single parameter, this is precisely
            neighborhood_dim["rank"] and neighborhood_dim["via_rank"].

        Notes
        -----
        Here neighborhood_dim={"rank": 1, "via_rank": -1} specifies the dimension for
        which the cell embeddings are going to be computed.
        "rank": 1 means that the embeddings will be computed for the first dimension.
        The integer "via_rank": -1 is ignored when the input is cell/simplicial complex
        and  must be specified when the input complex is a combinatorial complex or
        colored hypergraph.
        """
        self.ind, self.A = neighborhood_from_complex(
            complex, neighborhood_type, neighborhood_dim
        )

        g = nx.from_numpy_matrix(self.A)

        super(HOGLEE, self).fit(g)

    def get_embedding(self, get_dict: bool = False) -> Union[dict, np.ndarray]:
        """Get embedding.

        Parameters
        ----------
        get_dict : bool, optional
            Whether to return a dictionary. Defaults to False.

        Returns
        -------
        dict or numpy.ndarray
            Embedding.
        """
        emb = super(HOGLEE, self).get_embedding()
        if get_dict:
            return dict(zip(self.ind, emb))
        return emb
