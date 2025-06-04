import numpy as np

from fastapi import APIRouter

router = APIRouter()

@router.get("")

def hello_world() -> dict:
    return {"msg": "Hello, World!"}

@router.get("/matmul")

def matmul():
    a = np.random.rand(10, 10)
    b = np.random.rand(10, 10)
    
    product = np.dot(a, b)
    
    return {"matrix_a": a.tolist(), "matrix_b": b.tolist(), "product": product.tolist()}
