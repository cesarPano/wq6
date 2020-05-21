from wq.db import rest
from .models import Tdesf


rest.router.register_model(
    Tdesf,
    fields="__all__",
)
