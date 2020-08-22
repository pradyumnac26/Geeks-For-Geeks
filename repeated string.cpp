long repeatedString(string s, long n) {
long size = s.size();
    long count1 = 0;
    long count2 = 0;
    long ret;
    
    for(int i=0;i<size;i++)
    {
       if(s[i] == 'a')
       {
          count1++;
       }
    }
    
    long q = n/size;
    long r = n%size;
    
    for(int i=0;i<r;i++)
    {
        if(s[i] == 'a')
        {
            count2++;
        }
    }
    ret = count1*q + count2;
    return ret;
}




//////////////////// python 

 return s.count('a') *( n//(len(s))) + s[:(n%(len(s)))].count('a')
