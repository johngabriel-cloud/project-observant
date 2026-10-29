import pytest
from pydantic import ValidationError
from app.schemas.schemas import ServiceCreate


service_data = {
    "name": "My Websites",
    "url": "https://example.com/",
    "check_type": "http",
    "interval": 30
}
def test_service_create():
    service = ServiceCreate(**service_data)
    assert service.name == "My Websites"
    assert str(service.url) == "https://example.com/"
    assert service.check_type == "http"
    assert service.interval == 30

def test_service_create_name_less_min():
    with pytest.raises(ValidationError):
        ServiceCreate(name="Website", url="http://example.com/", check_type="http", interval=30)

def test_service_create_name_more_max():
    with pytest.raises(ValidationError):
        ServiceCreate(name="WebsitesWebsitesWebsitesWebsitesa", url="http://example.com/", check_type="http", interval=30)

def test_service_create_name_empty():
    with pytest.raises(ValidationError):
        ServiceCreate(name="", url="http://example.com/", check_type="http", interval=30)

def test_service_create_name_whitespace_leading():
    with pytest.raises(ValidationError, match="Name must not contain leading or trailing whitespace"):
        ServiceCreate(name=" websites", url="http://example.com/", check_type="http", interval=30)

def test_service_create_name_whitespace_trailing():
    with pytest.raises(ValidationError, match="Name must not contain leading or trailing whitespace"):
        ServiceCreate(name="websites ", url="http://example.com/", check_type="http", interval=30)

def test_service_create_name_whitespace_only():
    with pytest.raises(ValidationError, match="Name must not be empty or whitespace only"):
        ServiceCreate(name="        ", url="http://example.com/", check_type="http", interval=30)

def test_service_create_invalid_url():
    with pytest.raises(ValidationError):
        ServiceCreate( name="Websites", url="invalid-url", check_type="http", interval=30)

def test_service_create_invalid_check_type():
    with pytest.raises(ValidationError):
        ServiceCreate(name="Websites", url="http://example.com/", check_type="dns", interval=30)

def test_service_create_invalid_interval():
    with pytest.raises(ValidationError):
        ServiceCreate(name="Websites", url="http://example.com/", check_type="http", interval=15)
