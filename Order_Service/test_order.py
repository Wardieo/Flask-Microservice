import pytest
from unittest.mock import patch
from oService import app, db, Order

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  
    with app.app_context():
        db.create_all()  
    client = app.test_client()
    yield client
    with app.app_context():
        db.drop_all()  

def test_create_order(client):
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200  

        response = client.post('/order', json={"user_id": 1, "product": "Laptop"})
        assert response.status_code == 201
        assert response.json['message'] == 'Order created'

def test_get_order(client):
    with app.app_context():
        order = Order(user_id=1, product="Laptop")
        db.session.add(order)
        db.session.commit()
        db.session.refresh(order)  
        response = client.get(f'/orders/{order.id}')
        assert response.status_code == 200
        assert response.json['product'] == 'Laptop'

def test_update_order(client):
    with app.app_context():
        order = Order(user_id=1, product="Laptop")
        db.session.add(order)
        db.session.commit()
        db.session.refresh(order) 
        response = client.put(f'/orders/{order.id}', json={"product": "Tablet"})
        assert response.status_code == 200
        assert response.json['message'] == 'Order updated'
        assert response.json['order']['product'] == 'Tablet'

def test_delete_order(client):
    with app.app_context():
        order = Order(user_id=1, product="Laptop")
        db.session.add(order)
        db.session.commit()
        db.session.refresh(order)

        response = client.delete(f'/orders/{order.id}')
        assert response.status_code == 200
        assert response.json['message'] == 'Order deleted'
