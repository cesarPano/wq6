from wq.db import rest
from .models import Revi


rest.router.register_model(
    Revi,
    fields="__all__",
)
