import os
import typing

from doctelligence.ipfs import IPFSClient
from doctelligence.web3 import Web3Client


class Evaluator:
    """Client class for model evaluators in the Doctelligence protocol."""

    def __init__(
        self,
        ipfs_client: IPFSClient,
        web3_client: Web3Client,
    ) -> None:
        """
        Args:
            ipfs_client: A client to interact with IPFS. Use a mock one for unit tests.
            web3_client: A client to interact with the Doctelligence smart contract. Use a mock one for unit tests.
        """
        self.ipfs_client = ipfs_client
        self.web3_client = web3_client

    def download_updated_models(
        self,
        address: int,
        models_dir: typing.Union[str, bytes, os.PathLike]
    ) -> None:
        """
        Downloads the latest trained model from the given smart contract.
        Args:
            address: The smart contract address for the training job.
            model: The filepath to download the trained model to.
        """
        ipfs_hashes = self.web3_client.get_updated_model_hashes(address)
        for hash in ipfs_hashes:
            self.ipfs_client.download(hash, os.path.join(models_dir, hash))

    def submit_evaluations(
        self,
        address: int,
        evaluations: typing.Dict[str, float]
    ):
        """
        Submits model evaluations to the given smart contract.
        Args:
            address: The smart contract address for the training job.
            evaluations: A dict of each ipfs_hash => evaluated score, eg. loss.
        """
        self.web3_client.submit_evaluations(address, evaluations)
