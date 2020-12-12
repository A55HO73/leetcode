int sumOddLengthSubarrays(int* arr, int arrSize){

    int i,j,count =0;

    for( i =0 ; i < arrSize; i++)
    {
        for ( j = i+ 1; j < arrSize+ 1; j++ )
            if((i+j) % 2 != 0 )
            {
                int k, sum =0;
                for(k = i; k < j; k++)
                {
                    sum = sum + arr[k];
                }
                count = count + sum;

            }

    }
    return count;
}
