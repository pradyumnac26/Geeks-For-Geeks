int divisibleSumPairs(int n, int k, vector<int> ar) {
    int i,j,count=0;
for(i=0;i<n;i++)
{
    for(j=i+1;j<n;j++)
    {
        if((ar[i]+ar[j])%k==0)
        count++;
    }
}
return count;
}
