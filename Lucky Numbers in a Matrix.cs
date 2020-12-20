public class Solution {
    public IList<int> LuckyNumbers (int[][] matrix) 
    {
        IList<int> ans = new List<int>();
        Dictionary<int,int> cache = new Dictionary<int,int>();
        
        for(int i=0;i<matrix.Length;i++)
        {
            int min = matrix[i].Min();
            
            for(int j=0;j<matrix[0].Length;j++)
            {
                if(!cache.ContainsKey(j))
                    cache.Add(j,MaxInColumn(matrix,j));
                
                int max = cache[j];
                
                if(matrix[i][j]==min && matrix[i][j]==max)
                    ans.Add(matrix[i][j]);
            }
        }
        
        return ans;
    }
    
    private int MaxInColumn(int[][] matrix,int col)
    {
        int max = matrix[0][col];
        
        for(int i=1;i<matrix.Length;i++)
        {
            max = Math.Max(max,matrix[i][col]);
        }
        
        return max;
    }
}
