from wq.db import rest
from .models import Trevi


rest.router.register_model(
    Trevi,
    fields="__all__",
)
