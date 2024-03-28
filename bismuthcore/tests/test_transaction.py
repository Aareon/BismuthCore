import pytest
from bismuthcore.transaction import Transaction

def test_initialization():
    """Test the initialization of a Transaction."""
    tx = Transaction(amount=12345678)
    assert tx.amount == 12345678, "Amount should be initialized correctly"

def test_sanitize():
    """Test input sanitization."""
    tx = Transaction(address='A' * 100, operation='B' * 100, openfield='C' * 200000, sanitize=True)
    assert len(tx.address) <= 56, "Address should be truncated"
    assert len(tx.operation) <= 30, "Operation should be truncated"
    assert len(tx.openfield) <= 100000, "Openfield should be truncated"

@pytest.mark.parametrize("amount_str, expected", [
    ("1.23456789", 123456789),
    ("0.00000001", 1),
    ("-1.23456789", -123456789),
])
def test_f8_to_int(amount_str, expected):
    """Test conversion from float string to int."""
    assert Transaction.f8_to_int(amount_str) == expected, "Conversion from float string to int did not work as expected"

@pytest.mark.parametrize("amount_int, expected", [
    (123456789, "1.23456789"),
    (1, "0.00000001"),
    (-123456789, "-1.23456789"),
])
def test_int_to_f8(amount_int, expected):
    """Test conversion from int to float string."""
    assert Transaction.int_to_f8(amount_int) == expected, "Conversion from int to float string did not work as expected"

def test_from_legacy_params():
    """Test the from_legacy_params class method."""
    tx = Transaction.from_legacy_params(amount='0.00000001')
    assert tx.amount == 1, "from_legacy_params did not convert amount correctly"

def test_to_dict():
    """Test the to_dict method."""
    tx = Transaction(amount=1)
    tx_dict = tx.to_dict(legacy=True)
    assert tx_dict['amount'] == "0.00000001", "to_dict did not export amount correctly"

def test_to_json():
    """Test the to_json method."""
    tx = Transaction(amount=1)
    tx_json = tx.to_json()
    assert '"amount": "0.00000001"' in tx_json, "to_json did not export amount correctly"

def test_to_tuple():
    """Test the to_tuple method."""
    tx = Transaction(amount=1)
    tx_tuple = tx.to_tuple()
    assert tx_tuple[4] == "0.00000001", "to_tuple did not export amount correctly"

def test_from_legacy():
    """Test the from_legacy class method."""
    legacy_tx_list = [0, 1234567890.0, 'sender_address', 'recipient_address', '0.00000001', 'signature_str',
                      'public_key_str', '7cfa75dc3d8e7c4243267124320b7c3f14d941b4f124361a1ef4995f0d1e67a8', '0.00000002', '0.00000003', 'operation_str', 'openfield_str']
    tx = Transaction.from_legacy(legacy_tx_list)
    assert tx.amount == 1, "Amount should be correctly converted from legacy format"
    assert tx.fee == 2, "Fee should be correctly converted from legacy format"
    assert tx.reward == 3, "Reward should be correctly converted from legacy format"