# Python Documentation

## Python Version 3.7.5

### Lecture From Save In Your Brain

Numpy is A Python Library for dealing with numerical useful python package.

Use the package manger [numpy](https://pip.pypa.io/en/stabler/) to install numpy package.[Google](google.com)
Press Facebook
[Facebook](www.facebook.com)
[Python](https://www.python.org)

```bash
pip install numpy
```



## Usage

```python
import numpy
numpy.pluralized('image') # returns 'image'
numpy.pluralized('goose') # returns 'goose'
numpy.singularize('phenomena') # returns 'phenomena'
```
```java
public class Combination {

	
	public static void main(String[] args){
		Object[] elements = new Object[] {'A','B','C','D','E'};
		combination(elements,3);
	}
	
	
	public static void combination(Object[]  elements, int K){

		// get the length of the array
		// e.g. for {'A','B','C','D'} => N = 4 
		int N = elements.length;
		
		if(K > N){
			System.out.println("Invalid input, K > N");
			return;
		}
		
		// calculate the possible combinations
		c(N,K);
		
		// init combination index array
		int combination[] = new int[K];
		

		int r = 0; // index for combination array
		int i = 0; // index for elements array
		
		while(r >= 0){
		
			// forward step if i < (N + (r-K))
			if(i <= (N + (r - K))){
					combination[r] = i;
					
				// if combination array is full print and increment i;
				if(r == K-1){
					print(combination, elements);
					i++;				
				}
				else{
					// if combination is not full yet, select next element
					i = combination[r]+1;
					r++;										
				}
				
			}
			
			// backward step
			else{
				r--;
				if(r >= 0)
					i = combination[r]+1;
				
			}			
		}
	}
	

	
	private static int c(int n, int r){
		int nf=fact(n);
		int rf=fact(r);
		int nrf=fact(n-r);
		int npr=nf/nrf;
		int ncr=npr/rf; 
		
		System.out.println("C("+n+","+r+") = "+ ncr);

		return ncr;
	}
	
	private static int fact(int n)
	{
		if(n == 0)
			return 1;
		else
			return n * fact(n-1);
	}
	

	private static void print(int[] combination, Object[] elements){

		String output = "";
		for(int z = 0 ; z < combination.length;z++){
			output += elements[combination[z]];
		}
		System.out.println(output);
	}
}
```





![alt text](https://d17fnq9dkz9hgj.cloudfront.net/uploads/2012/11/153558006-tips-healthy-cat-632x475.jpg)
![alt text](http://static01.nyt.com/2014/01/28/science/28SlOT_SPAN/28SLOT-jumbo.jpg)
![alt ironman](https://www.gematsu.com/wp-content/uploads/2019/03/Iron-Man-VR_03-25-19.jpg)

<img src="https://www.gematsu.com/wp-content/uploads/2019/03/Iron-Man-VR_03-25-19.jpg" width="193" height="130">
<img src="" width="300" height="">



##Contributing

```
Pull Request are Welcome.For Major Changes,Please open an issuw first to discuss what you would like to change.
```

```
Make Software For Major Changes Please open the new world.
```

```python
from math import pi
```
-numpy

-matplotlib

-scipy

-tensor-core

Please make sure to update testds as appropriste

-![#FF0000]'RED'

```diff
-text in red
+text in green
!text in orange
#text in grey
```
```diff
-Red
+Green
!Orange
#Grey
```

``diff
-text
+word
!character
#string

[Okkr Min](https://www.facebook.com/okkrmin.info)

[MIT](http://cgooselicnse.com//licenses/mit)
