string pangrams(string s) {
int i;
    int n=s.length();
    vector<int> b(26,0);
    vector<int> a(26,0);
    for(i=0;i<n;i++)
    {
        if(s[i]>='a' && s[i]<='z')
            b[s[i]-'a']=1;
        if(s[i]>='A' && s[i]<='Z')
            a[s[i]-'A']=1;
    }
    for(i=0;i<26;i++){
      if(!(b[i]==1 || a[i]==1))
          return "not pangram";
      
    }
    return "pangram";
}s
