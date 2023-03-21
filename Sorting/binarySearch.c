/**
 * @file binarySearch.c
 * @author Minh Le  
 * @brief 
 *      Implement Binary Search in C
 * @version 0.1
 * @date 2023-02-25
 * 
 * @copyright Copyright (c) 2023
 * 
 */

#include <stdio.h>
#include <stdlib.h>

/* Require Array to be a SORTED one to work */
int binarySearch(int target, int *arr, int start, int end){
    if (start > end)
        return -1;
    if (arr[start] == target)
        return start;
    if(arr[end] == target)
        return end;
        
    /* Actual Algorithm */
    int mid = (start+end)/2;
    if (arr[mid] == target)
        return mid;
    else if(arr[mid] > target)
        return binarySearch(target, arr, start, mid-1);
    else
        return binarySearch(target, arr, mid+1, end);
}