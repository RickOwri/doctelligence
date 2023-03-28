import os
import typing

from doctelligence.ipfs import IPFSClient
from doctelligence.web3 import Web3Client

class Trainer:
    """Client class for model trainers in the Doctelligence protocol."""

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

    def download_latest_model(
        self,
        address: int,
        model: typing.Union[str, bytes, os.PathLike]
    ) -> None:
        """
        Downloads the latest trained model from the given smart contract.
        Args:
            address: The smart contract address for the training job.
            model: The filepath to download the trained model to.
        """
        ipfs_hash = self.web3_client.get_latest_model_hash(address)
        self.ipfs_client.download(ipfs_hash, model)

    def upload_updated_model(
        self,
        address: int,
        model: typing.Union[str, bytes, os.PathLike]
    ) -> None:
        """
        Uploads an updated model and records it in the given smart contract.
        Args:
            address: The smart contract address for the training job.
            model: The filepath of the updated model.
        """
        ipfs_hash = self.ipfs_client.upload(model)
        self.web3_client.submit_model_update(address, ipfs_hash)
