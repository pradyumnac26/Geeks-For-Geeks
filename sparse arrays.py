def matchingStrings(strings, queries):
    q=[]
    for i in queries:
        if i in strings:
            q.append(strings.count(i))
        else :
            q.append(0)
    return q

////////////////
vector<int> matchingStrings(vector<string> strings, vector<string> queries) {
int i,j;
    vector<int> b;
    for(i=0;i<queries.size();i++)
    {
        int count=0;
        for(j=0;j<strings.size();j++)
        {
            if(queries[i]==strings[j])
            {
               count++; 
            }
        }
        b.push_back(count);
    }
return b;
}
