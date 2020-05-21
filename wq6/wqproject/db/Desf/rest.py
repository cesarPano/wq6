from wq.db import rest
from .models import Desf


rest.router.register_model(
    Desf,
    fields="__all__",
)
