import os
import typing

class IPFSClient:
    def __init__(self) -> None:
        raise NotImplementedError

    def upload(
        self,
        filepath: typing.Union[str, bytes, os.PathLike]
    ) -> str:
        """
        Args:
            filepath: Path to the file to upload.
        Returns:
            The IPFS hash of the uploaded file.
        """
        raise NotImplementedError

    def download(
        self,
        ipfs_hash: str,
        filepath: typing.Union[str, bytes, os.PathLike]
    ) -> str:
        """
        Args:
            ipfs_hash: The IPFS hash to download.
            filepath: Path to download the file to.
        """
        raise NotImplementedError
