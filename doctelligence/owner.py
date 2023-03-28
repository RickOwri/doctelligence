import os
import typing

from doctelligence.ipfs import IPFSClient
from doctelligence.web3 import Web3Client


class Owner:
    """Client class for model owners in the Doctelligence protocol."""

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

    def submit_training_job(
        self,
        model: typing.Union[str, bytes, os.PathLike],
        eval_data: typing.Union[str, bytes, os.PathLike],
        trainer_fee: int,
        evaluator_fee: int,
    ) -> int:
        """
        Deploys a smart contract for a training job.
        Args:
            model: Filepath of the model to be trained.
            eval_data: Filepath of the evaluation dataset for the model.
            trainer_fee: Total number of wei to pay to trainers, in wei.
            evaluator_fee: Total number of wei to pay to evaluators.
        Returns:
            The address of the smart contract that was deployed.
        """
        model_ipfs_hash = self.ipfs_client.upload(model)
        eval_data_ipfs_hash = self.ipfs_client.upload(eval_data)
        address = self.web3_client.submit_training_job(
            model_ipfs_hash,
            eval_data_ipfs_hash,
            trainer_fee,
            evaluator_fee
        )
        return address

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
