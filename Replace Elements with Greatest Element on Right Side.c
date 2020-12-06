/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* replaceElements(int* arr, int arrSize, int* returnSize){

    int *x;
	int i, j, k, max_;

	x = (int *)malloc(sizeof(int) * arrSize);
	if (x) {
		j = 0;
		for (i = 0; i < arrSize - 1; i++) {
			if (i >= j) {
				j = k = i + 1;
				max_ = arr[k];
				for (++k; k < arrSize; k++) {
					if (arr[k] > max_) {
						max_ = arr[k];
						j = k;
					}
				}
			}
			x[i] = max_;
		}
		x[i] = -1;
		*returnSize = arrSize;
	} else {
		*returnSize = 0;
	}
	return x;

}
