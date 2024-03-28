import pytest
from time import time as ttime
from bismuthcore.bismuthcore.transaction import Transaction
from bismuthcore.bismuthcore.block import Block

@pytest.fixture
def setup_block():
    # Setup for creating dummy transactions and a block
    transactions = [Transaction(
        i,
        ttime(),
        "f6c0363ca1c5aa28cc584252e65a63998493ff0a5ec1bb16beda9bac",
        "d11ea307ea6de821bc28c645b1ff8dd25c6e8a9f70b3a6aeb9928754",
        i,
    ) for i in range(5)]  # Add appropriate dummy transactions
    block = Block(transactions, compute=True)
    return block, transactions

@pytest.fixture
def setup_invalid_block():
    # Setup for creating dummy transactions and a block
    transactions = [Transaction(
        i,
        ttime(),
        "f6c0363ca1c5aa28cc584252e65a63998493ff0a5ec1bb16beda9bac",
        "d11ea307ea6de821bc28c645b1ff8dd25c6e8a9f70b3a6aeb9928754",
        i,
        operation="invalid_operation"
    ) for i in range(5)]  # Add appropriate dummy transactions
    block = Block(transactions, compute=True)
    return block, transactions

def test_initialization(setup_block):
    """Test block initialization."""
    block, transactions = setup_block
    assert len(block.transactions) == len(transactions)
    assert isinstance(block, Block)
    
def test_compute(setup_block):
    """Test the _compute method functionality."""
    block, _ = setup_block
    # block fixture does not use `operation` field
    assert not block.tokens_operation_present
        
def test_tx_list_for_hash(setup_block):
    """Test correct transaction list formation for block hash."""
    block, transactions = setup_block
    tx_list = block.tx_list_for_hash()
    assert len(tx_list) == len(transactions)
    # Additional checks to ensure the tuple format is correct
