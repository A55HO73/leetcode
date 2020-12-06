bool isMonotonic(int* A, int ASize){

  bool increasing = true;
	bool decreasing = true;
	int i;
	for( i = 0 ; i < ASize -1 ; i++)
	{
		increasing = ( increasing && ( A[i] >= A[i+1] ));
		decreasing = ( decreasing && ( A[i] <= A[i+1] ));
	}
	return (increasing || decreasing);
}
