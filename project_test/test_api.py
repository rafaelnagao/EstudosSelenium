# arquivo: test_fake_store_api.py
import pytest
import requests

pytestmark = pytest.mark.api

# URL base da Fake Store API
BASE_URL = "https://fakestoreapi.com"


def test_listar_todos_os_produtos():
    """
    Este teste valida se a API consegue retornar a lista completa de produtos.
    É um teste básico de leitura (GET).
    """
    response = requests.get(f"{BASE_URL}/products")

    # Verifica se a resposta foi bem-sucedida
    assert response.status_code == 200

    # Converte o corpo da resposta para JSON
    body = response.json()

    # Valida que veio uma lista com pelo menos 1 produto
    assert isinstance(body, list)
    assert len(body) > 0

    # Valida alguns campos esperados no primeiro item
    primeiro_produto = body[0]
    assert "id" in primeiro_produto
    assert "title" in primeiro_produto
    assert "price" in primeiro_produto
    assert "category" in primeiro_produto


def test_buscar_um_produto_especifico():
    """
    Este teste valida a busca de um produto por ID.
    """
    product_id = 1

    response = requests.get(f"{BASE_URL}/products/{product_id}")

    assert response.status_code == 200

    body = response.json()

    # Confirma que o produto retornado é o produto correto
    assert body["id"] == product_id
    assert "title" in body
    assert "description" in body
    assert "price" in body
    assert "image" in body


def test_fazer_login_e_receber_token():
    """
    Este teste faz login usando as credenciais aceitas pela Fake Store API.
    O retorno esperado é um token JWT.
    """
    payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }

    response = requests.post(
        f"{BASE_URL}/auth/login",
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code in [200, 201]
    # Valida que o corpo da resposta contém um token
    body = response.json()
    assert "token" in body
    assert body["token"] != ""


def test_listar_carrinhos_de_um_usuario():
    """
    Este teste busca os carrinhos de um usuário específico.
    """
    user_id = 1

    response = requests.get(f"{BASE_URL}/carts/user/{user_id}")

    assert response.status_code in [200, 201]

    body = response.json()

    # A API deve devolver uma lista
    assert isinstance(body, list)

    # Se houver carrinhos, validamos a estrutura do primeiro
    if len(body) > 0:
        primeiro_carrinho = body[0]
        assert "id" in primeiro_carrinho
        assert "userId" in primeiro_carrinho
        assert "date" in primeiro_carrinho
        assert "products" in primeiro_carrinho


def test_criar_um_carrinho():
    """
    Este teste cria um novo carrinho com dois produtos.
    Em APIs REST, criação normalmente retorna 201 Created.
    """
    payload = {
        "userId": 1,
        "date": "2026-05-14",
        "products": [
            {
                "productId": 1,
                "quantity": 2
            },
            {
                "productId": 2,
                "quantity": 1
            }
        ]
    }

    response = requests.post(
        f"{BASE_URL}/carts",
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code == 201

    body = response.json()

    # Valida os dados principais do carrinho criado
    assert "id" in body
    assert body["userId"] == 1
    assert len(body["products"]) == 2


def test_fluxo_completo_de_compra_em_nivel_de_api():
    """
    Este teste simula um fluxo completo de compra no nível de API:
    1. Faz login
    2. Busca um produto
    3. Monta um carrinho
    4. Cria o carrinho
    Observação:
    A Fake Store API não tem um endpoint final real de 'checkout/finish order',
    então o ponto mais próximo do fechamento da compra é a criação do carrinho.
    """

    # -------------------------
    # ETAPA 1 - LOGIN
    # -------------------------
    login_payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }

    login_response = requests.post(
        f"{BASE_URL}/auth/login",
        json=login_payload,
        headers={"Content-Type": "application/json"}
    )

    assert login_response.status_code in [200, 201]

    login_body = login_response.json()
    assert "token" in login_body
    assert login_body["token"] != ""

    # -------------------------
    # ETAPA 2 - BUSCAR PRODUTO
    # -------------------------
    product_response = requests.get(f"{BASE_URL}/products/1")

    assert product_response.status_code == 200

    product_body = product_response.json()
    assert product_body["id"] == 1
    assert "title" in product_body
    assert "price" in product_body

    # -------------------------
    # ETAPA 3 - MONTAR CARRINHO
    # -------------------------
    cart_payload = {
        "userId": 1,
        "date": "2026-05-14",
        "products": [
            {
                "productId": product_body["id"],
                "quantity": 1
            }
        ]
    }

    # -------------------------
    # ETAPA 4 - CRIAR CARRINHO
    # -------------------------
    cart_response = requests.post(
        f"{BASE_URL}/carts",
        json=cart_payload,
        headers={"Content-Type": "application/json"}
    )

    assert cart_response.status_code == 201

    cart_body = cart_response.json()

    # Valida que o carrinho foi criado corretamente
    assert "id" in cart_body
    assert cart_body["userId"] == 1
    assert len(cart_body["products"]) == 1
    assert cart_body["products"][0]["productId"] == 1
    assert cart_body["products"][0]["quantity"] == 1