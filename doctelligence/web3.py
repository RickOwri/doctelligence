import os
import typing

class Web3Client:
    """
    A wrapper class for interacting with the Doctelligence smart contract.
    Each public method in this class should correspond to a function in the smart contract,
    with the contract address and the function's arguments as its parameters.
    submit_training_job() is an exception as it deploys a smart contract and returns the address instead.
    """
    def __init__(self) -> None:
        raise NotImplementedError
    
    def submit_training_job(
            model_ipfs_hash: str,
            eval_data_ipfs_hash: str,
            trainer_fee: int,
            evaluator_fee: int,
        ) -> int:
        """
        Deploys a new smart contract for a new training job.
        Args:
            model_ipfs_hash: The IPFS hash of the model to be trained.
            eval_data_ipfs_hash: The IPFS hash of the evaluation data for the model.
            trainer_fee: Total number of wei to pay to trainers, in wei.
            evaluator_fee: Total number of wei to pay to evaluators.
        Returns:
            The address of the smart contract that was deployed.
        """
        raise NotImplementedError

    def get_latest_model_hash(address: int) -> str:
        raise NotImplementedError

    def submit_model_update(address: int) -> None:
        raise NotImplementedError
    
    def submit_evaluations(
            address: int,
            evaluations: typing.Dict[str, float]
        ) -> None:
        raise NotImplementedError