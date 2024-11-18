import pytest
import os
import sys

# Adiciona o caminho raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

# Configura o Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

# Importações do projeto
from blog.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'

