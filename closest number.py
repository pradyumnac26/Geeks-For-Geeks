vector<int> closestNumbers(vector<int> arr) {
int n=arr.size();
int i;
vector<int> b;

    sort(arr.begin(),arr.end());
    int min=INT_MAX; 
   for ( i = 1 ; i < n ; i++){ 
       if(arr[i]-arr[i-1]<=min)
           min=arr[i]-arr[i-1];}
  for(i=1;i<n;i++)
  {
      if(arr[i]-arr[i-1]==min){
          b.push_back(arr[i-1]);
          b.push_back(arr[i]);
              }
  }
  
  
return b;
}
