# Using F2PY bindings in Python

All wrappers for Fortran/C routines, common blocks, or for Fortran
90 module data generated by F2PY are exposed to Python as ``fortran``
type objects.  Routine wrappers are callable ``fortran`` type objects
while wrappers to Fortran data have attributes referring to data
objects.

All ``fortran`` type object have attribute ``_cpointer`` that contains
CObject referring to the C pointer of the corresponding Fortran/C
function or variable in C level. Such CObjects can be used as a
callback argument of F2PY generated functions to bypass Python C/API
layer of calling Python functions from Fortran or C when the
computational part of such functions is implemented in C or Fortran
and wrapped with F2PY (or any other tool capable of providing CObject
of a function).

Consider a Fortran 77 file ``ftype.f``:

``` python
C FILE: FTYPE.F
      SUBROUTINE FOO(N)
      INTEGER N
Cf2py integer optional,intent(in) :: n = 13
      REAL A,X
      COMMON /DATA/ A,X(3)
      PRINT*, "IN FOO: N=",N," A=",A," X=[",X(1),X(2),X(3),"]"
      END
C END OF FTYPE.F
```

and build a wrapper using ``f2py -c ftype.f -m ftype``.

In Python:

``` python
>>> import ftype
>>> print ftype.__doc__
This module 'ftype' is auto-generated with f2py (version:2.28.198-1366).
Functions:
  foo(n=13)
COMMON blocks:
  /data/ a,x(3)
.
>>> type(ftype.foo),type(ftype.data)
(<type 'fortran'>, <type 'fortran'>)
>>> ftype.foo()
 IN FOO: N= 13 A=  0. X=[  0.  0.  0.]
>>> ftype.data.a = 3
>>> ftype.data.x = [1,2,3]
>>> ftype.foo()
 IN FOO: N= 13 A=  3. X=[  1.  2.  3.]
>>> ftype.data.x[1] = 45  
>>> ftype.foo(24)
 IN FOO: N= 24 A=  3. X=[  1.  45.  3.]
>>> ftype.data.x
array([  1.,  45.,   3.],'f')
```

## Scalar arguments

In general, a scalar argument of a F2PY generated wrapper function can
be ordinary Python scalar (integer, float, complex number) as well as
an arbitrary sequence object (list, tuple, array, string) of
scalars. In the latter case, the first element of the sequence object
is passed to Fortran routine as a scalar argument.

Note that when type-casting is required and there is possible loss of
information (e.g. when type-casting float to integer or complex to
float), F2PY does not raise any exception. In complex to real
type-casting only the real part of a complex number is used.

``intent(inout)`` scalar arguments are assumed to be array objects in
order to  *in situ*  changes to be effective. It is recommended to use
arrays with proper type but also other types work.

Consider the following Fortran 77 code:

``` python
C FILE: SCALAR.F
      SUBROUTINE FOO(A,B)
      REAL*8 A, B
Cf2py intent(in) a
Cf2py intent(inout) b
      PRINT*, "    A=",A," B=",B
      PRINT*, "INCREMENT A AND B"
      A = A + 1D0
      B = B + 1D0
      PRINT*, "NEW A=",A," B=",B
      END
C END OF FILE SCALAR.F
```

and wrap it using ``f2py -c -m scalar scalar.f``.

In Python:

``` python
>>> import scalar
>>> print scalar.foo.__doc__
foo - Function signature:
  foo(a,b)
Required arguments:
  a : input float
  b : in/output rank-0 array(float,'d')
 
>>> scalar.foo(2,3)   
     A=  2. B=  3.
 INCREMENT A AND B
 NEW A=  3. B=  4.
>>> import numpy
>>> a=numpy.array(2)   # these are integer rank-0 arrays
>>> b=numpy.array(3)
>>> scalar.foo(a,b)
     A=  2. B=  3.
 INCREMENT A AND B
 NEW A=  3. B=  4.
>>> print a,b            # note that only b is changed in situ
2 4
```

## String arguments

F2PY generated wrapper functions accept (almost) any Python object as
a string argument, ``str`` is applied for non-string objects.
Exceptions are NumPy arrays that must have type code ``'c'`` or
``'1'`` when used as string arguments.

A string can have arbitrary length when using it as a string argument
to F2PY generated wrapper function. If the length is greater than
expected, the string is truncated. If the length is smaller that
expected, additional memory is allocated and filled with ``\0``.

Because Python strings are immutable, an ``intent(inout)`` argument
expects an array version of a string in order to  *in situ*  changes to
be effective.

Consider the following Fortran 77 code:

``` python
C FILE: STRING.F
      SUBROUTINE FOO(A,B,C,D)
      CHARACTER*5 A, B
      CHARACTER*(*) C,D
Cf2py intent(in) a,c
Cf2py intent(inout) b,d
      PRINT*, "A=",A
      PRINT*, "B=",B
      PRINT*, "C=",C
      PRINT*, "D=",D
      PRINT*, "CHANGE A,B,C,D"
      A(1:1) = 'A'
      B(1:1) = 'B'
      C(1:1) = 'C'
      D(1:1) = 'D'
      PRINT*, "A=",A
      PRINT*, "B=",B
      PRINT*, "C=",C
      PRINT*, "D=",D
      END
C END OF FILE STRING.F
```

and wrap it using ``f2py -c -m mystring string.f``.

Python session:

``` python
>>> import mystring
>>> print mystring.foo.__doc__
foo - Function signature:
  foo(a,b,c,d)
Required arguments:
  a : input string(len=5)
  b : in/output rank-0 array(string(len=5),'c')
  c : input string(len=-1)
  d : in/output rank-0 array(string(len=-1),'c')

>>> import numpy
>>> a=numpy.array('123')
>>> b=numpy.array('123')
>>> c=numpy.array('123')
>>> d=numpy.array('123')
>>> mystring.foo(a,b,c,d)
 A=123
 B=123
 C=123
 D=123
 CHANGE A,B,C,D
 A=A23
 B=B23
 C=C23
 D=D23
>>> a.tostring(),b.tostring(),c.tostring(),d.tostring()
('123', 'B23', '123', 'D23')
```

## Array arguments

In general, array arguments of F2PY generated wrapper functions accept
arbitrary sequences that can be transformed to NumPy array objects.
An exception is ``intent(inout)`` array arguments that always must be
proper-contiguous and have proper type, otherwise an exception is
raised. Another exception is ``intent(inplace)`` array arguments that
attributes will be changed in-situ if the argument has different type
than expected (see ``intent(inplace)`` attribute for more
information).

In general, if a NumPy array is proper-contiguous and has a proper
type then it is directly passed to wrapped Fortran/C function.
Otherwise, an element-wise copy of an input array is made and the
copy, being proper-contiguous and with proper type, is used as an
array argument.

There are two types of proper-contiguous NumPy arrays:

- Fortran-contiguous arrays when data is stored column-wise,
i.e. indexing of data as stored in memory starts from the lowest
dimension;
- C-contiguous or simply contiguous arrays when data is stored
row-wise, i.e. indexing of data as stored in memory starts from the
highest dimension.

For one-dimensional arrays these notions coincide.

For example, a 2x2 array ``A`` is Fortran-contiguous if its elements
are stored in memory in the following order:

``` python
A[0,0] A[1,0] A[0,1] A[1,1]
```

and C-contiguous if the order is as follows:

``` python
A[0,0] A[0,1] A[1,0] A[1,1]
```

To test whether an array is C-contiguous, use ``.iscontiguous()``
method of NumPy arrays.  To test for Fortran contiguity, all
F2PY generated extension modules provide a function
``has_column_major_storage()``. This function is equivalent to
``.flags.f_contiguous`` but more efficient.

Usually there is no need to worry about how the arrays are stored in
memory and whether the wrapped functions, being either Fortran or C
functions, assume one or another storage order. F2PY automatically
ensures that wrapped functions get arguments with proper storage
order; the corresponding algorithm is designed to make copies of
arrays only when absolutely necessary. However, when dealing with very
large multidimensional input arrays with sizes close to the size of
the physical memory in your computer, then a care must be taken to use
always proper-contiguous and proper type arguments.

To transform input arrays to column major storage order before passing
them to Fortran routines, use a function
``as_column_major_storage()`` that is provided by all F2PY
generated extension modules.

Consider Fortran 77 code:

``` python
C FILE: ARRAY.F
      SUBROUTINE FOO(A,N,M)
C
C     INCREMENT THE FIRST ROW AND DECREMENT THE FIRST COLUMN OF A
C
      INTEGER N,M,I,J
      REAL*8 A(N,M)
Cf2py intent(in,out,copy) a
Cf2py integer intent(hide),depend(a) :: n=shape(a,0), m=shape(a,1)
      DO J=1,M
         A(1,J) = A(1,J) + 1D0
      ENDDO
      DO I=1,N
         A(I,1) = A(I,1) - 1D0
      ENDDO
      END
C END OF FILE ARRAY.F
```

and wrap it using ``f2py -c -m arr array.f -DF2PY_REPORT_ON_ARRAY_COPY=1``.

In Python:

``` python
>>> import arr
>>> from numpy import array
>>> print arr.foo.__doc__
foo - Function signature:
  a = foo(a,[overwrite_a])
Required arguments:
  a : input rank-2 array('d') with bounds (n,m)
Optional arguments:
  overwrite_a := 0 input int
Return objects:
  a : rank-2 array('d') with bounds (n,m)

>>> a=arr.foo([[1,2,3],
...            [4,5,6]])
copied an array using PyArray_CopyFromObject: size=6, elsize=8
>>> print a
[[ 1.  3.  4.]
 [ 3.  5.  6.]]
>>> a.iscontiguous(), arr.has_column_major_storage(a)
(0, 1)
>>> b=arr.foo(a)              # even if a is proper-contiguous
...                           # and has proper type, a copy is made
...                           # forced by intent(copy) attribute
...                           # to preserve its original contents
... 
copied an array using copy_ND_array: size=6, elsize=8
>>> print a
[[ 1.  3.  4.]
 [ 3.  5.  6.]]
>>> print b
[[ 1.  4.  5.]
 [ 2.  5.  6.]]
>>> b=arr.foo(a,overwrite_a=1) # a is passed directly to Fortran
...                            # routine and its contents is discarded
... 
>>> print a
[[ 1.  4.  5.]
 [ 2.  5.  6.]]
>>> print b
[[ 1.  4.  5.]
 [ 2.  5.  6.]]
>>> a is b                       # a and b are actually the same objects
1
>>> print arr.foo([1,2,3])       # different rank arrays are allowed
copied an array using PyArray_CopyFromObject: size=3, elsize=8
[ 1.  1.  2.]
>>> print arr.foo([[[1],[2],[3]]])
copied an array using PyArray_CopyFromObject: size=3, elsize=8
[ [[ 1.]
  [ 3.]
  [ 4.]]]
>>>
>>> # Creating arrays with column major data storage order:
...
>>> s = arr.as_column_major_storage(array([[1,2,3],[4,5,6]]))
copied an array using copy_ND_array: size=6, elsize=4
>>> arr.has_column_major_storage(s)
1
>>> print s
[[1 2 3]
 [4 5 6]]
>>> s2 = arr.as_column_major_storage(s)
>>> s2 is s    # an array with column major storage order 
               # is returned immediately
1
```

## Call-back arguments

F2PY supports calling Python functions from Fortran or C codes.

Consider the following Fortran 77 code:

``` python
C FILE: CALLBACK.F
      SUBROUTINE FOO(FUN,R)
      EXTERNAL FUN
      INTEGER I
      REAL*8 R
Cf2py intent(out) r
      R = 0D0
      DO I=-5,5
         R = R + FUN(I)
      ENDDO
      END
C END OF FILE CALLBACK.F
```

and wrap it using ``f2py -c -m callback callback.f``.

In Python:

``` python
>>> import callback
>>> print callback.foo.__doc__
foo - Function signature:
  r = foo(fun,[fun_extra_args])
Required arguments:
  fun : call-back function
Optional arguments:
  fun_extra_args := () input tuple
Return objects:
  r : float
Call-back functions:
  def fun(i): return r
  Required arguments:
    i : input int
  Return objects:
    r : float

>>> def f(i): return i*i
... 
>>> print callback.foo(f)     
110.0
>>> print callback.foo(lambda i:1)
11.0
```

In the above example F2PY was able to guess accurately the signature
of a call-back function. However, sometimes F2PY cannot establish the
signature as one would wish and then the signature of a call-back
function must be modified in the signature file manually. Namely,
signature files may contain special modules (the names of such modules
contain a substring ``__user__``) that collect various signatures of
call-back functions.  Callback arguments in routine signatures have
attribute ``external`` (see also ``intent(callback)`` attribute).  To
relate a callback argument and its signature in ``__user__`` module
block, use ``use`` statement as illustrated below. The same signature
of a callback argument can be referred in different routine
signatures.

We use the same Fortran 77 code as in previous example but now
we???ll pretend that F2PY was not able to guess the signatures of
call-back arguments correctly. First, we create an initial signature
file ``callback2.pyf`` using F2PY:

``` python
f2py -m callback2 -h callback2.pyf callback.f
```

Then modify it as follows

``` python
!    -*- f90 -*-
python module __user__routines 
    interface
        function fun(i) result (r)
            integer :: i
            real*8 :: r
        end function fun
    end interface
end python module __user__routines

python module callback2
    interface
        subroutine foo(f,r)
            use __user__routines, f=>fun
            external f
            real*8 intent(out) :: r
        end subroutine foo
    end interface 
end python module callback2
```

Finally, build the extension module using ``f2py -c callback2.pyf callback.f``.

An example Python session would be identical to the previous example
except that argument names would differ.

Sometimes a Fortran package may require that users provide routines
that the package will use. F2PY can construct an interface to such
routines so that Python functions could be called from Fortran.

Consider the following Fortran 77 subroutine that takes an array
and applies a function ``func`` to its elements.

``` python
subroutine calculate(x,n)
cf2py intent(callback) func
      external func
c     The following lines define the signature of func for F2PY:
cf2py real*8 y
cf2py y = func(y)
c
cf2py intent(in,out,copy) x
      integer n,i
      real*8 x(n)
      do i=1,n
         x(i) = func(x(i))
      end do
      end
```

It is expected that function ``func`` has been defined
externally. In order to use a Python function as ``func``, it must
have an attribute ``intent(callback)`` (it must be specified before
the ``external`` statement).

Finally, build an extension module using ``f2py -c -m foo calculate.f``

In Python:

``` python
>>> import foo
>>> foo.calculate(range(5), lambda x: x*x)
array([  0.,   1.,   4.,   9.,  16.])
>>> import math
>>> foo.calculate(range(5), math.exp)
array([  1.        ,   2.71828175,   7.38905621,  20.08553696,  54.59814835])
```

The function is included as an argument to the python function call to
the Fortran subroutine even though it was  *not*  in the Fortran subroutine argument
list. The ???external??? refers to the C function generated by f2py, not the python
function itself. The python function must be supplied to the C function.

The callback function may also be explicitly set in the module.
Then it is not necessary to pass the function in the argument list to
the Fortran function. This may be desired if the Fortran function calling
the python callback function is itself called by another Fortran function.

Consider the following Fortran 77 subroutine:

``` python
subroutine f1()
         print *, "in f1, calling f2 twice.."
         call f2()
         call f2()
         return
      end
      
      subroutine f2()
cf2py    intent(callback, hide) fpy
         external fpy
         print *, "in f2, calling f2py.."
         call fpy()
         return
      end
```

and wrap it using ``f2py -c -m pfromf extcallback.f``.

In Python:

``` python
>>> import pfromf
>>> pfromf.f2()
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
pfromf.error: Callback fpy not defined (as an argument or module pfromf attribute).

>>> def f(): print "python f"
... 
>>> pfromf.fpy = f
>>> pfromf.f2()
 in f2, calling f2py..
python f
>>> pfromf.f1()
 in f1, calling f2 twice..
 in f2, calling f2py..
python f
 in f2, calling f2py..
python f
>>>
```

### Resolving arguments to call-back functions

F2PY generated interface is very flexible with respect to call-back
arguments.  For each call-back argument an additional optional
argument ``_extra_args`` is introduced by F2PY. This argument
can be used to pass extra arguments to user provided call-back
arguments.

If a F2PY generated wrapper function expects the following call-back
argument:

``` python
def fun(a_1,...,a_n):
   ...
   return x_1,...,x_k
```

but the following Python function

``` python
def gun(b_1,...,b_m):
   ...
   return y_1,...,y_l
```

is provided by a user, and in addition,

``` python
fun_extra_args = (e_1,...,e_p)
```

is used, then the following rules are applied when a Fortran or C
function calls the call-back argument ``gun``:

- If ``p == 0`` then ``gun(a_1, ..., a_q)`` is called, here
``q = min(m, n)``.
- If ``n + p <= m`` then ``gun(a_1, ..., a_n, e_1, ..., e_p)`` is called.
- If ``p <= m < n + p`` then ``gun(a_1, ..., a_q, e_1, ..., e_p)`` is called, here
``q=m-p``.
- If ``p > m`` then ``gun(e_1, ..., e_m)`` is called.
- If ``n + p`` is less than the number of required arguments to ``gun``
then an exception is raised.

The function ``gun`` may return any number of objects as a tuple. Then
following rules are applied:

- If ``k < l``, then ``y_{k + 1}, ..., y_l`` are ignored.
- If ``k > l``, then only ``x_1, ..., x_l`` are set.

## Common blocks

F2PY generates wrappers to ``common`` blocks defined in a routine
signature block. Common blocks are visible by all Fortran codes linked
with the current extension module, but not to other extension modules
(this restriction is due to how Python imports shared libraries).  In
Python, the F2PY wrappers to ``common`` blocks are ``fortran`` type
objects that have (dynamic) attributes related to data members of
common blocks. When accessed, these attributes return as NumPy array
objects (multidimensional arrays are Fortran-contiguous) that
directly link to data members in common blocks. Data members can be
changed by direct assignment or by in-place changes to the
corresponding array objects.

Consider the following Fortran 77 code:

``` python
C FILE: COMMON.F
      SUBROUTINE FOO
      INTEGER I,X
      REAL A
      COMMON /DATA/ I,X(4),A(2,3)
      PRINT*, "I=",I
      PRINT*, "X=[",X,"]"
      PRINT*, "A=["
      PRINT*, "[",A(1,1),",",A(1,2),",",A(1,3),"]"
      PRINT*, "[",A(2,1),",",A(2,2),",",A(2,3),"]"
      PRINT*, "]"
      END
C END OF COMMON.F
```

and wrap it using ``f2py -c -m common common.f``.

In Python:

``` python
>>> import common
>>> print common.data.__doc__
i - 'i'-scalar
x - 'i'-array(4)
a - 'f'-array(2,3)

>>> common.data.i = 5
>>> common.data.x[1] = 2 
>>> common.data.a = [[1,2,3],[4,5,6]]
>>> common.foo()
 I= 5
 X=[ 0 2 0 0]
 A=[
 [  1.,  2.,  3.]
 [  4.,  5.,  6.]
 ]
>>> common.data.a[1] = 45
>>> common.foo()
 I= 5
 X=[ 0 2 0 0]
 A=[
 [  1.,  2.,  3.]
 [  45.,  45.,  45.]
 ]
>>> common.data.a                 # a is Fortran-contiguous
array([[  1.,   2.,   3.],
       [ 45.,  45.,  45.]],'f')
```

## Fortran 90 module data

The F2PY interface to Fortran 90 module data is similar to Fortran 77
common blocks.

Consider the following Fortran 90 code:

``` python
module mod
  integer i
  integer :: x(4)
  real, dimension(2,3) :: a
  real, allocatable, dimension(:,:) :: b 
contains
  subroutine foo
    integer k
    print*, "i=",i
    print*, "x=[",x,"]"
    print*, "a=["
    print*, "[",a(1,1),",",a(1,2),",",a(1,3),"]"
    print*, "[",a(2,1),",",a(2,2),",",a(2,3),"]"
    print*, "]"
    print*, "Setting a(1,2)=a(1,2)+3"
    a(1,2) = a(1,2)+3
  end subroutine foo
end module mod
```

and wrap it using ``f2py -c -m moddata moddata.f90``.

In Python:

``` python
>>> import moddata
>>> print moddata.mod.__doc__
i - 'i'-scalar
x - 'i'-array(4)
a - 'f'-array(2,3)
foo - Function signature:
  foo()


>>> moddata.mod.i = 5  
>>> moddata.mod.x[:2] = [1,2]
>>> moddata.mod.a = [[1,2,3],[4,5,6]]
>>> moddata.mod.foo()                
 i=           5
 x=[           1           2           0           0 ]
 a=[
 [   1.000000     ,   2.000000     ,   3.000000     ]
 [   4.000000     ,   5.000000     ,   6.000000     ]
 ]
 Setting a(1,2)=a(1,2)+3
>>> moddata.mod.a               # a is Fortran-contiguous
array([[ 1.,  5.,  3.],
       [ 4.,  5.,  6.]],'f')
```

### Allocatable arrays

F2PY has basic support for Fortran 90 module allocatable arrays.

Consider the following Fortran 90 code:

``` python
module mod
  real, allocatable, dimension(:,:) :: b 
contains
  subroutine foo
    integer k
    if (allocated(b)) then
       print*, "b=["
       do k = 1,size(b,1)
          print*, b(k,1:size(b,2))
       enddo
       print*, "]"
    else
       print*, "b is not allocated"
    endif
  end subroutine foo
end module mod
```

and wrap it using ``f2py -c -m allocarr allocarr.f90``.

In Python:

``` python
>>> import allocarr 
>>> print allocarr.mod.__doc__
b - 'f'-array(-1,-1), not allocated
foo - Function signature:
  foo()

>>> allocarr.mod.foo()  
 b is not allocated
>>> allocarr.mod.b = [[1,2,3],[4,5,6]]         # allocate/initialize b
>>> allocarr.mod.foo()
 b=[
   1.000000       2.000000       3.000000    
   4.000000       5.000000       6.000000    
 ]
>>> allocarr.mod.b                             # b is Fortran-contiguous
array([[ 1.,  2.,  3.],
       [ 4.,  5.,  6.]],'f')
>>> allocarr.mod.b = [[1,2,3],[4,5,6],[7,8,9]] # reallocate/initialize b
>>> allocarr.mod.foo()
 b=[
   1.000000       2.000000       3.000000    
   4.000000       5.000000       6.000000    
   7.000000       8.000000       9.000000    
 ]
>>> allocarr.mod.b = None                      # deallocate array
>>> allocarr.mod.foo()
 b is not allocated
```
