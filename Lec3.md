![equation](http://www.sciweavers.org/tex2img.php?eq=1%2Bsin%28mc%5E2%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)

Insertion Sort(A)							Cost		Times
	for j = 2 to length(A)						C1		n
		do key = A[j]						C2		n-1
		// insert A[j] into sorted sequence A[i...j-1]
		i = j-1							C4		n-1
		while i>0 and A[i]>key					C5		\Sum_{j=1}^{n} t_j
			do A[i+1]=A[i]					C6		\Sum_{j=1}^{n} (t_j-1)
				i=1-1					C7		\Sum_{j=1}^{n} (t_j-1)
			A[i+1]=key					C8		n-1
Let t_j = the number of times the while loop is executed for a given value of j.

T(n)=c_1 n + c_2 (n-1) + c_4(n-1) + c_5 \Sum_{j=2}^{n} t_j + c_6 \Sum_{j=2}^{n} (t_j - 1) + c_7 \Sum_{j=1}^{n} (t_j-1) + c_8 (n-1)

Best case T(n)=c_1 n + c_2 (n-1) + c_4 (n-1) + c_5 (n-1) + c_8 (n-1) = (c_1+c_2+c_4+c_5+c_8)n-(c_2+c_4+c_5+c_8)
Can be written as a_n+b, i.e. a linear function of n.

Worst case t_j = j for j = 2, 3, ..., n
\Sum_{j=2}^{n} j = n(n+1)/2 - 1
\Sum_{j=2}^{n} (j-1) = n(n-1)/2

T(n)=c_1 n + c_2 (n-1) + c_4(n-1) + c_5 (n(n+1)/2 - 1) + c_6 (n(n-1)/2) + c_7 (n(n-1)/2) + c_8 (n-1) = (c_5/2+c_6/2+c_7/2)n^2 + (c_1+c_2+c_4+c_3/2-c_6/2-c_7/2+c_8)n-(c_2+c_4+c_1+c_8)=an^2+bn+c


j = 2
A = [3, 2, 1]
i = 2
key = 2
i = j - 1 = 1
A[1+1] = A[1]=3
A=[3 3 1]
i=i-1=0
A[i+1]=A[1]=key=2
A=[2 3 1]

j = 3
key = A[3] = 1
i = 3-1 =2
A[i+1]=A[2+1]=A[3]=A[2]=3
A = [2 3 3]
i = 2 - 1 = 1
A[i]=A[1]=2>key = 1
A[i+1] = A[2]= A[i]= A[1]= 2
A = [2 2 3]
i = i - 1 = 0
A[i+1]=A[1]=key=1
A = [1 2 3]

i = 4>lenght(A) stop

We say insertion sort has a worst-case running time of \Theta(n^2).