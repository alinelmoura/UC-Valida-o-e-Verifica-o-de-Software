import pytest
from unittest.mock import patch
from process_payment import process_payment, InvalidPaymentDetails, PaymentGatewayError

def test_invalid_user_id():
    with pytest.raises(InvalidPaymentDetails):
        process_payment("", 100)

def test_invalid_amount():
    with pytest.raises(InvalidPaymentDetails):
        process_payment("user1", -50)

def test_unsupported_currency():
    with pytest.raises(InvalidPaymentDetails):
        process_payment("user1", 100, currency="GBP")

@patch("random.random", return_value=0.5)
@patch("random.randint", return_value=123456)
def test_successful_payment(mock_randint, mock_random):
    result = process_payment("user1", 100, currency="EUR")
    assert result["status"] == "success"
    assert result["transaction_id"] == "TXN-123456"
    assert result["amount_charged"] == 90.0
    assert result["currency"] == "EUR"

#apenas falha
@patch("random.random", side_effect=[0.2, 0.2, 0.2]) 
@patch("time.sleep") 
def test_payment_gateway_error(mock_sleep, mock_random):
    with pytest.raises(PaymentGatewayError):
        process_payment("user1", 100, retries=3)
    assert mock_sleep.call_count == 2 

#erro, erro, acerta
@patch("random.random", side_effect=[0.2, 0.2, 0.5]) 
@patch("random.randint", return_value=654321)
@patch("time.sleep")
def test_payment_success_after_retries(mock_sleep, mock_randint, mock_random):
    result = process_payment("user1", 100, retries=3)
    assert result["status"]=="success"
    assert result["transaction_id"]=="TXN-654321"
    assert result["amount_charged"]==100.0
    assert result["currency"]=="USD"
    assert mock_sleep.call_count==2 
