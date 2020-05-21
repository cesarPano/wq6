from wq.db import rest
from .models import Tran


rest.router.register_model(
    Tran,
    fields="__all__",
)
