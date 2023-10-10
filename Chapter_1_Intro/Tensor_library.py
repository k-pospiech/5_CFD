import numpy as np

def tensor_add(A, B):
    """
    Add two tensors element-wise.
    
    Parameters:
        A (np.array): The first tensor.
        B (np.array): The second tensor.
    
    Returns:
        np.array: The resulting tensor after addition.
    """
    return np.add(A, B)


def tensor_subtract(A, B):
    """
    Subtract two tensors element-wise.
    
    Parameters:
        A (np.array): The first tensor.
        B (np.array): The second tensor.
    
    Returns:
        np.array: The resulting tensor after subtraction.
    """
    return np.subtract(A, B)


def scalar_multiply(scalar, A):
    """
    Multiply a tensor by a scalar.
    
    Parameters:
        scalar (float or int): The scalar to multiply.
        A (np.array): The tensor to be multiplied.
    
    Returns:
        np.array: The resulting tensor after multiplication.
    """
    return np.multiply(scalar, A)


def tensor_dot_product(A, B):
    """
    Compute the dot product of two tensors.
    
    Parameters:
        A (np.array): The first tensor.
        B (np.array): The second tensor.
    
    Returns:
        np.array: The dot product of tensors A and B.
    """
    return np.tensordot(A, B, axes=1)


def tensor_product(A, B):
    """
    Compute the tensor product of two tensors.
    
    Parameters:
        A (np.array): The first tensor.
        B (np.array): The second tensor.
    
    Returns:
        np.array: The tensor product of A and B.
    """
    return np.tensordot(A, B, axes=0)

def cross_product(A, B):
    """
    Compute the cross product of two 3D vectors.

    Parameters:
        A (np.array): The first vector.
        B (np.array): The second vector.

    Returns:
        np.array: The cross product of A and B.
    """
    return np.cross(A, B)

def divergence(vector_field):
    """
    Compute the divergence of a vector field.

    Parameters:
        vector_field (np.array): A 3D vector field.

    Returns:
        float: The divergence of the vector field.
    """
    return np.sum(np.gradient(vector_field), axis=0)

def curl(vector_field):
    """
    Compute the curl of a 3D vector field.

    Parameters:
        vector_field (np.array): A 3D vector field.

    Returns:
        np.array: The curl of the vector field.
    """
    return np.cross(np.gradient(vector_field), vector_field, axis=0)

def gradient(scalar_field):
    """
    Compute the gradient of a scalar field.

    Parameters:
        scalar_field (np.array): A scalar field.

    Returns:
        np.array: The gradient of the scalar field.
    """
    return np.gradient(scalar_field)

def tensor_inverse(A):
    """
    Compute the inverse of a square tensor.

    Parameters:
        A (np.array): A square tensor.

    Returns:
        np.array: The inverse of tensor A.
    """
    return np.linalg.inv(A)

def tensor_transpose(A):
    """
    Compute the transpose of a tensor.

    Parameters:
        A (np.array): A tensor.

    Returns:
        np.array: The transpose of tensor A.
    """
    return np.transpose(A)

def tensor_contraction(A, axis):
    """
    Contract a tensor along the specified axis.

    Parameters:
        A (np.array): A tensor.
        axis (int): The axis along which to contract the tensor.

    Returns:
        np.array: The contracted tensor.
    """
    return np.trace(A, axis1=axis, axis2=axis+1)

