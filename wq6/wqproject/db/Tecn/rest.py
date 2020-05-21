from wq.db import rest
from .models import Tecn


rest.router.register_model(
    Tecn,
    fields="__all__",
)
